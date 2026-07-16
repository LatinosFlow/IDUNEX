#!/usr/bin/env python3
"""IDUNEX H396 real command matrix runner for H391-H410.

Legacy H238 name is retained only for path compatibility.

Single authoritative executable for the H238 matrix: 1 demo N2 case plus
basic/intermediate/complete N1..N10. It writes compact evidence only and removes
all generated project directories/ZIPs unless --keep-work is passed.
"""
from __future__ import annotations
from pathlib import Path
import argparse, csv, hashlib, json, os, shutil, signal, subprocess, sys, tempfile, time, zipfile

SCRIPT_DIR = Path(__file__).resolve().parent
FACTORY = SCRIPT_DIR / "IDUNEX_PROJECT_FACTORY_v1.0.0.py"
DEFAULT_TIMEOUT = 300


def resolve_semantic_version() -> str:
    # Current release metadata is authoritative. Factory constant is fallback only.
    for candidate in (
        SCRIPT_DIR.parents[1] / "00_INDEX" / "00_CONTROL_CENTER" / "ACTIVE_VERSION.md",
        SCRIPT_DIR.parents[1] / "00_INDEX" / "ACTIVE_VERSION.txt",
    ):
        if candidate.is_file():
            for line in candidate.read_text(encoding="utf-8", errors="replace").splitlines():
                if line.strip().startswith("SEMANTIC_VERSION="):
                    value = line.split("=", 1)[1].strip()
                    if value:
                        return value
    try:
        text = FACTORY.read_text(encoding="utf-8", errors="replace")
        import re
        m = re.search(r'^SEMANTIC_VERSION\s*=\s*["\']([^"\']+)["\']', text, re.M)
        if m:
            return m.group(1)
    except Exception:
        pass
    return "v1.0.0"


SEMANTIC_VERSION = resolve_semantic_version()
PROJECT_VERSION_TOKEN = SEMANTIC_VERSION
LEGACY_TOKEN = "V1" + "_0_0"


def sha256(path: Path) -> str:
    h = hashlib.sha256(); h.update(path.read_bytes()); return h.hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _process_group_members(pgid: int) -> list[int]:
    if os.name != "posix":
        return []
    try:
        ps = subprocess.run(["ps", "-o", "pid=", "-g", str(pgid)], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, timeout=3, check=False)
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


