#!/usr/bin/env python3
from pathlib import Path
import json, hashlib, collections, re, sys, zipfile
ROOT = Path(__file__).resolve().parents[1]

# ACTIVE_VERSION_RENORMALIZATION_GUARD_v1_0_0: integrated hard gate, no parallel validator.
def _active_version_v1_0_0_guard(root: Path):
    failures=[]
    text_exts={'.json','.md','.txt','.csv','.sh','.py'}
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix.lower() not in text_exts:
            continue
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/')):
            continue
        tx=p.read_text(encoding='utf-8', errors='ignore')
        legacy_semver='v1.' + '1.0'
        if legacy_semver in tx:
            failures.append({'path':rel,'code':'FAIL_ACTIVE_V1_1_0_LITERAL_REMAINS'})
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/')):
            continue
        legacy_semver='v1.' + '1.0'
        if legacy_semver in rel:
            failures.append({'path':rel,'code':'FAIL_ACTIVE_V1_1_0_PATH_REMAINS'})
    required=root/'12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json'
    if required.is_file():
        tx=required.read_text(encoding='utf-8', errors='ignore')
        for needle in ['IDUNEX_MOTOR_v1.0.0.zip','IDUNEX_MOTOR_v1.0.0.zip.sha256','IDUNEX_MOTOR_v1.0.0_RELEASE_CERTIFICATE.txt']:
            if needle not in tx:
                failures.append({'path':'12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json','code':'FAIL_ENGINE_OUTPUT_CONTRACT_V1_0_0_ARTIFACT_MISSING','needle':needle})
        legacy_zip='IDUNEX_MOTOR_' + ('v1.' + '1.0') + '.zip'
        if legacy_zip in tx:
            failures.append({'path':'12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json','code':'FAIL_ENGINE_OUTPUT_CONTRACT_ACTIVE_V1_1_0'})
    return failures

def sha256(p: Path) -> str:
    h=hashlib.sha256();
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()

def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()

def loadj(p: Path):
    return json.loads(p.read_text(encoding='utf-8'))

def files():
    return sorted([p for p in ROOT.rglob('*') if p.is_file()], key=rel)


# ACTIVE-SURFACE-SCOPE-SYNC-001 and DUP-LEDGER-REALITY-001: integrated hard gates; no parallel validator.

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



# LIN-MAN-001: internal manifest lineage truthfulness gate. Integrated in existing validator; no parallel validator.
MANIFEST_SELF_EXCLUDED = {
    '99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt',
    '99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt',
}
MANIFEST_SELF_EXCLUSION_REASON = 'NON_SELF_REFERENTIAL_INTERNAL_MANIFEST_POLICY'
MANIFEST_JSON_LEDGER_PATHS = [
    '99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json',
    '99_MANIFESTS_SHA_LINEAGE/MANIFEST.json',
]
MANIFEST_TEXT_LEDGER_PATHS = [
    '99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt',
    '99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt',
]

def _lin_manifest_sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def _lin_manifest_actual_records():
    records = {}
    for p in sorted([q for q in ROOT.rglob('*') if q.is_file()], key=lambda q: q.relative_to(ROOT).as_posix()):
        r = p.relative_to(ROOT).as_posix()
        if r in MANIFEST_SELF_EXCLUDED:
            continue
        records[r] = {'sha256': _lin_manifest_sha256(p), 'bytes': p.stat().st_size}
    return records

def _lin_manifest_parse_text(path: Path):
    listed = {}
    for raw in path.read_text(encoding='utf-8', errors='ignore').splitlines():
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            return None, {'malformed_line': raw[:120]}
        sha_v, rel_v = parts[0], parts[1].strip()
        listed[rel_v] = {'sha256': sha_v, 'bytes': (ROOT/rel_v).stat().st_size if (ROOT/rel_v).is_file() else None}
    return listed, None

