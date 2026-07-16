#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, re, sys, zipfile, hashlib, collections
sys.dont_write_bytecode=True
VALIDATOR="VALIDATE_PROJECT_EXACT_DUPLICATE_ALLOWLIST_VISIBLE"
# DUP-LEDGER-REALITY-001 integrated hard gate; no parallel validator.

CURRENT_SCOPE="RENORMALIZACION_VERSION_OFICIAL_v1.0.0_Y_DEMO_000_2_MODELOS"
PREVIOUS_SCOPE_COMPATIBILITY="MUTATION_SELF_TEST_H62_MATRIX_PROOF_PARITY_AND_ACTIVE_LEDGER_EXCLUSION_CLARITY"
LEGACY_SCOPE_COMPATIBILITY="DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY"
ACTIVE_SCOPE_SURFACES=(
 "00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md",
 "00_INDEX/00_CONTROL_CENTER/STATUS.md",
 "00_INDEX/ACTIVE_VERSION.txt",
 "00_INDEX/CHANGELOG.md",
 "11_RELEASE_INTERNAL/CHANGELOG.md",
)

def _read_text_safe(p: Path):
    return p.read_text(encoding="utf-8", errors="ignore")

def _active_surface_scope_sync_gate(root: Path):
    failures=[]
    for rel in ACTIVE_SCOPE_SURFACES:
        p=root/rel
        if not p.is_file():
            failures.append({"path":rel,"code":"FAIL_ACTIVE_SCOPE_SURFACE_MISSING"}); continue
        tx=_read_text_safe(p)
        if f"CORRECTION_SCOPE={CURRENT_SCOPE}" not in tx:
            failures.append({"path":rel,"code":"FAIL_ACTIVE_CORRECTION_SCOPE_NOT_CURRENT"})
        if PREVIOUS_SCOPE_COMPATIBILITY not in tx:
            failures.append({"path":rel,"code":"FAIL_PREVIOUS_SCOPE_COMPATIBILITY_MISSING"})
        if LEGACY_SCOPE_COMPATIBILITY not in tx:
            failures.append({"path":rel,"code":"FAIL_LEGACY_SCOPE_COMPATIBILITY_MISSING"})
        if f"CORRECTION_SCOPE={LEGACY_SCOPE_COMPATIBILITY}" in tx or f"CORRECTION_SCOPE={PREVIOUS_SCOPE_COMPATIBILITY}" in tx:
            failures.append({"path":rel,"code":"FAIL_ACTIVE_CORRECTION_SCOPE_STALE"})
    text_exts={'.json','.md','.txt','.csv','.sh'}
    stale_patterns=(
        f"CORRECTION_SCOPE={LEGACY_SCOPE_COMPATIBILITY}",
        f"correction_scope: {LEGACY_SCOPE_COMPATIBILITY}",
        f"\"correction_scope\": \"{LEGACY_SCOPE_COMPATIBILITY}\"",
        f"\"CORRECTION_SCOPE\": \"{LEGACY_SCOPE_COMPATIBILITY}\"",
    )
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix.lower() not in text_exts:
            continue
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/')):
            continue
        tx=_read_text_safe(p)
        if any(pat in tx for pat in stale_patterns) and 'SCANNER_LITERAL_NON_AUTHORITY' not in tx:
            failures.append({"path":rel,"code":"FAIL_STALE_ACTIVE_CORRECTION_SCOPE_LITERAL"})
        if 'VERSION_BUMP=YES' in tx or '"version_bump": "YES"' in tx or '"version_bump":"YES"' in tx:
            failures.append({'path':rel,'code':'FAIL_ACTIVE_VERSION_BUMP_YES_SURFACE'})
        lower_matrix_fail = any(t in tx for t in ['"max_matrix_current_run": "FAIL"','"max_matrix_current_run":"FAIL"','max_matrix_current_run=FAIL','"n1_to_n10_x3_matrix": "FAIL"','"n1_to_n10_x3_matrix":"FAIL"','n1_to_n10_x3_matrix=FAIL'])
        upper_matrix_pass = any(t in tx for t in ['"MAX_MATRIX_CURRENT_RUN": "PASS"','"MAX_MATRIX_CURRENT_RUN":"PASS"','MAX_MATRIX_CURRENT_RUN=PASS','"N1_TO_N10_X3_MATRIX": "PASS"','"N1_TO_N10_X3_MATRIX":"PASS"','N1_TO_N10_X3_MATRIX=PASS'])
        if lower_matrix_fail and upper_matrix_pass:
            failures.append({'path':rel,'code':'FAIL_ACTIVE_MATRIX_FAIL_PASS_CONTRADICTION'})
        score_10 = any(t in tx for t in ['SCORE=10/10','"SCORE": "10/10"','"SCORE":"10/10"'])
        blocked_markers = ['READY_FOR_REAUDIT','FAIL_MAX_MATRIX_NOT_EXECUTED_CURRENT_RUN','"SCORE": "BLOCKED"','"SCORE":"BLOCKED"','SCORE=BLOCKED','VALIDATORS_FAIL=1','"VALIDATORS_FAIL": 1','"validators_fail": 1','"validators_fail":1','ACTIVE_BLOCKED_WHILE_MAX_MATRIX_FAIL']
        if score_10 and any(t in tx for t in blocked_markers):
            failures.append({'path':rel,'code':'FAIL_ACTIVE_SCORE_10_WITH_BLOCKED_OR_FAIL_MARKER'})
    contract=root/'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json'
    if contract.is_file():
        try:
            d=json.loads(contract.read_text(encoding='utf-8'))
            if not (d.get('MAX_MATRIX_CURRENT_RUN')=='PASS' and d.get('N1_TO_N10_X3_MATRIX')=='PASS' and d.get('VALIDATORS_FAIL')==0 and d.get('BLOCKING_WARNINGS')==0 and d.get('FAIL_CODES')==[] and d.get('SCORE')=='10/10'):
                failures.append({'path':'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','code':'FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_NOT_SYNCED'})
        except Exception:
            failures.append({'path':'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','code':'FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_UNREADABLE'})
    else:
        failures.append({'path':'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','code':'FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_MISSING'})
    return not failures, failures

