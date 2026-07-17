import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.audit.baseline_scanner import (
    CURRENT_MANIFEST_REL,
    audit_repository,
    verify_manifest_records,
)


REPO_ROOT = Path(__file__).resolve().parents[2]


class BaselineScannerTest(unittest.TestCase):
    def test_repository_baseline_is_reproducible(self):
        report = audit_repository(REPO_ROOT)
        self.assertEqual(report["result"], "PASS", json.dumps(report, indent=2))
        self.assertEqual(report["aud003_scope_result"], "PARTIAL_PASS")
        self.assertEqual(report["m02_result"], "M02_FAIL")
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
        self.assertEqual(json.loads(result.stdout)["result"], "PASS")


if __name__ == "__main__":
    unittest.main()
