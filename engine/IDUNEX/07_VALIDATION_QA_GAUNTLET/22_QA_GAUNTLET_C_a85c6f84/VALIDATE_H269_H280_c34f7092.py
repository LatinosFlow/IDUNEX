#!/usr/bin/env python3
from pathlib import Path
import json, os, signal, subprocess, sys, time
sys.dont_write_bytecode = True

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
DEFAULT_CHILD_TIMEOUT_SECONDS = int(os.environ.get("IDUNEX_CHILD_VALIDATOR_TIMEOUT_SECONDS", "120"))
TIMEOUT_FAIL_CODE = "FAIL_CHILD_VALIDATOR_TIMEOUT_OR_STUCK_PROCESS"
validators = [
    "VALIDATE_PROJECT_ACTIVE_RESULTS_ALL_PASS.py",
    "VALIDATE_PROJECT_ZIP_REOPENED_COUNTS_AUTHORITATIVE.py",
    "VALIDATE_AGENT_FORENSIC_COMPANION_LEDGER_TRUTHFULNESS.py",
    "VALIDATE_PROJECT_PROMPT_PACK_CLASSIFICATION.py",
    "VALIDATE_RUNTIME_CANONICAL_MODEL_NAME_ALLOWLIST.py",
    "VALIDATE_PROJECT_EXACT_DUPLICATE_ALLOWLIST_VISIBLE.py",
    "VALIDATE_ACTIVE_PLACEHOLDER_AND_AMBIGUOUS_TOKEN_GUARD.py",
    "VALIDATE_PROJECT_MATRIX_COMPLETION_PROOF.py",
    "VALIDATE_CREATIVE_CERTIFICATION_TRUTHFULNESS.py",
    "VALIDATE_FINAL_CERTIFICATE_SURFACE_SYNC.py",
]


def _process_group_members(pgid: int) -> list[int]:
    if os.name != "posix":
        return []
    try:
        ps = subprocess.run(
            ["ps", "-o", "pid=", "-g", str(pgid)],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=3,
            check=False,
        )
        return sorted({int(x.strip()) for x in ps.stdout.splitlines() if x.strip().isdigit()})
    except Exception:
        return []


def _kill_process_group(pgid: int) -> None:
    if os.name != "posix":
        return
    try:
        os.killpg(pgid, signal.SIGTERM)
    except ProcessLookupError:
        return
    except Exception:
        return
    deadline = time.monotonic() + 3.0
    while time.monotonic() < deadline:
        if not _process_group_members(pgid):
            return
        time.sleep(0.05)
    try:
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        return
    except Exception:
        return


def run_child_validator(path: Path, timeout_seconds: int = DEFAULT_CHILD_TIMEOUT_SECONDS) -> dict:
    cmd = [sys.executable, str(path), str(root)]
    start = time.monotonic()
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=(os.name == "posix"),
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    pgid = None
    if os.name == "posix":
        try:
            pgid = os.getpgid(proc.pid)
        except Exception:
            pgid = None
    timed_out = False
    killed_tree = False
    try:
        stdout, stderr = proc.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        killed_tree = True
        if pgid is not None:
            _kill_process_group(pgid)
        else:
            proc.kill()
        try:
            stdout, stderr = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
    rc = proc.returncode
    live_pids_after = _process_group_members(pgid) if pgid is not None else ([] if proc.poll() is not None else [proc.pid])
    seconds = round(time.monotonic() - start, 3)
    payload = None
    parse_error = None
    if stdout and not timed_out:
        try:
            payload = json.loads(stdout)
        except Exception as exc:
            parse_error = str(exc)
    result = payload.get("result") if isinstance(payload, dict) else None
    fail_codes = []
    if timed_out or live_pids_after:
        fail_codes.append(TIMEOUT_FAIL_CODE)
    elif parse_error:
        fail_codes.append("FAIL_H269_H280_VALIDATOR_STDOUT_INVALID")
    elif rc != 0 or result != "PASS":
        if isinstance(payload, dict) and isinstance(payload.get("fail_codes"), list):
            fail_codes.extend(payload.get("fail_codes"))
        fail_codes.append("FAIL_H269_H280_CHILD_VALIDATOR_RC_OR_RESULT")
    return {
        "validator": path.name,
        "command": cmd,
        "rc": rc,
        "seconds": seconds,
        "timeout_seconds": timeout_seconds,
        "timed_out": timed_out,
        "killed_process_group": killed_tree,
        "stdout_captured": True,
        "stderr_captured": True,
        "stdout_tail": (stdout or "")[-1000:],
        "stderr_tail": (stderr or "")[-1000:],
        "payload_result": result,
        "payload": payload if isinstance(payload, dict) else None,
        "stdout_parse_error": parse_error,
        "process_group_id": pgid,
        "live_pids_after": live_pids_after,
        "no_live_processes_after": len(live_pids_after) == 0,
        "fail_codes": fail_codes,
    }

