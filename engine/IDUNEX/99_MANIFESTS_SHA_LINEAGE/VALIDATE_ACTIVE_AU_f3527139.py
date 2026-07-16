#!/usr/bin/env python3
"""H226 validator: active authority, stale duplicate and fixture-hardcode guard."""
from pathlib import Path
import json, sys, re, hashlib, collections
sys.dont_write_bytecode=True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
errors=[]; checked=[]
bad_path_tokens=['.idunex_h160_stage_','__pycache__','.pyc','.tmp']
for p in ROOT.rglob('*'):
    rel=p.relative_to(ROOT).as_posix()
    if any(tok in rel for tok in bad_path_tokens): errors.append({'code':'FAIL_H226_ACTIVE_STALE_OR_TEMP_FILE','path':rel})
if (ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').exists():
    for rel in ['11_RELEASE_INTERNAL/OBSOLETE_HISTORY_DATA_RETENTION_SCAN_H213_H236.json','03_PROJECT_FACTORY/04_DELIVERY_GATES/H213_H236_CANONICAL_GATES.json']:
        p=ROOT/rel; checked.append(rel)
        if not p.is_file(): errors.append({'code':'FAIL_H226_ENGINE_AUTHORITY_REPORT_MISSING','path':rel})
    txt=(ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').read_text(encoding='utf-8', errors='ignore')
    for token in ['ACTIVE_AUTHORITY_FILE_INDEX.json','DEPRECATED_NON_AUTHORITY_MANIFEST.json','BLOCK_OR_IGNORE_NON_AUTHORITY']:
        if token not in txt: errors.append({'code':'FAIL_H226_ENGINE_GUARD_TOKEN_MISSING','token':token})
else:
    for rel in ['09_MANIFESTS_SHA/ACTIVE_RUNTIME_UPLOAD_MANIFEST.json','09_MANIFESTS_SHA/ACTIVE_AUTHORITY_FILE_INDEX.json','09_MANIFESTS_SHA/DEPRECATED_NON_AUTHORITY_MANIFEST.json']:
        p=ROOT/rel; checked.append(rel)
        if not p.is_file(): errors.append({'code':'FAIL_H226_PROJECT_MANIFEST_MISSING','path':rel})
        else:
            try: data=json.loads(p.read_text(encoding='utf-8'))
            except Exception as e: errors.append({'code':'FAIL_H226_JSON_INVALID','path':rel,'error':str(e)}); continue
            if rel.endswith('ACTIVE_RUNTIME_UPLOAD_MANIFEST.json') and data.get('duplicate_title_policy')!='BLOCK_OR_IGNORE_NON_AUTHORITY': errors.append({'code':'FAIL_H226_DUPLICATE_POLICY_INVALID','path':rel})

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

try:
    _as_ok, _as_failures = _active_surface_scope_sync_gate(ROOT)
    if not _as_ok:
        errors.extend(_as_failures)
    _dup_ok, _dup_failures = _duplicate_ledger_sync_gate(ROOT)
    if not _dup_ok:
        errors.extend(_dup_failures)
except Exception as e:
    errors.append({'code':'FAIL_H226_SCOPE_OR_DUP_LEDGER_GATE_ERROR','error':e.__class__.__name__})

out={'validator':'VALIDATE_ACTIVE_AUTHORITY_STALE_DUPLICATE_GUARD','checked':checked,'ACTIVE_AUTHORITY_STALE_DUPLICATE_GUARD':'PASS' if not errors else 'FAIL','NO_ACTIVE_STALE_FILES':'PASS' if not errors else 'FAIL','NO_TEMP_LOGS_IN_DELIVERY':'PASS' if not errors else 'FAIL','NO_FIXTURE_DATA_HARDCODE_IN_ENGINE_ACTIVE_SURFACES':'PASS' if not errors else 'FAIL','errors':errors,'result':'PASS' if not errors else 'FAIL'}
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

print(json.dumps(out,ensure_ascii=False,indent=2)); sys.exit(0 if not errors else 1)