def validate_internal_manifest_lineage_truthfulness():
    actual = _lin_manifest_actual_records()
    summary = {
        'policy': MANIFEST_SELF_EXCLUSION_REASON,
        'actual_tree_file_count': len([q for q in ROOT.rglob('*') if q.is_file()]),
        'non_excluded_file_count': len(actual),
        'self_excluded_count': len(MANIFEST_SELF_EXCLUDED),
        'self_excluded_paths': sorted(MANIFEST_SELF_EXCLUDED),
        'ledgers': {},
        'extra_count': 0,
        'missing_count': 0,
        'mismatch_count': 0,
    }
    ok = True
    for rel_path in MANIFEST_JSON_LEDGER_PATHS:
        path = ROOT / rel_path
        ledger = {'exists': path.is_file(), 'extra': [], 'missing': [], 'mismatch': [], 'excluded_listed': []}
        if not path.is_file():
            ledger['missing_ledger'] = rel_path; ok = False; summary['ledgers'][rel_path] = ledger; continue
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
            files = data.get('files', [])
            listed = {row.get('path'): {'sha256': row.get('sha256'), 'bytes': row.get('bytes')} for row in files if isinstance(row, dict) and row.get('path')}
            ledger['declared_file_count'] = data.get('file_count')
            ledger['declared_policy'] = data.get('SELF_HASH_EXCLUDED_WITH_REASON') or data.get('self_hash_excluded_with_reason')
        except Exception as exc:
            ledger['parse_error'] = exc.__class__.__name__; ok = False; summary['ledgers'][rel_path] = ledger; continue
        if ledger.get('declared_policy') != MANIFEST_SELF_EXCLUSION_REASON:
            ledger['policy_error'] = 'SELF_HASH_EXCLUDED_WITH_REASON_MISSING_OR_WRONG'; ok = False
        ledger['excluded_listed'] = sorted(set(listed) & MANIFEST_SELF_EXCLUDED)
        ledger['extra'] = sorted(set(actual) - set(listed))
        ledger['missing'] = sorted(set(listed) - set(actual) - MANIFEST_SELF_EXCLUDED)
        for r in sorted(set(actual) & set(listed)):
            if listed[r].get('sha256') != actual[r]['sha256'] or int(listed[r].get('bytes', -1)) != actual[r]['bytes']:
                ledger['mismatch'].append({'path': r, 'manifest_sha': listed[r].get('sha256'), 'actual_sha': actual[r]['sha256'], 'manifest_bytes': listed[r].get('bytes'), 'actual_bytes': actual[r]['bytes']})
        if data.get('file_count') != len(actual):
            ledger['file_count_error'] = {'declared': data.get('file_count'), 'expected': len(actual)}
        if ledger['excluded_listed'] or ledger['extra'] or ledger['missing'] or ledger['mismatch'] or ledger.get('file_count_error'):
            ok = False
        summary['ledgers'][rel_path] = ledger
    for rel_path in MANIFEST_TEXT_LEDGER_PATHS:
        path = ROOT / rel_path
        ledger = {'exists': path.is_file(), 'extra': [], 'missing': [], 'mismatch': [], 'excluded_listed': []}
        if not path.is_file():
            ledger['missing_ledger'] = rel_path; ok = False; summary['ledgers'][rel_path] = ledger; continue
        listed, err = _lin_manifest_parse_text(path)
        if err:
            ledger.update(err); ok = False; summary['ledgers'][rel_path] = ledger; continue
        ledger['declared_file_count'] = len(listed)
        ledger['excluded_listed'] = sorted(set(listed) & MANIFEST_SELF_EXCLUDED)
        ledger['extra'] = sorted(set(actual) - set(listed))
        ledger['missing'] = sorted(set(listed) - set(actual) - MANIFEST_SELF_EXCLUDED)
        for r in sorted(set(actual) & set(listed)):
            if listed[r].get('sha256') != actual[r]['sha256']:
                ledger['mismatch'].append({'path': r, 'manifest_sha': listed[r].get('sha256'), 'actual_sha': actual[r]['sha256']})
        if ledger['excluded_listed'] or ledger['extra'] or ledger['missing'] or ledger['mismatch'] or len(listed) != len(actual):
            ok = False
        summary['ledgers'][rel_path] = ledger
    for ledger in summary['ledgers'].values():
        summary['extra_count'] += len(ledger.get('extra', []))
        summary['missing_count'] += len(ledger.get('missing', []))
        summary['mismatch_count'] += len(ledger.get('mismatch', []))
    summary['INTERNAL_MANIFEST_SYNC'] = 'PASS' if ok else 'FAIL'
    summary['fail_code'] = None if ok else 'FAIL_INTERNAL_MANIFEST_STALE_OR_INCOMPLETE'
    return ok, summary

fail=[]; warn=[]; checks={}
for _vf in _active_version_v1_0_0_guard(ROOT):
    fail.append(_vf.get('code','FAIL_ACTIVE_VERSION_RENORMALIZATION_GUARD'))
