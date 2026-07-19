import tempfile
import unittest
from pathlib import Path

from tests.intake.post_demo_support import control_spec, load_factory, read_json


class AgentLoadContractSurfacesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = load_factory("idunex_agent_load")

    def test_required_surfaces_are_materialized_10_of_10_per_agent(self):
        with tempfile.TemporaryDirectory(prefix="idunex_agent_load_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            for platform in ("CHATGPT", "COPILOT"):
                base = project / "03_AGENTS" / platform / "02_AGENT_LOAD_SURFACES"
                self.assertEqual({p.name for p in base.iterdir()}, set(self.factory.PROJECT_AGENT_LOAD_SURFACE_FILES.values()))
                manifest = read_json(project / "03_AGENTS" / platform / "03_MANIFESTS/AGENT_LOAD_SURFACE_MANIFEST.json")
                self.assertEqual(manifest["required_count"], 10)
                self.assertEqual(manifest["actual_count"], 10)
                self.assertEqual(manifest["result"], "PASS")
            index = read_json(project / "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json")
            self.assertEqual(self.factory.validate_post_demo_required_surfaces(project, index), [])

    def test_missing_surface_blocks_contract(self):
        with tempfile.TemporaryDirectory(prefix="idunex_agent_mutation_") as td:
            project = self.factory.make_project(control_spec(), Path(td))
            (project / "03_AGENTS/CHATGPT/02_AGENT_LOAD_SURFACES/NEGATIVE_AVOID_GLOBAL.json").unlink()
            index = read_json(project / "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json")
            codes = {x["fail_code"] for x in self.factory.validate_post_demo_required_surfaces(project, index)}
            self.assertIn("FAIL_AGENT_LOAD_CONTRACT", codes)


if __name__ == "__main__":
    unittest.main()
