from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import inspect
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
import zipfile
from collections import Counter
from pathlib import Path
from typing import Any, Callable


sys.dont_write_bytecode = True
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

REPO_ROOT = Path(__file__).resolve().parents[2]
ENGINE_ROOT = REPO_ROOT / "engine" / "IDUNEX"
LINEAGE_PATH = Path(__file__).with_name("m03_adversarial_lineage.json")
FACTORY_PATH = ENGINE_ROOT / "03_PROJECT_FACTORY" / "02_PROTOCOLS" / "IDUNEX_PROJECT_FACTORY_v1.0.0.py"
RUNNER_PATH = ENGINE_ROOT / "03_PROJECT_FACTORY" / "02_PROTOCOLS" / "IDUNEX_PROJECT_MATRIX_31_RUNNER.py"
VALIDATOR_PATH = ENGINE_ROOT / "99_MANIFESTS_SHA_LINEAGE" / "VALIDATE_IDUNEX_RUNTIME.py"
BASELINE_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "baseline_scanner.py"
DEMO_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "demo_hardcoding_check.py"
GOVERNANCE_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "governance_state_check.py"
NO_BLOAT_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "no_bloat_no_history_check.py"
WINDOWS_REMAP_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "windows_path_remap_check.py"
SECURITY_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "security_lite_scan.py"
INTAKE_SCANNER_PATH = REPO_ROOT / "tools" / "audit" / "intake_audit.py"
CURRENT_STATE_PATH = REPO_ROOT / "governance" / "CURRENT_STATE.json"
CURRENT_MANIFEST_PATH = REPO_ROOT / "governance" / "baseline" / "IDUNEX_CURRENT_TREE_MANIFEST.json"

EXPECTED_FILE_COUNT = 981
EXPECTED_BYTE_COUNT = 47_302_063
EXPECTED_ENGINE_TREE_SHA256 = "628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9"
EXPECTED_IDS = [f"{number:02d}" for number in range(1, 26)]
EXPECTED_RUNTIME_IDS = [f"M03-{number:02d}" for number in range(1, 26)]
RESULT_AUTHORITY = "CURRENT_ENGINE_CONTRACT_NOT_HISTORICAL_BYTE_EQUIVALENCE"
M03_DECISION = "NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY"

REQUIRED_LINEAGE_FIELDS = {
    "historical_case_id",
    "proposed_runtime_id",
    "historical_description",
    "classification",
    "attack_surface",
    "historical_source",
    "historical_input_status",
    "historical_failcode",
    "current_authority_contract",
    "current_expected_behavior",
    "current_expected_failcodes",
    "execution_method",
    "mutation_scope",
    "restoration_requirement",
    "evidence_notes",
    "result_authority",
}

_MODULE_CACHE: dict[str, Any] = {}


def _load_module(path: Path, name: str) -> Any:
    cached = _MODULE_CACHE.get(name)
    if cached is not None:
        return cached
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load authoritative module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    _MODULE_CACHE[name] = module
    return module


def load_lineage() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    payload = json.loads(LINEAGE_PATH.read_text(encoding="utf-8"))
    cases = payload.get("cases")
    if not isinstance(cases, list):
        raise AssertionError("FAIL_LINEAGE_CASES_NOT_LIST")
    return payload, cases