allf=files()
checks['file_count']=len(allf)
if any(p.stat().st_size==0 for p in allf): fail.append('ZERO_BYTE_FILE')
lin_ok, lin_detail = validate_internal_manifest_lineage_truthfulness()
checks['INTERNAL_MANIFEST_SYNC'] = 'PASS' if lin_ok else 'FAIL'
checks['INTERNAL_MANIFEST_SYNC_DETAIL'] = lin_detail
if not lin_ok:
    fail.append('FAIL_INTERNAL_MANIFEST_STALE_OR_INCOMPLETE')

# Required active paths for H391-H410, with H341/H281 preserved as base contracts.
required=[
 '00_INDEX/ACTIVE_VERSION.txt',
 '00_INDEX/CHANGELOG.md',
 '03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py',
 '03_PROJECT_FACTORY/04_DELIVERY_GATES/H391_H410_DIRECT_CANONICAL_ENGINE_CLOSURE/H391_H410_DIRECT_CANONICAL_POLICY.json',
 '03_PROJECT_FACTORY/04_DELIVERY_GATES/H341_H360_DIRECT_CANONICAL_ENGINE_CLOSURE/H341_H360_DIRECT_CANONICAL_POLICY.json',
 '03_PROJECT_FACTORY/09_H281_H310_PROJECT_OUTPUT_CONTRACTS/PROJECT_OUTPUT_CONTRACT.json',
 '03_PROJECT_FACTORY/09_H281_H310_PROJECT_OUTPUT_CONTRACTS/FULL_MODEL_360_RUNTIME_CONTRACT.json',
 '03_PROJECT_FACTORY/09_H281_H310_PROJECT_OUTPUT_CONTRACTS/HUMAN_READABLE_CANON_CONTRACT.json',
 '03_PROJECT_FACTORY/09_H281_H310_PROJECT_OUTPUT_CONTRACTS/PROMPT_PACK_A_J_UNIVERSAL_CONTRACT.json',
 '04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/AGENT_TASK_REGISTRY.json',
 '04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/AGENT_READ_MAP.json',
 '04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/REFERENCE_IMAGE_HANDLER.json',
 '04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/SAFE_REWRITE_AND_ADULT_EDITORIAL_POLICY.json',
 '04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/MODEL_SELECTOR_RULES.json',
 '04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/SAFE_REWRITE_POLICY.json',
 '04_AGENT_FACTORY/12_H281_H310_RUNTIME_10_PLUS_N/AGENT_RUNTIME_10_PLUS_N_CONTRACT.json',
 '07_VALIDATION_QA_GAUNTLET/15_H281_H310_VALIDATION/STATIC_SMOKE_TEST_MATRIX_TEMPLATE.json',
 '07_VALIDATION_QA_GAUNTLET/15_H281_H310_VALIDATION/REAL_AGENT_LOAD_TEST_PROTOCOL.md',
 '99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json'
]
for r in required:
    if not (ROOT/r).exists(): fail.append('REQUIRED_FILE_MISSING:IDUNEX/'+r)
# Policy flags.
try:
    policy=loadj(ROOT/'03_PROJECT_FACTORY/04_DELIVERY_GATES/H391_H410_DIRECT_CANONICAL_ENGINE_CLOSURE/H391_H410_DIRECT_CANONICAL_POLICY.json')
    for key in [f'H{i}_{name}' for i,name in []]:
        pass
    for key in ['H361_FINALIZER_REAL_CONVERGENCE_LOOP','H362_FINAL_SURFACE_SENTINEL_ZERO','H363_CERTIFICATE_PROOF_SUMMARY_SYNC_REAL','H364_DUPLICATE_ALLOWLIST_AFTER_FINAL_ZIP','H365_VALIDATE_RECOMPUTED_TRUTH_HARD_FAIL','H366_ENGINE_CLOSURE_VALIDATOR_PATH_FIX','H367_N10_STRESS_COMPLETION_SLA','H368_UPDATE_CONTRACT_ALIAS_NORMALIZER_SAFE','H369_UPDATE_NO_DRIFT_LEDGER_FOR_ALL_OPERATIONS','H370_BRAND_UPDATE_NO_TIMEOUT','H371_SAME_VERSION_MIGRATION_REAL_OUTPUT','H372_INTERNAL_DUPLICATE_GOVERNANCE','H373_HISTORICAL_BLOAT_FINAL_PURGE','H374_FULL_PROFILE360_FORENSIC_PRESERVATION','H375_PROMPT_EXTERNAL_POLICY_CLARITY','H376_OUTPUT_CONTRACT_PROJECT_000_STILL_REQUIRED','H377_AGENT_RUNTIME_CONTRACT_PRESERVED','H378_UPDATE_AND_GENERATION_MATRIX_FULL','H379_SCORE_10_10_GATE','H380_FINAL_DELIVERY_ONLY_AFTER_RECOMPUTED_PASS']:
        if policy.get(key) is not True: fail.append('POLICY_FLAG_MISSING:'+key)
    if policy.get('SEMANTIC_VERSION')!='v1.0.0': fail.append('POLICY_SEMVER_NOT_EXACT')
