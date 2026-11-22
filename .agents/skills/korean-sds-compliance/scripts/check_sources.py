#!/usr/bin/env python3
"""Read-only structural preflight for a Korean SDS regulatory knowledge base.

This program does NOT determine legal validity, chemical classification, or SDS
compliance. It does not make network calls or modify confidential data.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines()
            if x.strip()]


def find_kb(argument: str | None) -> Path:
    paths = [argument, os.environ.get("KOREAN_SDS_KB"),
             str(Path.cwd() / "korean"),
             str(Path(__file__).resolve().parents[4] / "korean")]
    for value in paths:
        if value and (Path(value).expanduser() / "annexes").is_dir():
            return Path(value).expanduser().resolve()
    # Preserve explicit user-selected path for the diagnostic.
    return Path(argument or paths[2]).expanduser().resolve()


def check(kb: Path) -> dict:
    errors: list[str] = []
    warnings = [
        "All annex HWP files require official version and source-layout verification.",
        "A successful knowledge-base check is NOT an SDS legal compliance determination.",
        "External statutes, original pictograms/formulas, scientific data and product evidence may be required.",
    ]
    counts: dict[str, int] = {}

    def require_file(path: Path) -> bool:
        if not path.is_file():
            errors.append(f"Missing source: {path.relative_to(kb) if kb in path.parents else path}")
            return False
        return True

    def safe_json(relative: str) -> dict | None:
        path = kb / relative
        if not require_file(path):
            return None
        try:
            obj = read_json(path)
        except (ValueError, OSError) as exc:
            errors.append(f"Invalid JSON {relative}: {exc}")
            return None
        if not isinstance(obj, dict):
            errors.append(f"Expected JSON object: {relative}")
            return None
        return obj

    manifest = safe_json("annexes/annex_sources_manifest.json")
    if manifest:
        annexes = manifest.get("annexes", {})
        counts["annexes_listed"] = len(annexes)
        for number in range(1, 8):
            a = annexes.get(str(number), {})
            if not a or a.get("status") != "UPLOADED_AS_SEPARATE_HWP":
                errors.append(f"Annex {number} not recorded as uploaded")
            if len(str(a.get("original_hwp_sha256", ""))) != 64:
                errors.append(f"Annex {number} original source hash missing")
            if a.get("ready_for_final_compliance_verdict") is True:
                warnings.append(f"Annex {number} claims ready status; independently verify!")
            require_file(kb / f"annexes/annex_{number}.extracted_ko.txt")
            chunk_path = kb / f"annexes/annex_{number}_rag_chunks.jsonl"
            if require_file(chunk_path):
                try:
                    chunks = read_jsonl(chunk_path)
                    counts[f"annex_{number}_rag_chunks"] = len(chunks)
                    if not chunks:
                        errors.append(f"Annex {number} retrieval index empty")
                except (ValueError, OSError) as exc:
                    errors.append(f"Invalid Annex {number} JSONL: {exc}")

    rules = safe_json("compliance_rules_en_ko.json")
    if rules:
        records = rules.get("rules", [])
        counts["operational_rules"] = len(records)
        if len(records) != 60 or len({r.get("rule_id") for r in records}) != 60:
            errors.append("Expected 60 distinct operational rule IDs")

    main_chunks = kb / "rag_source_chunks.jsonl"
    if require_file(main_chunks):
        try:
            counts["main_body_provisions"] = len(read_jsonl(main_chunks))
            if counts["main_body_provisions"] != 131:
                errors.append("Expected 131 main-body provision chunks")
        except (ValueError, OSError) as exc:
            errors.append(f"Invalid main-body JSONL: {exc}")

    a4 = safe_json("annexes/annex_4_sds_field_requirements.json")
    if a4:
        sections = a4.get("sections", [])
        ids = [f.get("field_id") for s in sections for f in s.get("fields", [])]
        counts.update(sds_sections=len(sections), sds_field_rules=len(ids))
        if [s.get("number") for s in sections] != list(range(1, 17)):
            errors.append("Annex 4 SDS Sections 1–16 missing or out of order")
        if len(ids) != 97 or len(set(ids)) != len(ids):
            errors.append("Expected 97 unique Annex 4 field/subfield IDs")

    a5 = safe_json("annexes/annex_5_use_categories.json")
    if a5:
        uses = a5.get("categories", [])
        parent = {u.get("use_code") for u in uses if u.get("parent_use_code") is None}
        sub = [u for u in uses if u.get("parent_use_code") is not None]
        counts.update(annex5_parent_codes=len(parent), annex5_sub_codes=len(sub))
        if len(parent) != 48 or len(sub) != 31 or any(u.get("parent_use_code") not in parent for u in sub):
            errors.append("Annex 5 expected 48 parents, 31 subcategories with valid parents")

    a6 = safe_json("annexes/annex_6_concentration_limits.json")
    if a6:
        limits = a6.get("limits", [])
        counts["annex6_thresholds"] = len(limits)
        if len(limits) != 14 or {r.get("hazard_number") for r in limits} != set(range(1, 14)):
            errors.append("Annex 6 expected 14 threshold entries covering hazard headings 1–13")
        if any("DISCLOSURE_THRESHOLD" not in str(r.get("purpose", "")) for r in limits):
            errors.append("Annex 6 limits must be labelled as disclosure, not hazard classification")

    return {
        "knowledge_base_path": str(kb),
        "structural_check": "PASS" if not errors else "FAIL",
        "source_accessible_for_preliminary_review": not errors,
        "legal_compliance_determined": False,
        "source_revision_and_layout_verified": False,
        "counts": counts,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kb", help="Path to repository's korean/ knowledge-base folder")
    arguments = parser.parse_args()
    result = check(find_kb(arguments.kb))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not result["errors"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
