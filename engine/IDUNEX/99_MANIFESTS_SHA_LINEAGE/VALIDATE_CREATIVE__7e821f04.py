#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, re, sys, zipfile, hashlib
sys.dont_write_bytecode=True
VALIDATOR="VALIDATE_CREATIVE_CERTIFICATION_TRUTHFULNESS"
ENGINE_CONTRACT="03_PROJECT_FACTORY/04_DELIVERY_GATES/H269_H280_PROJECT__a7b1a62c.json"

def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))

def sha(p: Path):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def out(result="PASS", **kw):
    d={"validator":VALIDATOR,"result":result,"fail_codes":[],"blocking_warnings":0,"CREATIVE_OUTPUT_CERTIFIED":False}
    d.update(kw)
    if result!="PASS" and not d.get("fail_codes"):
        d["fail_codes"]=["FAIL_"+VALIDATOR.replace("VALIDATE_","")]
    d.setdefault("validators_fail", 0 if result=="PASS" else len(d.get("fail_codes", [])))
    d.setdefault("blocking_warnings", 0)
    d.setdefault("fail_codes", [])
    d.setdefault("CREATIVE_OUTPUT_CERTIFIED", False)
    # VALIDATOR_OUTPUT_NORMALIZATION_V1_0_0: standard active validator result fields; no validation weakening.
    print(json.dumps(d,ensure_ascii=False,indent=2)); return 0 if result=="PASS" else 1

def engine_mode(root: Path):
    c=root/ENGINE_CONTRACT
    if not c.is_file(): return out("FAIL", fail_codes=["FAIL_H269_H280_CONTRACT_MISSING"], path=str(c))
    data=load_json(c)
    needed=["H269","H270","H271","H272","H273","H274","H275","H276","H277","H278","H279","H280"]
    missing=[x for x in needed if x not in data.get("rules",{})]
    if missing: return out("FAIL", fail_codes=["FAIL_H269_H280_RULE_MISSING"], missing=missing)
    if data.get("creative_output_certified") is not False: return out("FAIL", fail_codes=["FAIL_CREATIVE_OUTPUT_CERTIFIED_TRUE"])
    return out("PASS", scope=data.get("scope"), engine_contract="PASS")