except Exception as e:
    fail.append('H391_H410_POLICY_UNREADABLE:'+e.__class__.__name__)
# Factory active labels and no semantic suffix.
factory=ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'
try:
    ftxt=factory.read_text(encoding='utf-8')
    if 'SEMANTIC_VERSION = "v1.0.0"' not in ftxt: fail.append('SEMANTIC_VERSION_NOT_EXACT')
    if 'INTERNAL_LABEL = "H391_H410_DIRECT_CANONICAL_PROJECT_FACTORY"' not in ftxt: fail.append('FACTORY_SCOPE_NOT_H391_H410')
    if 'def update_h49_h51_after_zip' not in ftxt or 'H361-H363' not in ftxt: fail.append('H361_FINALIZER_LOOP_NOT_IN_FACTORY')
    if 'validate_reopened_zip(project_zip, companion)' not in ftxt: fail.append('H365_VALIDATE_RECOMPUTED_TRUTH_NOT_ACTIVE')
except Exception as e:
    fail.append('FACTORY_UNREADABLE:'+e.__class__.__name__)
# Scan for banned suffixes, active project fixture leakage and bytecode/temp/zip bloat.
suffix_re=re.compile(r'v1\.0\.0_(UNCHANGED|SAFE|CLEAN|FIX|PATCH)')
leak_terms=['PROJECT_REAL_'+'BRAND_PLACEHOLDER','PROJECT_VALIDATION_'+'DEMO_PLACEHOLDER','PROJECT_MODEL_'+'NAME_PLACEHOLDER']
for p in allf:
    r=rel(p); low=r.lower()
    if p.suffix.lower() in ['.pyc'] or '__pycache__' in r: fail.append('BYTECODE_ACTIVE_TREE:'+r)
    if low.endswith('.zip'): fail.append('INTERNAL_ZIP_FILE:'+r)
    if '/staging' in low or 'staging_' in low or '/temp_' in low or '/tmp_' in low: fail.append('TEMP_OR_STAGING_IN_FINAL:'+r)
    if p.suffix.lower() in ['.md','.txt','.json','.py','.csv','.yaml','.yml','.xml','.html','.ini','.cfg']:
        txt=p.read_text(encoding='utf-8', errors='ignore')
        scanner_literal_ok = (r.startswith('99_MANIFESTS_SHA_LINEAGE/VALIDATE_') and 'SCANNER_LITERAL_NON_AUTHORITY' in txt)
        if suffix_re.search(txt) and not scanner_literal_ok: fail.append('SEMANTIC_SUFFIX_ACTIVE:'+r)
        if not r.startswith('12_HISTORICAL_NON_AUTHORITY/'):
            hits=[t for t in leak_terms if t in txt]
            if hits: fail.append('ENGINE_PROJECT_DATA_LEAKAGE_ACTIVE:'+r+':'+'|'.join(hits))

# VALIDATE_RELEASE_SURFACE_SCOPE_SYNC and VALIDATE_AGENT_LOAD_NAMED_SURFACE_CONTRACT integrated into existing closure validator.
expected_scope = CURRENT_SCOPE
release_surface_paths = [
 '00_INDEX/RELEASE_CERTIFICATE.txt','00_INDEX/VERSION_MANIFEST.json','00_INDEX/FINAL_AUDIT_REPORT.md',
 '11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','11_RELEASE_INTERNAL/FINAL_AUDIT_REPORT.md','11_RELEASE_INTERNAL/FINAL_MACHINE_AUDIT_SUMMARY.json',
 '11_RELEASE_INTERNAL/H391_H410_DIRECT_CANONICAL_CLOSURE_REPORT.json','11_RELEASE_INTERNAL/H391_H410_EXECUTED_VALIDATION_COMPACT_EVIDENCE.json',
 '99_MANIFESTS_SHA_LINEAGE/FINAL_RECOMPUTED_RELEASE_EVIDENCE.json','99_MANIFESTS_SHA_LINEAGE/FINAL_RELEASE_STATUS.json'
]
for r in release_surface_paths:
    p=ROOT/r
    if not p.exists():
        fail.append('RELEASE_SURFACE_MISSING:'+r); continue
    tx=p.read_text(encoding='utf-8', errors='ignore')
    if expected_scope not in tx: fail.append('RELEASE_SURFACE_SCOPE_MISMATCH:'+r)
    if 'VERSION_BUMP=YES' in tx or '"version_bump": "YES"' in tx or '"version_bump":"YES"' in tx: fail.append('RELEASE_SURFACE_VERSION_BUMP_YES:'+r)
    if 'CREATIVE_OUTPUT_CERTIFIED=FALSE' not in tx and '"CREATIVE_OUTPUT_CERTIFIED": false' not in tx and '"creative_output_certified": false' not in tx: fail.append('RELEASE_SURFACE_CREATIVE_CERT_MISSING_FALSE:'+r)
