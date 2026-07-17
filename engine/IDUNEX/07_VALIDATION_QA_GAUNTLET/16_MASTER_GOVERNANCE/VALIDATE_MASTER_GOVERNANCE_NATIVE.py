#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import json, sys, re, hashlib, collections
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
REQUIRED_FAMILIES = ['GOV','VER','ENG','PRJ','AGT','CAN','RES','RUN','PMT','VAL','AUD','UPD','MIG','BRD','REF','SAF','ZIP','DUP','LIN','BLT','CRT']
REQUIRED_RULE_IDS = ['GOV-CORE-001','GOV-LVL-001','VER-SEM-001','VER-COR-001','ENG-CORE-001','ENG-STR-001','PRJ-CON-001','AGT-LOAD-001','CAN-P360-001','CAN-TEXT-001','RES-CORPUS-001','RUN-10N-001','PMT-AJ-001','VAL-REC-001','AUD-MAX-001','UPD-MAT-001','MIG-MAT-001','BRD-DEF-001','BRD-PAL-001','REF-SAFE-001','SAF-ADULT-001','ZIP-EXT-001','DUP-EXA-001','LIN-HDEM-001','BLT-NBH-001','CRT-FALSE-001','PRJ-NAME-001','PRJ-TPL-001','PRJ-SKEL-001','PRJ-STAT-001']
DYNAMIC_DUPLICATE_EXCLUSIONS = {
 '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json',
 '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/EXACT_DUPLICATE_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.md',
 '99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt',
 '99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt',
 '99_MANIFESTS_SHA_LINEAGE/MANIFEST.json'
}
REQUIRED_PATHS = [
 '00_INDEX/MASTER_GOVERNANCE_MAP.json','00_INDEX/MASTER_GOVERNANCE_MAP.md','01_CANON_REGISTRIES/MASTER_GOVERNANCE_RULE_REGISTRY.json','01_CANON_REGISTRIES/15_SCHEMAS/MASTER_GOVERNANCE__758ce4d2.json','00_INDEX/00_CONTROL_CENTER/ENGINE_PROJECT_AGENT_LEVEL_CONTRACTS.json','00_INDEX/00_CONTROL_CENTER/ROOT_STRUCTURE_EQUIVALENCE_MAP.json','12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json','12_OUTPUT_CONTRACTS/PROJECT_OUTPUT_CONTRACT.json','12_OUTPUT_CONTRACTS/AGENT_LOAD_CONTRACT.json','02_RESEARCH_CORPUS/RES_POLICY_REGISTRY.json','13_UPDATE_MIGRATION/UPDATE_MIGRATION_CONTRACTS.json','14_HISTORICAL_NON_AUTHORITY/H_DEMOTION_REGISTRY.json','03_PROJECT_FACTORY/04_DELIVERY_GATES/ZIP_EXT_001_WHOLE__0cccfebc.json','03_PROJECT_FACTORY/04_DELIVERY_GATES/STABLE_FAMILY_GOVERNANCE_GATE.json','07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/NO_BLOAT_NO_HISTORY_POLICY.json','03_PROJECT_FACTORY/04_DELIVERY_GATES/PROJECT_NO_PLACEHOLDER_EXECUTION_GATE.json','03_PROJECT_FACTORY/04_DELIVERY_GATES/GENERIC_SKELETON_NON_AUTHORITY_GATE.json','03_PROJECT_FACTORY/09_PROJECT_OUTPUT_CONTRACTS/PROJECT_FILENAME_CANON.json','03_PROJECT_FACTORY/09_PROJECT_OUTPUT_CONTRACTS/PROJECT_STATUS_CONTRACT.json','03_PROJECT_FACTORY/09_PROJECT_OUTPUT_CONTRACTS/PROJECT_TEMPLATE_FILL_VALIDATOR.json','07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/VALIDATE_PROMPTS_PROJECT_POLICY.py']
fail=[]; checks={}; details={}
def add(name, ok, detail=None):
    checks[name]=bool(ok)
    if detail is not None: details[name]=detail
    if not ok: fail.append(name)