fail = []
results = {}
lifecycle = []
for v in validators:
    p = root / "99_MANIFESTS_SHA_LINEAGE" / v
    if not p.is_file():
        item = {"validator": v, "fail_codes": ["FAIL_H269_H280_VALIDATOR_MISSING"]}
        fail.append(item)
        lifecycle.append(item)
        continue
    item = run_child_validator(p)
    lifecycle.append(item)
    results[v] = {
        "rc": item.get("rc"),
        "payload_result": item.get("payload_result"),
        "timed_out": item.get("timed_out"),
        "no_live_processes_after": item.get("no_live_processes_after"),
    }
    if item.get("fail_codes"):
        fail.append({"validator": v, "fail_codes": item.get("fail_codes", []), "rc": item.get("rc"), "timed_out": item.get("timed_out"), "live_pids_after": item.get("live_pids_after", [])})

out = {
    "scope": "H269_H280_APPLIED_ON_H01_H268",
    "lifecycle_policy": "BOUNDED_CHILD_VALIDATORS_WITH_PROCESS_GROUP_KILL_TREE",
    "timeout_fail_code": TIMEOUT_FAIL_CODE,
    "timeout_seconds_per_child": DEFAULT_CHILD_TIMEOUT_SECONDS,
    "wrapper_observes_real_child_rc": True,
    "stdout_stderr_captured_without_pipe_deadlock": True,
    "validators": results,
    "child_lifecycle": lifecycle,
    "no_live_processes_after_all_children": all(item.get("no_live_processes_after", False) for item in lifecycle if "no_live_processes_after" in item),
    "H269-H280_APPLIED": "PASS" if not fail else "FAIL",
    "VALIDADORES_H269_H280_PASS": "PASS" if not fail else "FAIL",
    "validators_fail": len(fail),
    "blocking_warnings": 0 if not fail else 1,
    "fail_codes": [] if not fail else sorted({code for item in fail for code in item.get("fail_codes", [])}) or ["FAIL_H269_H280_VALIDATOR_SUITE"],
    "failures": fail,
    "CREATIVE_OUTPUT_CERTIFIED": False,
    "result": "PASS" if not fail else "FAIL",
}
# VALIDATOR_OUTPUT_NORMALIZATION_V1_0_0: standard active validator result fields; no validation weakening.
if 'validators_fail' not in out and 'VALIDATORS_FAIL' not in out:
    _errs = out.get('errors') or out.get('failures') or out.get('fail_codes') or out.get('FAIL_CODES') or []
    out['validators_fail'] = 0 if out.get('result') == 'PASS' else len(_errs)
if 'blocking_warnings' not in out and 'BLOCKING_WARNINGS' not in out:
    out['blocking_warnings'] = 0
if 'fail_codes' not in out and 'FAIL_CODES' not in out:
    _errs = out.get('errors') or out.get('failures') or []
    out['fail_codes'] = [] if out.get('result') == 'PASS' else [e.get('code') for e in _errs if isinstance(e, dict) and e.get('code')]
if 'CREATIVE_OUTPUT_CERTIFIED' not in out and 'creative_output_certified' not in out:
    out['CREATIVE_OUTPUT_CERTIFIED'] = False

print(json.dumps(out, ensure_ascii=False, indent=2))
sys.exit(0 if not fail else 1)
