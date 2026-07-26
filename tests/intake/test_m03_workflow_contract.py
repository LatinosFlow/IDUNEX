from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = REPO_ROOT / "governance" / "CURRENT_STATE.json"
BASELINE_PATH = REPO_ROOT / "governance" / "baseline" / "IDUNEX_CURRENT_TREE_MANIFEST.json"
MANIFEST_PATH = REPO_ROOT / "REPOSITORY_MANIFEST.yml"
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "m03-adversarial.yml"
HARNESS_PATH = REPO_ROOT / "tests" / "m03" / "test_adversarial_harness.py"

FILE_COUNT = 981
BYTE_COUNT = 47_324_981
TREE_SHA256 = "c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e"
FORBIDDEN_ACTIVE_CONTRACTS = (
    "8a3c191c266647acd754a56c1e5555ca1a36ab807d2e04e72a5ff21edb3e92bd",
    "47321777",
    "d6a66c316650a86c64ed20752b39e593f43f25e88b654538095124b7ebfedf8d",
    "47322002",
    "58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7",
    "47_323_574",
    "47323574",
    "22d64b639ed7657605787051d936bffc736cfa3d45b8799475adc28ef7ea0aeb",
    "47_324_957",
    "47324957",
)


def physical_identity() -> dict[str, object]:
    rows: list[tuple[str, int, str]] = []
    for path in (REPO_ROOT / "engine" / "IDUNEX").rglob("*"):
        if path.is_file():
            data = path.read_bytes()
            rows.append((path.relative_to(REPO_ROOT).as_posix(), len(data), hashlib.sha256(data).hexdigest()))
    rows.sort()
    aggregate = hashlib.sha256()
    for relative, size, digest in rows:
        aggregate.update(relative.encode("utf-8")); aggregate.update(b"\0")
        aggregate.update(str(size).encode("ascii")); aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii")); aggregate.update(b"\n")
    return {"file_count": len(rows), "byte_count": sum(row[1] for row in rows), "tree_sha256": aggregate.hexdigest()}


def current_manifest_identity(text: str) -> tuple[int, int, str]:
    match = re.search(r"current_corrected_tree:\n(?:.*\n)*?  file_count: (\d+)\n  bytes: (\d+)\n  tree_sha256: ([0-9a-f]{64})\n", text)
    if match is None:
        raise AssertionError("FAIL_AUD032_REPOSITORY_MANIFEST_CURRENT_IDENTITY_MISSING")
    return int(match.group(1)), int(match.group(2)), match.group(3)