try:
    agent_contract=loadj(ROOT/'12_OUTPUT_CONTRACTS/AGENT_LOAD_CONTRACT.json')
    required=set(agent_contract.get('required_per_agent',[]))
    named={'MODEL_SELECTOR_RULES':'04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/MODEL_SELECTOR_RULES.json','SAFE_REWRITE_POLICY':'04_AGENT_FACTORY/11_H281_H310_AGENT_RUNTIME/SAFE_REWRITE_POLICY.json'}
    for name,path in named.items():
        if name in required and not (ROOT/path).is_file(): fail.append('AGENT_LOAD_NAMED_SURFACE_MISSING:'+path)
except Exception as e:
    fail.append('AGENT_LOAD_CONTRACT_UNREADABLE:'+e.__class__.__name__)
try:
    matrix=loadj(ROOT/'11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json')
    if not (matrix.get('result')=='PASS' and matrix.get('pass_count')==31 and matrix.get('fail_count')==0):
        fail.append('FAIL_MAX_MATRIX_NOT_EXECUTED_CURRENT_RUN')
except Exception as e:
    fail.append('MAX_MATRIX_SUMMARY_UNREADABLE:'+e.__class__.__name__)

# Active surface scope sync and validator parity gate.
try:
    _as_ok, _as_failures = _active_surface_scope_sync_gate(ROOT)
    checks['RENORMALIZACION_VERSION_OFICIAL_v1.0.0_Y_DEMO_000_2_MODELOS'] = 'PASS' if _as_ok else 'FAIL'
    if not _as_ok:
        fail.extend(sorted({f.get('code','FAIL_ACTIVE_SURFACE_SCOPE_SYNC') for f in _as_failures}))
        checks['ACTIVE_SURFACE_SCOPE_SYNC_FAILURES'] = _as_failures[:50]
except Exception as e:
    fail.append('ACTIVE_SURFACE_SCOPE_SYNC_GATE_ERROR:'+e.__class__.__name__)
try:
    _dup_ok, _dup_failures = _duplicate_ledger_sync_gate(ROOT)
    checks['DUPLICATE_LEDGER_REALITY_SYNC'] = 'PASS' if _dup_ok else 'FAIL'
    if not _dup_ok:
        fail.extend(sorted({f.get('code','FAIL_DUPLICATE_LEDGER_SYNC') for f in _dup_failures}))
        checks['DUPLICATE_LEDGER_SYNC_FAILURES'] = _dup_failures[:50]
except Exception as e:
    fail.append('DUPLICATE_LEDGER_SYNC_GATE_ERROR:'+e.__class__.__name__)

# Runtime 10+N, prompt A-J and preservation checks.
try:
    rt=loadj(ROOT/'04_AGENT_FACTORY/12_H281_H310_RUNTIME_10_PLUS_N/AGENT_RUNTIME_10_PLUS_N_CONTRACT.json')
    if len(rt.get('base_files',[]))!=10 or not rt.get('human_readable_canon_first'):
        fail.append('RUNTIME_10_PLUS_N_CONTRACT_INVALID')
except Exception: fail.append('RUNTIME_10_PLUS_N_JSON_INVALID')
try:
    pp=loadj(ROOT/'03_PROJECT_FACTORY/09_H281_H310_PROJECT_OUTPUT_CONTRACTS/PROMPT_PACK_A_J_UNIVERSAL_CONTRACT.json')
    if len(pp.get('sections',[]))!=10: fail.append('PROMPT_PACK_A_J_INVALID')