def validate_lineage(payload: dict[str, Any], cases: list[dict[str, Any]]) -> dict[str, Any]:
    failures: list[str] = []
    if len(cases) != 25:
        failures.append("FAIL_LINEAGE_CASE_COUNT")

    ids = [str(case.get("historical_case_id", "")) for case in cases]
    runtime_ids = [str(case.get("proposed_runtime_id", "")) for case in cases]
    if ids != EXPECTED_IDS or len(set(ids)) != 25:
        failures.append("FAIL_LINEAGE_HISTORICAL_IDS")
    if runtime_ids != EXPECTED_RUNTIME_IDS or len(set(runtime_ids)) != 25:
        failures.append("FAIL_LINEAGE_RUNTIME_IDS")

    counts = Counter(str(case.get("classification", "")) for case in cases)
    expected_counts = {
        "RECUPERADO_EXACTO": 2,
        "RECONSTRUIDO_TRAZABLE": 23,
        "NO_RECUPERABLE": 0,
    }
    if {key: counts.get(key, 0) for key in expected_counts} != expected_counts:
        failures.append("FAIL_LINEAGE_CLASSIFICATION_COUNTS")
    if set(counts) - set(expected_counts):
        failures.append("FAIL_LINEAGE_UNKNOWN_CLASSIFICATION")

    for case in cases:
        case_id = str(case.get("historical_case_id", "UNKNOWN"))
        missing = sorted(REQUIRED_LINEAGE_FIELDS - set(case))
        if missing:
            failures.append(f"FAIL_LINEAGE_REQUIRED_FIELDS:{case_id}:{','.join(missing)}")
        for field in REQUIRED_LINEAGE_FIELDS - {"historical_failcode", "current_expected_failcodes"}:
            value = case.get(field)
            if value in (None, "", []):
                failures.append(f"FAIL_LINEAGE_EMPTY_FIELD:{case_id}:{field}")
        if case.get("historical_input_status") == "NO_DOCUMENTADO" and case.get("classification") == "RECUPERADO_EXACTO":
            failures.append(f"FAIL_LINEAGE_UNDOCUMENTED_PRESENTED_EXACT:{case_id}")
        if case.get("mutation_scope") != "TEMPORARY_COPY_ONLY":
            failures.append(f"FAIL_LINEAGE_MUTATION_SCOPE:{case_id}")
        if case.get("result_authority") != RESULT_AUTHORITY:
            failures.append(f"FAIL_LINEAGE_RESULT_AUTHORITY:{case_id}")
        if not isinstance(case.get("historical_source"), list):
            failures.append(f"FAIL_LINEAGE_HISTORICAL_SOURCE_TYPE:{case_id}")
        if not isinstance(case.get("current_expected_failcodes"), list):
            failures.append(f"FAIL_LINEAGE_EXPECTED_FAILCODES_TYPE:{case_id}")

    exact_ids = [case.get("historical_case_id") for case in cases if case.get("classification") == "RECUPERADO_EXACTO"]
    if exact_ids != ["18", "19"]:
        failures.append("FAIL_LINEAGE_EXACT_IDS")
    if payload.get("historical_harness_recovered") is not False:
        failures.append("FAIL_LINEAGE_HISTORICAL_HARNESS_TRUTHFULNESS")

    report = {
        "case_count": len(cases),
        "historical_ids": ids,
        "runtime_ids": runtime_ids,
        "classification_counts": {key: counts.get(key, 0) for key in expected_counts},
        "result": "PASS" if not failures else "FAIL",
        "fail_codes": failures,
        "historical_harness_recovered": False,
        "result_authority": RESULT_AUTHORITY,
    }
    if failures:
        raise AssertionError(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def engine_identity() -> dict[str, Any]:
    rows: list[tuple[str, int, str]] = []
    for path in ENGINE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        data = path.read_bytes()
        rows.append(
            (
                path.relative_to(REPO_ROOT).as_posix(),
                len(data),
                hashlib.sha256(data).hexdigest(),
            )
        )
    rows.sort(key=lambda row: row[0])
    aggregate = hashlib.sha256()
    for relative, size, digest in rows:
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(str(size).encode("ascii"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")
    return {
        "scope": "engine/IDUNEX",
        "file_count": len(rows),
        "byte_count": sum(row[1] for row in rows),
        "tree_sha256": aggregate.hexdigest(),
    }


def _git_output(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO_ROOT, text=True).strip()


def _tail(value: str, limit: int = 4000) -> str:
    return value[-limit:]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@contextlib.contextmanager
def _working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def _command_env(temp_root: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["TMP"] = str(temp_root)
    env["TEMP"] = str(temp_root)
    env["TMPDIR"] = str(temp_root)
    return env


def _run_subprocess(command: list[str], temp_root: Path, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    case_timeout = timeout or int(os.environ.get("M03_TIMEOUT_PER_CASE", "300"))
    return subprocess.run(
        command,
        cwd=REPO_ROOT,
        env=_command_env(temp_root),
        capture_output=True,
        text=True,
        check=False,
        timeout=case_timeout,
    )


def _outcome(
    *,
    ok: bool,
    behavior: str,
    command: list[str],
    actual_failcodes: list[str] | None = None,
    return_code: int = 0,
    stdout: str = "",
    stderr: str = "",
    surface_restored: bool = True,
) -> dict[str, Any]:
    return {
        "ok": ok,
        "actual_behavior": behavior,
        "actual_failcodes": actual_failcodes or [],
        "command": command,
        "return_code": return_code,
        "stdout": stdout,
        "stderr": stderr,
        "surface_restored": surface_restored,
    }


def _factory() -> Any:
    return _load_module(FACTORY_PATH, "idunex_m03_factory_authority")


def _runner() -> Any:
    return _load_module(RUNNER_PATH, "idunex_m03_runner_authority")


def _baseline() -> Any:
    return _load_module(BASELINE_SCANNER_PATH, "idunex_m03_baseline_authority")


def _governance() -> Any:
    return _load_module(GOVERNANCE_SCANNER_PATH, "idunex_m03_governance_authority")


def _case_01(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    project = temp_root / "project"
    outside = temp_root / "outside"
    project.mkdir()
    outside.mkdir()
    sentinel = outside / "marker.txt"
    sentinel.write_text("old value", encoding="utf-8")
    before = _sha256(sentinel)
    code = ""
    try:
        factory._apply_semantic_replacements_limited(
            project,
            [("old value", "new value")],
            [project / ".." / "outside"],
        )
    except factory.InputContractError as exc:
        code = exc.fail_code
    after = _sha256(sentinel)
    ok = code == "FAIL_CLI_PATH_OUTSIDE_PROJECT_ROOT" and before == after
    return _outcome(
        ok=ok,
        behavior="TRAVERSAL_BLOCKED_EXTERNAL_SENTINEL_UNCHANGED" if ok else "TRAVERSAL_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_apply_semantic_replacements_limited"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"sentinel_sha_before": before, "sentinel_sha_after": after}),
        surface_restored=before == after,
    )


def _case_02(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    project = temp_root / "project input"
    update = temp_root / "contracts" / "update.json"
    project.mkdir()
    update.parent.mkdir()
    update.write_text("{}", encoding="utf-8")
    with _working_directory(temp_root):
        relative = argparse.Namespace(
            cmd="update-project",
            project=Path("project input"),
            update=Path("contracts/update.json"),
            output=Path("output"),
            output_json=Path("evidence/result.json"),
        )
        factory._normalize_related_cli_paths(relative)
    absolute = argparse.Namespace(
        cmd="update-project",
        project=project.resolve(),
        update=update.resolve(),
        output=(temp_root / "output").resolve(),
        output_json=(temp_root / "evidence/result.json").resolve(),
    )
    factory._normalize_related_cli_paths(absolute)
    fields = ("project", "update", "output", "output_json")
    ok = all(getattr(relative, field) == getattr(absolute, field) and getattr(relative, field).is_absolute() for field in fields)
    return _outcome(
        ok=ok,
        behavior="RELATIVE_ABSOLUTE_PATHS_CANONICALIZED_IDENTICALLY" if ok else "PATH_CANONICALIZATION_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_normalize_related_cli_paths"],
        stdout=json.dumps({field: str(getattr(relative, field)) for field in fields}, ensure_ascii=False),
    )


def _case_03(temp_root: Path) -> dict[str, Any]:
    del temp_root
    factory = _factory()
    alpha = factory._project_policy_status_payload("IDUNEX_PROJECT_ALPHA", False, True)
    beta = factory._project_policy_status_payload("IDUNEX_PROJECT_BETA", False, True)
    alpha.pop("project_id", None)
    beta.pop("project_id", None)
    mutation_source = inspect.getsource(factory.mutation_self_test)
    code_present = "FAIL_MOTOR_PROJECT_BOUNDARY" in mutation_source
    ok = alpha == beta and code_present
    return _outcome(
        ok=ok,
        behavior="NAME_NEUTRAL_POLICY_AND_CURRENT_BOUNDARY_FAILCODE_BOUND" if ok else "ENGINE_PROJECT_BOUNDARY_BINDING_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_project_policy_status_payload", "mutation_self_test"],
        actual_failcodes=["FAIL_MOTOR_PROJECT_BOUNDARY"] if code_present else [],
        stdout=json.dumps({"name_neutral": alpha == beta, "boundary_contract_present": code_present}),
    )


def _case_04(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    governance = _governance()
    state = json.loads(CURRENT_STATE_PATH.read_text(encoding="utf-8"))
    state["ready_for_project_demo_generation"] = True
    findings = governance.validate_current_state_data(state)
    mutated = temp_root / "mutated_factory.py"
    protected_name = "Proyecto " + "000 Demo"
    mutated.write_text(
        "def select(project_name):\n"
        f"    if project_name == {protected_name!r}:\n"
        "        return 'special'\n",
        encoding="utf-8",
    )
    mutation = factory._aud007_factory_hardcoding_mutation_case(mutated)
    code = str(mutation.get("expected_failcode", ""))
    ok = bool(findings) and mutation.get("result") == "FAIL" and code == "FAIL_FACTORY_HARDCODED_DEMO_BRANCH"
    return _outcome(
        ok=ok,
        behavior="UNAUTHORIZED_DEMO_INTERLOCK_AND_AST_MUTATION_BLOCKED" if ok else "DEMO_INTERLOCK_MISMATCH",
        command=["PYTHON_API", "tools/audit/governance_state_check.py", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_aud007_factory_hardcoding_mutation_case"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"governance_findings": findings, "factory_mutation": mutation}, ensure_ascii=False),
    )


def _case_05(temp_root: Path) -> dict[str, Any]:
    del temp_root
    governance = _governance()
    baseline = json.loads(CURRENT_STATE_PATH.read_text(encoding="utf-8"))
    release_state = json.loads(json.dumps(baseline))
    tag_state = json.loads(json.dumps(baseline))
    release_state["release_authorized"] = True
    tag_state["tag_authorized"] = True
    release_findings = governance.validate_current_state_data(release_state)
    tag_findings = governance.validate_current_state_data(tag_state)
    ok = any("release_authorized" in finding for finding in release_findings) and any("tag_authorized" in finding for finding in tag_findings)
    return _outcome(
        ok=ok,
        behavior="RELEASE_AND_TAG_FLAGS_REJECTED_WITHOUT_GIT_OPERATION" if ok else "GOVERNANCE_RELEASE_TAG_MISMATCH",
        command=["PYTHON_API", "tools/audit/governance_state_check.py", "validate_current_state_data"],
        stdout=json.dumps({"release_findings": release_findings, "tag_findings": tag_findings}, ensure_ascii=False),
    )


def _case_06(temp_root: Path) -> dict[str, Any]:
    del temp_root
    governance = _governance()
    state = json.loads(CURRENT_STATE_PATH.read_text(encoding="utf-8"))
    state["motor_status"] = "OFICIAL"
    findings = governance.validate_current_state_data(state)
    ok = any("motor_status" in finding and "EN_REVISION" in finding for finding in findings)
    return _outcome(
        ok=ok,
        behavior="OFICIAL_STATUS_REJECTED_EXPECTED_EN_REVISION" if ok else "MOTOR_STATUS_GOVERNANCE_MISMATCH",
        command=["PYTHON_API", "tools/audit/governance_state_check.py", "validate_current_state_data"],
        stdout=json.dumps({"findings": findings}, ensure_ascii=False),
    )


def _case_07(temp_root: Path) -> dict[str, Any]:
    governance = _governance()
    rogue = temp_root / "engine" / "IDUNEX" / "00_INDEX" / "ROGUE_CERTIFICATE.txt"
    rogue.parent.mkdir(parents=True)
    rogue.write_text("M02_RESULT=M02_PASS\nREADY_FOR_PROJECT_DEMO_GENERATION=TRUE\n", encoding="utf-8")
    findings, historical_matches = governance.scan_contradictions(temp_root)
    ok = bool(findings) and historical_matches == 0
    return _outcome(
        ok=ok,
        behavior="UNCLASSIFIED_PASS_READINESS_CONTRADICTION_DETECTED" if ok else "TRUTHFULNESS_SCANNER_MISMATCH",
        command=["PYTHON_API", "tools/audit/governance_state_check.py", "scan_contradictions"],
        stdout=json.dumps({"findings": findings, "historical_matches": historical_matches}, ensure_ascii=False),
    )


def _case_08(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    runner = _runner()
    basic = runner.model_spec("basic", 1)
    normalized = factory.normalize_model(basic, 1, 1)
    code = ""
    try:
        factory.make_project(
            {"project_name": "Proyecto Sintético Adulto", "project_entity_profile": factory.fixture_entity_profile()},
            temp_root,
        )
    except factory.InputContractError as exc:
        code = exc.fail_code
    delegated = normalized.get("age", 0) >= 18 and bool(normalized.get("model_id"))
    ok = basic == {} and delegated and code == "FAIL_INPUT_CONTRACT_MISSING_REQUIRED_FIELD"
    return _outcome(
        ok=ok,
        behavior="LOW_INFO_SLOT_DELEGATED_AND_MISSING_MODELS_BLOCKED_EARLY" if ok else "LOW_INFO_INPUT_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(RUNNER_PATH.relative_to(REPO_ROOT)), "model_spec", str(FACTORY_PATH.relative_to(REPO_ROOT)), "normalize_model/make_project"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"delegated_model_id": normalized.get("model_id"), "blocked_failcode": code}, ensure_ascii=False),
    )


def _case_09(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    index_path = temp_root / "00_PROJECT_INDEX" / "PROJECT_MODEL_INDEX.json"
    factory.write_json(
        index_path,
        {
            "models": [
                {"model_id": "MODEL_ALPHA", "model_code": "ALPHA"},
                {"model_id": "MODEL_BETA", "model_code": "BETA"},
            ]
        },
    )
    code = ""
    try:
        factory._model_by_selector(temp_root, {})
    except factory.InputContractError as exc:
        code = exc.fail_code
    ok = code == "FAIL_UPDATE_TARGET_MODEL_NOT_FOUND"
    return _outcome(
        ok=ok,
        behavior="AMBIGUOUS_MULTI_MODEL_SELECTOR_BLOCKED" if ok else "AMBIGUOUS_SELECTOR_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_model_by_selector"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"model_count": 2, "blocked_failcode": code}),
    )


def _case_10(temp_root: Path) -> dict[str, Any]:
    del temp_root
    factory = _factory()
    code = ""
    try:
        factory.normalize_input_aliases({"name": "ALPHA", "canonical_name": "BETA"}, 1)
    except factory.InputContractError as exc:
        code = exc.fail_code
    ok = code == "FAIL_INPUT_ALIAS_CANONICAL_CONFLICT"
    return _outcome(
        ok=ok,
        behavior="CONTRADICTORY_ALIAS_CANON_BLOCKED_EARLY" if ok else "ALIAS_CONFLICT_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "normalize_input_aliases"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"blocked_failcode": code}),
    )


def _case_11(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    output_json = temp_root / "large-output.json"
    payload = {"result": "PASS", "fail_codes": [], "payload": "X" * 1_000_000}
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        emitted = factory._emit_json_safely(payload, command="m03-adversarial", output_json=str(output_json))
    stdout_payload = json.loads(captured.getvalue())
    file_payload = json.loads(output_json.read_text(encoding="utf-8"))
    ok = emitted and stdout_payload == payload and file_payload == payload
    return _outcome(
        ok=ok,
        behavior="LARGE_PAYLOAD_COMPLETE_IN_STDOUT_AND_OUTPUT_JSON" if ok else "LARGE_PAYLOAD_SERIALIZATION_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_emit_json_safely"],
        stdout=json.dumps({"payload_bytes": len(payload["payload"]), "stdout_parseable": stdout_payload == payload, "output_json_parseable": file_payload == payload}),
    )


def _case_12(temp_root: Path) -> dict[str, Any]:
    del temp_root
    factory = _factory()
    name = "Álvaro Ñandú — adulto 🚀 / QA"
    slug_one = factory.slug(name)
    slug_two = factory.slug(name)
    identity = factory._project_policy_canonical_identity({"project_name": name, "models": [{}]})
    safe = bool(re.fullmatch(r"[A-Z0-9_]+", slug_one)) and re.fullmatch(r"IDUNEX_PROJECT_[A-Z0-9_]+_v1\.0\.0", identity["project_id"])
    ok = bool(safe) and slug_one == slug_two and identity["filename_canon"].endswith(".zip")
    return _outcome(
        ok=ok,
        behavior="RARE_CHARACTER_NAME_CANONICALIZED_SAFELY_AND_DETERMINISTICALLY" if ok else "NAME_CANONICALIZATION_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "slug/_project_policy_canonical_identity"],
        stdout=json.dumps({"input": name, "slug": slug_one, "project_id": identity["project_id"]}, ensure_ascii=False),
    )


def _case_13(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    remap = _load_module(WINDOWS_REMAP_SCANNER_PATH, "idunex_m03_windows_remap_authority")
    with _working_directory(temp_root):
        args = argparse.Namespace(cmd="migrate-project", project="nested/project", output="nested/output", output_json=None)
        factory._normalize_related_cli_paths(args)
    table = remap.load_remap_table(REPO_ROOT)
    original = remap.h62_original_path(table)
    resolved_repo = table.resolve(original)
    resolved_engine = table.resolve(original.removeprefix("engine/IDUNEX/"))
    ok = (
        args.project == (temp_root / "nested/project").resolve()
        and resolved_repo == remap.H62_SAFE
        and resolved_engine == remap.H62_SAFE.removeprefix("engine/IDUNEX/")
    )
    return _outcome(
        ok=ok,
        behavior="HOST_POSIX_PATH_AND_WINDOWS_REMAP_RESOLVE_CANONICALLY" if ok else "CROSS_PLATFORM_PATH_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_normalize_related_cli_paths", "tools/audit/windows_path_remap_check.py", "RemapTable.resolve"],
        stdout=json.dumps({"normalized_project": str(args.project), "remap_repository": resolved_repo, "remap_engine": resolved_engine}, ensure_ascii=False),
    )


def _manifest_target_record() -> tuple[dict[str, Any], Path]:
    manifest = json.loads(CURRENT_MANIFEST_PATH.read_text(encoding="utf-8"))
    relative = "engine/IDUNEX/00_INDEX/ACTIVE_VERSION.txt"
    record = next(row for row in manifest["files"] if row.get("path") == relative)
    return record, REPO_ROOT / relative


def _copy_single_manifest_surface(temp_root: Path) -> tuple[Path, Path, dict[str, Any]]:
    record, source = _manifest_target_record()
    engine = temp_root / "IDUNEX"
    target = engine / "00_INDEX" / "ACTIVE_VERSION.txt"
    target.parent.mkdir(parents=True)
    shutil.copy2(source, target)
    return engine, target, record


def _case_14(temp_root: Path) -> dict[str, Any]:
    baseline = _baseline()
    engine, target, record = _copy_single_manifest_surface(temp_root)
    original = target.read_bytes()
    before = _sha256(target)
    target.write_bytes(original + b"\nM03_MANIFEST_MUTATION\n")
    mutated = baseline.verify_manifest_records(engine, [record], repository_paths=True)
    target.write_bytes(original)
    restored = baseline.verify_manifest_records(engine, [record], repository_paths=True)
    after = _sha256(target)
    surface_restored = before == after and restored["hash_mismatch_count"] == 0
    ok = mutated["hash_mismatch_count"] == 1 and surface_restored
    return _outcome(
        ok=ok,
        behavior="MANIFEST_BYTE_MUTATION_DETECTED_AND_COPY_RESTORED" if ok else "MANIFEST_MUTATION_CONTRACT_MISMATCH",
        command=["PYTHON_API", "tools/audit/baseline_scanner.py", "verify_manifest_records"],
        stdout=json.dumps({"mutated": mutated, "restored": restored, "copy_sha_before": before, "copy_sha_after": after}, ensure_ascii=False),
        surface_restored=surface_restored,
    )


def _case_15(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    package = temp_root / "synthetic-project.zip"
    with zipfile.ZipFile(package, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("SYNTHETIC_NON_AUTHORITY.txt", "adult synthetic QA fixture")
    companion = package.with_suffix(package.suffix + ".sha256")
    companion.write_text(f"{'0' * 64}  {package.name}\n", encoding="utf-8")
    result = factory.validate_reopened_zip(package, companion)
    codes = list(result.get("fail_codes", []))
    ok = result.get("result") == "FAIL" and codes == ["FAIL_PACKAGE_SHA"]
    return _outcome(
        ok=ok,
        behavior="MISMATCHED_SHA_COMPANION_BLOCKED" if ok else "SHA_COMPANION_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "validate_reopened_zip"],
        actual_failcodes=codes,
        stdout=json.dumps(result, ensure_ascii=False),
    )


def _case_16(temp_root: Path) -> dict[str, Any]:
    factory = _factory()
    project = temp_root / "project"
    outside = temp_root / "outside"
    project.mkdir()
    outside.mkdir()
    sentinel = outside / "marker.txt"
    sentinel.write_text("UNCHANGED", encoding="utf-8")
    before = _sha256(sentinel)
    code = ""
    try:
        factory._project_relative_path(project, outside / "marker.txt", purpose="M03 update/migrate boundary")
    except factory.InputContractError as exc:
        code = exc.fail_code
    after = _sha256(sentinel)
    ok = code == "FAIL_CLI_PATH_OUTSIDE_PROJECT_ROOT" and before == after
    return _outcome(
        ok=ok,
        behavior="UPDATE_MIGRATE_OUTSIDE_ROOT_BLOCKED_SENTINEL_UNCHANGED" if ok else "UPDATE_MIGRATE_BOUNDARY_MISMATCH",
        command=["PYTHON_API", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_project_relative_path"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"sentinel_sha_before": before, "sentinel_sha_after": after}),
        surface_restored=before == after,
    )


def _case_17(temp_root: Path) -> dict[str, Any]:
    del temp_root
    runner = _runner()
    rows = runner.cases()
    level_counts = Counter(row.get("level") for row in rows)
    model_counts = {level: sorted(row.get("model_count") for row in rows if row.get("level") == level) for level in ("basic", "intermediate", "complete")}
    complete_n10 = runner.model_spec("complete", 10)
    ok = (
        len(rows) == 30
        and level_counts == Counter({"basic": 10, "intermediate": 10, "complete": 10})
        and all(values == list(range(1, 11)) for values in model_counts.values())
        and not any("demo" in json.dumps(row).casefold() for row in rows)
        and bool(complete_n10.get("safety_notes"))
    )
    return _outcome(
        ok=ok,
        behavior="CANONICAL_RUNNER_BOUND_TO_30_NON_DEMO_N1_N10_X3_CASES" if ok else "RUNNER_MATRIX_CONTRACT_MISMATCH",
        command=["PYTHON_API", str(RUNNER_PATH.relative_to(REPO_ROOT)), "cases/model_spec", "WORKFLOW_GATE:30/30"],
        stdout=json.dumps({"case_count": len(rows), "level_counts": dict(level_counts), "model_counts": model_counts}, ensure_ascii=False),
    )


def _case_18(temp_root: Path) -> dict[str, Any]:
    command = [sys.executable, "-B", str(FACTORY_PATH), "--help"]
    process = _run_subprocess(command, temp_root)
    bound = "mutation-self-test" in process.stdout
    ok = process.returncode == 0 and bound
    return _outcome(
        ok=ok,
        behavior="CANONICAL_MUTATION_CLI_BOUND_WORKFLOW_506_GATE_REQUIRED" if ok else "MUTATION_CLI_BINDING_MISMATCH",
        command=command,
        return_code=process.returncode,
        stdout=process.stdout,
        stderr=process.stderr,
    )


def _case_19(temp_root: Path) -> dict[str, Any]:
    command = [sys.executable, "-B", str(VALIDATOR_PATH), str(ENGINE_ROOT)]
    process = _run_subprocess(command, temp_root)
    try:
        report = json.loads(process.stdout)
    except json.JSONDecodeError:
        report = {}
    codes = report.get("fail_codes") if isinstance(report.get("fail_codes"), list) else []
    ok = (
        process.returncode == 0
        and report.get("result") == "PASS"
        and report.get("validators_fail") == 0
        and report.get("blocking_warnings") == 0
        and codes == []
    )
    return _outcome(
        ok=ok,
        behavior="GLOBAL_RUNTIME_VALIDATOR_PASS_ZERO_FAILURES_WARNINGS_FAILCODES" if ok else "GLOBAL_RUNTIME_VALIDATOR_MISMATCH",
        command=command,
        actual_failcodes=codes,
        return_code=process.returncode,
        stdout=process.stdout,
        stderr=process.stderr,
    )


def _case_20(temp_root: Path) -> dict[str, Any]:
    del temp_root
    governance = _governance()
    baseline = json.loads(CURRENT_STATE_PATH.read_text(encoding="utf-8"))
    baseline_findings = governance.validate_current_state_data(baseline)
    mutations = {
        "demo": ("ready_for_project_demo_generation", True),
        "release": ("release_authorized", True),
        "tag": ("tag_authorized", True),
        "official": ("motor_status", "OFICIAL"),
    }
    reports: dict[str, list[str]] = {}
    for name, (field, value) in mutations.items():
        payload = json.loads(json.dumps(baseline))
        payload[field] = value
        reports[name] = governance.validate_current_state_data(payload)
    ok = baseline_findings == [] and all(reports[name] for name in mutations)
    return _outcome(
        ok=ok,
        behavior="GOVERNANCE_BASELINE_VALID_AND_FOUR_MUTATIONS_REJECTED" if ok else "GOVERNANCE_MUTATION_MATRIX_MISMATCH",
        command=["PYTHON_API", "tools/audit/governance_state_check.py", "validate_current_state_data"],
        stdout=json.dumps({"baseline_findings": baseline_findings, "mutation_findings": reports}, ensure_ascii=False),
    )


def _case_21(temp_root: Path) -> dict[str, Any]:
    audit = _load_module(NO_BLOAT_SCANNER_PATH, "idunex_m03_no_bloat_authority")
    engine = temp_root / "active-engine"
    active = engine / "01_ACTIVE"
    active.mkdir(parents=True)
    (active / "a.txt").write_text("same", encoding="utf-8")
    (active / "b.txt").write_text("same", encoding="utf-8")
    (active / "H500_STALE_PROOF.json").write_text("{}", encoding="utf-8")
    active_scan = audit.scan_active_tree(engine)

    historical_engine = temp_root / "historical-engine"
    historical = historical_engine / "14_HISTORICAL_NON_AUTHORITY"
    historical.mkdir(parents=True)
    (historical / "H500_STALE_PROOF.json").write_text("{}", encoding="utf-8")
    historical_scan = audit.scan_active_tree(historical_engine)

    moved = historical / "AUD_008_ACTIVE_HISTORY" / "old.json"
    moved.parent.mkdir(parents=True)
    moved.write_text("{}", encoding="utf-8")
    conflicts = audit.movement_conflicts(
        historical_engine,
        {
            "movements": [
                {
                    "origin": "99_MANIFESTS_SHA_LINEAGE/old.json",
                    "destination": "14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/old.json",
                    "operation": "MOVE_TO_HISTORICAL",
                    "authority_after": "ACTIVE",
                    "sha256_after": audit._sha256(moved),
                }
            ]
        },
    )
    ok = (
        active_scan.get("unjustified_duplicate_group_count") == 1
        and active_scan.get("active_h_route_count") == 1
        and historical_scan.get("active_h_route_count") == 0
        and any(item.get("code") == "HISTORICAL_EVIDENCE_HAS_ACTIVE_AUTHORITY" for item in conflicts)
    )
    return _outcome(
        ok=ok,
        behavior="BLOAT_ACTIVE_HISTORY_AND_AUTHORITY_CONFLICTS_DETECTED" if ok else "NO_BLOAT_NO_HISTORY_CONTRACT_MISMATCH",
        command=["PYTHON_API", "tools/audit/no_bloat_no_history_check.py", "scan_active_tree/movement_conflicts"],
        stdout=json.dumps({"active_scan": active_scan, "historical_scan": historical_scan, "conflicts": conflicts}, ensure_ascii=False),
    )


def _case_22(temp_root: Path) -> dict[str, Any]:
    audit = _load_module(DEMO_SCANNER_PATH, "idunex_m03_demo_authority")
    factory = _factory()
    mutated = temp_root / "mutated_factory.py"
    protected_name = "Proyecto " + "000 Demo"
    mutated.write_text(
        "def select(project_name):\n"
        f"    return 'special' if project_name == {protected_name!r} else 'generic'\n",
        encoding="utf-8",
    )
    findings = audit.hardcoded_named_project_branches(mutated)
    mutation = factory._aud007_factory_hardcoding_mutation_case(mutated)
    code = str(mutation.get("expected_failcode", ""))
    ok = len(findings) == 1 and mutation.get("result") == "FAIL" and code == "FAIL_FACTORY_HARDCODED_DEMO_BRANCH"
    return _outcome(
        ok=ok,
        behavior="NAMED_PROJECT_BRANCH_DETECTED_BY_AST_AND_FACTORY_SELF_TEST" if ok else "DEMO_HARDCODING_CONTRACT_MISMATCH",
        command=["PYTHON_API", "tools/audit/demo_hardcoding_check.py", "hardcoded_named_project_branches", str(FACTORY_PATH.relative_to(REPO_ROOT)), "_aud007_factory_hardcoding_mutation_case"],
        actual_failcodes=[code] if code else [],
        stdout=json.dumps({"findings": findings, "factory_mutation": mutation}, ensure_ascii=False),
    )


def _case_23(temp_root: Path) -> dict[str, Any]:
    baseline = _baseline()
    live = baseline.audit_repository(REPO_ROOT)
    engine, target, record = _copy_single_manifest_surface(temp_root)
    original = target.read_bytes()
    before = _sha256(target)
    target.write_bytes(original + b"\nM03_BASELINE_MUTATION\n")
    mutated = baseline.verify_manifest_records(engine, [record], repository_paths=True)
    target.write_bytes(original)
    restored = baseline.verify_manifest_records(engine, [record], repository_paths=True)
    after = _sha256(target)
    surface_restored = before == after and restored.get("hash_mismatch_count") == 0
    ok = live.get("result") == "PASS" and mutated.get("hash_mismatch_count") == 1 and surface_restored
    return _outcome(
        ok=ok,
        behavior="LIVE_BASELINE_PASS_MUTATION_DETECTED_COPY_RESTORED" if ok else "BASELINE_REPRODUCIBILITY_MISMATCH",
        command=["PYTHON_API", "tools/audit/baseline_scanner.py", "audit_repository/verify_manifest_records"],
        stdout=json.dumps({"live_result": live.get("result"), "mutated": mutated, "restored": restored, "copy_sha_before": before, "copy_sha_after": after}, ensure_ascii=False),
        surface_restored=surface_restored,
    )


def _case_24(temp_root: Path) -> dict[str, Any]:
    baseline_command = [sys.executable, "-B", str(SECURITY_SCANNER_PATH), "--repo-root", str(REPO_ROOT)]
    baseline_process = _run_subprocess(baseline_command, temp_root)
    synthetic_repo = temp_root / "synthetic-security-repo"
    synthetic_repo.mkdir()
    token = "sk-" + ("A" * 24)
    (synthetic_repo / "fixture.txt").write_text(token + "\n", encoding="utf-8")
    mutation_command = [sys.executable, "-B", str(SECURITY_SCANNER_PATH), "--repo-root", str(synthetic_repo)]
    mutation_process = _run_subprocess(mutation_command, temp_root)
    ok = (
        baseline_process.returncode == 0
        and "PASS:" in baseline_process.stdout
        and mutation_process.returncode == 1
        and "OPENAI_OR_GENERIC_SK_TOKEN" in mutation_process.stdout
    )
    return _outcome(
        ok=ok,
        behavior="LIVE_SECURITY_SCAN_PASS_SYNTHETIC_TOKEN_DETECTED" if ok else "SECURITY_LITE_CONTRACT_MISMATCH",
        command=mutation_command,
        return_code=mutation_process.returncode,
        stdout="BASELINE:\n" + baseline_process.stdout + "\nMUTATION:\n" + mutation_process.stdout,
        stderr="BASELINE:\n" + baseline_process.stderr + "\nMUTATION:\n" + mutation_process.stderr,
    )


def _case_25(temp_root: Path) -> dict[str, Any]:
    synthetic_repo = temp_root / "empty-repository"
    synthetic_repo.mkdir()
    command = [sys.executable, "-B", str(INTAKE_SCANNER_PATH), "--repo-root", str(synthetic_repo)]
    process = _run_subprocess(command, temp_root)
    try:
        report = json.loads(process.stdout)
    except json.JSONDecodeError:
        report = {}
    failures = report.get("failures", []) if isinstance(report.get("failures"), list) else []
    ok = process.returncode == 1 and report.get("result") == "FAIL" and "Missing engine/IDUNEX directory" in failures
    return _outcome(
        ok=ok,
        behavior="MISSING_ENGINE_INTAKE_REJECTED_WITH_EXACT_FINDING" if ok else "INTAKE_AUDIT_CONTRACT_MISMATCH",
        command=command,
        return_code=process.returncode,
        stdout=process.stdout,
        stderr=process.stderr,
    )


CASE_HANDLERS: dict[str, Callable[[Path], dict[str, Any]]] = {
    "01": _case_01,
    "02": _case_02,
    "03": _case_03,
    "04": _case_04,
    "05": _case_05,
    "06": _case_06,
    "07": _case_07,
    "08": _case_08,
    "09": _case_09,
    "10": _case_10,
    "11": _case_11,
    "12": _case_12,
    "13": _case_13,
    "14": _case_14,
    "15": _case_15,
    "16": _case_16,
    "17": _case_17,
    "18": _case_18,
    "19": _case_19,
    "20": _case_20,
    "21": _case_21,
    "22": _case_22,
    "23": _case_23,
    "24": _case_24,
    "25": _case_25,
}


class LineageContractTest(unittest.TestCase):
    def test_lineage_contract_25_2_23_0(self):
        payload, cases = load_lineage()
        report = validate_lineage(payload, cases)
        self.assertEqual(report["result"], "PASS")


class M03AdversarialHarness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lineage_payload, cases = load_lineage()
        cls.lineage_report = validate_lineage(cls.lineage_payload, cases)
        cls.cases_by_id = {case["historical_case_id"]: case for case in cases}
        if set(CASE_HANDLERS) != set(EXPECTED_IDS):
            raise AssertionError("FAIL_HANDLER_CASE_SET")

        configured = os.environ.get("M03_EVIDENCE_DIR", "").strip()
        cls._temporary_evidence: tempfile.TemporaryDirectory[str] | None = None
        if configured:
            evidence_dir = Path(configured).resolve()
            if evidence_dir == REPO_ROOT or REPO_ROOT in evidence_dir.parents:
                raise AssertionError("FAIL_EVIDENCE_DIR_INSIDE_REPOSITORY")
            evidence_dir.mkdir(parents=True, exist_ok=True)
        else:
            cls._temporary_evidence = tempfile.TemporaryDirectory(prefix="idunex-m03-local-evidence-")
            evidence_dir = Path(cls._temporary_evidence.name).resolve()
        cls.evidence_dir = evidence_dir
        cls.case_dir = evidence_dir / "cases"
        cls.case_dir.mkdir(parents=True, exist_ok=True)
        cls.results: dict[str, dict[str, Any]] = {}
        cls.repository_commit = _git_output("rev-parse", "HEAD")

    @classmethod
    def tearDownClass(cls):
        cls._write_consolidated_result()
        print(f"M03 evidence directory: {cls.evidence_dir}")
        if cls._temporary_evidence is not None:
            cls._temporary_evidence.cleanup()

    @classmethod
    def _write_consolidated_result(cls) -> dict[str, Any]:
        ordered_results = [cls.results[case_id] for case_id in EXPECTED_IDS if case_id in cls.results]
        pass_count = sum(result.get("result") == "PASS" for result in ordered_results)
        fail_count = 25 - pass_count
        restoration_pass_count = sum(result.get("restoration_result") == "PASS" for result in ordered_results)
        engine = engine_identity()
        failures: list[str] = []
        if len(ordered_results) != 25:
            failures.append("FAIL_M03_CASE_EXECUTION_COUNT")
        for result in ordered_results:
            if result.get("result") != "PASS":
                failures.extend(result.get("fail_codes", []) or [f"FAIL_M03_CASE_{result.get('historical_case_id')}"])
        if restoration_pass_count != len(ordered_results):
            failures.append("FAIL_M03_RESTORATION_COUNT")
        if engine["tree_sha256"] != EXPECTED_ENGINE_TREE_SHA256:
            failures.append("FAIL_M03_ENGINE_TREE_SHA256")

        summary = {
            "schema_version": 1,
            "audit_id": "AUD-027",
            "case_count": 25,
            "executed_case_count": len(ordered_results),
            "exact_recovered_count": 2,
            "traceable_reconstructed_count": 23,
            "non_recoverable_count": 0,
            "pass_count": pass_count,
            "fail_count": fail_count,
            "restoration_pass_count": restoration_pass_count,
            "engine_tree_sha256": engine["tree_sha256"],
            "engine_file_count": engine["file_count"],
            "engine_byte_count": engine["byte_count"],
            "repository_commit": cls.repository_commit,
            "historical_harness_recovered": False,
            "reconstruction_truthfulness": "PASS" if cls.lineage_report.get("result") == "PASS" else "FAIL",
            "M03_DECISION": M03_DECISION,
            "CREATIVE_OUTPUT_CERTIFIED": False,
            "result": "PASS" if not failures and pass_count == 25 and restoration_pass_count == 25 else "FAIL",
            "fail_codes": sorted(set(failures)),
            "individual_result_directory": str(cls.case_dir),
        }
        (cls.evidence_dir / "M03_ADVERSARIAL_RESULT.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return summary

    def _execute(self, case_id: str) -> None:
        lineage = self.cases_by_id[case_id]
        before = engine_identity()
        started = time.monotonic()
        harness_failures: list[str] = []
        outcome: dict[str, Any]
        try:
            with tempfile.TemporaryDirectory(prefix=f"idunex-m03-{case_id}-") as temp_dir:
                outcome = CASE_HANDLERS[case_id](Path(temp_dir))
        except Exception as exc:  # noqa: BLE001 - evidence must survive any case failure
            outcome = _outcome(
                ok=False,
                behavior="CASE_EXECUTION_EXCEPTION",
                command=["M03_CASE", case_id],
                return_code=1,
                stderr=f"{type(exc).__name__}: {exc}",
                surface_restored=False,
            )
            harness_failures.append("FAIL_M03_CASE_EXCEPTION")
        after = engine_identity()

        identity_ok = (
            before == after
            and before["file_count"] == EXPECTED_FILE_COUNT
            and before["byte_count"] == EXPECTED_BYTE_COUNT
            and before["tree_sha256"] == EXPECTED_ENGINE_TREE_SHA256
        )
        surface_restored = bool(outcome.get("surface_restored", False))
        restoration_ok = identity_ok and surface_restored
        if not identity_ok:
            harness_failures.append("FAIL_M03_ENGINE_RESTORATION")
        if not surface_restored:
            harness_failures.append("FAIL_M03_TEMPORARY_SURFACE_RESTORATION")

        expected_codes = list(lineage["current_expected_failcodes"])
        actual_codes = list(outcome.get("actual_failcodes", []))
        if sorted(expected_codes) != sorted(actual_codes):
            harness_failures.append("FAIL_M03_EXPECTED_FAILCODE_MISMATCH")
        if not outcome.get("ok"):
            harness_failures.append("FAIL_M03_EXPECTED_BEHAVIOR_MISMATCH")

        result = {
            "historical_case_id": case_id,
            "runtime_case_id": lineage["proposed_runtime_id"],
            "classification": lineage["classification"],
            "expected_behavior": lineage["current_expected_behavior"],
            "expected_failcodes": expected_codes,
            "actual_behavior": outcome.get("actual_behavior", "NOT_REPORTED"),
            "actual_failcodes": actual_codes,
            "command": outcome.get("command", []),
            "return_code": int(outcome.get("return_code", 1)),
            "stdout_tail": _tail(str(outcome.get("stdout", ""))),
            "stderr_tail": _tail(str(outcome.get("stderr", ""))),
            "restoration_result": "PASS" if restoration_ok else "FAIL",
            "engine_hash_before": before["tree_sha256"],
            "engine_hash_after": after["tree_sha256"],
            "result": "PASS" if not harness_failures else "FAIL",
            "fail_codes": sorted(set(harness_failures)),
            "duration_seconds": round(time.monotonic() - started, 3),
            "result_authority": RESULT_AUTHORITY,
        }
        runtime_id = lineage["proposed_runtime_id"]
        result_path = self.case_dir / f"{runtime_id}.json"
        result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (self.case_dir / f"{runtime_id}.stdout.log").write_text(str(outcome.get("stdout", "")), encoding="utf-8")
        (self.case_dir / f"{runtime_id}.stderr.log").write_text(str(outcome.get("stderr", "")), encoding="utf-8")
        (self.case_dir / f"{runtime_id}.rc").write_text(f"{int(outcome.get('return_code', 1))}\n", encoding="utf-8")
        type(self).results[case_id] = result
        type(self)._write_consolidated_result()
        self.assertEqual(result["result"], "PASS", json.dumps(result, ensure_ascii=False, indent=2))

    def test_m03_01_path_traversal(self):
        self._execute("01")

    def test_m03_02_dangerous_absolute_relative_paths(self):
        self._execute("02")

    def test_m03_03_engine_project_agent_separation(self):
        self._execute("03")

    def test_m03_04_unauthorized_demo_generation(self):
        self._execute("04")

    def test_m03_05_unauthorized_release_tag(self):
        self._execute("05")

    def test_m03_06_force_official_motor_status(self):
        self._execute("06")

    def test_m03_07_unsubstantiated_m02_claim(self):
        self._execute("07")

    def test_m03_08_low_information_inputs(self):
        self._execute("08")

    def test_m03_09_ambiguous_inputs(self):
        self._execute("09")

    def test_m03_10_contradictory_inputs(self):
        self._execute("10")

    def test_m03_11_large_payloads(self):
        self._execute("11")

    def test_m03_12_unusual_name_characters(self):
        self._execute("12")

    def test_m03_13_windows_posix_paths(self):
        self._execute("13")

    def test_m03_14_manifest_mutation(self):
        self._execute("14")

    def test_m03_15_sha_mutation(self):
        self._execute("15")

    def test_m03_16_update_migrate_outside_project_root(self):
        self._execute("16")

    def test_m03_17_n1_n10_x3_runner_contract(self):
        self._execute("17")

    def test_m03_18_mutation_self_test_contract(self):
        self._execute("18")

    def test_m03_19_global_runtime_validator(self):
        self._execute("19")

    def test_m03_20_governance_state_adversarial(self):
        self._execute("20")

    def test_m03_21_no_bloat_no_history_adversarial(self):
        self._execute("21")

    def test_m03_22_demo_hardcoding_adversarial(self):
        self._execute("22")

    def test_m03_23_reproducible_baseline_adversarial(self):
        self._execute("23")

    def test_m03_24_security_lite_adversarial(self):
        self._execute("24")

    def test_m03_25_intake_audit_adversarial(self):
        self._execute("25")


if __name__ == "__main__":
    unittest.main()