def contract_failures(workflow: str, harness: str) -> list[str]:
    required_workflow = {
        "FAIL_AUD032_WORKFLOW_DISPATCH_ONLY": "on:\n  workflow_dispatch:",
        "FAIL_AUD032_WORKFLOW_SHA": f"default: {TREE_SHA256}",
        "FAIL_AUD032_WORKFLOW_FILE_COUNT": "if len(files) != 981:",
        "FAIL_AUD035_WORKFLOW_BYTE_COUNT": "if byte_count != 47_324_981:",
        "FAIL_AUD035_WORKFLOW_POSTFLIGHT_BYTE_COUNT": "identity.get('byte_count') != 47_324_981",
        "FAIL_AUD035_WORKFLOW_MANIFEST_BYTES": "r'bytes:\\s*47324981\\b'",
        "FAIL_AUD035_WORKFLOW_ISSUE": "'issue': 'AUD-035'",
        "FAIL_AUD035_WORKFLOW_M02": "'m02_result': 'NOT_RECOMPUTED_POST_AUD035'",
        "FAIL_AUD035_WORKFLOW_M03": "'m03_result': 'NOT_RECOMPUTED_POST_AUD035'",
        "FAIL_AUD032_WORKFLOW_OFICIAL_INTERLOCK": "'oficial_authorized': False",
        "FAIL_AUD032_WORKFLOW_AGENT_LOAD_INTERLOCK": "'agent_load_authorized': False",
        "FAIL_AUD032_WORKFLOW_AUD028_STATUS": "'status': 'CONSUMED'",
        "FAIL_AUD032_WORKFLOW_AUD028_AUTHORIZED": "'authorized': False",
        "FAIL_AUD032_WORKFLOW_AUD028_CONSUMED": "'consumed': True",
        "FAIL_AUD032_WORKFLOW_AUD028_GENERATE": "'generate_executions_allowed': 0",
        "FAIL_AUD032_WORKFLOW_AUD028_VALIDATE": "'validate_executions_allowed': 0",
        "FAIL_AUD032_WORKFLOW_AUD028_FAILCODE": "FAIL_AUD028_CONSUMED_INTERLOCK",
        "FAIL_AUD032_WORKFLOW_DECISION": "'M03_DECISION': 'NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY'",
        "FAIL_AUD032_WORKFLOW_CREATIVE": "'CREATIVE_OUTPUT_CERTIFIED': False",
    }
    required_harness = {
        "FAIL_AUD032_HARNESS_FILE_COUNT": "EXPECTED_FILE_COUNT = 981",
        "FAIL_AUD035_HARNESS_BYTE_COUNT": "EXPECTED_BYTE_COUNT = 47_324_981",
        "FAIL_AUD032_HARNESS_SHA": f'EXPECTED_ENGINE_TREE_SHA256 = "{TREE_SHA256}"',
        "FAIL_AUD032_HARNESS_DECISION": 'M03_DECISION = "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY"',
        "FAIL_AUD032_HARNESS_CREATIVE": '"CREATIVE_OUTPUT_CERTIFIED": False',
    }
    failures = [code for code, required in required_workflow.items() if required not in workflow]
    failures.extend(code for code, required in required_harness.items() if required not in harness)
    triggers = {"push": "FAIL_AUD032_M03_PUSH_TRIGGER", "pull_request": "FAIL_AUD032_M03_PULL_REQUEST_TRIGGER", "schedule": "FAIL_AUD032_M03_SCHEDULE_TRIGGER"}
    failures.extend(code for trigger, code in triggers.items() if re.search(rf"(?m)^  {trigger}:", workflow))
    failures.extend(f"FAIL_AUD032_OBSOLETE_ACTIVE_CONTRACT:{value}" for value in FORBIDDEN_ACTIVE_CONTRACTS if value in workflow or value in harness)
    return failures