except Exception: fail.append('PROMPT_PACK_JSON_INVALID')
# Profile360/TechExt no-loss coverage.
try:
    prof=loadj(ROOT/'01_CANON_REGISTRIES/PROFILE360_SYSTEM/01_SCHEMA/PROFILE360_CANONICAL_REGISTRY_00_60.json')
    checks['profile360_registry_sections']=len(prof.get('sections',[]))
    if len(prof.get('sections',[]))!=61: fail.append('PROFILE360_REGISTRY_COUNT_NOT_61')
except Exception: fail.append('PROFILE360_REGISTRY_UNREADABLE')
try:
    tech=loadj(ROOT/'01_CANON_REGISTRIES/TECHEXT_SYSTEM/TECHEXT_FULL10_OFFICIAL_FIELD_REGISTRY.json') if (ROOT/'01_CANON_REGISTRIES/TECHEXT_SYSTEM/TECHEXT_FULL10_OFFICIAL_FIELD_REGISTRY.json').exists() else None
except Exception: tech=None
# Duplicate allowlist must exactly match current engine duplicate groups.
real=_active_duplicate_groups(ROOT)
try:
    allow=loadj(ROOT/'99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json')
    declared={g.get('sha256'):sorted(g.get('paths') or [g.get('authority_path')]+g.get('mirror_paths',[])) for g in (allow.get('groups') or allow.get('duplicate_groups') or []) if isinstance(g,dict)}
    if declared != real:
        fail.append('ENGINE_DUPLICATE_ALLOWLIST_STALE_OR_INCOMPLETE')
    for g in (allow.get('groups') or allow.get('duplicate_groups') or []):
        for k in ['sha256','paths','reason_code','authority_path','mirror_paths','consumer','retention_rule','blocking_if_missing']:
            if k not in g or g.get(k) in (None,'',[]): fail.append('ENGINE_DUPLICATE_GROUP_FIELD_MISSING:'+str(g.get('sha256'))+':'+k)
    checks['duplicate_groups']=len(real)
except Exception as e:
    fail.append('ENGINE_DUPLICATE_ALLOWLIST_UNREADABLE:'+e.__class__.__name__)
# Historical bloat compact only.
hist_count=sum(1 for p in (ROOT/'12_HISTORICAL_NON_AUTHORITY').rglob('*') if p.is_file()) if (ROOT/'12_HISTORICAL_NON_AUTHORITY').exists() else 0
checks['historical_non_authority_file_count']=hist_count
if hist_count>5: fail.append('HISTORICAL_BLOAT_ACTIVE')
# Closure report truthfulness parity. If the max matrix is not PASS, the active closure report must be blocked, not PASS.
try:
    report=loadj(ROOT/'11_RELEASE_INTERNAL/H391_H410_DIRECT_CANONICAL_CLOSURE_REPORT.json')
    matrix=loadj(ROOT/'11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json')
    matrix_pass = matrix.get('result')=='PASS' and matrix.get('pass_count')==31 and matrix.get('fail_count')==0
    if matrix_pass:
        if report.get('VALIDATORS_FAIL')!=0 or report.get('BLOCKING_WARNINGS')!=0 or report.get('FAIL_CODES') not in ([], None) or report.get('SCORE') not in ('10/10', None):
            fail.append('H391_H410_CLOSURE_REPORT_FAIL')
    else:
        blocked_codes = report.get('FAIL_CODES') or report.get('fail_codes') or []
        if not (report.get('result')=='FAIL' and report.get('VALIDATORS_FAIL', report.get('validators_fail'))>=1 and 'FAIL_MAX_MATRIX_NOT_EXECUTED_CURRENT_RUN' in blocked_codes and str(report.get('SCORE','BLOCKED')).upper()!='10/10'):
            fail.append('H391_H410_BLOCKED_REPORT_TRUTHFULNESS_FAIL')
except Exception:
    warn.append('H391_H410_CLOSURE_REPORT_PENDING')
out={'VALIDATORS_FAIL':len(fail),'BLOCKING_WARNINGS':len(warn),'FAIL_CODES':fail,'WARNINGS':warn,'CHECKS':checks,'SEMANTIC_VERSION':'v1.0.0','CORRECTION_SCOPE':CURRENT_SCOPE,'CREATIVE_OUTPUT_CERTIFIED':False,'result':'PASS' if not fail else 'FAIL'}
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

print(json.dumps(out, indent=2, ensure_ascii=False))
sys.exit(1 if fail else 0)
