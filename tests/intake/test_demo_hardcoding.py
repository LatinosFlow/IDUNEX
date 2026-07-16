import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
FACTORY_PATH = REPO_ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py"
RUNNER_PATH = REPO_ROOT / "engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py"
AUDIT_PATH = REPO_ROOT / "tools/audit/demo_hardcoding_check.py"


def _load(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class DemoHardcodingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sys.dont_write_bytecode = True
        cls.audit = _load(AUDIT_PATH, "idunex_demo_hardcoding_audit")
        cls.factory = _load(FACTORY_PATH, "idunex_project_factory_aud007")
        cls.runner = _load(RUNNER_PATH, "idunex_matrix_runner_aud007")

    def test_repository_has_no_active_named_project_branch(self):
        result = self.audit.audit_repo(REPO_ROOT)
        self.assertEqual(result["result"], "PASS", json.dumps(result["failures"], ensure_ascii=False, indent=2))
        self.assertEqual(result["active_named_project_branch_count"], 0)
        self.assertEqual(result["prohibited_active_literal_reference_count"], 0)

    def test_ast_guard_rejects_exact_project_name_comparison(self):
        with tempfile.TemporaryDirectory(prefix="aud007_ast_exact_") as temp_dir:
            mutated = Path(temp_dir) / "mutated_factory.py"
            mutated.write_text(
                'def select(project_name):\n    if project_name == "Proyecto 000 Demo":\n        return "special"\n',
                encoding="utf-8",
            )
            findings = self.audit.hardcoded_named_project_branches(mutated)
        self.assertEqual(len(findings), 1)
        self.assertIn("project_name ==", findings[0]["condition"])

    def test_factory_self_test_case_fails_for_reintroduced_branch(self):
        with tempfile.TemporaryDirectory(prefix="aud007_factory_self_test_") as temp_dir:
            mutated = Path(temp_dir) / "mutated_factory.py"
            mutated.write_text(
                'def select(project_name):\n    if project_name == "Proyecto 000 Demo":\n        return "special"\n',
                encoding="utf-8",
            )
            case = self.factory._aud007_factory_hardcoding_mutation_case(mutated)
        self.assertEqual(case["case"], "463_H27_FACTORY_HARDCODED_DEMO_BRANCH_BLOCKED")
        self.assertEqual(case["result"], "FAIL")
        self.assertTrue(case["observed"])

    def test_ast_guard_rejects_normalized_equivalent(self):
        with tempfile.TemporaryDirectory(prefix="aud007_ast_normalized_") as temp_dir:
            mutated = Path(temp_dir) / "mutated_factory.py"
            mutated.write_text(
                'def select(project_name):\n    return "special" if project_name == "PROYECTO_000_DEMO" else "generic"\n',
                encoding="utf-8",
            )
            findings = self.audit.hardcoded_named_project_branches(mutated)
        self.assertEqual(len(findings), 1)

    def test_external_validation_flag_is_name_neutral(self):
        alpha = self.factory._project_policy_status_payload("IDUNEX_PROJECT_ALPHA", False, True)
        beta = self.factory._project_policy_status_payload("IDUNEX_PROJECT_BETA", False, True)
        alpha.pop("project_id")
        beta.pop("project_id")
        self.assertEqual(alpha, beta)
        self.assertTrue(alpha["PROJECT_EXTERNAL_VALIDATION_REQUIRED"])
        self.assertNotIn("PROJECT_DEMO_PASS", alpha)

    def test_runner_is_exactly_thirty_non_demo_cases(self):
        cases = self.runner.cases()
        self.assertEqual(len(cases), 30)
        self.assertEqual({level: sum(case["level"] == level for case in cases) for level in ("basic", "intermediate", "complete")}, {"basic": 10, "intermediate": 10, "complete": 10})
        self.assertFalse(any("demo" in json.dumps(case).casefold() for case in cases))

    def test_non_demo_n1_generation_and_validation_do_not_use_demo_name(self):
        spec = {
            "project_name": "Proyecto Control Alfa",
            "external_validation_required": True,
            "project_entity_profile": self.factory.fixture_entity_profile(),
            "models": [
                {
                    "name": "CONTROL_MODEL_001 IDENTITY",
                    "age": 28,
                    "origin": "SYNTH_ORIGIN_CONTROL",
                    "gender": "persona adulta ficticia",
                    "role": "comunicador de marca",
                    "height_cm": 170,
                }
            ],
        }
        with tempfile.TemporaryDirectory(prefix="aud007_n1_") as temp_dir:
            root = self.factory.make_project(spec, Path(temp_dir))
            validation = self.factory.validate_project(root)
            manifest = json.loads((root / "00_PROJECT_INDEX/PROJECT_MANIFEST.json").read_text(encoding="utf-8"))
            status = json.loads((root / "00_PROJECT_INDEX/PROJECT_STATUS_CONTRACT.json").read_text(encoding="utf-8"))
            generated_names = [path.name.upper() for path in root.rglob("*")]
        self.assertEqual(root.name, "IDUNEX_PROJECT_PROYECTO_CONTROL_ALFA_v1.0.0")
        self.assertTrue(manifest["PROJECT_EXTERNAL_VALIDATION_REQUIRED"])
        self.assertTrue(status["PROJECT_EXTERNAL_VALIDATION_REQUIRED"])
        self.assertFalse(any("PROYECTO_000_DEMO" in name for name in generated_names))
        self.assertFalse(any("DEMO" in code for code in validation.get("fail_codes", [])))
        self.assertTrue(set(validation.get("fail_codes", [])).issubset({"FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE"}))


if __name__ == "__main__":
    unittest.main()