class M03WorkflowContractTest(unittest.TestCase):
    def assert_rejected(self, workflow: str, harness: str, expected_code: str) -> None:
        self.assertIn(expected_code, contract_failures(workflow, harness))

    def test_current_state_baseline_physical_tree_and_manifest_are_in_parity(self):
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        expected = {"file_count": FILE_COUNT, "byte_count": BYTE_COUNT, "tree_sha256": TREE_SHA256}
        self.assertEqual(physical_identity(), expected)
        self.assertEqual({key: baseline.get(key) for key in expected}, expected)
        self.assertEqual(current_manifest_identity(MANIFEST_PATH.read_text(encoding="utf-8")), (FILE_COUNT, BYTE_COUNT, TREE_SHA256))
        self.assertEqual(state.get("issue"), "AUD-035")
        self.assertEqual(state.get("motor_status"), "EN_REVISION")
        self.assertEqual(state.get("m02_result"), "NOT_RECOMPUTED_POST_AUD035")
        self.assertEqual(state.get("m03_result"), "NOT_RECOMPUTED_POST_AUD035")
        for key in ("ready_for_project_demo_generation", "release_authorized", "tag_authorized", "productive_closure_authorized", "oficial_authorized", "agent_load_authorized", "creative_output_certified"):
            self.assertFalse(state.get(key), key)
        controlled = state.get("controlled_external_demo_execution", {})
        self.assertEqual({key: controlled.get(key) for key in ("status", "authorized", "consumed", "generate_executions_allowed", "validate_executions_allowed")}, {"status": "CONSUMED", "authorized": False, "consumed": True, "generate_executions_allowed": 0, "validate_executions_allowed": 0})

    def test_workflow_and_harness_contracts_are_current_and_static_only(self):
        self.assertEqual(contract_failures(WORKFLOW_PATH.read_text(encoding="utf-8"), HARNESS_PATH.read_text(encoding="utf-8")), [])

    def test_contract_checker_rejects_each_required_divergence(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        harness = HARNESS_PATH.read_text(encoding="utf-8")
        cases = (
            (workflow.replace(f"default: {TREE_SHA256}", "default: " + "0" * 64, 1), harness, "FAIL_AUD032_WORKFLOW_SHA"),
            (workflow.replace("if byte_count != 47_324_981:", "if byte_count != 1:", 1), harness, "FAIL_AUD035_WORKFLOW_BYTE_COUNT"),
            (workflow.replace("identity.get('byte_count') != 47_324_981", "identity.get('byte_count') != 1", 1), harness, "FAIL_AUD035_WORKFLOW_POSTFLIGHT_BYTE_COUNT"),
            (workflow.replace("if len(files) != 981:", "if len(files) != 1:", 1), harness, "FAIL_AUD032_WORKFLOW_FILE_COUNT"),
            (workflow, harness.replace(f'EXPECTED_ENGINE_TREE_SHA256 = "{TREE_SHA256}"', 'EXPECTED_ENGINE_TREE_SHA256 = "' + "0" * 64 + '"', 1), "FAIL_AUD032_HARNESS_SHA"),
            (workflow, harness.replace("EXPECTED_BYTE_COUNT = 47_324_981", "EXPECTED_BYTE_COUNT = 1", 1), "FAIL_AUD035_HARNESS_BYTE_COUNT"),
            (workflow, harness.replace("EXPECTED_FILE_COUNT = 981", "EXPECTED_FILE_COUNT = 1", 1), "FAIL_AUD032_HARNESS_FILE_COUNT"),
            (workflow.replace("'issue': 'AUD-035'", "'issue': 'AUD-030'", 1), harness, "FAIL_AUD035_WORKFLOW_ISSUE"),
            (workflow.replace("'m02_result': 'NOT_RECOMPUTED_POST_AUD035'", "'m02_result': 'M02_PASS'", 1), harness, "FAIL_AUD035_WORKFLOW_M02"),
            (workflow.replace("'m02_result': 'NOT_RECOMPUTED_POST_AUD035'", "'m02_result': 'NOT_RECOMPUTED_POST_AUD030'", 1), harness, "FAIL_AUD035_WORKFLOW_M02"),
            (workflow.replace("'m03_result': 'NOT_RECOMPUTED_POST_AUD035'", "'m03_result': 'M03_PASS'", 1), harness, "FAIL_AUD035_WORKFLOW_M03"),
            (workflow.replace("workflow_dispatch:", "push:", 1), harness, "FAIL_AUD032_M03_PUSH_TRIGGER"),
            (workflow.replace("workflow_dispatch:", "pull_request:", 1), harness, "FAIL_AUD032_M03_PULL_REQUEST_TRIGGER"),
            (workflow.replace("workflow_dispatch:", "schedule:", 1), harness, "FAIL_AUD032_M03_SCHEDULE_TRIGGER"),
            (workflow.replace("'status': 'CONSUMED'", "'status': 'AUTHORIZED'", 1), harness, "FAIL_AUD032_WORKFLOW_AUD028_STATUS"),
            (workflow.replace("'authorized': False", "'authorized': True", 1), harness, "FAIL_AUD032_WORKFLOW_AUD028_AUTHORIZED"),
            (workflow.replace("'consumed': True", "'consumed': False", 1), harness, "FAIL_AUD032_WORKFLOW_AUD028_CONSUMED"),
            (workflow.replace("'generate_executions_allowed': 0", "'generate_executions_allowed': 1", 1), harness, "FAIL_AUD032_WORKFLOW_AUD028_GENERATE"),
            (workflow.replace("'validate_executions_allowed': 0", "'validate_executions_allowed': 1", 1), harness, "FAIL_AUD032_WORKFLOW_AUD028_VALIDATE"),
        )
        for mutated_workflow, mutated_harness, expected_code in cases:
            with self.subTest(expected_code=expected_code):
                self.assert_rejected(mutated_workflow, mutated_harness, expected_code)

    def test_superseded_byte_identities_are_rejected_in_workflow_and_harness(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        harness = HARNESS_PATH.read_text(encoding="utf-8")
        for legacy in ("47_323_574", "47323574", "47_324_957", "47324957"):
            with self.subTest(surface="workflow", legacy=legacy):
                self.assertTrue(contract_failures(workflow + f"\n# {legacy}\n", harness))
            with self.subTest(surface="harness", legacy=legacy):
                self.assertTrue(contract_failures(workflow, harness + f"\n# {legacy}\n"))


if __name__ == "__main__":
    unittest.main()
