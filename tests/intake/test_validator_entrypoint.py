import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.validator_entrypoint_check import REGISTRY_PATH, check_repository


REPO_ROOT = Path(__file__).resolve().parents[2]
ENTRYPOINT = (
    REPO_ROOT
    / "engine"
    / "IDUNEX"
    / "99_MANIFESTS_SHA_LINEAGE"
    / "VALIDATE_IDUNEX_RUNTIME.py"
)
class ValidatorEntrypointTest(unittest.TestCase):
    def test_repository_has_one_authoritative_entrypoint(self):
        findings, summary = check_repository(REPO_ROOT)
        self.assertEqual(findings, [])
        self.assertEqual(summary["entrypoint_count"], 1)
        self.assertEqual(summary["subvalidator_count"], 20)

    def test_scanner_rejects_a_second_global_entrypoint(self):
        registry = json.loads((REPO_ROOT / REGISTRY_PATH).read_text(encoding="utf-8"))
        mutated = copy.deepcopy(registry)
        second = dict(mutated["engine_surfaces"]["subvalidators"][0])
        second.update(
            {
                "role": "GLOBAL_VALIDATOR_ENTRYPOINT",
                "public_cli": True,
                "global_closure_capable": True,
            }
        )
        mutated["engine_surfaces"]["authoritative_entrypoints"].append(second)
        mutated["global_closure_entrypoint_count"] = 2

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "registry.json"
            path.write_text(json.dumps(mutated), encoding="utf-8")
            findings, _ = check_repository(REPO_ROOT, path)
        self.assertTrue(any("exactly one authoritative entrypoint" in item for item in findings))

    def test_every_direct_secondary_cli_is_blocked(self):
        registry = json.loads((REPO_ROOT / REGISTRY_PATH).read_text(encoding="utf-8"))
        engine_root = REPO_ROOT / "engine" / "IDUNEX"
        for surface in registry["engine_surfaces"]["subvalidators"]:
            with self.subTest(subvalidator=surface["id"]):
                result = subprocess.run(
                    [sys.executable, str(engine_root / surface["path"])],
                    cwd=REPO_ROOT,
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, 3, result.stdout + result.stderr)
                payload = json.loads(result.stdout)
                self.assertEqual(
                    payload["result"], "BLOCKED_NON_AUTHORITATIVE_ENTRYPOINT"
                )
                self.assertFalse(payload["global_closure_authorized"])
                self.assertFalse(payload["m02_decision_authority"])

    def test_entrypoint_can_delegate_the_same_subcheck_without_global_closure(self):
        result = subprocess.run(
            [
                sys.executable,
                str(ENTRYPOINT),
                "--subcheck",
                "VALIDATE_PROMPTS_PROJECT_POLICY",
                "--",
                str(REPO_ROOT / "engine" / "IDUNEX"),
            ],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertIn(result.returncode, (0, 1), result.stdout + result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["scope"], "SUBCHECK_DELEGATION")
        self.assertFalse(payload["global_closure_authorized"])
        self.assertFalse(payload["m02_decision_authority"])
        self.assertNotEqual(payload["result"], "PASS")


if __name__ == "__main__":
    unittest.main()
