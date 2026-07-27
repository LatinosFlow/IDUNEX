from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = REPO_ROOT / "governance/CURRENT_STATE.json"
BASELINE_PATH = REPO_ROOT / "governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json"
MANIFEST_PATH = REPO_ROOT / "REPOSITORY_MANIFEST.yml"
WORKFLOW_PATH = REPO_ROOT / ".github/workflows/m03-adversarial.yml"
HARNESS_PATH = REPO_ROOT / "tests/m03/test_adversarial_harness.py"

FILE_COUNT = 981
BYTE_COUNT = 47_370_003
TREE_SHA256 = "87c0e9e681a3a4995d4f096eaaa73cd5c7a889e9c10a5f0f4b3c9897e80c2346"
SUPERSEDED_TREE_SHA256 = "c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e"
INTERMEDIATE_TREE_SHA256 = "ff6a3a6d376206bd052d124031a72ca55c90827f5f69e3d3c851033128028ea3"


def physical_identity() -> dict[str, object]:
    rows: list[tuple[str, int, str]] = []
    for path in (REPO_ROOT / "engine/IDUNEX").rglob("*"):
        if path.is_file():
            data = path.read_bytes()
            rows.append((path.relative_to(REPO_ROOT).as_posix(), len(data), hashlib.sha256(data).hexdigest()))
    rows.sort()
    aggregate = hashlib.sha256()
    for relative, size, digest in rows:
        aggregate.update(f"{relative}\0{size}\0{digest}\n".encode("utf-8"))
    return {"file_count": len(rows), "byte_count": sum(row[1] for row in rows), "tree_sha256": aggregate.hexdigest()}


def current_manifest_identity(text: str) -> tuple[int, int, str]:
    match = re.search(
        r"current_corrected_tree:\n(?:.*\n)*?  file_count: (\d+)\n"
        r"  bytes: (\d+)\n  tree_sha256: ([0-9a-f]{64})\n",
        text,
    )
    if match is None:
        raise AssertionError("FAIL_AUD037_REPOSITORY_MANIFEST_CURRENT_IDENTITY_MISSING")
    return int(match.group(1)), int(match.group(2)), match.group(3)


def contract_failures(workflow: str, harness: str) -> list[str]:
    required_workflow = {
        "FAIL_AUD037_WORKFLOW_DISPATCH_ONLY": "on:\n  workflow_dispatch:",
        "FAIL_AUD037_WORKFLOW_SHA": f"default: {TREE_SHA256}",
        "FAIL_AUD037_WORKFLOW_FILE_COUNT": "if len(files) != 981:",
        "FAIL_AUD037_WORKFLOW_BYTE_COUNT": "if byte_count != 47_370_003:",
        "FAIL_AUD037_WORKFLOW_POSTFLIGHT_BYTE_COUNT": "identity.get('byte_count') != 47_370_003",
        "FAIL_AUD037_WORKFLOW_MANIFEST_BYTES": "r'bytes:\\s*47370003\\b'",
        "FAIL_AUD037_WORKFLOW_ISSUE": "'issue': 'AUD-037'",
        "FAIL_AUD037_WORKFLOW_M02_GATE": "'m02_result': 'M02_PASS'",
        "FAIL_AUD037_WORKFLOW_M03": "'m03_result': 'NOT_RECOMPUTED_POST_AUD037'",
        "FAIL_AUD037_WORKFLOW_M02_EVIDENCE_GATE": "FAIL_M02_FORMALIZATION_REQUIRED_FOR_M03",
        "FAIL_AUD037_WORKFLOW_M02_TECHNICAL": "'technical_result': 'PASS'",
        "FAIL_AUD037_WORKFLOW_M02_AUDIT": "'independent_audit_result': 'VALIDADO_PASS'",
        "FAIL_AUD037_WORKFLOW_M02_CLASS": "'evidence_class': 'VALIDATED_CURRENT_TREE_EVIDENCE'",
        "FAIL_AUD037_WORKFLOW_M02_FORMALIZATION": "'governance_formalization_status': 'VALIDADO'",
        "FAIL_AUD037_WORKFLOW_M02_DECISION": "'workflow_decision': 'NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY'",
        "FAIL_AUD037_WORKFLOW_OFFICIAL_EVIDENCE_INTERLOCK": "FAIL_PREMATURE_OFFICIAL_TRANSITION_EVIDENCE",
        "FAIL_AUD037_WORKFLOW_OFICIAL_INTERLOCK": "'oficial_authorized': False",
        "FAIL_AUD037_WORKFLOW_AGENT_LOAD_INTERLOCK": "'agent_load_authorized': False",
        "FAIL_AUD037_WORKFLOW_AUD028_STATUS": "'status': 'CONSUMED'",
        "FAIL_AUD037_WORKFLOW_AUD028_AUTHORIZED": "'authorized': False",
        "FAIL_AUD037_WORKFLOW_AUD028_CONSUMED": "'consumed': True",
        "FAIL_AUD037_WORKFLOW_AUD028_EXECUTION_COUNT": "'execution_count': 1",
        "FAIL_AUD037_WORKFLOW_AUD028_GENERATE": "'generate_executions_allowed': 0",
        "FAIL_AUD037_WORKFLOW_AUD028_VALIDATE": "'validate_executions_allowed': 0",
        "FAIL_AUD037_WORKFLOW_DECISION": "'M03_DECISION': 'NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY'",
        "FAIL_AUD037_WORKFLOW_CREATIVE": "'CREATIVE_OUTPUT_CERTIFIED': False",
    }
    required_harness = {
        "FAIL_AUD037_HARNESS_FILE_COUNT": "EXPECTED_FILE_COUNT = 981",
        "FAIL_AUD037_HARNESS_BYTE_COUNT": "EXPECTED_BYTE_COUNT = 47_370_003",
        "FAIL_AUD037_HARNESS_SHA": f'EXPECTED_ENGINE_TREE_SHA256 = "{TREE_SHA256}"',
        "FAIL_AUD037_HARNESS_DECISION": 'M03_DECISION = "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY"',
        "FAIL_AUD037_HARNESS_CREATIVE": '"CREATIVE_OUTPUT_CERTIFIED": False',
    }
    failures = [code for code, token in required_workflow.items() if token not in workflow]
    failures.extend(code for code, token in required_harness.items() if token not in harness)
    for trigger in ("push", "pull_request", "schedule"):
        if re.search(rf"(?m)^  {trigger}:", workflow):
            failures.append(f"FAIL_AUD037_M03_{trigger.upper()}_TRIGGER")
    return failures


