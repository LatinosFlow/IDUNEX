import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
AUDIT_PATH = REPO_ROOT / "tools/audit/no_bloat_no_history_check.py"


def _load(path: Path):
    spec = importlib.util.spec_from_file_location("idunex_aud008_no_bloat", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class NoBloatNoHistoryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = _load(AUDIT_PATH)

    def test_current_repository_recomputes_clean(self):
        result = self.audit.audit_repo(REPO_ROOT)
        self.assertEqual(result["result"], "PASS", json.dumps(result, ensure_ascii=False, indent=2))
        self.assertEqual(result["active_tree"]["unjustified_duplicate_group_count"], 0)
        self.assertEqual(result["active_tree"]["active_h_route_count"], 0)
        self.assertEqual(result["historical_authority_conflict_count"], 0)
        self.assertEqual(result["motor_status"], "EN_REVISION")
        self.assertEqual(result["m02_result"], "M02_FAIL")

    def test_exact_duplicate_mutation_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="aud008_duplicate_") as temp_dir:
            engine = Path(temp_dir)
            (engine / "01_ACTIVE").mkdir()
            (engine / "01_ACTIVE/a.txt").write_text("same", encoding="utf-8")
            (engine / "01_ACTIVE/b.txt").write_text("same", encoding="utf-8")
            result = self.audit.scan_active_tree(engine)
        self.assertEqual(result["unjustified_duplicate_group_count"], 1)

    def test_active_h_route_mutation_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="aud008_h_route_") as temp_dir:
            engine = Path(temp_dir)
            (engine / "03_ACTIVE").mkdir()
            (engine / "03_ACTIVE/H500_STALE_PROOF.json").write_text("{}", encoding="utf-8")
            result = self.audit.scan_active_tree(engine)
        self.assertEqual(result["active_h_route_count"], 1)

    def test_h_route_inside_historical_zone_is_allowed(self):
        with tempfile.TemporaryDirectory(prefix="aud008_history_") as temp_dir:
            engine = Path(temp_dir)
            historical = engine / "14_HISTORICAL_NON_AUTHORITY"
            historical.mkdir()
            (historical / "H500_STALE_PROOF.json").write_text("{}", encoding="utf-8")
            result = self.audit.scan_active_tree(engine)
        self.assertEqual(result["active_h_route_count"], 0)

    def test_manifest_rejects_active_authority_in_history(self):
        with tempfile.TemporaryDirectory(prefix="aud008_authority_") as temp_dir:
            engine = Path(temp_dir)
            target = engine / "14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/old.json"
            target.parent.mkdir(parents=True)
            target.write_text("{}", encoding="utf-8")
            payload = {
                "movements": [{
                    "origin": "99_MANIFESTS_SHA_LINEAGE/old.json",
                    "destination": "14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/old.json",
                    "operation": "MOVE_TO_HISTORICAL",
                    "authority_after": "ACTIVE",
                    "sha256_after": self.audit._sha256(target),
                }]
            }
            conflicts = self.audit.movement_conflicts(engine, payload)
        self.assertTrue(any(item["code"] == "HISTORICAL_EVIDENCE_HAS_ACTIVE_AUTHORITY" for item in conflicts))


if __name__ == "__main__":
    unittest.main()