def load(rel):
    return json.loads((ROOT/rel).read_text(encoding='utf-8'))

# ACTIVE-SURFACE-SCOPE-SYNC-001: integrated hard gate; no parallel validator.
def _active_surface_scope_sync_gate(root: Path):
    text_exts={'.json','.md','.txt','.csv','.sh'}
    failures=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix.lower() not in text_exts:
            continue
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/')):
            continue
        tx=p.read_text(encoding='utf-8', errors='ignore')
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

add('ROOT_NAME_IDUNEX', ROOT.name == 'IDUNEX', {'root':ROOT.name})
missing=[p for p in REQUIRED_PATHS if not (ROOT/p).is_file()]
add('REQUIRED_GOVERNANCE_PATHS_PRESENT', not missing, {'missing':missing})
try:
    reg=load('01_CANON_REGISTRIES/MASTER_GOVERNANCE_RULE_REGISTRY.json')
    fams=[x.get('family') for x in reg.get('families',[])]
    ids=[x.get('rule_id') for x in reg.get('rules',[])]
    add('STABLE_FAMILY_COVERAGE', set(REQUIRED_FAMILIES).issubset(set(fams)) and len(set(fams))>=21, {'families':fams})
    add('STABLE_RULE_ID_COVERAGE', set(REQUIRED_RULE_IDS).issubset(set(ids)), {'missing_rule_ids':sorted(set(REQUIRED_RULE_IDS)-set(ids))})
    add('NO_H_PRIMARY_AUTHORITY_IN_REGISTRY', 'H382R_EXTERNAL_WHOLE_ZIP_AUTHORITY' not in ids and all(not str(i).startswith('H') for i in ids), {'rule_count':len(ids)})
except Exception as e:
    add('STABLE_FAMILY_REGISTRY_READABLE', False, {'error':str(e)})
try:
    zipg=load('03_PROJECT_FACTORY/04_DELIVERY_GATES/ZIP_EXT_001_WHOLE__0cccfebc.json')
    add('ZIP_EXT_001_ACTIVE', zipg.get('rule_id')=='ZIP-EXT-001' and zipg.get('historical_origin')=='H382R_EXTERNAL_WHOLE_ZIP_AUTHORITY' and zipg.get('status')=='INTEGRATED_INTO_ACTIVE_STABLE_CANON', zipg)
    add('ZIP_EXT_001_NO_INTERNAL_SELF_CERT', 'self_certifies_whole_zip_sha256' in zipg.get('internal_forbidden',[]), zipg.get('internal_forbidden'))
except Exception as e:
    add('ZIP_EXT_001_READABLE', False, {'error':str(e)})
try:
    lvl=load('00_INDEX/00_CONTROL_CENTER/ENGINE_PROJECT_AGENT_LEVEL_CONTRACTS.json')
    add('ENGINE_PROJECT_AGENT_CONTRACTS_EXPLICIT', all(k in lvl for k in ['ENGINE_LEVEL','PROJECT_LEVEL','AGENT_LEVEL']) and lvl.get('GOV_LVL_001')=='ENGINE_LEVEL != PROJECT_LEVEL != AGENT_LEVEL', lvl)
    blocked=' '.join(lvl.get('blocked_defaults',[]))
    add('NO_PROJECT_DEFAULT_LEAKAGE_CONTRACTED', all(t in blocked for t in ['named validation project','real company','brand palettes']), {'blocked_defaults':lvl.get('blocked_defaults',[])})
except Exception as e:
    add('LEVEL_CONTRACTS_READABLE', False, {'error':str(e)})

