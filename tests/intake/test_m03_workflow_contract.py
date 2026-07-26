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
BYTE_COUNT = 47_323_574
TREE_SHA256 = "58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7"
FORBIDDEN_ACTIVE_CONTRACTS = (
    "8a3c191c266647acd754a56c1e5555ca1a36ab807d2e04e72a5ff21edb3e92bd",
    "47321777",
    "d6a66c316650a86c64ed20752b39e593f43f25e88b654538095124b7ebfedf8d",
    "47322002",
)


def physical_identity() -> dict[str, object]:
    engine = REPO_ROOT / "engine" / "IDUNEX"
    rows: list[tuple[str, int, str]] = []
    for path in engine.rglob("*"):
        if path.is_file():
            data = path.read_bytes()
            rows.append((path.relative_to(REPO_ROOT).as_posix(), len(data), hashlib.sha256(data).hexdigest()))
    rows.sort()
    aggregate = hashlib.sha256()
    for relative, size, digest in rows:
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(str(size).encode("ascii"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")
    return {"file_count": len(rows), "byte_count": sum(row[1] for row in rows), "tree_sha256": aggregate.hexdigest()}


def current_manifest_identity(text: str) -> tuple[int, int, str]:
    match = re.search(
        r"current_corrected_tree:\n(?:.*\n)*?  file_count: (\d+)\n  bytes: (\d+)\n  tree_sha256: ([0-9a-f]{64})\n",
        text,
    )
    if match is None:
        raise AssertionError("FAIL_AUD032_REPOSITORY_MANIFEST_CURRENT_IDENTITY_MISSING")
    return int(match.group(1)), int(match.group(2)), match.group(3)


def contract_failures(workflow: str, harness: str) -> list[str]:
    failures: list[str] = []
    required_workflow = (
        "on:\n  workflow_dispatch:",
        f"default: {TREE_SHA256}",
        "if len(files) != 981:",
        "if byte_count != 47_323_574:",
        "r'bytes:\\s*47323574\\b'",
        "'issue': 'AUD-034'",
        "'m02_result': 'M02_PASS_RECOMPUTED_POST_AUD033'",
        "'m03_result': 'NOT_RECOMPUTED_POST_AUD030'",
        "'oficial_authorized': False",
        "'agent_load_authorized': False",
        "'M03_DECISION': 'NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY'",
        "'CREATIVE_OUTPUT_CERTIFIED': False",
    )
    for required in required_workflow:
        if required not in workflow:
            failures.append(f"FAIL_AUD032_WORKFLOW_CONTRACT:{required}")
    if re.search(r"(?m)^  (push|pull_request|schedule):", workflow):
        failures.append("FAIL_AUD032_M03_AUTOMATIC_TRIGGER")
    required_harness = (
        "EXPECTED_FILE_COUNT = 981",
        "EXPECTED_BYTE_COUNT = 47_323_574",
        f'EXPECTED_ENGINE_TREE_SHA256 = "{TREE_SHA256}"',
        'M03_DECISION = "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY"',
        '"CREATIVE_OUTPUT_CERTIFIED": False',
    )
    for required in required_harness:
        if required not in harness:
            failures.append(f"FAIL_AUD032_HARNESS_CONTRACT:{required}")
    for obsolete in FORBIDDEN_ACTIVE_CONTRACTS:
        if obsolete in workflow or obsolete in harness:
            failures.append(f"FAIL_AUD032_OBSOLETE_ACTIVE_CONTRACT:{obsolete}")
    return failures


class M03WorkflowContractTest(unittest.TestCase):
    def test_current_state_baseline_physical_tree_and_manifest_are_in_parity(self):
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(physical_identity(), {"file_count": FILE_COUNT, "byte_count": BYTE_COUNT, "tree_sha256": TREE_SHA256})
        self.assertEqual({key: baseline.get(key) for key in ("file_count", "byte_count", "tree_sha256")}, {"file_count": FILE_COUNT, "byte_count": BYTE_COUNT, "tree_sha256": TREE_SHA256})
        self.assertEqual(current_manifest_identity(MANIFEST_PATH.read_text(encoding="utf-8")), (FILE_COUNT, BYTE_COUNT, TREE_SHA256))
        self.assertEqual(state.get("issue"), "AUD-034")
        self.assertEqual(state.get("motor_status"), "EN_REVISION")
        self.assertEqual(state.get("m02_result"), "M02_PASS_RECOMPUTED_POST_AUD033")
        self.assertEqual(state.get("m03_result"), "NOT_RECOMPUTED_POST_AUD030")
        for key in ("ready_for_project_demo_generation", "release_authorized", "tag_authorized", "productive_closure_authorized", "oficial_authorized", "agent_load_authorized", "creative_output_certified"):
            self.assertFalse(state.get(key), key)
        controlled = state.get("controlled_external_demo_execution", {})
        self.assertEqual(controlled.get("status"), "CONSUMED")
        self.assertFalse(controlled.get("authorized"))
        self.assertTrue(controlled.get("consumed"))
        self.assertEqual(controlled.get("generate_executions_allowed"), 0)
        self.assertEqual(controlled.get("validate_executions_allowed"), 0)

    def test_workflow_and_harness_contracts_are_current_and_static_only(self):
        failures = contract_failures(WORKFLOW_PATH.read_text(encoding="utf-8"), HARNESS_PATH.read_text(encoding="utf-8"))
        self.assertEqual(failures, [], "\n".join(failures))

    def test_contract_checker_rejects_identity_authority_and_trigger_divergences(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        harness = HARNESS_PATH.read_text(encoding="utf-8")
        self.assertTrue(contract_failures(workflow.replace(TREE_SHA256, "0" * 64, 1), harness))
        self.assertTrue(contract_failures(workflow.replace("workflow_dispatch:", "push:", 1), harness))
        self.assertTrue(contract_failures(workflow.replace("'issue': 'AUD-034'", "'issue': 'AUD-030'", 1), harness))
        self.assertTrue(contract_failures(workflow, harness.replace("EXPECTED_BYTE_COUNT = 47_323_574", "EXPECTED_BYTE_COUNT = 47_321_777", 1)))


if __name__ == "__main__":
    unittest.main()