def project_mode(root: Path):
    failures=[]
    # H269 active results scan
    surfaces=("07_QA_VALIDATORS/VALIDATOR_RESULTS","09_MANIFESTS_SHA","10_RELEASE","AGENT_FORENSIC_COMPANION")
    if VALIDATOR.endswith("ACTIVE_RESULTS_ALL_PASS") or VALIDATOR.endswith("FINAL_CERTIFICATE_SURFACE_SYNC"):
        for p in root.rglob("*.json"):
            rel=p.relative_to(root).as_posix()
            if not any(rel.startswith(s+"/") for s in surfaces) or rel.startswith("12_HISTORICAL_NON_AUTHORITY/"): continue
            try: d=load_json(p)
            except Exception: failures.append({"path":rel,"code":"FAIL_ACTIVE_JSON_UNREADABLE"}); continue
            stack=[d]
            while stack:
                x=stack.pop()
                if isinstance(x,dict):
                    cls=str(x.get("classification") or x.get("authority_status") or "")
                    if cls not in {"NON_AUTHORITY_REFERENCE","NEGATIVE_TEST_FIXTURE","DOCUMENTATION_EXAMPLE"}:
                        if any(str(x.get(k,"")).upper()=="FAIL" for k in ("result","status","validator_result")): failures.append({"path":rel,"code":"FAIL_ACTIVE_RESULT_FAIL"})
                        if isinstance(x.get("fail_codes"),list) and x.get("fail_codes") and x.get("expected_block") is not True: failures.append({"path":rel,"code":"FAIL_ACTIVE_FAIL_CODES_NOT_EMPTY"})
                        if int(x.get("blocking_warnings",0) or 0)>0: failures.append({"path":rel,"code":"FAIL_ACTIVE_BLOCKING_WARNINGS"})
                    stack.extend(x.values())
                elif isinstance(x,list): stack.extend(x)
    if VALIDATOR.endswith("ZIP_REOPENED_COUNTS_AUTHORITATIVE"):
        proof=root/"09_MANIFESTS_SHA/PROJECT_REOPENED_ZIP_PROOF.json"
        if not proof.is_file(): failures.append({"code":"FAIL_PROJECT_REOPENED_ZIP_PROOF_MISSING"})
        else:
            d=load_json(proof);
            if d.get("result") not in {"PASS","CONTENT_TREE_PROOF_NOT_FINAL_ZIP_SHA_PENDING"}: failures.append({"code":"FAIL_PROJECT_REOPENED_ZIP_PROOF_NOT_PASS"})
    if VALIDATOR.endswith("COMPANION_LEDGER_TRUTHFULNESS"):
        for p in (root/"AGENT_FORENSIC_COMPANION").glob("FIELD_SOURCE_TRACE_LEDGER_MODEL_*.json"):
            d=load_json(p); rc=int(d.get("row_count",0) or 0); mode=d.get("mode")
            if d.get("result")=="PASS" and rc==0 and mode not in {"COMPACT_LEDGER_SUMMARY","NON_AUTHORITY_POINTER"}: failures.append({"path":p.name,"code":"FAIL_EMPTY_LEDGER_PASS"})
            if mode not in {"FULL_LEDGER_COPY","COMPACT_LEDGER_SUMMARY","NON_AUTHORITY_POINTER","NOT_EXECUTED_WITH_REASON"}: failures.append({"path":p.name,"code":"FAIL_LEDGER_MODE_INVALID"})
            if d.get("result")=="PASS" and not d.get("source_sha256"): failures.append({"path":p.name,"code":"FAIL_LEDGER_SOURCE_SHA_MISSING"})
    if VALIDATOR.endswith("PROMPT_PACK_CLASSIFICATION"):
        for p in (root/"AGENT_FORENSIC_COMPANION").glob("PROMPT_PACK_TEMPLATE_*.md"):
            txt=p.read_text(encoding="utf-8",errors="ignore")
            m=re.search(r"^classification=(.+)$",txt,re.M); c=m.group(1).strip() if m else ""
            if c not in {"RUNTIME_PROMPT_PACK","NON_RUNTIME_REFERENCE","VENDOR_HANDOFF_TEMPLATE","DOCUMENTATION_EXAMPLE"}: failures.append({"path":p.name,"code":"FAIL_PROMPT_PACK_CLASSIFICATION_MISSING"})
            if c!="RUNTIME_PROMPT_PACK" and ("reason_code=" not in txt or "validator_scope=excluded_from_AJ_runtime_validation" not in txt): failures.append({"path":p.name,"code":"FAIL_NON_RUNTIME_SCOPE_REASON_MISSING"})
    if VALIDATOR.endswith("CANONICAL_MODEL_NAME_ALLOWLIST"):
        allow=root/"09_MANIFESTS_SHA/RUNTIME_CANONICAL_MODEL_NAME_ALLOWLIST.json"
        if not allow.is_file(): failures.append({"code":"FAIL_RUNTIME_CANONICAL_MODEL_NAME_ALLOWLIST_MISSING"})
    if VALIDATOR.endswith("EXACT_DUPLICATE_ALLOWLIST_VISIBLE"):
        p=root/"09_MANIFESTS_SHA/EXACT_DUPLICATE_ALLOWLIST.json"
        if not p.is_file(): failures.append({"code":"FAIL_EXACT_DUPLICATE_ALLOWLIST_MISSING"})
        else:
            for g in load_json(p).get("duplicate_groups",[]):
                if not g.get("reason_code") or not g.get("authority_path"): failures.append({"code":"FAIL_DUPLICATE_GROUP_REASON_MISSING"})
    if VALIDATOR.endswith("AMBIGUOUS_TOKEN_GUARD"):
        hard={"TODO","TBD","PLACEHOLDER","DUMMY","STUB","REPRESENTATIVE_ONLY","ASSUMED_PASS","FACTORY_DEFINED_PROPOSED","PASS_BY_ACTIVE_FACTORY_CONTRACT"}
        for p in root.rglob("*"):
            if not p.is_file() or p.suffix.lower() not in {".json",".md",".txt",".csv"}: continue
            rel=p.relative_to(root).as_posix()
            if rel.startswith("12_HISTORICAL_NON_AUTHORITY/"): continue
            txt=p.read_text(encoding="utf-8",errors="ignore")
            if any(marker in txt for marker in ['"classification": "NEGATIVE_TEST_FIXTURE"', 'classification=NEGATIVE_TEST_FIXTURE', '"classification":"NEGATIVE_TEST_FIXTURE"']):
                continue
            for tok in hard:
                if re.search(r"(?<![A-Z0-9_])"+re.escape(tok)+r"(?![A-Z0-9_])",txt): failures.append({"path":rel,"token":tok,"code":"FAIL_ACTIVE_PLACEHOLDER_OR_AMBIGUOUS_TOKEN"})
    if VALIDATOR.endswith("MATRIX_COMPLETION_PROOF"):
        p=root/"09_MANIFESTS_SHA/PROJECT_MATRIX_COMPLETION_PROOF.json"
        if not p.is_file(): failures.append({"code":"FAIL_MATRIX_COMPLETION_PROOF_MISSING"})
        else:
            d=load_json(p)
            if not (d.get("MATRIX_CASES_EXECUTED")==d.get("MATRIX_CASES_TOTAL") and d.get("MATRIX_CASES_FAIL")==0 and d.get("MATRIX_COMPLETION_SIGNAL") in {"PASS","COMPLETE_PASS"}): failures.append({"code":"FAIL_MATRIX_COMPLETION_SIGNAL_INVALID"})
    if VALIDATOR.endswith("CREATIVE_CERTIFICATION_TRUTHFULNESS"):
        p=root/"09_MANIFESTS_SHA/CREATIVE_CERTIFICATION_TRUTHFULNESS.json"
        if not p.is_file(): failures.append({"code":"FAIL_CREATIVE_CERTIFICATION_TRUTHFULNESS_MISSING"})
        else:
            d=load_json(p)
            if d.get("CREATIVE_OUTPUT_CERTIFIED") is not False or d.get("PACKAGE_PASS_IMPLIES_CREATIVE_OUTPUT_PASS") is not False: failures.append({"code":"FAIL_CREATIVE_CERTIFICATION_CONTRADICTION"})
    return out("PASS" if not failures else "FAIL", failures=failures, validators_fail=len(failures), fail_codes=[f["code"] for f in failures])

def main():
    target=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
    if target.suffix.lower()==".zip":
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            with zipfile.ZipFile(target) as z:
                bad=z.testzip()
                if bad: return out("FAIL", fail_codes=["FAIL_ZIP_CRC"], bad_entry=bad)
                z.extractall(td)
            roots=[p for p in Path(td).iterdir() if p.is_dir()]
            return project_mode(roots[0]) if roots else out("FAIL", fail_codes=["FAIL_ZIP_ROOT_COUNT"])
    if (target/ENGINE_CONTRACT).is_file(): return engine_mode(target)
    return project_mode(target)
if __name__=="__main__":
    raise SystemExit(main())
