#!/usr/bin/env python3
"""Execution boundary for AUD-009 validator subchecks.

Secondary validators keep their functional implementation, but they may only
run as child processes delegated by the authoritative runtime validator.  A
subcheck result is local evidence and can never authorize global motor closure
or decide M02.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


ENTRYPOINT_RELATIVE_PATH = Path(
    "99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py"
)
ENTRYPOINT_ENV = "IDUNEX_VALIDATOR_ENTRYPOINT"
ENTRYPOINT_PID_ENV = "IDUNEX_VALIDATOR_ENTRYPOINT_PID"
SUBCHECK_ENV = "IDUNEX_VALIDATOR_SUBCHECK"
BLOCKED_EXIT_CODE = 3


def _engine_root(script_path: Path) -> Path:
    for parent in script_path.resolve().parents:
        if parent.name == "IDUNEX":
            return parent
    raise RuntimeError(f"Cannot resolve IDUNEX engine root from {script_path}")


def _relative_to_engine(script_path: Path) -> str:
    return script_path.resolve().relative_to(_engine_root(script_path)).as_posix()


def _blocked_payload(script_path: Path, reasons: list[str]) -> dict[str, Any]:
    return {
        "validator": script_path.stem,
        "authority_role": "SUBVALIDATOR",
        "scope": "LOCAL_SUBCHECK_ONLY",
        "result": "BLOCKED_NON_AUTHORITATIVE_ENTRYPOINT",
        "global_closure_capable": False,
        "global_closure_authorized": False,
        "m02_decision_authority": False,
        "fail_codes": ["FAIL_AUD_009_DIRECT_SUBVALIDATOR_INVOCATION"],
        "reasons": reasons,
    }


def enforce_subcheck_invocation(script_file: str, module_name: str) -> None:
    """Block direct CLI execution while leaving import use available."""
    if module_name != "__main__":
        return

    script_path = Path(script_file).resolve()
    engine_root = _engine_root(script_path)
    expected_entrypoint = (engine_root / ENTRYPOINT_RELATIVE_PATH).resolve()
    expected_subcheck = _relative_to_engine(script_path)
    reasons: list[str] = []

    delegated_entrypoint = os.environ.get(ENTRYPOINT_ENV)
    delegated_pid = os.environ.get(ENTRYPOINT_PID_ENV)
    delegated_subcheck = os.environ.get(SUBCHECK_ENV)

    if not delegated_entrypoint:
        reasons.append("missing authoritative entrypoint delegation")
    else:
        try:
            if Path(delegated_entrypoint).resolve() != expected_entrypoint:
                reasons.append("delegating entrypoint path is not authoritative")
        except OSError:
            reasons.append("delegating entrypoint path is invalid")

    if delegated_pid != str(os.getppid()):
        reasons.append("delegating parent process does not match")
    if delegated_subcheck != expected_subcheck:
        reasons.append("delegated subcheck identity does not match")

    if reasons:
        print(json.dumps(_blocked_payload(script_path, reasons), ensure_ascii=False))
        raise SystemExit(BLOCKED_EXIT_CODE)


def _load_registry(registry_path: Path) -> dict[str, Any]:
    return json.loads(registry_path.read_text(encoding="utf-8"))


def _parse_child_output(stdout: str) -> Any:
    text = stdout.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw_stdout": text}


def delegate_subcheck(
    *,
    entrypoint_file: str,
    engine_root: Path,
    registry_path: Path,
    subcheck_id: str,
    subcheck_args: list[str],
) -> int:
    """Execute one registered subcheck and emit a non-global envelope."""
    registry = _load_registry(registry_path)
    subchecks = registry.get("engine_surfaces", {}).get("subvalidators", [])
    matches = [item for item in subchecks if item.get("id") == subcheck_id]
    if len(matches) != 1:
        payload = {
            "validator": "VALIDATE_IDUNEX_RUNTIME",
            "authority_role": "GLOBAL_VALIDATOR_ENTRYPOINT",
            "scope": "SUBCHECK_DELEGATION",
            "result": "SUBCHECK_NOT_REGISTERED",
            "requested_subcheck": subcheck_id,
            "global_closure_authorized": False,
            "m02_decision_authority": False,
            "fail_codes": ["FAIL_AUD_009_SUBCHECK_NOT_REGISTERED"],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2

    surface = matches[0]
    relative_path = surface["path"]
    script_path = (engine_root / relative_path).resolve()
    if not script_path.is_file() or surface.get("global_closure_capable") is not False:
        payload = {
            "validator": "VALIDATE_IDUNEX_RUNTIME",
            "authority_role": "GLOBAL_VALIDATOR_ENTRYPOINT",
            "scope": "SUBCHECK_DELEGATION",
            "result": "SUBCHECK_REGISTRY_INVALID",
            "requested_subcheck": subcheck_id,
            "global_closure_authorized": False,
            "m02_decision_authority": False,
            "fail_codes": ["FAIL_AUD_009_SUBCHECK_REGISTRY_INVALID"],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2

    env = os.environ.copy()
    env[ENTRYPOINT_ENV] = str(Path(entrypoint_file).resolve())
    env[ENTRYPOINT_PID_ENV] = str(os.getpid())
    env[SUBCHECK_ENV] = relative_path
    proc = subprocess.run(
        [sys.executable, str(script_path), *subcheck_args],
        cwd=str(engine_root),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    payload = {
        "validator": "VALIDATE_IDUNEX_RUNTIME",
        "authority_role": "GLOBAL_VALIDATOR_ENTRYPOINT",
        "scope": "SUBCHECK_DELEGATION",
        "result": "SUBCHECK_COMPLETED" if proc.returncode == 0 else "SUBCHECK_FAILED",
        "subcheck_id": subcheck_id,
        "subcheck_path": relative_path,
        "subcheck_returncode": proc.returncode,
        "subcheck_output": _parse_child_output(proc.stdout),
        "subcheck_stderr": proc.stderr.strip() or None,
        "global_closure_capable": False,
        "global_closure_authorized": False,
        "m02_decision_authority": False,
        "fail_codes": [] if proc.returncode == 0 else ["FAIL_AUD_009_SUBCHECK_FAILED"],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return proc.returncode
