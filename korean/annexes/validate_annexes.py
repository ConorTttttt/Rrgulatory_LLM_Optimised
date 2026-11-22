#!/usr/bin/env python3
"""Structural QA for the seven user-supplied Korean SDS regulatory annexes.

This validates the *derived datasets*, not legal source revision alignment, HWP
graphics, scientific accuracy, or regulatory suitability for production.
Run: python korean/annexes/validate_annexes.py  (from repository root)
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
BASE = D.parent


def load(name):
    return json.loads((D / name).read_text(encoding="utf-8"))


def check_jsonl(name):
    lines = (D / name).read_text(encoding="utf-8").splitlines()
    records = [json.loads(line) for line in lines if line.strip()]
    assert records, f"{name}: no records"
    return records


def main():
    manifest = load("annex_sources_manifest.json")
    assert manifest["all_seven_uploaded_separately"] is True
    assert len(manifest["annexes"]) == 7
    for n in range(1, 8):
        key = str(n)
        entry = manifest["annexes"][key]
        assert entry["status"] == "UPLOADED_AS_SEPARATE_HWP", n
        assert len(entry["original_hwp_sha256"]) == 64, n
        assert (D / f"annex_{n}.extracted_ko.txt").exists(), n
        check_jsonl(f"annex_{n}_rag_chunks.jsonl")
        assert entry["source_file_stored_in_repository"] is False
        assert entry["ready_for_final_compliance_verdict"] is False

    section = load("annex_4_sds_field_requirements.json")
    assert len(section["sections"]) == 16
    assert [x["number"] for x in section["sections"]] == list(range(1, 17))
    fields = [f for s in section["sections"] for f in s["fields"]]
    assert len(fields) == 97
    assert len({f["field_id"] for f in fields}) == len(fields)
    assert len(section["cross_checks"]) == 8
    assert len(check_jsonl("annex_4_sds_field_rules.jsonl")) == 97
    assert len(check_jsonl("annex_4_rag_chunks.jsonl")) == 16
    assert section["layout_rules"][0]["expected_placement"].startswith("first page")

    use = load("annex_5_use_categories.json")["categories"]
    main_codes = {u["use_code"] for u in use if u["parent_use_code"] is None}
    sub = [u for u in use if u["parent_use_code"] is not None]
    assert len(main_codes) == 48 and len(sub) == 31
    assert all(u["parent_use_code"] in main_codes for u in sub)
    assert len({u["use_code"] for u in use}) == 79
    assert len(check_jsonl("annex_5_rag_chunks.jsonl")) == 79

    limits = load("annex_6_concentration_limits.json")["limits"]
    assert len(limits) == 14
    assert {x["hazard_number"] for x in limits} == set(range(1, 14))
    mut = {x["hazard_category"]: x["concentration_threshold_percent"]
           for x in limits if x["hazard_number"] == 6}
    assert mut == {"1A_and_1B": 0.1, "2": 1}
    assert {x["concentration_threshold_percent"] for x in limits} == {0.1, 1}
    assert all("DISCLOSURE_THRESHOLD" in x["purpose"] for x in limits)
    assert len(check_jsonl("annex_6_rag_chunks.jsonl")) == 14

    old_h = load("annex_2_h_p_phrase_catalog.json")["phrases"]
    assert len(old_h) == 218

    dep = json.loads((BASE / "missing_annex_dependency_manifest.json").read_text("utf-8"))
    assert dep["all_present"] is True
    assert dep["still_missing"] == []
    rules = json.loads((BASE / "compliance_rules_en_ko.json").read_text("utf-8"))
    assert len(rules["rules"]) == 60
    for rid, expected in [
        ("SDS-002", "annex_4_sds_field_requirements.json"),
        ("SDS-007", "annex_5_use_categories.json"),
        ("SDS-008", "annex_6_concentration_limits.json"),
    ]:
        rule = next(x for x in rules["rules"] if x["rule_id"] == rid)
        assert rule["implementation_artifact"].endswith(expected), rid

    for name in ["sds_intake.schema.json", "compliance_report.schema.json"]:
        json.loads((BASE / name).read_text("utf-8"))

    print("PASS: all 7 sources indexed; Annex 4: 16 sections / 97 fields; "
          "Annex 5: 48+31 use codes; Annex 6: 14 thresholds; 60 base rules.")
    print("CAUTION: original HWP graphics/tables/formulas, source legal revision, "
          "and actual SDS evidence have NOT been independently validated.")


if __name__ == "__main__":
    main()
