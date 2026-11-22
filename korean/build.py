#!/usr/bin/env python3
"""Validate Korean SDS regulatory LLM artifacts and rebuild derived retrieval indexes.

Source inputs are existing Korean legal markdown + bilingual rule JSON.
This is NOT the original HWPX extraction program. Annexes 1–7 remain absent.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "regulation_full_structured_ko.md"
RULES = ROOT / "compliance_rules_en_ko.json"
SECTIONS = ROOT / "sds_16_section_index.json"
CHUNKS = ROOT / "rag_source_chunks.jsonl"
COVERAGE = ROOT / "coverage_matrix.json"

ARTICLE_RE = re.compile(r"^## (제\d+조(?:의\d+)?) \(([^)]+)\)$")
PROVISION_RE = re.compile(r"^\*\*\[([^\]]+)\] ([^*]+)\*\* — (.*)$")
ANNEX_RE = re.compile(r"별표\s*[1-7]")


def source_provisions():
    articles, provisions = [], []
    current = None
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        heading = ARTICLE_RE.match(line)
        if heading:
            current = {"article": heading.group(1), "title": heading.group(2),
                       "provisions": []}
            articles.append(current)
            continue
        match = PROVISION_RE.match(line)
        if match and current is not None:
            prov = {"id": match.group(1), "ref": match.group(2),
                    "text_ko": match.group(3),
                    "article": current["article"],
                    "article_title_ko": current["title"]}
            current["provisions"].append(prov)
            provisions.append(prov)
    return articles, provisions


def make_derived(articles, provisions, rules_doc):
    rules = rules_doc["rules"]
    source_hash = rules_doc["metadata"]["source_sha256"]
    linked_by_source = defaultdict(list)
    for rule in rules:
        for src in rule["legal_sources"]:
            if src.get("source_id"):
                linked_by_source[src["source_id"]].append(rule["rule_id"])

    rule_by_id = {r["rule_id"]: r for r in rules}
    chunks = []
    for provision in provisions:
        linked = list(dict.fromkeys(linked_by_source[provision["id"]]))
        dependencies = " ".join(
            [provision["text_ko"]] +
            [str(d) for rule_id in linked for d in rule_by_id[rule_id].get("external_dependencies", [])]
        )
        annexes = list(dict.fromkeys(
            re.sub(r"\s+", " ", m.group(0)) for m in ANNEX_RE.finditer(dependencies)
        ))
        chunks.append({
            "chunk_id": provision["id"],
            "source_ref": provision["ref"],
            "article_ko": provision["article"],
            "article_title_ko": provision["article_title_ko"],
            "original_ko": provision["text_ko"],
            "text_for_retrieval":
                f'{provision["article"]} ({provision["article_title_ko"]}) / '
                f'{provision["ref"]}: {provision["text_ko"]}',
            "linked_rule_ids": linked,
            "source_file_sha256": source_hash,
            "annex_dependencies_unresolved": annexes,
        })

    coverage = []
    for article in articles:
        stem = article["article"]
        rule_ids = [
            r["rule_id"] for r in rules
            if any(s["ref"] == stem or s["ref"].startswith(stem + "제")
                   for s in r["legal_sources"])
        ]
        coverage.append({
            "article": stem,
            "title": article["title"],
            "source_provisions": len(article["provisions"]),
            "operational_rule_ids": rule_ids,
            "has_operational_rules": bool(rule_ids),
        })
    return chunks, {
        "coverage": coverage,
        "note": "Rule coverage is reviewer-screening coverage, not evidence of exhaustive statutory or Annex compliance.",
    }


def validate(articles, provisions, rules_doc):
    sections = json.loads(SECTIONS.read_text(encoding="utf-8"))
    rule_ids = [r["rule_id"] for r in rules_doc["rules"]]
    source_ids = {p["id"] for p in provisions}
    assert len(articles) == 22, f"expected 22 articles, got {len(articles)}"
    assert len(provisions) == 131, f"expected 131 indexed provisions, got {len(provisions)}"
    assert len(rule_ids) == 60, f"expected 60 rules, got {len(rule_ids)}"
    assert len(set(rule_ids)) == len(rule_ids), "duplicate rule IDs"
    assert len(source_ids) == len(provisions), "duplicate legal source IDs"
    assert [s["section_no"] for s in sections["sections"]] == list(range(1, 17))
    assert rules_doc["metadata"]["notice_number"] == "고용노동부고시 제2026-26호"
    assert rules_doc["metadata"]["annexes_referenced_but_absent"] == [
        f"별표 {n}" for n in range(1, 8)
    ]
    for r in rules_doc["rules"]:
        assert r["legal_sources"], f'{r["rule_id"]}: missing source'
        for src in r["legal_sources"]:
            assert src.get("verbatim_ko"), f'{r["rule_id"]}: missing Korean legal wording'
            assert src.get("source_id") in source_ids, (
                f'{r["rule_id"]}: source {src.get("source_id")} is not indexed'
            )
    for path in [ROOT / "sds_intake.schema.json", ROOT / "compliance_report.schema.json",
                 ROOT / "regulation_full_structured_ko.json",
                 ROOT / "missing_annex_dependency_manifest.json"]:
        json.loads(path.read_text(encoding="utf-8"))
    example = json.loads((ROOT / "SYNTHETIC_example_compliance_report.json").read_text(encoding="utf-8"))
    assert example["document_id"].startswith("SYNTHETIC")
    print(f"PASS: {len(articles)} articles, {len(provisions)} cited provisions, "
          f"{len(rule_ids)} rules, 16 SDS sections. Annexes 1–7 still missing.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true", help="validate without writing")
    parser.add_argument("--refresh-index", action="store_true",
                        help="regenerate RAG source chunks and article coverage")
    args = parser.parse_args()
    articles, provisions = source_provisions()
    rules_doc = json.loads(RULES.read_text(encoding="utf-8"))
    validate(articles, provisions, rules_doc)
    if args.refresh_index:
        chunks, coverage = make_derived(articles, provisions, rules_doc)
        CHUNKS.write_text(
            "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in chunks),
            encoding="utf-8",
        )
        COVERAGE.write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
        print(f"Rebuilt {CHUNKS.name} and {COVERAGE.name}.")


if __name__ == "__main__":
    main()