class M03WorkflowContractTest(unittest.TestCase):
    def test_current_state_baseline_physical_tree_and_manifest_are_in_parity(self):
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        expected = {"file_count": FILE_COUNT, "byte_count": BYTE_COUNT, "tree_sha256": TREE_SHA256}
        self.assertEqual(physical_identity(), expected)
        self.assertEqual({key: baseline.get(key) for key in expected}, expected)
        self.assertEqual(current_manifest_identity(MANIFEST_PATH.read_text(encoding="utf-8")), (FILE_COUNT, BYTE_COUNT, TREE_SHA256))
        self.assertEqual(state["issue"], "AUD-037")
        self.assertEqual(state["m02_result"], "NOT_RECOMPUTED_POST_AUD037")
        self.assertEqual(state["m03_result"], "NOT_RECOMPUTED_POST_AUD037")
        self.assertEqual(state["prior_m02_recomputation_evidence"]["engine_tree_sha256"], SUPERSEDED_TREE_SHA256)
        self.assertFalse(state["prior_m02_recomputation_evidence"]["current_tree_applicability"])
        self.assertEqual(state["engine_change_control"]["previous_engine_tree_sha256"], INTERMEDIATE_TREE_SHA256)
        self.assertIn("INTERMEDIATE", state["engine_change_control"]["previous_engine_tree_classification"])

    def test_m03_workflow_is_static_and_blocked_until_formalized_m02(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        harness = HARNESS_PATH.read_text(encoding="utf-8")
        self.assertEqual(contract_failures(workflow, harness), [])
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        self.assertNotEqual(state["m02_result"], "M02_PASS")
        self.assertNotIn("m02_evidence", state)

    def test_contract_checker_rejects_required_divergences(self):
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        harness = HARNESS_PATH.read_text(encoding="utf-8")
        cases = (
            (workflow.replace(f"default: {TREE_SHA256}", "default: " + "0" * 64, 1), harness, "FAIL_AUD037_WORKFLOW_SHA"),
            (workflow.replace("if byte_count != 47_370_003:", "if byte_count != 1:", 1), harness, "FAIL_AUD037_WORKFLOW_BYTE_COUNT"),
            (workflow.replace("if len(files) != 981:", "if len(files) != 1:", 1), harness, "FAIL_AUD037_WORKFLOW_FILE_COUNT"),
            (workflow.replace("'issue': 'AUD-037'", "'issue': 'AUD-030'", 1), harness, "FAIL_AUD037_WORKFLOW_ISSUE"),
            (workflow.replace("'m02_result': 'M02_PASS'", "'m02_result': 'NOT_RECOMPUTED_POST_AUD037'", 1), harness, "FAIL_AUD037_WORKFLOW_M02_GATE"),
            (workflow.replace("'governance_formalization_status': 'VALIDADO'", "'governance_formalization_status': 'PENDING'", 1), harness, "FAIL_AUD037_WORKFLOW_M02_FORMALIZATION"),
            (workflow.replace("workflow_dispatch:", "push:", 1), harness, "FAIL_AUD037_M03_PUSH_TRIGGER"),
            (workflow, harness.replace(f'EXPECTED_ENGINE_TREE_SHA256 = "{TREE_SHA256}"', 'EXPECTED_ENGINE_TREE_SHA256 = "' + "0" * 64 + '"', 1), "FAIL_AUD037_HARNESS_SHA"),
        )
        for mutated_workflow, mutated_harness, expected_code in cases:
            with self.subTest(expected_code=expected_code):
                self.assertIn(expected_code, contract_failures(mutated_workflow, mutated_harness))


if __name__ == "__main__":
    unittest.main()
