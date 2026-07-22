import copy
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


ENGINE_TREE_SHA = "628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9"
PACKAGE_SHA = "53711cae748d3f8cda29e17d0a7663c3f73dbae6a691c82edfce704292cb2ac5"
MASTER_SHA = "1158d68f4863ead61c22472bc604a2aa32b475f4f3a6ed85d9e2d6d7d2d6708f"
PROMPT_SHA = "b" * 64


def pending_state() -> dict:
    return {
        "motor_status": "EN_REVISION",
        "m02_result": "M02_PASS",
        "ready_for_project_demo_generation": False,
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
        "controlled_external_demo_execution": {
            "schema_version": 1,
            "status": "PENDING_AUTHORIZATION",
            "authorized": False,
            "consumed": False,
            "execution_limit": 1,
            "execution_count": 0,
            "allowed_environment": "CHATGPT_NORMAL_EXTERNAL",
            "general_project_generation_enabled": False,
            "generate_executions_allowed": 0,
            "validate_executions_allowed": 0,
            "authorization_id": None,
            "repository_commit": "53a235461a99c37cda7e2fc6c4bd31df4b5bd736",
            "engine_tree_sha256": ENGINE_TREE_SHA,
            "engine_package_filename": "IDUNEX_MOTOR_v1.0.0.zip",
            "engine_package_sha256": PACKAGE_SHA,
            "master_report_filename": "Informe Maestro - Gobernanza, Arquitectura y Políticas Oficiales del Motor IDUNEX.pdf",
            "master_report_sha256": MASTER_SHA,
            "prompt_path": None,
            "prompt_sha256": None,
            "allows_release": False,
            "allows_tag": False,
            "allows_oficial": False,
            "allows_productive_closure": False,
            "allows_agent_load": False,
            "creative_output_certified": False,
        },
    }


def authorized_state() -> dict:
    state = pending_state()
    controlled = state["controlled_external_demo_execution"]
    controlled.update(
        {
            "status": "AUTHORIZED_NOT_CONSUMED",
            "authorized": True,
            "generate_executions_allowed": 1,
            "validate_executions_allowed": 1,
            "authorization_id": "AUD-028",
            "prompt_path": "governance/authority/IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt",
            "prompt_sha256": PROMPT_SHA,
        }
    )
    return state


def consumed_state() -> dict:
    state = authorized_state()
    controlled = state["controlled_external_demo_execution"]
    controlled.update(
        {
            "status": "CONSUMED",
            "authorized": False,
            "consumed": True,
            "execution_count": 1,
            "generate_executions_allowed": 0,
            "validate_executions_allowed": 0,
        }
    )
    return state


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
        self.assertEqual(report["controlled_external_demo_status"], "CONSUMED")
        self.assertFalse(report["controlled_external_demo_authorized"])
        self.assertTrue(report["controlled_external_demo_consumed"])

    def test_02_pending_authorization_is_valid(self):
        self.assertEqual(validate_current_state_data(pending_state()), [])

    def test_03_authorized_not_consumed_complete_is_valid(self):
        self.assertEqual(validate_current_state_data(authorized_state()), [])

    def test_04_authorized_without_prompt_sha_fails(self):
        state = authorized_state()
        state["controlled_external_demo_execution"]["prompt_sha256"] = None
        findings = validate_current_state_data(state)
        self.assertTrue(any("prompt_sha256" in finding for finding in findings))

    def test_05_authorized_with_invalid_sha_fails(self):
        state = authorized_state()
        state["controlled_external_demo_execution"]["prompt_sha256"] = "BAD_SHA"
        findings = validate_current_state_data(state)
        self.assertTrue(any("prompt_sha256" in finding for finding in findings))

    def test_06_consumed_and_authorized_simultaneously_fails(self):
        state = consumed_state()
        state["controlled_external_demo_execution"]["authorized"] = True
        findings = validate_current_state_data(state)
        self.assertTrue(any("simultaneously" in finding for finding in findings))

    def test_07_execution_limit_greater_than_one_fails(self):
        state = copy.deepcopy(pending_state())
        state["controlled_external_demo_execution"]["execution_limit"] = 2
        findings = validate_current_state_data(state)
        self.assertTrue(any("execution_limit" in finding for finding in findings))

    def test_08_general_project_generation_enabled_fails(self):
        state = copy.deepcopy(pending_state())
        state["controlled_external_demo_execution"][
            "general_project_generation_enabled"
        ] = True
        findings = validate_current_state_data(state)
        self.assertTrue(
            any("general_project_generation_enabled" in finding for finding in findings)
        )

    def test_09_ready_for_project_demo_generation_true_still_fails(self):
        state = copy.deepcopy(pending_state())
        state["ready_for_project_demo_generation"] = True
        findings = validate_current_state_data(state)
        self.assertTrue(
            any("ready_for_project_demo_generation" in finding for finding in findings)
        )

    def test_10_consumed_state_is_valid(self):
        self.assertEqual(validate_current_state_data(consumed_state()), [])

    def test_11_scanner_rejects_unclassified_ready_true(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            rogue = root / "engine" / "IDUNEX" / "00_INDEX" / "ROGUE_CERTIFICATE.txt"
            rogue.parent.mkdir(parents=True)
            rogue.write_text(
                "M02_RESULT=M02_PASS\nREADY_FOR_PROJECT_DEMO_GENERATION=TRUE\n",
                encoding="utf-8",
            )
            findings, historical_matches = scan_contradictions(root)
        self.assertTrue(findings)
        self.assertEqual(historical_matches, 0)


if __name__ == "__main__":
    unittest.main()
