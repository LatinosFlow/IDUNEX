import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.governance_state_check import (
    scan_contradictions,
    validate_current_state_data,
)


class GovernanceStateTest(unittest.TestCase):
    def test_governance_state_is_consistent(self):
        result = subprocess.run(
            [sys.executable, "tools/audit/governance_state_check.py", "--repo-root", "."],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["result"], "CONSISTENT")
        self.assertEqual(report["active_contradiction_count"], 0)

    def test_current_state_rejects_demo_enablement_under_m02_fail(self):
        mutated = {
            "motor_status": "EN_REVISION",
            "m02_result": "M02_FAIL",
            "ready_for_project_demo_generation": True,
            "release_authorized": False,
            "tag_authorized": False,
            "productive_closure_authorized": False,
            "creative_output_certified": False,
            "interlock": {
                "denied_capabilities": [
                    "PROJECT_DEMO_GENERATION",
                    "RELEASE",
                    "TAG",
                    "PRODUCTIVE_CLOSURE",
                ]
            },
        }
        findings = validate_current_state_data(mutated)
        self.assertTrue(
            any("ready_for_project_demo_generation" in finding for finding in findings)
        )

    def test_scanner_rejects_unclassified_ready_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rogue = root / "engine" / "IDUNEX" / "00_INDEX" / "ROGUE_CERTIFICATE.txt"
            rogue.parent.mkdir(parents=True)
            rogue.write_text(
                "M02_RESULT=M02_FAIL\nREADY_FOR_PROJECT_DEMO_GENERATION=TRUE\n",
                encoding="utf-8",
            )
            findings, historical_matches = scan_contradictions(root)
        self.assertTrue(findings)
        self.assertEqual(historical_matches, 0)


if __name__ == "__main__":
    unittest.main()