# BRD-PAL-001: no active project brand palette leakage in generic runtime visual surfaces.
try:
    generic_surface_prefixes = (
        '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/',
        '06_MULTIMODAL_CONTRACTS/',
        '03_PROJECT_FACTORY/',
        '04_AGENT_FACTORY/',
    )
    allowed_non_authority_markers = ('NON_AUTHORITY', 'FIXTURE_ONLY', '14_HISTORICAL_NON_AUTHORITY/')
    blocked_hex = ['#FFBA06', '#332727', '#FF0000']
    required_tokens = [
        'PROJECT_BRAND_PRIMARY_COLOR',
        'PROJECT_BRAND_SECONDARY_COLOR',
        'PROJECT_BRAND_ACCENT_COLOR',
        'PROJECT_BRAND_TEXT_COLOR',
        'PROJECT_BRAND_BACKGROUND_COLOR',
        'PROJECT_BRAND_CONTRAST_PAIR_AA',
        'PROJECT_BRAND_REGISTRY',
    ]
    leakage = []
    combo = []
    for p in ROOT.rglob('*'):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if not rel.startswith(generic_surface_prefixes):
            continue
        if any(marker in rel for marker in allowed_non_authority_markers):
            continue
        if p.suffix.lower() not in {'.md', '.json', '.txt', '.py', '.sh', '.csv'}:
            continue
        tx = p.read_text(encoding='utf-8', errors='ignore')
        hits = [h for h in blocked_hex if h in tx]
        if hits:
            leakage.append({'path': rel, 'fingerprints': hits})
        if '#FFBA06' in tx and '#FF0000' in tx and 'PROJECT_BRAND_ENTITY' in tx:
            combo.append(rel)
    target_files = [
        '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYS_30e665af.md',
        '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYSTEM_DOCX_STYLE_GUIDE.md',
        '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYS_5c8a5d3c.md',
        '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYSTEM_WATERMARK_GUIDE.md',
    ]
    token_missing = []
    for rel in target_files:
        tx = (ROOT/rel).read_text(encoding='utf-8', errors='ignore')
        missing = [tok for tok in required_tokens if tok not in tx]
        if missing:
            token_missing.append({'path': rel, 'missing_tokens': missing})
    rule = next((r for r in load('01_CANON_REGISTRIES/MASTER_GOVERNANCE_RULE_REGISTRY.json').get('rules', []) if r.get('rule_id') == 'BRD-PAL-001'), {})
    add('BRD_PAL_001_RULE_ACTIVE', rule.get('status') == 'PASS' and rule.get('family') == 'BRD' and 'PROJECT_BRAND_REGISTRY' in rule.get('statement', ''), {'rule': rule})
    add('BRD_PAL_001_ACTIVE_RUNTIME_NO_HEX_LEAKAGE', not leakage and not combo, {'leakage': leakage[:20], 'combo': combo[:20]})
    add('BRD_PAL_001_GENERIC_VISUAL_TOKENS_PRESENT', not token_missing, {'token_missing': token_missing})
except Exception as e:
    add('BRD_PAL_001_VALIDATION_READABLE', False, {'error':str(e)})

try:
    sm=load('00_INDEX/00_CONTROL_CENTER/ROOT_STRUCTURE_EQUIVALENCE_MAP.json')
    official={x.get('official_root') for x in sm.get('official_structure',[])}
    add('ROOT_EQUIVALENCE_OFFICIAL_COMPLETE', {'00_INDEX','01_CANON_REGISTRIES','02_RESEARCH_CORPUS','03_PROJECT_FACTORY','04_AGENT_FACTORY','05_RUNTIME_CORE_LIBRARY','06_MULTIMODAL_CONTRACTS','07_VALIDATION_QA_GAUNTLET','08_EVIDENCE_LINEAGE','09_TEMPLATES_FIXTURES','10_INTERNAL_MANUALS','11_RELEASE_INTERNAL','12_OUTPUT_CONTRACTS','13_UPDATE_MIGRATION','14_HISTORICAL_NON_AUTHORITY','99_MANIFESTS_SHA_LINEAGE'}.issubset(official), {'official_count':len(official)})
except Exception as e:
    add('ROOT_EQUIVALENCE_READABLE', False, {'error':str(e)})
for rel,cid in [('12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json','ENGINE_OUTPUT_CONTRACT'),('12_OUTPUT_CONTRACTS/PROJECT_OUTPUT_CONTRACT.json','PROJECT_OUTPUT_CONTRACT'),('12_OUTPUT_CONTRACTS/AGENT_LOAD_CONTRACT.json','AGENT_LOAD_CONTRACT')]:
    try:
        obj=load(rel); add(cid+'_PRESENT', obj.get('contract_id')==cid, obj)
    except Exception as e: add(cid+'_READABLE', False, {'error':str(e)})
