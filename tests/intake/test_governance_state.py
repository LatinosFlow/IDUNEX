import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.governance_state_check import (
    scan_contradictions,
    validate_controlled_external_demo_execution,
    validate_current_state_data,
)


def aud030_state() -> dict:
    return json.loads(Path("governance/CURRENT_STATE.json").read_text(encoding="utf-8"))


class GovernanceStateTest(unittest.TestCase):
    def test_01_governance_state_is_consistent(self):
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
        self.assertEqual(report["m02_result"], "NOT_RECOMPUTED_POST_AUD030")
        self.assertEqual(report["m03_result"], "NOT_RECOMPUTED_POST_AUD030")
        self.assertEqual(report["controlled_external_demo_status"], "CONSUMED")
        self.assertFalse(report["controlled_external_demo_authorized"])
        self.assertTrue(report["controlled_external_demo_consumed"])

    def test_02_exact_aud030_transition_is_valid(self):
        self.assertEqual(validate_current_state_data(aud030_state()), [])

    def test_03_prior_m02_pass_is_rejected_for_changed_tree(self):
        state = aud030_state()
        state["m02_result"] = "M02_PASS"
        findings = validate_current_state_data(state)
        self.assertTrue(any("m02_result" in finding for finding in findings))

    def test_04_prior_m03_pass_is_rejected_for_changed_tree(self):
        state = aud030_state()
        state["m03_result"] = "M03_PASS"
        findings = validate_current_state_data(state)
        self.assertTrue(any("m03_result" in finding for finding in findings))

    def test_05_aud028_cannot_be_unconsumed_or_reauthorized(self):
        state = aud030_state()
        controlled = state["controlled_external_demo_execution"]
        controlled.update({"status": "AUTHORIZED_NOT_CONSUMED", "authorized": True, "consumed": False})
        findings = validate_current_state_data(state)
        self.assertTrue(any("status" in finding for finding in findings))
        self.assertTrue(any("authorized" in finding for finding in findings))
        self.assertTrue(any("consumed" in finding for finding in findings))

    def test_06_execution_counters_must_remain_zero(self):
        state = aud030_state()
        state["controlled_external_demo_execution"]["generate_executions_allowed"] = 1
        findings = validate_current_state_data(state)
        self.assertTrue(any("generate_executions_allowed" in finding for finding in findings))

    def test_07_project_audit_and_agent_load_remain_blocked(self):
        state = aud030_state()
        controlled = state["controlled_external_demo_execution"]
        controlled["project_audit_status"] = "PROJECT_AUDIT_PASS"
        controlled["project_agent_load_pass"] = True
        findings = validate_current_state_data(state)
        self.assertTrue(any("project_audit_status" in finding for finding in findings))
        self.assertTrue(any("project_agent_load_pass" in finding for finding in findings))

    def test_08_release_oficial_and_global_agent_load_remain_false(self):
        state = aud030_state()
        state.update({"release_authorized": True, "oficial_authorized": True, "agent_load_authorized": True})
        findings = validate_current_state_data(state)
        self.assertTrue(any("release_authorized" in finding for finding in findings))
        self.assertTrue(any("oficial_authorized" in finding for finding in findings))
        self.assertTrue(any("agent_load_authorized" in finding for finding in findings))

    def test_09_controlled_execution_schema_still_rejects_limit_above_one(self):
        controlled = copy.deepcopy(aud030_state()["controlled_external_demo_execution"])
        controlled["execution_limit"] = 2
        findings = validate_controlled_external_demo_execution(controlled)
        self.assertTrue(any("execution_limit" in finding for finding in findings))

    def test_10_scanner_rejects_unclassified_ready_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rogue = root / "engine" / "IDUNEX" / "00_INDEX" / "ROGUE_CERTIFICATE.txt"
            rogue.parent.mkdir(parents=True)
            rogue.write_text(
                "M02_RESULT=NOT_RECOMPUTED_POST_AUD030\nREADY_FOR_PROJECT_DEMO_GENERATION=TRUE\n",
                encoding="utf-8",
            )
            findings, historical_matches = scan_contradictions(root)
        self.assertTrue(findings)
        self.assertEqual(historical_matches, 0)


if __name__ == "__main__":
    unittest.main()
