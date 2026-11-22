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