try:
    res=load('02_RESEARCH_CORPUS/RES_POLICY_REGISTRY.json')
    add('RES_POLICY_NORMALIZED_DISTILLED', res.get('RES_CORPUS_001') and 'research-derived canon + evidence pointers + runtime-ready distilled knowledge' in res.get('project_distillation_rule','') and len(res.get('domains',[]))>=24, {'domain_count':len(res.get('domains',[]))})
except Exception as e: add('RES_POLICY_READABLE', False, {'error':str(e)})
try:
    um=load('13_UPDATE_MIGRATION/UPDATE_MIGRATION_CONTRACTS.json')
    add('UPDATE_MIGRATION_CONTRACTS_PRESENT', 'UPD_MAT_001' in um and 'MIG_MAT_001' in um, um)
except Exception as e: add('UPDATE_MIGRATION_CONTRACTS_READABLE', False, {'error':str(e)})
try:
    hd=load('14_HISTORICAL_NON_AUTHORITY/H_DEMOTION_REGISTRY.json')
    hist=hd.get('historical_files',[])
    add('H_DEMOTION_TO_NON_AUTHORITY', hd.get('active_authority_status')=='NO_H_MILESTONE_IS_PRIMARY_AUTHORITY' and len(hist)>0 and all(x.get('authority_status')=='NON_AUTHORITY_LINEAGE_COMPACT' for x in hist), {'historical_file_count':len(hist)})
except Exception as e: add('H_DEMOTION_REGISTRY_READABLE', False, {'error':str(e)})
try:
    agent_contract=load('12_OUTPUT_CONTRACTS/AGENT_LOAD_CONTRACT.json')
    required=set(agent_contract.get('required_per_agent',[]))
    named={'MODEL_SELECTOR_RULES':'04_AGENT_FACTORY/11_AGENT_RUNTIME/MODEL_SELECTOR_RULES.json','SAFE_REWRITE_POLICY':'04_AGENT_FACTORY/11_AGENT_RUNTIME/SAFE_REWRITE_POLICY.json'}
    missing=[path for name,path in named.items() if name in required and not (ROOT/path).is_file()]
    add('AGENT_LOAD_NAMED_SURFACE_CONTRACT', not missing, {'missing':missing})
except Exception as e: add('AGENT_LOAD_NAMED_SURFACE_CONTRACT_READABLE', False, {'error':str(e)})
try:
    release_scope_ok=True; release_details=[]
    for rel in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/00_INDEX/VERSION_MANIFEST.json','00_INDEX/FINAL_AUDIT_REPORT.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/FINAL_AUDIT_REPORT.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/FINAL_MACHINE_AUDIT_SUMMARY.json','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H391_H410_DIRECT_C_0d8663fc.json','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H391_H410_EXECUTED_202784b5.json','99_MANIFESTS_SHA_LINEAGE/FINAL_RECOMPUTED_RELEASE_EVIDENCE.json','99_MANIFESTS_SHA_LINEAGE/FINAL_RELEASE_STATUS.json']:
        tx=(ROOT/rel).read_text(encoding='utf-8', errors='ignore')
        ok=('RENORMALIZACION_VERSION_OFICIAL_v1.0.0_Y_DEMO_000_2_MODELOS' in tx and 'MUTATION_SELF_TEST_H62_MATRIX_PROOF_PARITY_AND_ACTIVE_LEDGER_EXCLUSION_CLARITY' in tx and 'DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY' in tx and 'VERSION_BUMP=YES' not in tx and '"version_bump": "YES"' not in tx)
        release_scope_ok = release_scope_ok and ok
        if not ok: release_details.append(rel)
    add('RELEASE_SURFACE_SCOPE_SYNC', release_scope_ok, {'mismatch':release_details})
except Exception as e: add('RELEASE_SURFACE_SCOPE_SYNC_READABLE', False, {'error':str(e)})

