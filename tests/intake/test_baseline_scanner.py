import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.baseline_scanner import (
    CURRENT_MANIFEST_REL,
    CURRENT_TREE_BYTE_COUNT,
    CURRENT_TREE_FILE_COUNT,
    CURRENT_TREE_SHA256,
    PHYSICAL_MANIFEST_M02_SNAPSHOT,
    PHYSICAL_MANIFEST_M03_SNAPSHOT,
    PHYSICAL_MANIFEST_STATE_CLASSIFICATION,
    ROOT_M02_RESULT,
    ROOT_M03_RESULT,
    audit_repository,
    verify_manifest_records,
    write_artifacts,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


class BaselineScannerTest(unittest.TestCase):
    def test_repository_baseline_is_reproducible(self):
        report = audit_repository(REPO_ROOT)
        self.assertEqual(report["result"], "PASS", json.dumps(report, indent=2))
        self.assertEqual(report["aud003_scope_result"], "PARTIAL_PASS")
        self.assertEqual(report["root_issue"], "AUD-037")
        self.assertEqual(report["root_m02_result"], ROOT_M02_RESULT)
        self.assertEqual(report["root_m03_result"], ROOT_M03_RESULT)
        self.assertEqual(
            report["physical_manifest_m02_snapshot"], PHYSICAL_MANIFEST_M02_SNAPSHOT
        )
        self.assertEqual(
            report["physical_manifest_m03_snapshot"], PHYSICAL_MANIFEST_M03_SNAPSHOT
        )
        self.assertEqual(
            report["physical_manifest_state_classification"],
            PHYSICAL_MANIFEST_STATE_CLASSIFICATION,
        )
        self.assertEqual(report["current_tree_sha256"], CURRENT_TREE_SHA256)
        self.assertEqual(report["current_tree_file_count"], CURRENT_TREE_FILE_COUNT)
        self.assertEqual(report["current_tree_byte_count"], CURRENT_TREE_BYTE_COUNT)
        self.assertEqual(report["indexed_missing_path_count"], 0)
        self.assertEqual(report["physical_unmanifested_path_count"], 0)
        self.assertEqual(report["stale_active_manifest_path_count"], 0)
        self.assertEqual(report["obsolete_hash_count"], 0)

    def test_hash_mutation_is_rejected(self):
        manifest = json.loads((REPO_ROOT / CURRENT_MANIFEST_REL).read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temp_dir:
            engine = Path(temp_dir) / "IDUNEX"
            shutil.copytree(REPO_ROOT / "engine" / "IDUNEX", engine)
            target = engine / "00_INDEX" / "ACTIVE_VERSION.txt"
            target.write_text(target.read_text(encoding="utf-8") + "\nMUTATION\n", encoding="utf-8")
            result = verify_manifest_records(engine, manifest["files"], repository_paths=True)
        self.assertEqual(result["hash_mismatch_count"], 1)

    def test_cli_returns_machine_readable_pass(self):
        result = subprocess.run(
            [sys.executable, "tools/audit/baseline_scanner.py", "--repo-root", "."],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["result"], "PASS")
        self.assertEqual(report["root_m02_result"], ROOT_M02_RESULT)
        self.assertEqual(
            report["physical_manifest_m02_snapshot"],
            PHYSICAL_MANIFEST_M02_SNAPSHOT,
        )

    def test_aud037_uses_canonical_manifest_regenerator(self):
        self.assertEqual(write_artifacts(REPO_ROOT)["tree_sha256"], CURRENT_TREE_SHA256)


if __name__ == "__main__":
    unittest.main()
