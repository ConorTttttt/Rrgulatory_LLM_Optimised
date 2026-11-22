"""Regression checks with entirely synthetic data; never commit real SDS formulations."""
import json
import tempfile
import unittest
from pathlib import Path

from korean.engine.preflight import Preflight, minimum_label_area


class PreflightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        base = Path(cls.temp.name)
        annex = base / "annexes"
        annex.mkdir()
        sections = [
            {"number": i, "title_ko": f"Section {i}", "fields": [
                {"field_id": f"KR-A4-S{i:02d}-{j}", "section_no": i,
                 "source_text_ko": f"Field {i}/{j}"}
                for j in range(1, 8 if i == 1 else 7)]}
            for i in range(1, 17)]
        use_codes = ([{"use_code": str(i), "parent_use_code": None}
                      for i in range(1, 49)] +
                     [{"use_code": f"8.{i}", "parent_use_code": "8"}
                      for i in range(1, 32)])
        names = [
            "급성 독성", "피부 부식성/피부 자극성", "심한 눈 손상성/눈 자극성",
            "호흡기 과민성", "피부 과민성", "생식세포 변이원성", "발암성",
            "생식독성", "특정표적장기독성 - 1회 노출",
            "특정표적장기독성 - 반복 노출", "흡인 유해성",
            "수생환경 유해성", "오존층 유해성"
        ]
        limits = []
        for i, name in enumerate(names, 1):
            thresholds = ([("1A_and_1B", 0.1), ("2", 1.0)] if i == 6
                          else [(None, 0.1 if i in (4, 5, 7, 8, 13) else 1.0)])
            for category, threshold in thresholds:
                limits.append({"rule_id": f"TEST-A6-{i}-{category}",
                               "hazard_number": i, "hazard_name_ko": name,
                               "hazard_category": category,
                               "concentration_threshold_percent": threshold,
                               "source_ref": f"별표 6 / {i}"})
        payloads = {
            "annex_4_sds_field_requirements.json": {"sections": sections},
            "annex_5_use_categories.json": {"categories": use_codes},
            "annex_6_concentration_limits.json": {"limits": limits},
            "annex_sources_manifest.json": {"annexes": {
                str(i): {"original_hwp_sha256": "a" * 64} for i in range(1, 8)}},
        }
        for name, data in payloads.items():
            (annex / name).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        cls.engine = Preflight(base)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_no_input_never_legal_pass(self):
        r = self.engine.review({"document_id": "SYNTHETIC-001"})
        self.assertEqual(r["overall_status"], "NEEDS_REVIEW")
        self.assertFalse(r["legal_compliance_determined"])
        self.assertEqual(r["annex_4_fields"]["count_by_observation"]["NOT_ASSESSED"], 97)

    def test_sixteen_headings_alone_not_compliance(self):
        sds = {"sections": [{"number": i} for i in range(1, 17)],
               "extraction_complete": True}
        r = self.engine.review({"sds": sds})
        self.assertTrue(all(c["observation"] == "HEADING_EXTRACTED"
                            for c in r["section_structure"]["checks"]))
        self.assertEqual(r["overall_status"], "NEEDS_REVIEW")

    def test_missing_section_with_complete_extraction(self):
        r = self.engine.review({"sds": {
            "sections": [{"number": 1}], "extraction_complete": True}})
        self.assertEqual(r["section_structure"]["checks"][1]["observation"],
                         "NOT_FOUND_IN_COMPLETE_EXTRACTION")
        self.assertEqual(r["overall_status"], "NEEDS_REVIEW")

    def test_out_of_order_and_duplicate(self):
        r = self.engine.review({"sds": {"sections": [
            {"number": 2}, {"number": 1}, {"number": 1}]}})
        self.assertEqual(r["section_structure"]["checks"][0]["observation"], "DUPLICATE")
        self.assertEqual(r["section_structure"]["checks"][1]["observation"],
                         "HEADING_EXTRACTED_ORDER_REVIEW")

    def test_placeholder_is_not_a_pass(self):
        r = self.engine.review({"sds": {"section_fields": [
            {"field_id": "KR-A4-S01-1", "source_text": "자료 없음"}]}})
        self.assertEqual(r["annex_4_fields"]["checks"][0]["observation"],
                         "TEXT_EXTRACTED_PLACEHOLDER_REVIEW")

    def test_unknown_field_id(self):
        r = self.engine.review({"sds": {"section_fields": [
            {"field_id": "UNKNOWN", "source_text": "x"}]}})
        self.assertEqual(r["annex_4_fields"]["checks"][-1]["observation"],
                         "UNKNOWN_FIELD_ID_REVIEW")

    def test_use_code_and_submission_context(self):
        r = self.engine.review({"product": {
            "is_submission_context": True, "annex_5_use_codes": ["8.1", "999"]}})
        self.assertEqual(r["annex_5_uses"]["known"], ["8.1"])
        self.assertEqual(r["annex_5_uses"]["unknown"], ["999"])
        missing = self.engine.review({"product": {"is_submission_context": True}})
        self.assertEqual(missing["annex_5_uses"]["observation"],
                         "MISSING_CODES_IN_CLAIMED_SUBMISSION_REVIEW")
        optional = self.engine.review({"product": {"is_submission_context": False}})
        self.assertEqual(optional["annex_5_uses"]["observation"],
                         "NOT_SELECTED_OPTIONAL_CONTEXT")

    def test_mutagenicity_threshold_boundaries(self):
        comps = [
            {"actual_pct": 0.1, "confirmed_hazard_categories": [
                {"hazard_name_ko": "생식세포 변이원성", "category": "1A"}]},
            {"actual_pct": 0.99, "confirmed_hazard_categories": [
                {"hazard_name_ko": "생식세포 변이원성", "category": "2"}]},
            {"actual_pct": 1, "confirmed_hazard_categories": [
                {"hazard_name_ko": "생식세포 변이원성", "category": "2"}]}
        ]
        r = self.engine.review({"components": comps})["annex_6_composition_thresholds"]
        self.assertEqual([i["lowest_known_threshold_percent"] for i in r], [0.1, 1, 1])
        self.assertTrue(r[1]["observation"].startswith("BELOW_"))
        self.assertTrue(all(i["legal_conclusion"] is None for i in r))

    def test_lower_overlapping_threshold(self):
        comp = {"actual_pct": 0.2,
                "physical_hazard_group_under_rule_annex_18_1a": True,
                "confirmed_hazard_categories": [
                    {"hazard_name_ko": "호흡기 과민성", "category": "1"}]}
        result = self.engine.review({"components": [comp]})
        matched = result["annex_6_composition_thresholds"][0]
        self.assertEqual(matched["lowest_known_threshold_percent"], 0.1)
        self.assertEqual(len(matched["known_matched_thresholds"]), 2)

    def test_invalid_mutagenicity_category_and_number(self):
        comp = {"actual_pct": "0.2", "confirmed_hazard_categories": [
            {"hazard_name_ko": "생식세포 변이원성", "category": "UNKNOWN"}]}
        r = self.engine.review({"components": [comp]})["annex_6_composition_thresholds"][0]
        self.assertEqual(r["observation"], "INSUFFICIENT_INPUT_REVIEW")
        self.assertTrue(r["unmatched_hazards"])

    def test_label_area_boundaries(self):
        for capacity, minimum in [(5, 90), (50, 180), (200, 300), (500, 450)]:
            self.assertEqual(minimum_label_area(capacity), minimum)
        self.assertAlmostEqual(minimum_label_area(4.99, 200), 10)
        self.assertIsNone(minimum_label_area(4.99))

    def test_pictogram_area_not_legal_pass(self):
        r = self.engine.review({"label": {
            "container_capacity_liters": 50,
            "printed_label_area_cm2": 200,
            "pictogram_areas_cm2": [5.0, 4.99]}})
        label = r["annex_3_label_measurements"]
        self.assertEqual(label["pictogram_minimum_each_cm2"], 5)
        self.assertEqual(label["pictogram_observation"],
                         "PICTOGRAM_BELOW_EXTRACTED_MINIMUM_REVIEW")
        self.assertEqual(r["overall_status"], "NEEDS_REVIEW")

    def test_submission_number_location_not_corroborated(self):
        r = self.engine.review({"msds_submission": {
            "submission_number": "SYNTHETIC-123",
            "document_number_on_first_page": True}})
        self.assertEqual(r["msds_number"]["observation"],
                         "REPORTED_ON_FIRST_PAGE_UNVERIFIED")


if __name__ == "__main__":
    unittest.main()
