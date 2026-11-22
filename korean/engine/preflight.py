"""Conservative Korean SDS preflight: deterministic observations, never legal PASS/FAIL.

Uses the user-supplied Annex 3–6 extracts. This is not a legal opinion:
official revision alignment, HWP layouts, scientific evidence and applicability
must be independently validated.
Run: python -m korean.engine.preflight intake.json
"""
from __future__ import annotations
import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _json(root, name):
    return json.loads((root / "annexes" / name).read_text(encoding="utf-8"))

def _numeric(value, limit=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    v = float(value)
    return v if math.isfinite(v) and v >= 0 and (limit is None or v <= limit) else None

def _normal(value):
    return re.sub(r"\s+", "", str(value or "").replace("－", "-").replace("–", "-"))

def minimum_label_area(capacity, side_area=None):
    if capacity >= 500: return 450.0
    if capacity >= 200: return 300.0
    if capacity >= 50: return 180.0
    if capacity >= 5: return 90.0
    return 0.05 * side_area if side_area is not None else None

class Preflight:
    """Preflight only: observed evidence and unverified threshold comparisons."""
    def __init__(self, root=ROOT):
        self.root = Path(root)
        self.sections = _json(self.root, "annex_4_sds_field_requirements.json")["sections"]
        self.fields = [field for section in self.sections for field in section["fields"]]
        self.codes = {row["use_code"] for row in _json(self.root, "annex_5_use_categories.json")["categories"]}
        self.limits = _json(self.root, "annex_6_concentration_limits.json")["limits"]
        manifest = _json(self.root, "annex_sources_manifest.json")
        self.sources = {str(n): {"sha256": row["original_hwp_sha256"],
                          "layout_verified": False, "revision_verified": False}
                        for n, row in manifest["annexes"].items()}
        if (len(self.sections), len(self.fields), len(self.codes), len(self.limits)) != (16, 97, 79, 14):
            raise ValueError("Source index counts inconsistent; run annex validation")

    def review(self, intake):
        if not isinstance(intake, dict):
            raise ValueError("Input must be a JSON object")
        sds = intake.get("sds") if isinstance(intake.get("sds"), dict) else {}
        product = intake.get("product") if isinstance(intake.get("product"), dict) else {}
        submission = intake.get("msds_submission") if isinstance(intake.get("msds_submission"), dict) else {}
        complete = sds.get("extraction_complete") is True
        sections, order = self.section_checks(sds, complete)
        fields = self.field_checks(sds, complete)
        counts = dict(Counter(row["observation"] for row in fields))
        return {
            "document_id": str(intake.get("document_id") or "UNSPECIFIED"),
            "engine": "KOREAN_SDS_PREFLIGHT_V1",
            "overall_status": "NEEDS_REVIEW",
            "legal_compliance_determined": False,
            "source_version_verified": False,
            "review_scope": intake.get("review_scope", "UNSPECIFIED"),
            "source_manifest": self.sources,
            "section_structure": {"checks": sections, "observed_order": order,
                                   "extraction_complete": complete},
            "annex_4_fields": {"checks": fields, "count_by_observation": counts,
                               "coverage_statement": "Text observation, not verification of content sufficiency"},
            "annex_5_uses": self.use_checks(product),
            "annex_6_composition_thresholds": self.component_checks(intake.get("components")),
            "annex_3_label_measurements": self.label_checks(intake.get("label")),
            "msds_number": self.msds_number_check(submission, complete),
            "limitations": [
                "DRAFT ONLY. No legal PASS or FAIL is issued by this engine.",
                "Original HWP images, tables, formula layout and official version alignment are unverified.",
                "Cross-referenced laws, exemptions, classification evidence and government approvals require review.",
                "Missing fields are review leads; extraction may be incomplete.",
                "Concentration thresholds do not themselves establish mixture hazard classification or ingredient omission rights."
            ]
        }

    def section_checks(self, sds, complete):
        entries = sds.get("sections")
        entries = entries if isinstance(entries, list) else []
        numbers = [e["number"] for e in entries if isinstance(e, dict)
                   and type(e.get("number")) is int]
        frequency = Counter(numbers)
        order = [n for n in numbers if 1 <= n <= 16]
        ordered = order == sorted(order)
        checks = []
        for section in self.sections:
            n = section["number"]
            observation = ("DUPLICATE" if frequency[n] > 1 else
                "HEADING_EXTRACTED" if frequency[n] == 1 else
                "NOT_FOUND_IN_COMPLETE_EXTRACTION" if complete else "NOT_ASSESSED")
            if frequency[n] == 1 and not ordered:
                observation = "HEADING_EXTRACTED_ORDER_REVIEW"
            checks.append({"section_no": n, "title_ko": section["title_ko"],
                           "observation": observation, "source_ref": f"별표 4 / {n}."})
        if any(n < 1 or n > 16 for n in numbers):
            checks.append({"section_no": None, "title_ko": "Unrecognised section number",
                           "observation": "EXTRA_NUMBERED_SECTION_REVIEW", "source_ref": "별표 4"})
        return checks, order

    def field_checks(self, sds, complete):
        entries = sds.get("section_fields")
        entries = entries if isinstance(entries, list) else []
        reported = {}
        for row in entries:
            if isinstance(row, dict) and isinstance(row.get("field_id"), str):
                value = row.get("source_text")
                reported.setdefault(row["field_id"], []).append(value if isinstance(value, str) else "")
        checks = []
        for field in self.fields:
            fid = field["field_id"]
            values = reported.get(fid, [])
            if len(values) > 1: observation = "DUPLICATE_EXTRACTION_REVIEW"
            elif not values:
                observation = "NOT_FOUND_IN_COMPLETE_EXTRACTION" if complete else "NOT_ASSESSED"
            elif not values[0].strip(): observation = "EMPTY_EXTRACT_REVIEW"
            elif values[0].strip().replace(" ", "") in ("자료없음", "해당없음"):
                observation = "TEXT_EXTRACTED_PLACEHOLDER_REVIEW"
            else: observation = "TEXT_EXTRACTED_NOT_VALIDATED"
            checks.append({"field_id": fid, "section_no": field["section_no"],
                           "observation": observation, "source_ref": f"별표 4 / {fid}",
                           "source_text_ko": field["source_text_ko"]})
        known = {row["field_id"] for row in self.fields}
        for fid in sorted(set(reported) - known):
            checks.append({"field_id": fid, "section_no": None,
                           "observation": "UNKNOWN_FIELD_ID_REVIEW", "source_ref": "별표 4"})
        return checks

    def use_checks(self, product):
        raw = product.get("annex_5_use_codes")
        if raw is not None and not isinstance(raw, list):
            return {"observation": "INVALID_INPUT_REVIEW", "known": [], "unknown": [],
                    "source_ref": "제11조제8항 / 별표 5"}
        codes = [str(code).strip() for code in (raw or [])]
        known = [code for code in codes if code in self.codes]
        unknown = [code for code in codes if code not in self.codes]
        context = product.get("is_submission_context")
        observation = ("UNKNOWN_CODES_REVIEW" if unknown else
            "CATALOGUE_CODES_MATCHED_NOT_LEGAL_VALIDATION" if known else
            "MISSING_CODES_IN_CLAIMED_SUBMISSION_REVIEW" if context is True else
            "NOT_SELECTED_OPTIONAL_CONTEXT" if context is False else
            "SUBMISSION_CONTEXT_UNKNOWN")
        return {"observation": observation, "known": known, "unknown": unknown,
                "is_submission_context": context if isinstance(context, bool) else None,
                "source_ref": "제11조제8항 / 별표 5",
                "limitation": "Catalogue membership is not evidence of actual product use."}

    def component_checks(self, components):
        if not isinstance(components, list):
            return []
        by_name = {}
        for limit in self.limits:
            by_name.setdefault(_normal(limit["hazard_name_ko"]), []).append(limit)
        result = []
        for i, comp in enumerate(components):
            if not isinstance(comp, dict):
                result.append({"component_index": i, "observation": "INVALID_COMPONENT_INPUT_REVIEW"})
                continue
            matched, unknown, seen = [], [], set()
            hazards = comp.get("confirmed_hazard_categories")
            for haz in hazards if isinstance(hazards, list) else []:
                if not isinstance(haz, dict):
                    unknown.append("Malformed hazard"); continue
                name = str(haz.get("hazard_name_ko") or "")
                category = str(haz.get("category") or "").upper()
                rows = by_name.get(_normal(name), [])
                if not rows:
                    unknown.append(name or "Unnamed hazard"); continue
                for row in rows:
                    if row["hazard_number"] == 6:
                        expected = "1A_and_1B" if category in ("1A", "1B") else category
                        if row["hazard_category"] != expected: continue
                    if row["rule_id"] not in seen:
                        matched.append({"source_rule_id": row["rule_id"],
                                        "hazard_name_ko": row["hazard_name_ko"],
                                        "threshold_percent": row["concentration_threshold_percent"],
                                        "source_ref": row["source_ref"]})
                        seen.add(row["rule_id"])
                if any(row["hazard_number"] == 6 for row in rows) and not any(
                    _normal(m["hazard_name_ko"]) == _normal(name) for m in matched
                ):
                    unknown.append(f"{name}: category {category or 'missing'}")
            physical = comp.get("physical_hazard_group_under_rule_annex_18_1a")
            if physical is True:
                matched.append({"source_rule_id": "KR-A11-9-PHYSICAL",
                                "hazard_name_ko": "User-asserted implementing-rule physical hazard group",
                                "threshold_percent": 1.0,
                                "source_ref": "제11조제9항 / 규칙 별표18 제1호가목"})
            concentration = _numeric(comp.get("actual_pct"), 100)
            minimum = min((x["threshold_percent"] for x in matched), default=None)
            observation = ("INSUFFICIENT_INPUT_REVIEW" if concentration is None or minimum is None else
                "AT_OR_ABOVE_LOWEST_KNOWN_THRESHOLD_REVIEW" if concentration >= minimum else
                "BELOW_LOWEST_KNOWN_THRESHOLD_OTHER_HAZARDS_UNVERIFIED")
            result.append({"component_index": i, "chemical_name": comp.get("chemical_name"),
                           "actual_percent": concentration,
                           "actual_percent_available": concentration is not None,
                           "known_matched_thresholds": matched,
                           "lowest_known_threshold_percent": minimum,
                           "unmatched_hazards": unknown,
                           "physical_hazard_group_1a_confirmed_by_input": physical is True,
                           "observation": observation, "legal_conclusion": None,
                           "source_ref": "제11조제9항 / 별표 6",
                           "limitation": "Known-cutoff comparison only, not a disclosure or mixture-classification verdict."})
        return result

    def label_checks(self, label):
        if not isinstance(label, dict):
            return {"observation": "OUTSIDE_DOCUMENT_SCOPE_NOT_ASSESSED", "source_ref": "별표 3"}
        capacity = _numeric(label.get("container_capacity_liters"))
        area = _numeric(label.get("printed_label_area_cm2"))
        side = _numeric(label.get("exterior_side_surface_area_cm2"))
        minimum = minimum_label_area(capacity, side) if capacity is not None else None
        status = ("MEASUREMENTS_MISSING" if minimum is None or area is None else
                  "MEETS_EXTRACTED_MINIMUM_AREA_NOT_LEGAL_PASS" if area >= minimum else
                  "BELOW_EXTRACTED_MINIMUM_AREA_REVIEW")
        pics = label.get("pictogram_areas_cm2")
        pic_min = max(0.5, area / 40) if area is not None else None
        pic_status = ("NO_PICTOGRAM_MEASUREMENTS"
                      if not isinstance(pics, list) or not pics or pic_min is None else
                      "INVALID_MEASUREMENT_REVIEW" if any(_numeric(p) is None for p in pics) else
                      "ALL_REPORTED_PICTOGRAMS_MEET_SIZE_MINIMUM_NOT_LEGAL_PASS"
                      if all(_numeric(p) >= pic_min for p in pics) else
                      "PICTOGRAM_BELOW_EXTRACTED_MINIMUM_REVIEW")
        return {"observation": status, "container_capacity_liters": capacity,
                "minimum_label_area_cm2": minimum, "measured_label_area_cm2": area,
                "pictogram_minimum_each_cm2": pic_min, "pictogram_observation": pic_status,
                "source_ref": "별표 3 / 2. 규격",
                "limitation": "Physical size only; label content and exceptions not evaluated."}

    def msds_number_check(self, submission, complete):
        value = str(submission.get("submission_number") or "").strip()
        loc = submission.get("document_number_on_first_page")
        if value and loc is True: observation = "REPORTED_ON_FIRST_PAGE_UNVERIFIED"
        elif value and loc is False: observation = "REPORTED_BUT_POSITION_DISPUTED"
        elif value: observation = "POSITION_UNVERIFIED"
        elif loc is True: observation = "INCONSISTENT_CLAIM"
        elif loc is False and complete: observation = "NOT_FOUND_IN_COMPLETE_EXTRACTION_REVIEW"
        else: observation = "UNASSESSED"
        return {"observation": observation, "value_reported": bool(value),
                "source_ref": "별표 4 — first-page MSDS number placement",
                "limitation": "Actual submission and legal applicability not verified."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("intake", help="Structured SDS input JSON; '-' means stdin")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        raw = sys.stdin.read() if args.intake == "-" else Path(args.intake).read_text(encoding="utf-8")
        result = Preflight(args.root).review(json.loads(raw))
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as err:
        print(f"preflight error: {err}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
