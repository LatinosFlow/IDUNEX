import subprocess
import sys


def test_intake_audit_passes():
    result = subprocess.run(
        [sys.executable, "tools/audit/intake_audit.py", "--repo-root", "."],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