def run_cmd(cmd: list[str], timeout: int) -> tuple[int, float, str, str, bool]:
    # Bounded deterministic command execution with process-group kill-tree.
    # The runner observes the real child rc and never treats an output JSON as enough if the command is stuck.
    start = time.monotonic()
    out_fd, out_name = tempfile.mkstemp(prefix="idunex_matrix_stdout_", suffix=".log")
    err_fd, err_name = tempfile.mkstemp(prefix="idunex_matrix_stderr_", suffix=".log")
    os.close(out_fd); os.close(err_fd)
    out_path = Path(out_name); err_path = Path(err_name)
    proc = None
    timed_out = False
    try:
        with out_path.open("w", encoding="utf-8") as out_f, err_path.open("w", encoding="utf-8") as err_f:
            proc = subprocess.Popen(
                cmd,
                stdout=out_f,
                stderr=err_f,
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
            try:
                rc = proc.wait(timeout=max(1, int(timeout)))
            except subprocess.TimeoutExpired:
                timed_out = True
                if pgid is not None:
                    _kill_process_group(pgid)
                else:
                    proc.kill()
                try:
                    rc = proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    rc = proc.wait()
        out = out_path.read_text(encoding="utf-8", errors="replace")[-4000:] if out_path.exists() else ""
        err = err_path.read_text(encoding="utf-8", errors="replace")[-4000:] if err_path.exists() else ""
    finally:
        out_path.unlink(missing_ok=True)
        err_path.unlink(missing_ok=True)
    return rc, round(time.monotonic() - start, 3), out, err, timed_out




def generation_complete(output_json: Path) -> bool:
    try:
        payload = json.loads(output_json.read_text(encoding="utf-8"))
        zip_path = Path(str(payload.get("project_zip", "")))
        companion = Path(str(payload.get("companion", "")))
        final_validation = payload.get("final_reopened_validation") if isinstance(payload.get("final_reopened_validation"), dict) else {}
        return payload.get("result") == "PASS" and final_validation.get("result") == "PASS" and zip_path.is_file() and companion.is_file()
    except Exception:
        return False


def run_generate_cmd(cmd: list[str], output_json: Path, timeout: int) -> tuple[int, float, str, str, bool, bool]:
    # H391-H396: bounded generation must observe real command termination.
    # A PASS out.json is not sufficient if the process stays alive.
    rc, seconds, out, err, timed_out = run_cmd(cmd, timeout)
    post_completion_kill = bool(timed_out and generation_complete(output_json))
    return rc, seconds, out, err, timed_out, post_completion_kill

def model_spec(level: str, i: int) -> dict:
    if level == "basic":
        return {}
    gender = "hombre adulto ficticio" if i % 2 else "mujer adulta ficticia"
    base = {
        "age": 24 + ((i * 3) % 17),
        "origin": f"SYNTH_ORIGIN_MATRIX_{i:02d}",
        "gender": gender,
        "role": "creador audiovisual y comunicador de marca" if i % 2 else "host creativa principal y comunicadora de marca",
        "height_cm": 160 + ((i * 5) % 22),
    }
    if level == "complete":
        base.update({
            "name": f"SYNTH_MODEL_MATRIX_{i:03d} IDENTITY",
            "style_direction": f"adult editorial identity-safe profile {i:02d}",
            "personality_direction": f"differentiated temperament marker {i:02d}",
            "visual_direction": f"natural photoreal human cues marker {i:02d}",
            "body_direction": f"coherent adult proportions marker {i:02d}",
            "hair_direction": f"distinct realistic hair physics marker {i:02d}",
            "wardrobe_direction": f"brand-safe non-explicit wardrobe marker {i:02d}",
            "voice_direction": f"original non-celebrity voice marker {i:02d}",
            "environment_direction": f"PROJECT_DECLARED_LOCALITY production context marker {i:02d}",
            "brand_alignment": "PROJECT_BRAND_ENTITY production-safe identity system",
            "safety_notes": "adult fictional model, no sexualized/minor-coded styling, no real-person copying",
        })
    return base


def entity_profile(scope: str) -> dict:
    return {
        "project_client_entity": "H238_MATRIX_CLIENT_ENTITY_NON_AUTHORITY",
        "project_owner_entity": "H238_MATRIX_OWNER_ENTITY_NON_AUTHORITY",
        "project_brand_entity": "H238_MATRIX_BRAND_ENTITY_NON_AUTHORITY",
        "service_provider_entity": "H238_MATRIX_SERVICE_PROVIDER_NON_AUTHORITY",
        "rights_holder_entity": "H238_MATRIX_RIGHTS_HOLDER_NON_AUTHORITY",
        "project_jurisdiction": "PROJECT_DECLARED_JURISDICTION H238 controlled QA jurisdiction",
        "brand_usage_scope": scope,
        "logo_asset_policy": "none",
        "brand_visual_identity_status": "NO_OFFICIAL_LOGO_ASSET_SUBMITTED",
        "model_ownership_statement": "All generated models are fictional adult synthetic QA cases and are not defaults for the engine.",
        "allowed_brand_contexts": ["H238 matrix QA", "internal validation", "non-authority evidence"],
        "forbidden_brand_contexts": ["third-party endorsement", "unlicensed logo reproduction", "real-person impersonation"],
    }


def cases() -> list[dict]:
    rows = [{"case_id": "H238_DEMO_N2", "level": "demo", "model_count": 2, "scope": "demo"}]
    for level in ("basic", "intermediate", "complete"):
        for n in range(1, 11):
            rows.append({"case_id": f"H238_{level.upper()}_N{n}", "level": level, "model_count": n, "scope": "internal" if level != "complete" else "commercial/internal"})
    return rows


def inspect_project_zip(zip_path: Path, project_id: str, n: int) -> dict:
    out = {
        "zipfile_testzip": "FAIL",
        "profile360_counts": [],
        "techext_counts": [],
        "runtime_chatgpt": 0,
        "runtime_copilot": 0,
        "field_source_trace_ledgers": 0,
        "active_runtime_upload_manifest_present": False,
        "creative_output_certified_false": False,
    }
    with zipfile.ZipFile(zip_path) as z:
        bad = z.testzip(); names = z.namelist(); prefix = project_id + "/"
        out["zipfile_testzip"] = "PASS" if bad is None else f"FAIL:{bad}"
        out["runtime_chatgpt"] = sum(1 for name in names if name.startswith(prefix + "03_AGENTS/CHATGPT/01_RUNTIME_UPLOAD/") and not name.endswith("/"))
        out["runtime_copilot"] = sum(1 for name in names if name.startswith(prefix + "03_AGENTS/COPILOT/01_RUNTIME_UPLOAD/") and not name.endswith("/"))
        out["field_source_trace_ledgers"] = sum(1 for name in names if name.startswith(prefix + "08_EVIDENCE_LINEAGE/FIELD_SOURCE_TRACE_LEDGER_MODEL_") and name.endswith(".json"))
        out["active_runtime_upload_manifest_present"] = prefix + "09_MANIFESTS_SHA/ACTIVE_RUNTIME_UPLOAD_MANIFEST.json" in names
        model_index = json.loads(z.read(prefix + "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json").decode("utf-8"))
        model_ids = [m.get("model_id") for m in model_index.get("models", [])]
        for mid in model_ids:
            p360 = json.loads(z.read(prefix + f"02_MODELS/{mid}/PROFILE360_FULL60.json").decode("utf-8"))
            tech = json.loads(z.read(prefix + f"02_MODELS/{mid}/TECHEXT_FULL10.json").decode("utf-8"))
            out["profile360_counts"].append(len(p360.get("sections", [])))
            out["techext_counts"].append(len(tech.get("fields", [])))
        manifest = json.loads(z.read(prefix + "00_PROJECT_INDEX/PROJECT_MANIFEST.json").decode("utf-8"))
        out["creative_output_certified_false"] = manifest.get("CREATIVE_OUTPUT_CERTIFIED") is False
    out["profile360_61_per_model"] = all(x == 61 for x in out["profile360_counts"]) and len(out["profile360_counts"]) == n
    out["techext_284_per_model"] = all(x == 284 for x in out["techext_counts"]) and len(out["techext_counts"]) == n
    out["runtime_logical_10_plus_n"] = out["runtime_chatgpt"] == 10 + n and out["runtime_copilot"] == 10 + n
    out["field_source_trace_ledger_all_models"] = out["field_source_trace_ledgers"] == n
    return out


def run_case(case: dict, work: Path, timeout: int) -> dict:
    project_id = f"IDUNEX_PROJECT_{case['case_id']}_{PROJECT_VERSION_TOKEN}"
    case_dir = work / case["case_id"]
    out_dir = case_dir / "out"
    input_path = case_dir / "input.json"
    case_dir.mkdir(parents=True, exist_ok=True)
    spec = {
        "project_id": project_id,
        "project_entity_profile": entity_profile(case["scope"]),
        "models": [model_spec(case["level"], i) for i in range(1, case["model_count"] + 1)],
    }
    if case["level"] == "basic":
        spec.pop("project_entity_profile")
    write_json(input_path, spec)
    generate_json = case_dir / "generate.json"
    validate_json = case_dir / "validate.json"
    gen_cmd = [sys.executable, str(FACTORY), "generate", "--input", str(input_path), "--output", str(out_dir), "--summary", "--output-json", str(generate_json)]
    gen_rc, gen_seconds, gen_stdout, gen_stderr, gen_timeout, post_completion_kill = run_generate_cmd(gen_cmd, generate_json, timeout)
    row = {**case, "project_id": project_id, "generate_rc": gen_rc, "generate_seconds": gen_seconds, "generate_timeout": gen_timeout, "post_completion_process_kill": post_completion_kill, "result": "FAIL", "fail_codes": []}
    gen = {}
    if generate_json.is_file():
        try: gen = json.loads(generate_json.read_text(encoding="utf-8"))
        except Exception as e: row["fail_codes"].append("FAIL_GENERATE_JSON_INVALID"); row["generate_json_error"] = str(e)
    else:
        row["fail_codes"].append("FAIL_GENERATE_JSON_MISSING")
    row["generate_result"] = gen.get("result")
    row["generated_zip"] = gen.get("project_zip")
    row["generated_companion"] = gen.get("companion")
    zip_path = Path(str(gen.get("project_zip", "")))
    companion = Path(str(gen.get("companion", "")))
    companion_match = False
    if zip_path.is_file() and companion.is_file():
        actual_sha = sha256(zip_path); row["zip_sha256"] = actual_sha; row["zip_bytes"] = zip_path.stat().st_size
        companion_sha = companion.read_text(encoding="utf-8").split()[0].lower()
        companion_match = companion_sha == actual_sha
    else:
        actual_sha = None; row["fail_codes"].append("FAIL_ZIP_OR_COMPANION_MISSING")
    row["companion_sha_match"] = "PASS" if companion_match else "FAIL"
    if zip_path.is_file():
        # H267: use the generate finalizer's real reopened validation as first-class evidence.
        # This avoids redundant long external validate calls while preserving actual ZIP reopen, testzip,
        # companion SHA and bounded validator evidence produced during generation.
        val = gen.get("final_reopened_validation") if isinstance(gen.get("final_reopened_validation"), dict) else None
        if val:
            row.update({"validate_rc": 0 if val.get("result") == "PASS" else 1, "validate_seconds": 0.0, "validate_timeout": False, "validation_source": "GENERATE_FINAL_REOPENED_VALIDATION"})
            write_json(validate_json, val)
        else:
            val_cmd = [sys.executable, str(FACTORY), "validate", str(zip_path), "--summary", "--output-json", str(validate_json)]
            val_rc, val_seconds, val_stdout, val_stderr, val_timeout = run_cmd(val_cmd, timeout)
            row.update({"validate_rc": val_rc, "validate_seconds": val_seconds, "validate_timeout": val_timeout, "validation_source": "EXTERNAL_VALIDATE_COMMAND"})
            if validate_json.is_file():
                try: val = json.loads(validate_json.read_text(encoding="utf-8"))
                except Exception as e: val = {}; row["fail_codes"].append("FAIL_VALIDATE_JSON_INVALID"); row["validate_json_error"] = str(e)
            else:
                val = {}; row["fail_codes"].append("FAIL_VALIDATE_JSON_MISSING")
        row["validate_result"] = val.get("result")
        row["validators_fail"] = val.get("validators_fail")
        row["blocking_warnings"] = val.get("blocking_warnings")
        row["validation_fail_codes"] = val.get("fail_codes", [])
        try:
            zi = inspect_project_zip(zip_path, project_id, case["model_count"])
            row.update(zi)
        except Exception as e:
            row["fail_codes"].append("FAIL_ZIP_INSPECTION_ERROR"); row["zip_inspection_error"] = str(e)
    else:
        row.update({"validate_rc": 1, "validate_result": "FAIL", "validators_fail": 1, "blocking_warnings": 0, "validation_fail_codes": ["FAIL_ZIP_MISSING"]})
    gates_ok = [
        row.get("generate_rc") == 0,
        row.get("generate_result") == "PASS",
        row.get("validate_rc") == 0,
        row.get("validate_result") == "PASS",
        row.get("companion_sha_match") == "PASS",
        row.get("zipfile_testzip") == "PASS",
        row.get("profile360_61_per_model") is True,
        row.get("techext_284_per_model") is True,
        row.get("runtime_logical_10_plus_n") is True,
        row.get("field_source_trace_ledger_all_models") is True,
        row.get("active_runtime_upload_manifest_present") is True,
        row.get("creative_output_certified_false") is True,
        row.get("validators_fail") == 0,
        row.get("blocking_warnings") == 0,
        not row.get("validation_fail_codes"),
        not row.get("fail_codes"),
        row.get("generate_timeout") is False,
        row.get("validate_timeout") is False,
        row.get("post_completion_process_kill") is False,
    ]
    row["delivery_allowed"] = "PASS" if gates_ok[0:3] and row.get("validate_result") == "PASS" else "FAIL"
    row["result"] = "PASS" if all(gates_ok) else "FAIL"
    if row["result"] != "PASS" and not row["fail_codes"]:
        row["fail_codes"].append("FAIL_H238_CASE_GATE")
    # Remove per-case project output immediately. Keep only compact row in memory.
    shutil.rmtree(out_dir, ignore_errors=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    ap.add_argument("--keep-work", action="store_true")
    ap.add_argument("--resume", action="store_true", help="Reuse existing partial summary and continue missing/failed cases")
    ap.add_argument("--stream-progress", action="store_true", help="Print one compact JSON progress line per case")
    args = ap.parse_args()
    work = Path(args.work).resolve(); output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    partial_path = output_dir / "H238_FULL_31_PROJECT_MATRIX_PARTIAL.json"
    if work.exists() and not args.resume: shutil.rmtree(work)
    work.mkdir(parents=True, exist_ok=True)
    rows = []
    if args.resume and partial_path.is_file():
        try:
            previous = json.loads(partial_path.read_text(encoding="utf-8"))
            rows = [r for r in previous.get("cases", []) if r.get("result") == "PASS"]
        except Exception:
            rows = []
    done_ids = {r.get("case_id") for r in rows}
    start = time.monotonic()
    all_cases = cases()
    for idx, case in enumerate(all_cases, 1):
        if case["case_id"] in done_ids:
            if args.stream_progress:
                print(json.dumps({"case_index": idx, "case_count": len(all_cases), "case_id": case["case_id"], "status": "RESUMED_PASS"}, ensure_ascii=False), flush=True)
            continue
        row = run_case(case, work, args.timeout)
        rows = [r for r in rows if r.get("case_id") != case["case_id"]] + [row]
        pass_count_partial = sum(1 for r in rows if r.get("result") == "PASS")
        partial = {
            "gate_id": "H238_FULL_31_PROJECT_MATRIX_REAL_EXECUTION",
            "runner": "IDUNEX_PROJECT_MATRIX_31_RUNNER.py",
            "semantic_version": SEMANTIC_VERSION,
            "project_version_token": PROJECT_VERSION_TOKEN,
            "matrix_lineage_version_parity": "PASS" if all(PROJECT_VERSION_TOKEN in r.get("project_id", "") and LEGACY_TOKEN not in r.get("project_id", "") for r in rows) else "FAIL",
            "streaming_progress": True,
            "resume_supported": True,
            "case_count": len(all_cases),
            "completed_count": len(rows),
            "pass_count": pass_count_partial,
            "fail_count": len(rows) - pass_count_partial,
            "last_case_id": case["case_id"],
            "last_case_result": row.get("result"),
            "CREATIVE_OUTPUT_CERTIFIED": False,
            "cases": sorted(rows, key=lambda x: x.get("case_id", "")),
        }
        write_json(partial_path, partial)
        if args.stream_progress:
            print(json.dumps({"case_index": idx, "case_count": len(all_cases), "case_id": case["case_id"], "result": row.get("result"), "pass_count": pass_count_partial, "fail_codes": row.get("fail_codes", [])}, ensure_ascii=False), flush=True)
    rows = sorted(rows, key=lambda x: x.get("case_id", ""))
    elapsed = round(time.monotonic() - start, 3)
    pass_count = sum(1 for r in rows if r.get("result") == "PASS")
    summary = {
        "gate_id": "H238_FULL_31_PROJECT_MATRIX_REAL_EXECUTION",
        "runner": "IDUNEX_PROJECT_MATRIX_31_RUNNER.py",
        "semantic_version": SEMANTIC_VERSION,
        "project_version_token": PROJECT_VERSION_TOKEN,
        "active_project_ids_version_parity": all(PROJECT_VERSION_TOKEN in r.get("project_id", "") and LEGACY_TOKEN not in r.get("project_id", "") for r in rows),
        "case_count": len(rows),
        "pass_count": pass_count,
        "fail_count": len(rows) - pass_count,
        "PROJECT_31_FULL_MATRIX_EXECUTED": "PASS" if pass_count == 31 else "FALSE",
        "PROJECT_31_FULL_MATRIX_PASS_COUNT": f"{pass_count}/31",
        "FULL_31_PROJECT_MATRIX_REAL_EXECUTION": "PASS" if pass_count == 31 else "FAIL",
        "result": "PASS" if pass_count == 31 else "FAIL",
        "elapsed_seconds": elapsed,
        "timeout_per_process_seconds": args.timeout,
        "no_test_output_zips_in_engine": True,
        "streaming_progress": True,
        "resume_supported": True,
        "partial_summary_path": "H238_FULL_31_PROJECT_MATRIX_PARTIAL.json",
        "compact_output_per_case": True,
        "CREATIVE_OUTPUT_CERTIFIED": False,
        "cases": rows,
    }
    write_json(output_dir / "H238_FULL_31_PROJECT_MATRIX_SUMMARY.json", summary)
    fields = sorted({k for r in rows for k in r.keys() if k not in {"generated_zip", "generated_companion"}})
    with (output_dir / "H238_FULL_31_PROJECT_MATRIX.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v for k, v in r.items() if k in fields})
    if not args.keep_work:
        shutil.rmtree(work, ignore_errors=True)
    return 0 if summary["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