DUPLICATE_SELF_EXCLUDED={
 '99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json','99_MANIFESTS_SHA_LINEAGE/EXACT_DUPLICATE_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_ALLOWLIST.json','07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.json','07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.md',
 '99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt','99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt'
}

def _sha256_path(p: Path):
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def _active_duplicate_groups(root: Path):
    groups={}
    for p in sorted(root.rglob('*')):
        if not p.is_file(): continue
        rel=p.relative_to(root).as_posix()
        if rel.startswith('14_HISTORICAL_NON_AUTHORITY/') or rel in DUPLICATE_SELF_EXCLUDED: continue
        groups.setdefault(_sha256_path(p),[]).append(rel)
    return {h:sorted(ps) for h,ps in groups.items() if len(ps)>1}

def _ledger_declared_groups(data):
    return {g.get('sha256'): sorted(g.get('paths') or ([g.get('authority_path')]+g.get('mirror_paths',[]))) for g in (data.get('groups') or data.get('duplicate_groups') or []) if isinstance(g,dict) and g.get('sha256')}

def _duplicate_ledger_sync_gate(root: Path):
    failures=[]
    real=_active_duplicate_groups(root)
    canonical_paths=[
      '99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json',
      '99_MANIFESTS_SHA_LINEAGE/EXACT_DUPLICATE_ALLOWLIST.json',
      '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_ALLOWLIST.json'
    ]
    for rel in canonical_paths:
        p=root/rel
        if not p.is_file():
            failures.append({'path':rel,'code':'FAIL_DUPLICATE_ALLOWLIST_MISSING'}); continue
        try: d=json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            failures.append({'path':rel,'code':'FAIL_DUPLICATE_ALLOWLIST_JSON_INVALID'}); continue
        if d.get('correction_scope') != CURRENT_SCOPE:
            failures.append({'path':rel,'code':'FAIL_DUPLICATE_ALLOWLIST_SCOPE_NOT_CURRENT'})
        if int(d.get('duplicate_group_count',-1)) != len(real) or int(d.get('duplicate_file_count',-1)) != sum(len(v) for v in real.values()):
            failures.append({'path':rel,'code':'FAIL_DUPLICATE_ALLOWLIST_COUNT_STALE'})
        if _ledger_declared_groups(d) != real:
            failures.append({'path':rel,'code':'FAIL_DUPLICATE_ALLOWLIST_HASH_OR_PATH_STALE'})
    rel='07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.json'
    p=root/rel
    if p.is_file():
        try: d=json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            failures.append({'path':rel,'code':'FAIL_RETENTION_ALLOWLIST_JSON_INVALID'}); return not failures, failures
        if str(d.get('scope','')).startswith('ACTIVE_') or d.get('surface_role') != 'COMPATIBILITY_ALIAS_NON_AUTHORITY' or d.get('active_authority') is not False:
            failures.append({'path':rel,'code':'FAIL_RETENTION_ALLOWLIST_STILL_ACTIVE_AUTHORITY'})
        if d.get('correction_scope') != CURRENT_SCOPE:
            failures.append({'path':rel,'code':'FAIL_RETENTION_ALLOWLIST_SCOPE_NOT_CURRENT'})
        if d.get('result') == 'PASS' and _ledger_declared_groups(d) != real:
            failures.append({'path':rel,'code':'FAIL_RETENTION_ALLOWLIST_PASS_STALE'})
        if int(d.get('duplicate_group_count',-1)) != len(real) or int(d.get('duplicate_file_count',-1)) != sum(len(v) for v in real.values()):
            failures.append({'path':rel,'code':'FAIL_RETENTION_ALLOWLIST_COUNT_STALE'})
    else:
        failures.append({'path':rel,'code':'FAIL_RETENTION_ALLOWLIST_MISSING'})
    return not failures, failures

ENGINE_CONTRACT="03_PROJECT_FACTORY/04_DELIVERY_GATES/H269_H280_PROJECT_FACTORY_TRUTHFULNESS_AND_COMPANION_CLEAN.json"

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
    _dup_ok, _dup_failures = _duplicate_ledger_sync_gate(root)
    if not _dup_ok:
        return out("FAIL", fail_codes=sorted({f.get('code','FAIL_DUPLICATE_LEDGER_SYNC') for f in _dup_failures}), failures=_dup_failures, validators_fail=len(_dup_failures))
    return out("PASS", scope=CURRENT_SCOPE, engine_contract="PASS", DUPLICATE_LEDGER_REALITY_SYNC="PASS")

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