# Coverage of Profile360 / TechExt registries
try:
    p360=load('01_CANON_REGISTRIES/PROFILE360_SYSTEM/01_SCHEMA/PROFILE360_CANONICAL_REGISTRY_00_60.json')
    add('PROFILE360_61_61', len(p360.get('sections',[]))==61 or p360.get('section_count')==61, {'sections':len(p360.get('sections',[]))})
except Exception as e: add('PROFILE360_READABLE', False, {'error':str(e)})
try:
    tech=load('01_CANON_REGISTRIES/PROFILE360_TECHN_c65d3be1/TECHEXT_FULL10_OFF_5d877c88.json')
    add('TECHEXT_284_284', len(tech.get('fields',[]))==284, {'fields':len(tech.get('fields',[]))})
except Exception as e: add('TECHEXT_READABLE', False, {'error':str(e)})
# Duplicate allowlist exact coverage
try:
    groups=collections.defaultdict(list)
    for p in ROOT.rglob('*'):
        if p.is_file():
            rel=p.relative_to(ROOT).as_posix()
            if rel in DYNAMIC_DUPLICATE_EXCLUSIONS or rel.startswith('14_HISTORICAL_NON_AUTHORITY/'):
                continue
            h=hashlib.sha256(p.read_bytes()).hexdigest(); groups[h].append(rel)
    actual={h:sorted(v) for h,v in groups.items() if len(v)>1}
    allow=load('07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_ALLOWLIST.json')
    allowed={g.get('sha256'):sorted(g.get('paths',[])) for g in allow.get('groups',[])}
    mismatch=[h for h,pths in actual.items() if h not in allowed or sorted(allowed[h])!=pths]
    add('DUPLICATE_ALLOWLIST_REAL_COVERAGE', not mismatch and allow.get('duplicate_group_count')==len(actual), {'duplicate_groups':len(actual),'mismatch':mismatch[:10]})
except Exception as e: add('DUPLICATE_ALLOWLIST_READABLE', False, {'error':str(e)})
# No-bloat scans: files names only, policy tokens are allowed in policy/validator documents.
forbidden_suffixes=['.zip','.log','.tmp']
forbidden_dirs=['__pycache__','.git','.pytest_cache']
bad_files=[]
for p in ROOT.rglob('*'):
    rel=p.relative_to(ROOT).as_posix()
    if p.is_file() and any(rel.lower().endswith(s) for s in forbidden_suffixes): bad_files.append(rel)
    if p.is_dir() and p.name in forbidden_dirs: bad_files.append(rel)
add('NO_ACTIVE_BLOAT', not bad_files, {'bad_files':bad_files[:20]})
# Output contract/matrix evidence compact gates
try:
    matrix=load('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json')
    add('N1_TO_N10_X3_MATRIX_PASS_OR_31_PASS', matrix.get('result')=='PASS' and matrix.get('pass_count')==31 and matrix.get('fail_count')==0, {'pass_count':matrix.get('pass_count'),'fail_count':matrix.get('fail_count')})
except Exception as e: add('N1_TO_N10_MATRIX_READABLE', False, {'error':str(e)})
try:
    mut=load('99_MANIFESTS_SHA_LINEAGE/FACTORY_MUTATION_S_5015ecbe.json')
    add('MUTATION_SELF_TEST_PASS', mut.get('result')=='PASS' and (mut.get('cases_fail')==0 or mut.get('failed')==0), {'mutation_count':mut.get('mutation_count'),'cases_fail':mut.get('cases_fail')})
except Exception as e: add('MUTATION_SELF_TEST_READABLE', False, {'error':str(e)})

