"""Smoke tests for the Gemini Korean SDS Agent Skill (standard library only)."""
from __future__ import annotations

import ast
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL.parents[2]
CHECKER = SKILL / "scripts" / "check_sources.py"


class KoreanSdsSkillTests(unittest.TestCase):
    def test_frontmatter_and_trigger_words(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\nname: korean-sds-compliance\n"))
        self.assertIn("description:", text.split("---", 2)[1])
        for phrase in ["MSDS", "Annex", "NEEDS_REVIEW", "NOT_APPLICABLE", "NOT_ASSESSED"]:
            self.assertIn(phrase, text)

    def test_reference_files_and_script_parse(self):
        for filename in ["source-map.md", "review-workflow.md",
                         "decision-policy.md", "installation.md"]:
            self.assertTrue((SKILL / "references" / filename).is_file(), filename)
        ast.parse(CHECKER.read_text(encoding="utf-8"))

    def test_negative_absent_knowledge_base(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(CHECKER), "--kb", tmp],
                text=True, capture_output=True, check=False
            )
            self.assertNotEqual(result.returncode, 0)
            report = json.loads(result.stdout)
            self.assertEqual(report["structural_check"], "FAIL")
            self.assertFalse(report["legal_compliance_determined"])
            self.assertTrue(report["errors"])

    def test_korean_specific_priority_matrix(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Korea-first routing", text)
        self.assertIn("korea-first-requirements.md", text)
        self.assertIn("korean-requirement-matrix.json", text)
        self.assertIn("Article 11", text)
        self.assertIn("NOT_ASSESSED", text)

        policy = (SKILL / "references" / "korea-first-requirements.md")
        self.assertTrue(policy.is_file())
        wording = policy.read_text(encoding="utf-8")
        for korean_term in ["산업안전보건법", "별표 4", "별표 5", "별표 6", "대체자료", "제출번호"]:
            self.assertIn(korean_term, wording)

        matrix = json.loads((SKILL / "assets" / "korean-requirement-matrix.json")
                            .read_text(encoding="utf-8"))
        self.assertEqual(matrix["module_count"], 12)
        self.assertEqual(matrix["rule_count"], 60)
        modules = matrix["modules"]
        self.assertEqual(len(modules), 12)
        self.assertEqual([m["module_id"] for m in modules],
                         [f"KR-{i:02d}" for i in range(1, 13)])
        ids = [rid for module in modules for rid in module["rule_ids"]]
        self.assertEqual(len(ids), 60)
        self.assertEqual(len(set(ids)), 60)
        self.assertTrue(all(m["legal_refs"] and m["evidence"] for m in modules))
        self.assertEqual(len([m for m in modules if m["priority"] == "P0"]), 7)

        kb = ROOT / "korean"
        rule_file = kb / "compliance_rules_en_ko.json"
        if rule_file.is_file():
            sources = json.loads(rule_file.read_text(encoding="utf-8"))
            actual_ids = {r["rule_id"] for r in sources["rules"]}
            self.assertEqual(actual_ids, set(ids))

    def test_real_repository_sources(self):
        kb = ROOT / "korean"
        if not kb.is_dir():
            self.skipTest("Skill copied without private Korean knowledge-base folder")
        result = subprocess.run(
            [sys.executable, str(CHECKER), "--kb", str(kb)],
            text=True, capture_output=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr + "\n" + result.stdout)
        data = json.loads(result.stdout)
        self.assertEqual(data["counts"]["operational_rules"], 60)
        self.assertEqual(data["counts"]["main_body_provisions"], 131)
        self.assertEqual(data["counts"]["sds_field_rules"], 97)
        self.assertEqual(data["counts"]["annex5_parent_codes"], 48)
        self.assertEqual(data["counts"]["annex5_sub_codes"], 31)
        self.assertEqual(data["counts"]["annex6_thresholds"], 14)
        self.assertFalse(data["legal_compliance_determined"])


if __name__ == "__main__":
    unittest.main()
