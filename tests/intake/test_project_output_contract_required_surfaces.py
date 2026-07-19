import tempfile
import unittest
from pathlib import Path

from tests.intake.post_demo_support import control_spec, load_factory, read_json


class ProjectOutputContractRequiredSurfacesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = load_factory("idunex_project_output")

    def test_model_registry_and_no_drift_are_cross_referenced(self):
        with tempfile.TemporaryDirectory(prefix="idunex_output_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            index = read_json(project / "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json")
            registry = read_json(project / "00_PROJECT_INDEX/MODEL_REGISTRY.json")
            ledger = read_json(project / "01_CANON/NO_DRIFT_LEDGERS.json")
            self.assertEqual([m["model_id"] for m in registry["models"]], [m["model_id"] for m in index["models"]])
            self.assertEqual({m["model_id"] for m in ledger["models"]}, {m["model_id"] for m in index["models"]})
            self.assertEqual(self.factory.validate_post_demo_required_surfaces(project, index), [])

    def test_missing_model_registry_and_no_drift_block(self):
        with tempfile.TemporaryDirectory(prefix="idunex_output_mutation_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            index = read_json(project / "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json")
            (project / "00_PROJECT_INDEX/MODEL_REGISTRY.json").unlink()
            (project / "01_CANON/NO_DRIFT_LEDGERS.json").unlink()
            codes = {x["fail_code"] for x in self.factory.validate_post_demo_required_surfaces(project, index)}
            self.assertIn("FAIL_MODEL_REGISTRY_CONTRACT", codes)
            self.assertIn("FAIL_NO_DRIFT_CONTRACT", codes)


if __name__ == "__main__":
    unittest.main()