# Active release surface truthfulness parity. Existing validators must reject stale PASS if the current max matrix is not PASS.
try:
    mx=load('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json')
    matrix_pass = mx.get('result')=='PASS' and mx.get('pass_count')==31 and mx.get('fail_count')==0
    active_surface_paths=[
        '00_INDEX/ACTIVE_VERSION.txt',
        '00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md',
        '00_INDEX/00_CONTROL_CENTER/STATUS.md',
        '00_INDEX/CHANGELOG.md',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md',
        '00_INDEX/MASTER_GOVERNANCE_MAP.json',
    ]
    findings=[]
    if not matrix_pass:
        forbidden=['SCORE=10/10','VALIDATORS_FAIL=0','FAIL_CODES=[]','PRODUCT_READY','MAX_MATRIX_CURRENT_RUN=PASS','"SCORE": "10/10"','"VALIDATORS_FAIL": 0','"FAIL_CODES": []']
        required=['FAIL_MAX_MATRIX_NOT_EXECUTED_CURRENT_RUN','SCORE']
        for rel in active_surface_paths:
            tx=(ROOT/rel).read_text(encoding='utf-8', errors='ignore')
            hits=[t for t in forbidden if t in tx]
            miss=[] if 'FAIL_MAX_MATRIX_NOT_EXECUTED_CURRENT_RUN' in tx and ('BLOCKED' in tx or 'READY_FOR_REAUDIT' in tx) else ['BLOCKED_MATRIX_FAIL_STATE']
            if hits or miss:
                findings.append({'path':rel,'forbidden':hits,'missing':miss})
    add('ACTIVE_SURFACE_TRUTHFULNESS_PARITY', not findings, {'findings':findings})
except Exception as e:
    add('ACTIVE_SURFACE_TRUTHFULNESS_PARITY_READABLE', False, {'error':str(e)})


# Active surface scope sync and validator parity gate.
try:
    _as_ok, _as_failures = _active_surface_scope_sync_gate(ROOT)
    add('DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY', _as_ok, {'failures': _as_failures})
except Exception as e:
    add('DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY_READABLE', False, {'error': str(e)})

try:
    policy_corpus='\n'.join(p.read_text(encoding='utf-8', errors='ignore') for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in {'.md','.json','.txt','.py','.csv','.sh'})
    required_policy_tokens=['external_validation_required','EDITABLE_FIELDS_FOR_CUSTOM_PROJECTS','TEMPLATE_REQUIRED_FIELDS','DO_NOT_EXECUTE_TEMPLATE_WITH_PLACEHOLDERS','GENERIC_SKELETON_NON_AUTHORITY','PROJECT_FILENAME_CANON','PROJECT_NAME_SLUG','PROJECT_UID','PROJECT_STATUS_CONTRACT','PROJECT_EXTERNAL_VALIDATION_REQUIRED','PROJECT_TEMPLATE_FILL_VALIDATOR','PROJECT_NO_PLACEHOLDER_EXECUTION_GATE']
    missing_policy_tokens=[t for t in required_policy_tokens if t not in policy_corpus]
    add('PROMPTS_PROJECT_POLICY_NATIVE_TOKENS_PRESENT', not missing_policy_tokens, {'missing_policy_tokens':missing_policy_tokens})
except Exception as e:
    add('PROMPTS_PROJECT_POLICY_NATIVE_TOKENS_READABLE', False, {'error':str(e)})
result='PASS' if not fail else 'FAIL'
out={'validator':'VALIDATE_MASTER_GOVERNANCE_NATIVE','semantic_version':'v1.0.0','result':result,'MASTER_GOVERNANCE_NATIVE':'PASS' if result=='PASS' else 'FAIL','STABLE_FAMILY_COVERAGE':'PASS' if checks.get('STABLE_FAMILY_COVERAGE') and checks.get('STABLE_RULE_ID_COVERAGE') else 'FAIL','ZIP_EXT_001':'PASS' if checks.get('ZIP_EXT_001_ACTIVE') and checks.get('ZIP_EXT_001_NO_INTERNAL_SELF_CERT') else 'FAIL','H_DEMOTION_TO_NON_AUTHORITY':'PASS' if checks.get('H_DEMOTION_TO_NON_AUTHORITY') else 'FAIL','VALIDATORS_FAIL':0 if result=='PASS' else len(fail),'BLOCKING_WARNINGS':0,'FAIL_CODES':[] if result=='PASS' else ['FAIL_'+x for x in fail],'SCORE':'10/10' if result=='PASS' else 'BLOCKED','CREATIVE_OUTPUT_CERTIFIED':False,'checks':checks,'details':details}
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
sys.exit(0 if result=='PASS' else 1)
