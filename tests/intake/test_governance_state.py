import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.governance_state_check import (
    M02_RECOMPUTATION_STATE,
    scan_contradictions,
    validate_current_state_data,
)


def aud034_state() -> dict:
    return json.loads(Path("governance/CURRENT_STATE.json").read_text(encoding="utf-8"))


class GovernanceStateTest(unittest.TestCase):
    def test_01_current_aud035_state_passes_checker(self):
        result = subprocess.run(
            [sys.executable, "tools/audit/governance_state_check.py", "--repo-root", "."],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["result"], "CONSISTENT")
        self.assertEqual(report["m02_result"], M02_RECOMPUTATION_STATE)
        self.assertEqual(report["m03_result"], "NOT_RECOMPUTED_POST_AUD035")

    def test_02_generic_m02_pass_is_rejected(self):
        state = aud034_state()
        state["m02_result"] = "M02_PASS"
        self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_03_post_pr44_m02_pass_is_rejected(self):
        state = aud034_state()
        state["m02_result"] = "M02_PASS_RECOMPUTED_POST_PR44"
        self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_04_old_m02_not_recomputed_state_is_rejected(self):
        state = aud034_state()
        state["m02_result"] = "NOT_RECOMPUTED_POST_AUD030"
        self.assertTrue(any("m02_result" in finding for finding in validate_current_state_data(state)))

    def test_05_m03_pass_is_rejected(self):
        state = aud034_state()
        state["m03_result"] = "M03_PASS"
        self.assertTrue(any("m03_result" in finding for finding in validate_current_state_data(state)))

    def test_06_aud028_cannot_be_reauthorized(self):
        state = aud034_state()
        state["controlled_external_demo_execution"].update(
            {"status": "AUTHORIZED_NOT_CONSUMED", "authorized": True, "consumed": False}
        )
        findings = validate_current_state_data(state)
        self.assertTrue(any("status" in finding for finding in findings))
        self.assertTrue(any("authorized" in finding for finding in findings))
        self.assertTrue(any("consumed" in finding for finding in findings))

    def test_07_generate_execution_counter_must_remain_zero(self):
        state = aud034_state()
        state["controlled_external_demo_execution"]["generate_executions_allowed"] = 1
        self.assertTrue(any("generate_executions_allowed" in finding for finding in validate_current_state_data(state)))

    def test_08_artifact_sha_must_match_authorized_evidence(self):
        state = aud034_state()
        state["prior_m02_recomputation_evidence"]["artifact_sha256"] = "0" * 64
        self.assertTrue(any("artifact_sha256" in finding for finding in validate_current_state_data(state)))

    def test_09_engine_tree_sha_must_match_authorized_evidence(self):
        state = aud034_state()
        state["prior_m02_recomputation_evidence"]["engine_tree_sha256"] = "0" * 64
        self.assertTrue(any("engine_tree_sha256" in finding for finding in validate_current_state_data(state)))

    def test_10_release_oficial_and_agent_load_remain_disabled(self):
        state = aud034_state()
        state.update({"release_authorized": True, "oficial_authorized": True, "agent_load_authorized": True})
        findings = validate_current_state_data(state)
        self.assertTrue(any("release_authorized" in finding for finding in findings))
        self.assertTrue(any("oficial_authorized" in finding for finding in findings))
        self.assertTrue(any("agent_load_authorized" in finding for finding in findings))

    def test_11_creative_output_certification_must_remain_false(self):
        state = aud034_state()
        state["creative_output_certified"] = True
        self.assertTrue(any("creative_output_certified" in finding for finding in validate_current_state_data(state)))

    def test_12_intact_current_state_passes_direct_validation(self):
        self.assertEqual(validate_current_state_data(copy.deepcopy(aud034_state())), [])

    def test_13_scanner_rejects_unclassified_demo_enablement(self):
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
