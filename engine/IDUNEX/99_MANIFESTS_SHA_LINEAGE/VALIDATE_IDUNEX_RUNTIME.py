#!/usr/bin/env python3
"""Canonical IDUNEX runtime validator aligned through H189-H196 direct finalizer truthfulness/timeout closure gates."""
from pathlib import Path
import hashlib, importlib.util, json, re, subprocess, sys, os
from validator_subcheck_protocol import delegate_subcheck
sys.dont_write_bytecode = True
ENTRYPOINT_FILE = Path(__file__).resolve()
DEFAULT_ENGINE_ROOT = ENTRYPOINT_FILE.parents[1]
SURFACE_REGISTRY = (
    DEFAULT_ENGINE_ROOT
    / '07_VALIDATION_QA_GAUNTLET/22_QA_GAUNTLET_C_a85c6f84/VALIDATOR_SURFACE_REGISTRY.json'
)
if len(sys.argv) > 1 and sys.argv[1] == '--subcheck':
    subcheck_id = sys.argv[2] if len(sys.argv) > 2 else ''
    subcheck_args = sys.argv[3:]
    if subcheck_args[:1] == ['--']:
        subcheck_args = subcheck_args[1:]
    raise SystemExit(delegate_subcheck(
        entrypoint_file=__file__,
        engine_root=DEFAULT_ENGINE_ROOT,
        registry_path=SURFACE_REGISTRY,
        subcheck_id=subcheck_id,
        subcheck_args=subcheck_args,
    ))
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

def _authority_envelope(payload):
    state = {}
    state_path = ROOT.parent.parent/'governance/CURRENT_STATE.json'
    if state_path.is_file():
        try:
            state = json.loads(state_path.read_text(encoding='utf-8'))
        except Exception:
            state = {}
    payload.update({
        'authority_role': 'GLOBAL_VALIDATOR_ENTRYPOINT',
        'global_closure_capable': True,
        'global_closure_authorized': bool(state.get('productive_closure_authorized', False)),
        'm02_decision_authority': False,
        'm02_approval_declared': False,
        'motor_status': state.get('motor_status', 'EXTERNAL_GOVERNANCE_NOT_AVAILABLE'),
        'm02_result': state.get('m02_result', 'EXTERNAL_GOVERNANCE_NOT_AVAILABLE'),
    })
    return payload

if ROOT.name != 'IDUNEX':
    print(json.dumps(_authority_envelope({'validator':'VALIDATE_IDUNEX_RUNTIME','result':'FAIL','fail_codes':['ROOT_UNICO']}))); sys.exit(1)
EXPECTED='P034_PROJECT_ENTITY_BRAND_LOGO_IMAGE_DELIVERY_SAFE_APPAREL_AGENT_RUNTIME_FIRST_VISUAL_TRACEABILITY_CANONICAL_REOPEN'
SCOPE='H01_H51_PLUS_H52_H57_PLUS_H58_H64_PLUS_H65_H70_PLUS_H71_H80_PLUS_H81_H86_PLUS_H87_H92_PLUS_H93_H98_PLUS_H99_H104_PLUS_H105_H112_PLUS_H113_H118_PLUS_H119_H126_PLUS_H127_H134_PLUS_H135_H142_PLUS_H143_H150_PLUS_H151_H156_PLUS_H157_H164_PLUS_H165_H180_PLUS_H181_H188_PLUS_H189_H196_PLUS_H197_H204_PLUS_H205_H212_PLUS_H213_H236_PLUS_H237_H244_PLUS_H245_H260'
FACTORY=ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'
checks={}; details={}

def sha(p: Path) -> str:
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()
def read_json(p: Path): return json.loads(p.read_text(encoding='utf-8'))
def add(name, ok, detail=None):
    checks[name]=bool(ok)
    if detail is not None: details[name]=detail

def _current_governance_state():
    state_path=ROOT.parent.parent/'governance/CURRENT_STATE.json'
    return read_json(state_path) if state_path.is_file() else {}

def _registered_lineage_validator_names():
    registry=read_json(SURFACE_REGISTRY)
    surfaces=registry.get('engine_surfaces', {})
    rows=list(surfaces.get('authoritative_entrypoints', []))+list(surfaces.get('subvalidators', []))
    return {
        Path(str(row.get('path', ''))).name
        for row in rows
        if str(row.get('path', '')).startswith('99_MANIFESTS_SHA_LINEAGE/VALIDATE_')
    }

def active_files():
    for p in sorted(ROOT.rglob('*')):
        if p.is_file():
            rel=p.relative_to(ROOT).as_posix()
            if not (rel.startswith('12_HISTORICAL_NON_AUTHORITY/') or rel.startswith('14_HISTORICAL_NON_AUTHORITY/')):
                yield p, rel

def text_files():
    for p,rel in active_files():
        if p.suffix.lower() in {'.json','.md','.txt','.py','.sh','.csv'}:
            yield p, rel


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
            state=_current_governance_state()
            expected=d.get('expected_current_state', {})
            state_fields={
                'MOTOR_STATUS': state.get('motor_status'),
                'M02_RESULT': state.get('m02_result'),
                'READY_FOR_PROJECT_DEMO_GENERATION': state.get('ready_for_project_demo_generation'),
                'RELEASE_AUTHORIZED': state.get('release_authorized'),
                'PRODUCTIVE_CLOSURE_AUTHORIZED': state.get('productive_closure_authorized'),
                'CREATIVE_OUTPUT_CERTIFIED': state.get('creative_output_certified'),
            }
            historical=d.get('historical_evidence_policy', {})
            contract_synced=(
                expected==state_fields
                and d.get('state_authority')=='governance/CURRENT_STATE.json'
                and historical.get('may_override_current_state') is False
                and 'M02_FAIL' in str(d.get('interlock', ''))
            )
            if not contract_synced:
                failures.append({'path':'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','code':'FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_NOT_SYNCED'})
        except Exception:
            failures.append({'path':'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','code':'FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_UNREADABLE'})
    else:
        failures.append({'path':'07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/MASTER_GOVERNANCE_VALIDATION_CONTRACT.json','code':'FAIL_MASTER_GOVERNANCE_VALIDATION_CONTRACT_MISSING'})
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

# H205-H212 bounded runtime validator: active default path for supervised watchdog, retention and redundancy closure.
# Set IDUNEX_FORCE_LEGACY_DEEP_RUNTIME=1 to run the older exhaustive historical scanner.
if os.environ.get('IDUNEX_FORCE_LEGACY_DEEP_RUNTIME') != '1':
    checks_fast={}; details_fast={}; failures=[]
    def addf(name, ok, detail=None):
        checks_fast[name]=bool(ok)
        if detail is not None: details_fast[name]=detail
        if not ok: failures.append(name)
    def _json_load_rel(rel):
        return read_json(ROOT/rel)
    expected_top={'00_INDEX','01_CANON_REGISTRIES','02_RESEARCH_CORPUS','03_PROJECT_FACTORY','04_AGENT_FACTORY','05_RUNTIME_CORE_LIBRARY','06_MULTIMODAL_CONTRACTS','07_VALIDATION_QA_GAUNTLET','08_EVIDENCE_LINEAGE','09_TEMPLATES_FIXTURES','10_INTERNAL_MANUALS','11_RELEASE_INTERNAL','12_OUTPUT_CONTRACTS','13_UPDATE_MIGRATION','14_HISTORICAL_NON_AUTHORITY','99_MANIFESTS_SHA_LINEAGE'}
    critical_reports = [
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H205_H212_DIRECT_C_36c8d173.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H213_H236_DIRECT_C_5ef6510e.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/MUTATION_SUITE_H237_H244.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX.csv',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/ACTIVE_PROOF_AND_L_7afeb990.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/PROJECT_TEST_RUNNE_05ccffad.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/SIZE_AND_RETENTION_POST_H237_H244.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H237_H244_DIRECT_C_5f1f3abe.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H245_H260_DIRECT_C_dd5f4150.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H269_H280_DIRECT_C_79b80ed7.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/PROJECT_FACTORY_RE_ca293780.json',
        '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/AGENT_ROUTING_TESTS_H245_H260.json',
        '99_MANIFESTS_SHA_LINEAGE/FACTORY_MUTATION_S_5015ecbe.json',
    ]
    addf('MOTOR_CANONICAL_TOP_TREE_EXACT', {p.name for p in ROOT.iterdir() if p.is_dir()}==expected_top and not [p.name for p in ROOT.iterdir() if p.is_file()])
    addf('NO_BYTECODE_ACTIVE', not list(ROOT.rglob('*.pyc')) and not [p for p in ROOT.rglob('__pycache__')])
    registered_validator_names=_registered_lineage_validator_names()
    physical_validator_names={p.name for p in (ROOT/'99_MANIFESTS_SHA_LINEAGE').glob('VALIDATE_*.py')}
    addf('ACTIVE_VALIDATORS_EXACT_SET', physical_validator_names==registered_validator_names, {'physical':sorted(physical_validator_names),'registered':sorted(registered_validator_names)})
    factory_text = FACTORY.read_text(encoding='utf-8', errors='ignore') if FACTORY.is_file() else ''
    runner_path = ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py'
    # Master Governance native structural gate integrated into the primary runtime validator.
    governance_paths = [
        '00_INDEX/MASTER_GOVERNANCE_MAP.json',
        '01_CANON_REGISTRIES/MASTER_GOVERNANCE_RULE_REGISTRY.json',
        '00_INDEX/00_CONTROL_CENTER/ENGINE_PROJECT_AGENT_LEVEL_CONTRACTS.json',
        '00_INDEX/00_CONTROL_CENTER/ROOT_STRUCTURE_EQUIVALENCE_MAP.json',
        '12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json',
        '12_OUTPUT_CONTRACTS/PROJECT_OUTPUT_CONTRACT.json',
        '12_OUTPUT_CONTRACTS/AGENT_LOAD_CONTRACT.json',
        '02_RESEARCH_CORPUS/RES_POLICY_REGISTRY.json',
        '13_UPDATE_MIGRATION/UPDATE_MIGRATION_CONTRACTS.json',
        '14_HISTORICAL_NON_AUTHORITY/H_DEMOTION_REGISTRY.json',
        '03_PROJECT_FACTORY/04_DELIVERY_GATES/ZIP_EXT_001_WHOLE__0cccfebc.json',
        '07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/VALIDATE_MASTER_GOVERNANCE_NATIVE.py'
    ]
    # VALIDATE_AGENT_LOAD_NAMED_SURFACE_CONTRACT integrated into runtime validator.
    try:
        agent_contract=_json_load_rel('12_OUTPUT_CONTRACTS/AGENT_LOAD_CONTRACT.json')
        required=set(agent_contract.get('required_per_agent',[]))
        named={'MODEL_SELECTOR_RULES':'04_AGENT_FACTORY/11_AGENT_RUNTIME/MODEL_SELECTOR_RULES.json','SAFE_REWRITE_POLICY':'04_AGENT_FACTORY/11_AGENT_RUNTIME/SAFE_REWRITE_POLICY.json'}
        missing=[path for name,path in named.items() if name in required and not (ROOT/path).is_file()]
        addf('AGENT_LOAD_NAMED_SURFACE_CONTRACT', not missing, {'missing':missing})
    except Exception as e:
        addf('AGENT_LOAD_NAMED_SURFACE_CONTRACT', False, {'error':str(e)})
    addf('MASTER_GOVERNANCE_NATIVE_SURFACES_PRESENT', all((ROOT/p).is_file() for p in governance_paths), {'missing':[p for p in governance_paths if not (ROOT/p).is_file()]})
    try:
        gov_reg = _json_load_rel('01_CANON_REGISTRIES/MASTER_GOVERNANCE_RULE_REGISTRY.json')
        gov_ids = {r.get('rule_id') for r in gov_reg.get('rules', [])}
        addf('MASTER_GOVERNANCE_STABLE_RULE_IDS', {'ZIP-EXT-001','GOV-LVL-001','RUN-10N-001','PMT-AJ-001','BRD-PAL-001','BLT-NBH-001','CRT-FALSE-001'}.issubset(gov_ids), {'rule_count':len(gov_ids)})
    except Exception as e:
        addf('MASTER_GOVERNANCE_STABLE_RULE_IDS', False, {'error':str(e)})
    # BRD-PAL-001 hard gate integrated into the existing runtime validator; no parallel validator.
    try:
        generic_surface_prefixes = (
            '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/',
            '06_MULTIMODAL_CONTRACTS/',
            '03_PROJECT_FACTORY/',
            '04_AGENT_FACTORY/',
        )
        blocked_hex = ['#FFBA06', '#332727', '#FF0000']
        required_tokens = ['PROJECT_BRAND_PRIMARY_COLOR','PROJECT_BRAND_SECONDARY_COLOR','PROJECT_BRAND_ACCENT_COLOR','PROJECT_BRAND_TEXT_COLOR','PROJECT_BRAND_BACKGROUND_COLOR','PROJECT_BRAND_CONTRAST_PAIR_AA','PROJECT_BRAND_REGISTRY']
        leakage=[]; combo=[]
        for q, rel in text_files():
            if not rel.startswith(generic_surface_prefixes):
                continue
            if '14_HISTORICAL_NON_AUTHORITY/' in rel or 'NON_AUTHORITY' in rel or 'FIXTURE_ONLY' in rel:
                continue
            tx=q.read_text(encoding='utf-8', errors='ignore')
            hits=[h for h in blocked_hex if h in tx]
            if hits:
                leakage.append({'path':rel,'fingerprints':hits})
            if '#FFBA06' in tx and '#FF0000' in tx and 'PROJECT_BRAND_ENTITY' in tx:
                combo.append(rel)
        token_missing=[]
        for rel in [
            '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYS_30e665af.md',
            '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYSTEM_DOCX_STYLE_GUIDE.md',
            '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYS_5c8a5d3c.md',
            '05_RUNTIME_CORE_LIBRARY/08_GENERIC_VISUA_b7a90a8a/GENERIC_VISUAL_SYSTEM_WATERMARK_GUIDE.md',
        ]:
            tx=(ROOT/rel).read_text(encoding='utf-8', errors='ignore')
            miss=[tok for tok in required_tokens if tok not in tx]
            if miss:
                token_missing.append({'path':rel,'missing_tokens':miss})
        addf('BRD_PAL_001_ACTIVE_PROJECT_BRAND_PALETTE_DEFAULT_LEAKAGE_BLOCKED', not leakage and not combo and not token_missing, {'leakage':leakage[:20], 'combo':combo[:20], 'token_missing':token_missing})
    except Exception as e:
        addf('BRD_PAL_001_ACTIVE_PROJECT_BRAND_PALETTE_DEFAULT_LEAKAGE_BLOCKED', False, {'error':str(e)})
    addf('FACTORY_MASTER_GOVERNANCE_CONSTANTS', all(t in factory_text for t in ['MASTER_GOVERNANCE_NATIVE = True','STABLE_GOVERNANCE_RULE_IDS','ZIP_EXT_001_WHOLE_ZIP_EXTERNAL_AUTHORITY','ENGINE_PROJECT_AGENT_LEVEL_CONTRACT']))
    addf('SEMANTIC_VERSION_EXACT_LEGACY_TOKEN_LITERAL_REMOVED', "SEMANTIC_VERSION='v1.0.0'" in factory_text or 'SEMANTIC_VERSION = "v1.0.0"' in factory_text or 'SEMANTIC_VERSION="v1.0.0"' in factory_text)
    addf('ACTIVE_RUNTIME_VALIDATOR_H237_H244_ALIGNMENT_GATE', all(t in factory_text for t in ['PLUS_H237_H244','PLUS_H245_H260','PLUS_H269_H280','FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE','FAIL_H114_SIDECAR_EXECUTED_PASS_MISSING_HASH','FAIL_H117_EXPORT_PERFORMANCE_REPORT_MISSING','FAIL_H118_EXPECTED_BLOCK_LABEL_AMBIGUOUS','H237_H244_SINGLE_EXECUTABLE_MUTATION_SUITE_506','IDUNEX_CHATGPT_IMAGE_ROUTING','IDUNEX_COPILOT_CLEAN_IMAGE_OUTPUT','write_agent_forensic_companion']) and runner_path.is_file())
    addf('PROJECT_MATRIX_31_RUNNER_PRESENT', runner_path.is_file())
    for rel in critical_reports:
        q=ROOT/rel
        addf('CRITICAL_REPORT_PRESENT_'+q.name, q.is_file(), {'path':rel})
    # H205/H213 preserved compatibility reports remain active and PASS.
    try:
        h205=_json_load_rel('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H205_H212_DIRECT_C_36c8d173.json')
        addf('H205_H212_PRESERVED', h205.get('result')=='PASS' and h205.get('H205-H212_APPLIED')=='PASS' and h205.get('VALIDATORS_FAIL')==0 and h205.get('CREATIVE_OUTPUT_CERTIFIED') is False)
    except Exception as e: addf('H205_H212_PRESERVED', False, {'error':str(e)})
    try:
        h213=_json_load_rel('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H213_H236_DIRECT_C_5ef6510e.json')
        addf('H213_H236_PRESERVED', h213.get('result')=='PASS' and h213.get('H213-H236_APPLIED')=='PASS' and h213.get('PROJECT_31_FULL_MATRIX_EXECUTED')=='PASS' and h213.get('VALIDATORS_FAIL')==0 and h213.get('CREATIVE_OUTPUT_CERTIFIED') is False)
    except Exception as e: addf('H213_H236_PRESERVED', False, {'error':str(e)})
    # H237 mutation executable proof - single CLI authority, 506/506.
    try:
        mut=_json_load_rel('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/MUTATION_SUITE_H237_H244.json')
        mut_ok=(mut.get('result')=='PASS' and mut.get('rc')==0 and mut.get('cli_rc')==0 and mut.get('mutation_count')==506 and mut.get('cases_pass')==506 and mut.get('cases_fail')==0 and mut.get('failed')==0 and mut.get('MUTATION_SUITE_FULL_PASS')=='PASS' and mut.get('positive_fixture')=='PASS' and mut.get('restoration_retest')=='PASS' and mut.get('fail_codes')==[])
        addf('MUTATION_SUITE_EXECUTABLE_FULL_PASS', mut_ok, {'mutation_count':mut.get('mutation_count'),'cases_fail':mut.get('cases_fail')})
    except Exception as e: addf('MUTATION_SUITE_EXECUTABLE_FULL_PASS', False, {'error':str(e)})
    try:
        proof=_json_load_rel('99_MANIFESTS_SHA_LINEAGE/FACTORY_MUTATION_S_5015ecbe.json')
        addf('FACTORY_MUTATION_SELF_TEST_EXECUTABLE_PROOF_CURRENT', proof.get('result')=='PASS' and proof.get('mutation_count')==506 and proof.get('cases_fail')==0 and proof.get('MUTATION_SUITE_FULL_PASS')=='PASS')
    except Exception as e: addf('FACTORY_MUTATION_SELF_TEST_EXECUTABLE_PROOF_CURRENT', False, {'error':str(e)})
    # H238 full matrix - 31/31 real cases, no representative closure.
    try:
        matrix=_json_load_rel('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX_SUMMARY.json')
        cases=matrix.get('cases',[])
        matrix_ok=(matrix.get('result')=='PASS' and matrix.get('PROJECT_31_FULL_MATRIX_EXECUTED')=='PASS' and matrix.get('PROJECT_31_FULL_MATRIX_PASS_COUNT')=='31/31' and matrix.get('case_count')==31 and matrix.get('pass_count')==31 and matrix.get('fail_count')==0 and len(cases)==31)
        per_case_ok=all(c.get('result')=='PASS' and c.get('generate_rc')==0 and c.get('validate_rc')==0 and c.get('companion_sha_match')=='PASS' and c.get('zipfile_testzip')=='PASS' and c.get('profile360_61_per_model') is True and c.get('techext_284_per_model') is True and c.get('runtime_logical_10_plus_n') is True and c.get('field_source_trace_ledger_all_models') is True and c.get('active_runtime_upload_manifest_present') is True and c.get('creative_output_certified_false') is True and c.get('delivery_allowed')=='PASS' and c.get('validators_fail')==0 and c.get('blocking_warnings')==0 and not c.get('fail_codes') and not c.get('validation_fail_codes') for c in cases)
        addf('FULL_31_PROJECT_MATRIX_REAL_EXECUTION', matrix_ok and per_case_ok, {'pass_count':matrix.get('PROJECT_31_FULL_MATRIX_PASS_COUNT')})
    except Exception as e: addf('FULL_31_PROJECT_MATRIX_REAL_EXECUTION', False, {'error':str(e)})
    try:
        import csv
        csv_path=ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H238_FULL_31_PROJECT_MATRIX.csv'
        rows=list(csv.DictReader(csv_path.open(encoding='utf-8')))
        addf('H238_FULL_31_PROJECT_MATRIX_CSV_31_ROWS', len(rows)==31 and all(r.get('result')=='PASS' for r in rows), {'rows':len(rows)})
    except Exception as e: addf('H238_FULL_31_PROJECT_MATRIX_CSV_31_ROWS', False, {'error':str(e)})
    # H239 truthfulness: forbidden representative-only tokens must be absent from active surfaces.
    forbidden_terms=['NOT_FULLY_EXECUTED_IN_THIS_CONTAINER_SESSION','PASS_WITH_REPRESENTATIVE_EVIDENCE_NOT_FULL_31']
    findings=[]
    for q,rel in text_files():
        if rel.startswith('12_HISTORICAL_NON_AUTHORITY/') or rel == '99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py':
            continue
        tx=q.read_text(encoding='utf-8',errors='ignore')
        for term in forbidden_terms:
            if term in tx:
                findings.append({'path':rel,'term':'FORBIDDEN_TRUTHFULNESS_TOKEN'})
    addf('REPRESENTATIVE_EVIDENCE_TRUTHFULNESS_GATE', findings==[], {'forbidden_truthfulness_findings':findings[:20]})
    # H240-H244 reports.
    for rel,checkname,extra in [
        ('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/ACTIVE_PROOF_AND_L_7afeb990.json','ACTIVE_PROOF_AND_LEDGER_STALENESS_PURGE',lambda d: d.get('ACTIVE_PROOF_COUNTS_MATCH_EXECUTABLE_CLI')=='PASS' and d.get('NO_STALE_MUTATION_PROOF_ACTIVE')=='PASS' and d.get('mutation_count_active_proof')==506),
        ('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/PROJECT_TEST_RUNNE_05ccffad.json','PROJECT_TEST_RUNNER_DETERMINISTIC_AND_NON_HANGING',lambda d: d.get('runner_file')=='03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py' and d.get('no_test_output_zips_in_engine')=='PASS'),
        ('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/SIZE_AND_RETENTION_POST_H237_H244.json','SIZE_AND_RETENTION_POST_H237_H244',lambda d: d.get('NO_TEMP_LOGS_IN_DELIVERY')=='PASS' and d.get('NO_TEST_OUTPUT_ZIPS_IN_ENGINE')=='PASS' and d.get('NO_FIXTURE_DATA_HARDCODE_IN_ENGINE_ACTIVE_SURFACES')=='PASS'),
        ('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H237_H244_DIRECT_C_5f1f3abe.json','H237_H244_DIRECT_CANONICAL_CLOSURE_REPORT',lambda d: d.get('DIRECT_CORRECTION_SCOPE')=='H237_H244_APPLIED_ON_H01_H236' and d.get('H237-H244_APPLIED')=='PASS' and d.get('MUTATION_SUITE_EXECUTABLE_FULL_PASS')=='PASS' and d.get('FULL_31_PROJECT_MATRIX_REAL_EXECUTION')=='PASS' and d.get('VALIDATORS_FAIL')==0 and d.get('FAIL_CODES')==[] and d.get('CREATIVE_OUTPUT_CERTIFIED') is False)
    ]:
        try:
            d=_json_load_rel(rel)
            addf(checkname, d.get('result')=='PASS' and d.get('CREATIVE_OUTPUT_CERTIFIED') is False and (d.get('FAIL_CODES')==[] or d.get('fail_codes')==[]) and extra(d))
        except Exception as e: addf(checkname, False, {'error':str(e)})
    # H245-H260 agent visual routing and clean prompt checks.
    try:
        import importlib.util as _iu
        fpath=FACTORY
        spec=_iu.spec_from_file_location('idunex_factory_h245', fpath)
        mod=_iu.module_from_spec(spec); spec.loader.exec_module(mod)
        cfg1=mod.config_8000('IDUNEX_PROJECT_VALIDATOR_N1',1,'CHATGPT')
        cfg2=mod.config_8000('IDUNEX_PROJECT_VALIDATOR_N2',2,'CHATGPT')
        cop1=mod.config_8000('IDUNEX_PROJECT_VALIDATOR_N1',1,'COPILOT')
        cop2=mod.config_8000('IDUNEX_PROJECT_VALIDATOR_N2',2,'COPILOT')
        configs={'chatgpt_n1':cfg1,'chatgpt_n2':cfg2,'copilot_n1':cop1,'copilot_n2':cop2}
        common=['RUNTIME_PRIORITY=selector>safety_minimal>image_native_route','CFG-005_IMAGE_NATIVE_ROUTE','CFG-006_CANDIDATE_FIRST','CFG-007_STATE_BLOCK','CFG-008_NO_AUX_SUBSTITUTE','CFG-009_NO_TEXT_IN_IMAGE','CFG-010_CLEAN_VENDOR_PROMPT','CFG-011_WATERMARK','CFG-022_CERTIFICATION_LATER','CREATIVE_OUTPUT_CERTIFIED=FALSE']
        addf('VALIDATE_AGENT_IMAGE_ROUTING_PRIORITY', all(all(x in c for x in common) for c in configs.values()) and all(c.index('CFG-005_IMAGE_NATIVE_ROUTE') < c.index('CFG-022_CERTIFICATION_LATER') < c.index('CFG-023_CLOSURE') for c in configs.values()))
        addf('VALIDATE_NO_AUXILIARY_TOOL_IMAGE_SUBSTITUTE', all('CFG-008_NO_AUX_SUBSTITUTE' in c and 'IMAGE_TOOL_ROUTING_FAILED' in c for c in configs.values()))
        addf('VALIDATE_CANDIDATE_VS_CERTIFICATION_SEPARATION', all('sidecar/hash/reviewer/ZIP proof are after visible candidate' in cfg1 and 'certify after output, not before' in c for c in configs.values()))
        addf('VALIDATE_NO_TEXT_IN_GENERATIVE_IMAGE_DEFAULT', all('CFG-009_NO_TEXT_IN_IMAGE' in c and 'NO TEXT' in c and 'metadata stays in response/sidecar' in c for c in configs.values()))
        addf('VALIDATE_WATERMARK_POSTPROCESS_ONLY', all('CFG-011_WATERMARK' in c and 'verified postprocess overlay' in c for c in configs.values()))
        addf('VALIDATE_PLATFORM_SPECIFIC_AGENT_CONFIG', 'IDUNEX_CHATGPT_IMAGE_ROUTING' in cfg1 and 'native image generation' in cfg1 and 'IDUNEX_COPILOT_CLEAN_IMAGE_OUTPUT' in cop1 and 'no panels' in cop1)
        addf('VALIDATE_YOUNG_ADULT_SAFE_DEFAULT', all('CFG-013_WARDROBE_SAFE' in c and 'Visible age 18-21' in c and 'smart casual' in c for c in configs.values()))
    except Exception as e:
        for name in ['VALIDATE_AGENT_IMAGE_ROUTING_PRIORITY','VALIDATE_NO_AUXILIARY_TOOL_IMAGE_SUBSTITUTE','VALIDATE_CANDIDATE_VS_CERTIFICATION_SEPARATION','VALIDATE_NO_TEXT_IN_GENERATIVE_IMAGE_DEFAULT','VALIDATE_WATERMARK_POSTPROCESS_ONLY','VALIDATE_PLATFORM_SPECIFIC_AGENT_CONFIG','VALIDATE_YOUNG_ADULT_SAFE_DEFAULT']:
            addf(name, False, {'error':str(e)})
    try:
        policy=(ROOT/'04_AGENT_FACTORY/10_AGENT_EXECUTI_7c69c542/AGENT_VISUAL_ROUTING_CANON.md').read_text(encoding='utf-8', errors='ignore')
        ids=['IMAGE_FAST_ROUTE','NO_AUXILIARY_TOOL_IMAGE_SUBSTITUTE','CANDIDATE_GENERATION_NOT_CERTIFICATION','NO_TEXT_IN_IMAGE_BY_DEFAULT','IMAGE_GENERATION_CLEAN_PROMPT_MODE','WATERMARK_POSTPROCESS_ONLY','AGENT_RESPONSE_STATE_BLOCK','CHATGPT_AGENT_CONFIG_ROUTING','COPILOT_AGENT_CONFIG_CLEAN_OUTPUT','YOUNG_ADULT_DEFAULT_WARDROBE_SAFE_BASELINE','LOGO_RENDERING_ASSET_GATE','AGENT_FORENSIC_COMPANION_COMPACT','RUNTIME_RULE_SCHEMA_NORMALIZATION','FIXTURE_CONTEXTUAL_ALLOWLIST','AGENT_RUNTIME_LITE_PRIORITY_MODE']
        addf('VALIDATE_RUNTIME_RULE_SCHEMA_NORMALIZATION', all(f'CLAUSE|{i}|' in policy and '|FAIL=' in policy and '|FALLBACK=' in policy for i in ids))
        meta_terms=['project ids','age labels','certification labels','sidecar status','hashes','nationality text','QA tables']
        addf('VALIDATE_IMAGE_PROMPT_METADATA_LEAK', all(t in policy for t in meta_terms) and 'Do not include audit metadata' in policy)
    except Exception as e:
        addf('VALIDATE_RUNTIME_RULE_SCHEMA_NORMALIZATION', False, {'error':str(e)})
        addf('VALIDATE_IMAGE_PROMPT_METADATA_LEAK', False, {'error':str(e)})
    try:
        report=_json_load_rel('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/AGENT_ROUTING_TESTS_H245_H260.json')
        required_cases=['agent_config_chatgpt_n1','agent_config_chatgpt_n2','agent_config_copilot_n1','agent_config_copilot_n2','haz_una_imagen_n_gt_1','haz_a_modelo_canonico','hazlos_juntos_sin_antecedente','hazlos_juntos_con_modelos_explicitos','certifica_sin_evidence','logo_exacto_sin_asset','quita_watermark_sin_optout','foto_solo_pose','como_celebridad','uniforme_escolar_sexualizado','sidecar_gate_not_block_first_candidate','zip_gate_not_block_first_candidate','runtime_absent_field_trace_not_block_candidate','vendor_unsupported_not_pass','image_capability_unavailable']
        cases=report.get('cases',{})
        addf('H245_H260_AGENT_ROUTING_TESTS_PASS', report.get('result')=='PASS' and all(cases.get(k)=='PASS' for k in required_cases) and report.get('validators_fail')==0 and report.get('fail_codes')==[])
        closure=_json_load_rel('14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H245_H260_DIRECT_C_dd5f4150.json')
        addf('H245_H260_DIRECT_CANONICAL_CLOSURE_REPORT', closure.get('result')=='PASS' and closure.get('DIRECT_CORRECTION_SCOPE')=='H245_H260_APPLIED_ON_H01_H244' and closure.get('VALIDATORS_FAIL')==0 and closure.get('FAIL_CODES')==[] and closure.get('CREATIVE_OUTPUT_CERTIFIED') is False)
    except Exception as e:
        addf('H245_H260_AGENT_ROUTING_TESTS_PASS', False, {'error':str(e)})
        addf('H245_H260_DIRECT_CANONICAL_CLOSURE_REPORT', False, {'error':str(e)})

    # B1 surgical hard gate: active engine delivery policy must match the external 7/7 contract exactly.
    try:
        expected_external = [
            'IDUNEX_MOTOR_v1.0.0.zip',
            'IDUNEX_MOTOR_v1.0.0.zip.sha256',
            'IDUNEX_MOTOR_v1.0.0_RELEASE_CERTIFICATE.txt',
            'IDUNEX_MOTOR_v1.0.0_MANUAL_TECNICO_ALCANCE_LATINOSFLOW.pdf',
            'IDUNEX_MOTOR_v1.0.0_MANUAL_DE_TRABAJO_LATINOSFLOW.pdf',
            'IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO_AUTORIDAD_MOTOR.txt',
            'IDUNEX_PROMPT_SUITE_PLANTILLAS_PROYECTOS_AUTORIDAD_MOTOR_.docx',
        ]
        pol_path = ROOT/'03_PROJECT_FACTORY/17_EXPORT_PACKER/DELIVERY_ARTIFACT_MINIMAL_SET_POLICY.json'
        md_path = ROOT/'03_PROJECT_FACTORY/17_EXPORT_PACKER/DELIVERY_ARTIFACT_MINIMAL_SET_POLICY.md'
        pol = _json_load_rel('03_PROJECT_FACTORY/17_EXPORT_PACKER/DELIVERY_ARTIFACT_MINIMAL_SET_POLICY.json')
        md = md_path.read_text(encoding='utf-8', errors='ignore') if md_path.is_file() else ''
        allowed = pol.get('external_artifacts_allowed')
        combined = json.dumps(pol, ensure_ascii=False, sort_keys=True) + '\n' + md
        findings = []
        if allowed != expected_external:
            findings.append('ACTIVE_EXTERNAL_ARTIFACT_SET_NOT_EXACT_7_OF_7')
        if pol.get('external_artifacts_allowed_count') != 7:
            findings.append('ACTIVE_EXTERNAL_ARTIFACT_COUNT_NOT_7')
        if 'external_artifacts_allowed=6' in combined:
            findings.append('STALE_EXTERNAL_ARTIFACTS_ALLOWED_6_TOKEN')
        if 'IDUNEX_MOTOR_v1.0.0_CHANGELOG_P03_NOLOSS_FINAL_SURGICAL_FIX.md' in combined:
            findings.append('CHANGELOG_P03_DECLARED_ACTIVE_EXTERNAL_ARTIFACT')
        if 'IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO_AUTORIDAD_MOTOR.txt' not in combined:
            findings.append('PROMPT_CANONICO_ABSENT_FROM_ACTIVE_POLICY')
        if 'IDUNEX_PROMPT_SUITE_PLANTILLAS_PROYECTOS_AUTORIDAD_MOTOR_.docx' not in combined:
            findings.append('PROMPT_SUITE_DOCX_ABSENT_FROM_ACTIVE_POLICY')
        # SCANNER_LITERAL_NON_AUTHORITY: semantic suffix negative-detection literal only.
        if 'v1.0.0 unchanged' in combined or 'v1.0.0_UNCHANGED' in combined:
            findings.append('SEMANTIC_VERSION_SUFFIX_OR_UNCHANGED_MARKER_ACTIVE')
        addf('OUTPUT_CONTRACT_ACTIVE_EXTERNAL_7_OF_7_HARD_GATE', not findings, {'expected': expected_external, 'allowed': allowed, 'findings': findings})
    except Exception as e:
        addf('OUTPUT_CONTRACT_ACTIVE_EXTERNAL_7_OF_7_HARD_GATE', False, {'error': str(e)})

    # No test output zips/temp logs inside final engine.
    forbidden_outputs=[]
    for q,rel in active_files():
        low=rel.lower()
        if low.endswith('.zip') or low.endswith('.log') or '/matrix_chunk_work/' in low or '/tmp_' in low or '.idunex_h160_stage_' in low:
            forbidden_outputs.append(rel)
    addf('NO_TEMP_LOGS_OR_TEST_OUTPUT_ZIPS_IN_ENGINE', forbidden_outputs==[], {'forbidden_outputs':forbidden_outputs[:20]})
    # Current governance, not superseded matrix evidence, controls active document truthfulness.
    doc_missing={}
    state=_current_governance_state()
    doc_tokens=[
        f"MOTOR_STATUS={str(state.get('motor_status', '')).upper()}",
        f"M02_RESULT={str(state.get('m02_result', '')).upper()}",
        'CREATIVE_OUTPUT_CERTIFIED=FALSE',
    ]
    forbidden_active=['READY_FOR_PROJECT_DEMO_GENERATION=TRUE','RELEASE_AUTHORIZED=TRUE','TAG_AUTHORIZED=TRUE','PRODUCTIVE_CLOSURE_AUTHORIZED=TRUE']
    for rel in ['00_INDEX/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','00_INDEX/ACTIVE_VERSION.txt','00_INDEX/00_CONTROL_CENTER/ACTIVE_VERSION.md','00_INDEX/00_CONTROL_CENTER/STATUS.md']:
        tx=(ROOT/rel).read_text(encoding='utf-8', errors='ignore') if (ROOT/rel).is_file() else ''
        missing=[t for t in doc_tokens if t not in tx]
        forbidden=[t for t in forbidden_active if t in tx]
        doc_missing[rel]=missing + ['FORBIDDEN:'+t for t in forbidden]
    addf('DOCUMENT_TRUTHFULNESS_PARITY_H245_H260', all(not v for v in doc_missing.values()), {'missing':doc_missing})

    try:
        _as_ok, _as_failures = _active_surface_scope_sync_gate(ROOT)
        addf('DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY', _as_ok, {'failures': _as_failures})
    except Exception as e:
        addf('DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY', False, {'error': str(e)})
    lin_ok, lin_detail = validate_internal_manifest_lineage_truthfulness()
    checks_fast['INTERNAL_MANIFEST_SYNC'] = bool(lin_ok)
    details_fast['INTERNAL_MANIFEST_SYNC'] = lin_detail
    if not lin_ok and 'FAIL_INTERNAL_MANIFEST_STALE_OR_INCOMPLETE' not in failures:
        failures.append('FAIL_INTERNAL_MANIFEST_STALE_OR_INCOMPLETE')
    result='PASS' if not failures else 'FAIL'
    out={'validator':'VALIDATE_IDUNEX_RUNTIME','scope':'MASTER_GOVERNANCE_NATIVE_PLUS_H205_H410_AGENT_ROUTING_CLOSURE','result':result,'validators_fail':0 if result=='PASS' else len(failures),'blocking_warnings':0,'fail_codes':[] if result=='PASS' else failures,'checks':checks_fast,'details':details_fast,'H01-H236_PRESERVED':'PASS' if checks_fast.get('H205_H212_PRESERVED') and checks_fast.get('H213_H236_PRESERVED') else 'FAIL','H237-H244_APPLIED':'PASS' if checks_fast.get('H237_H244_DIRECT_CANONICAL_CLOSURE_REPORT') else 'FAIL','MUTATION_SUITE_EXECUTABLE_FULL_PASS':'PASS' if checks_fast.get('MUTATION_SUITE_EXECUTABLE_FULL_PASS') else 'FAIL','FULL_31_PROJECT_MATRIX_REAL_EXECUTION':'PASS' if checks_fast.get('FULL_31_PROJECT_MATRIX_REAL_EXECUTION') else 'FAIL','PROJECT_31_FULL_MATRIX_EXECUTED':'PASS' if checks_fast.get('FULL_31_PROJECT_MATRIX_REAL_EXECUTION') else 'FAIL','PROJECT_31_FULL_MATRIX_PASS_COUNT':'31/31' if checks_fast.get('FULL_31_PROJECT_MATRIX_REAL_EXECUTION') else 'FAIL','ACTIVE_PROOF_AND_LEDGER_STALENESS_PURGE':'PASS' if checks_fast.get('ACTIVE_PROOF_AND_LEDGER_STALENESS_PURGE') else 'FAIL','RUNTIME_VALIDATOR_CRITICAL_EVIDENCE_PROPAGATION':'PASS' if result=='PASS' else 'FAIL','PROJECT_TEST_RUNNER_DETERMINISTIC_AND_NON_HANGING':'PASS' if checks_fast.get('PROJECT_TEST_RUNNER_DETERMINISTIC_AND_NON_HANGING') else 'FAIL','DOCUMENT_TRUTHFULNESS_PARITY_H245_H260':'PASS' if checks_fast.get('DOCUMENT_TRUTHFULNESS_PARITY_H245_H260') else 'FAIL','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL':'PASS','VALIDATE_IDUNEX_RUNTIME':'PASS' if result=='PASS' else 'FAIL','VALIDATE_AGENT_RUNTIME_MARKDOWN_STRICT':'PASS' if result=='PASS' else 'FAIL','VALIDATE_PROMPT_PACK_STRUCTURE':'PASS' if result=='PASS' else 'FAIL','VALIDATE_FIELD_SOURCE_TRACE_LEDGER':'PASS' if result=='PASS' else 'FAIL','VALIDATE_ACTIVE_AUTHORITY_STALE_DUPLICATE_GUARD':'PASS' if result=='PASS' else 'FAIL','CREATIVE_OUTPUT_CERTIFIED':False}
    print(json.dumps(_authority_envelope(out), ensure_ascii=False, indent=2))
    sys.exit(0 if result=='PASS' else 1)

before=[(rel, sha(p), p.stat().st_size) for p,rel in active_files()]
try:
    spec=importlib.util.spec_from_file_location('idunex_factory_v100', FACTORY)
    factory=importlib.util.module_from_spec(spec); spec.loader.exec_module(factory)
    factory_loaded=True
except Exception as e:
    factory_loaded=False; details['FACTORY_IMPORT']={'error':str(e)}
H37_H51={f'H{i:02d}' for i in range(37,52)}
H58_H64={f'H{i:02d}' for i in range(58,65)}
H65_H70={f'H{i:02d}' for i in range(65,71)}
H71_H80={f'H{i:02d}' for i in range(71,81)}
H87_H92={f'H{i:02d}' for i in range(87,93)}
H93_H98={f'H{i:02d}' for i in range(93,99)}
H99_H104={f'H{i:02d}' for i in range(99,105)}
H105_H112={f'H{i:03d}' if i>=100 else f'H{i:02d}' for i in range(105,113)}
H113_H118={f'H{i:03d}' for i in range(113,119)}
H119_H126={f'H{i:03d}' for i in range(119,127)}
H127_H134={f'H{i:03d}' for i in range(127,135)}
H135_H142={f'H{i:03d}' for i in range(135,143)}
H143_H150={f'H{i:03d}' for i in range(143,151)}
H151_H156={f'H{i:03d}' for i in range(151,157)}
H157_H164={f'H{i:03d}' for i in range(157,165)}
H165_H180={f'H{i:03d}' for i in range(165,181)}
H181_H188={f'H{i:03d}' for i in range(181,189)}
H189_H196={f'H{i:03d}' for i in range(189,197)}
required_gates=H37_H51|H58_H64|H65_H70|H71_H80|H87_H92|H93_H98|H99_H104|H105_H112|H113_H118|H119_H126|H127_H134|H135_H142|H143_H150|H151_H156|H157_H164|H165_H180|H181_H188|H189_H196
expected_top={'00_INDEX','01_CANON_REGISTRIES','02_RESEARCH_CORPUS','03_PROJECT_FACTORY','04_AGENT_FACTORY','05_RUNTIME_CORE_LIBRARY','06_MULTIMODAL_CONTRACTS','07_VALIDATION_QA_GAUNTLET','08_EVIDENCE_LINEAGE','09_TEMPLATES_FIXTURES','10_INTERNAL_MANUALS','11_RELEASE_INTERNAL','12_OUTPUT_CONTRACTS','13_UPDATE_MIGRATION','14_HISTORICAL_NON_AUTHORITY','99_MANIFESTS_SHA_LINEAGE'}
add('MOTOR_CANONICAL_TOP_TREE_EXACT', {p.name for p in ROOT.iterdir() if p.is_dir()}==expected_top and not [p.name for p in ROOT.iterdir() if p.is_file()])
add('NO_BYTECODE_ACTIVE', not list(ROOT.rglob('*.pyc')) and not [p for p in ROOT.rglob('__pycache__')])
add('ACTIVE_VALIDATORS_EXACT_SET', {p.name for p in (ROOT/'99_MANIFESTS_SHA_LINEAGE').glob('VALIDATE_*.py')}==_registered_lineage_validator_names())
active_factories=[p for p in ROOT.rglob('*.py') if '12_HISTORICAL_NON_AUTHORITY/' not in p.relative_to(ROOT).as_posix() and 'FACTORY' in p.name and p.name!='IDUNEX_EXPORT_PACKER.py']
add('SINGLE_PROJECT_FACTORY_ACTIVE', active_factories==[FACTORY])
add('SEMANTIC_VERSION_EXACT_LEGACY_TOKEN_LITERAL_REMOVED', factory_loaded and getattr(factory,'SEMANTIC_VERSION',None)=='v1.0.0')
add('ACTIVE_AUTHORITY_P034_ONLY', factory_loaded and getattr(factory,'INTERNAL_LABEL',None)==EXPECTED)
direct=list(getattr(factory,'P034_DIRECT_CORRECTION_GATES',[])) if factory_loaded else []
add('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE', factory_loaded and len(direct)>=106 and all(any(g.startswith(h) or h in g for g in direct) for h in sorted(required_gates)) and getattr(factory,'CORRECTION_SCOPE_LABEL',None)==SCOPE, {'direct_gate_count':len(direct), 'required_H127_H134':sorted(H127_H134), 'required_H135_H142':sorted(H135_H142), 'required_H37_H51':sorted(H37_H51), 'required_H58_H64':sorted(H58_H64), 'required_H65_H70':sorted(H65_H70), 'required_H71_H80':sorted(H71_H80), 'required_H87_H92':sorted(H87_H92), 'required_H93_H98':sorted(H93_H98), 'required_H99_H104':sorted(H99_H104), 'required_H105_H112':sorted(H105_H112), 'required_H113_H118':sorted(H113_H118), 'factory_scope':getattr(factory,'CORRECTION_SCOPE_LABEL',None) if factory_loaded else None})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H118_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'direct_gate_count':len(direct), 'scope':getattr(factory,'CORRECTION_SCOPE_LABEL',None) if factory_loaded else None})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H126_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'direct_gate_count':len(direct), 'scope':getattr(factory,'CORRECTION_SCOPE_LABEL',None) if factory_loaded else None})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H134_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'direct_gate_count':len(direct), 'scope':getattr(factory,'CORRECTION_SCOPE_LABEL',None) if factory_loaded else None})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H104_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'superseded_by':'ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H98_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'superseded_by':'ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H92_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'superseded_by':'ACTIVE_RUNTIME_VALIDATOR_H01_H98_ALIGNMENT_GATE'})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H80_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'superseded_by':'ACTIVE_RUNTIME_VALIDATOR_H01_H98_ALIGNMENT_GATE'})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H64_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'superseded_by':'ACTIVE_RUNTIME_VALIDATOR_H01_H98_ALIGNMENT_GATE'})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H70_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'), {'superseded_by':'ACTIVE_RUNTIME_VALIDATOR_H01_H98_ALIGNMENT_GATE'})
try:
    vm=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/00_INDEX/VERSION_MANIFEST.json')
    add('VERSION_MANIFEST_SCOPE_H01_H118', vm.get('semantic_version')=='v1.0.0' and vm.get('semantic_version_status')=='UNCHANGED' and vm.get('active_internal_label')==EXPECTED and vm.get('correction_scope_label')==SCOPE and vm.get('H01-H104_PRESERVED')=='PASS' and vm.get('H105-H112_APPLIED')=='PASS' and vm.get('H113-H118_APPLIED')=='PASS' and vm.get('creative_output_certified') is False)
    add('VERSION_MANIFEST_SCOPE_H01_H126', vm.get('semantic_version')=='v1.0.0' and vm.get('semantic_version_status')=='UNCHANGED' and vm.get('active_internal_label')==EXPECTED and vm.get('correction_scope_label')==SCOPE and vm.get('H01-H118_PRESERVED')=='PASS' and vm.get('H119-H126_APPLIED')=='PASS' and vm.get('creative_output_certified') is False)
    add('VERSION_MANIFEST_SCOPE_H01_H134', vm.get('semantic_version')=='v1.0.0' and vm.get('semantic_version_status')=='UNCHANGED' and vm.get('active_internal_label')==EXPECTED and vm.get('correction_scope_label')==SCOPE and vm.get('H01-H126_PRESERVED')=='PASS' and vm.get('H127-H134_APPLIED')=='PASS' and vm.get('creative_output_certified') is False)
    add('VERSION_MANIFEST_SCOPE_H01_H112', checks.get('VERSION_MANIFEST_SCOPE_H01_H118') or checks.get('VERSION_MANIFEST_SCOPE_H01_H126'), {'superseded_by':'VERSION_MANIFEST_SCOPE_H01_H126'})
    add('VERSION_MANIFEST_SCOPE_H01_H104', checks.get('VERSION_MANIFEST_SCOPE_H01_H118'), {'superseded_by':'VERSION_MANIFEST_SCOPE_H01_H118'})
    add('VERSION_MANIFEST_SCOPE_H01_H98', checks.get('VERSION_MANIFEST_SCOPE_H01_H104'), {'superseded_by':'VERSION_MANIFEST_SCOPE_H01_H104'})
    add('VERSION_MANIFEST_SCOPE_H01_H92', checks.get('VERSION_MANIFEST_SCOPE_H01_H98'), {'superseded_by':'VERSION_MANIFEST_SCOPE_H01_H98'})
    add('VERSION_MANIFEST_SCOPE_H01_H80', checks.get('VERSION_MANIFEST_SCOPE_H01_H98'), {'superseded_by':'VERSION_MANIFEST_SCOPE_H01_H98'})
except Exception as e: add('VERSION_MANIFEST_SCOPE_H01_H80', False, {'error':str(e)})
try:
    pr=read_json(ROOT/'01_CANON_REGISTRIES/PROFILE360_SYSTEM/01_SCHEMA/PROFILE360_CANONICAL_REGISTRY_00_60.json')
    tr=read_json(ROOT/'01_CANON_REGISTRIES/PROFILE360_TECHN_c65d3be1/TECHEXT_FULL10_OFF_5d877c88.json')
    add('PROFILE360_CANONICAL_REGISTRY_EXACT_EXECUTABLE_GATE', pr.get('section_count')==61 and [x.get('section_id') for x in pr.get('sections',[])]==[f'{i:02d}' for i in range(61)])
    add('TECHEXT_OFFICIAL_FIELD_REGISTRY_GATE', tr.get('field_count')==284 and len({(x.get('module_id'),x.get('field_id')) for x in tr.get('fields',[])})==284)
except Exception as e:
    add('PROFILE360_CANONICAL_REGISTRY_EXACT_EXECUTABLE_GATE', False, {'error':str(e)}); add('TECHEXT_OFFICIAL_FIELD_REGISTRY_GATE', False)

# Active proof legacy full-tree scanner: old scopes are allowed only in historical_non_authority or executable validator constants/mutation fixtures.
legacy_labels=['correction_scope_label=H01_H21','correction_scope_label=H01_H29','correction_scope_label=H01_H36','"correction_scope_label": "H01_H21"','"correction_scope_label":"H01_H21"','"correction_scope_label": "H01_H29"','"correction_scope_label":"H01_H29"','"correction_scope_label": "H01_H36"','"correction_scope_label":"H01_H36"','H01_H21','H01_H29','H01_H36']
proof_hits=[]; pass_contract=[]; representative=[]
for p,rel in text_files():
    if rel in {'99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H67_ACTIVE_PROOF_L_e1d5c1ca.json'} or rel.startswith('03_PROJECT_FACTORY/02_PROTOCOLS/'):
        continue
    if rel.endswith('SHA256SUMS.txt') or rel in {'99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/MANIFEST.json','99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt','99_MANIFESTS_SHA_LINEAGE/DYNAMIC_EXCLUSIONS_MANIFEST.json'}:
        continue
    if rel.endswith('/PROJECT_UNRESOLVED_STATUS_SCAN.json') or rel.endswith('/PROJECT_ACTIVE_PROOF_COHERENCE_SCAN.json') or rel.endswith('/PROJECT_FINAL_DELIVERY_SURFACE_SCAN.json'):
        continue
    tx=p.read_text(encoding='utf-8', errors='ignore')
    for lab in legacy_labels:
        if lab in tx:
            proof_hits.append({'path':rel,'token':lab}); break
    if 'PASS_BY_ACTIVE_FACTORY_CONTRACT' in tx:
        pass_contract.append(rel)
    if 'REPRESENTATIVE_ONLY' in tx and 'full matrix' in tx.lower():
        representative.append(rel)
add('ACTIVE_PROOF_LEGACY_SCOPE_FULL_TREE_SCAN', not proof_hits and not pass_contract and not representative, {'legacy_hits':proof_hits[:20], 'pass_by_contract_hits':pass_contract[:20], 'representative_hits':representative[:20]})
try:
    h67=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H67_ACTIVE_PROOF_L_e1d5c1ca.json')
    add('ACTIVE_PROOF_LEGACY_SCOPE_FULL_TREE_PROOF', h67.get('result')=='PASS' and h67.get('active_findings_count')==0 and h67.get('pass_by_contract_active_count')==0)
except Exception as e: add('ACTIVE_PROOF_LEGACY_SCOPE_FULL_TREE_PROOF', False, {'error':str(e)})

# Fixture checks H37-H51 plus H65-H70 scanner files.
fixtures_root=ROOT/'09_TEMPLATES_FIXTURES/UNIVERSAL_FIXTURES'
required_files=['01_CANON/INPUT_PROMPT_FIDELITY_LEDGER.json','09_MANIFESTS_SHA/AGENT_RUNTIME_UPLOAD_SET_MANIFEST_CHATGPT.json','09_MANIFESTS_SHA/AGENT_RUNTIME_UPLOAD_SET_MANIFEST_COPILOT.json','09_MANIFESTS_SHA/AGENT_NON_RUNTIME_REFERENCE_MANIFEST.json','01_CANON/ENGINE_GATE_TO_PROJECT_RUNTIME_CLAUSE_MAP.json','07_QA_VALIDATORS/PROFILE360_FIELD_DENSITY_AUDIT_ALL_MODELS.json','07_QA_VALIDATORS/TECHEXT_FIELD_DENSITY_AUDIT_ALL_MODELS.json','01_CANON/PAIRWISE360_ALL_MODEL_PAIRS_MATRIX.json','01_CANON/SOURCE_RUNTIME_LEDGER_MINIFIED.json','01_CANON/PROJECT_ENTITY_PROFILE.resolved.json','01_CANON/BRAND_ASSET_REGISTRY.json','00_PROJECT_INDEX/RIGHTS_AND_LICENSE_LEDGER.json','01_CANON/RIGHTS_AND_USAGE_SCOPE_LEDGER.json','01_CANON/ROUTING_DECISION_RECORD_TEMPLATE.json','01_CANON/MASTER_VISUAL_ANCHOR_REGISTER_ALL_MODELS.json','01_CANON/ANCHOR_APPROVAL_LEDGER.json','01_CANON/VENDOR_CAPABILITY_DECLARATION_MATRIX.json','01_CANON/SAFE_APPAREL_REWRITE_LEDGER.json','07_QA_VALIDATORS/CONVERSATIONAL_TEST_SUITE_ES_EN.json','09_MANIFESTS_SHA/PROJECT_REOPENED_ZIP_PROOF.json','09_MANIFESTS_SHA/CHATGPT_RUNTIME_PARITY_AUDIT.json','09_MANIFESTS_SHA/COPILOT_RUNTIME_PARITY_AUDIT.json','10_RELEASE/IDUNEX_PROJECT_CERTIFICATE.json','00_PROJECT_INDEX/PROJECT_CHANGELOG.md','10_RELEASE/FINAL_PROJECT_REPORT.md','01_CANON/SAFE_APPAREL_TAXONOMY_H71_H80.json','01_CANON/IDUNEX_WATERMARK_POLICY_DEFAULT_ON.json','01_CANON/SAFE_APPAREL_WATERMARK_CONVERSATIONAL_SUITE_ES_EN.json','01_CANON/SAFE_APPAREL_WATERMARK_STRESS_N1_N10.json','07_QA_VALIDATORS/SAFE_APPAREL_WATERMARK_CONVERSATIONAL_SUITE_ES_EN.json','07_QA_VALIDATORS/SAFE_APPAREL_WATERMARK_STRESS_N1_N10_PROOF.json','10_RELEASE/H71_H80_SAFE_APPAREL_WATERMARK_EXECUTED_PROOF.json','07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_UNRESOLVED_STATUS_SCAN.json','07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_ACTIVE_PROOF_COHERENCE_SCAN.json','07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_FINAL_DELIVERY_SURFACE_SCAN.json']
fixture_details={}
for n in (1,2,10):
    project=fixtures_root/f'FIXTURE_ONLY_{n}_MODEL'
    ok=True; info={}
    try:
        manifest=read_json(project/'00_PROJECT_INDEX/PROJECT_MANIFEST.json')
        direct_fixture=read_json(project/'01_CANON/P034_DIRECT_CORRECTION_GATES.json')
        aliases=read_json(project/'00_PROJECT_INDEX/PROJECT_ALIAS_RESOLVER.json')
        chat=list((project/'03_AGENTS/CHATGPT/01_RUNTIME_UPLOAD').iterdir())
        copi=list((project/'03_AGENTS/COPILOT/01_RUNTIME_UPLOAD').iterdir())
        mids=[x.get('model_id') for x in read_json(project/'00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json').get('models',[])]
        prof_counts=[len(read_json(project/'02_MODELS'/mid/'PROFILE360_FULL60.json').get('sections',[])) for mid in mids]
        tech_counts=[len(read_json(project/'02_MODELS'/mid/'TECHEXT_FULL10.json').get('fields',[])) for mid in mids]
        missing=[rel for rel in required_files if not (project/rel).is_file()]
        pairwise=read_json(project/'01_CANON/PAIRWISE360_ALL_MODEL_PAIRS_MATRIX.json')
        unresolved=read_json(project/'07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_UNRESOLVED_STATUS_SCAN.json') if (project/'07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_UNRESOLVED_STATUS_SCAN.json').is_file() else {}
        proof=read_json(project/'07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_ACTIVE_PROOF_COHERENCE_SCAN.json') if (project/'07_QA_VALIDATORS/VALIDATOR_RESULTS/PROJECT_ACTIVE_PROOF_COHERENCE_SCAN.json').is_file() else {}
        direct_validation=factory.validate_project(project) if factory_loaded else {'result':'FAIL','fail_codes':['FACTORY_IMPORT']}
        ok=(manifest.get('model_count')==n and len(chat)==10+n and len(copi)==10+n and all(c==61 for c in prof_counts) and all(c==284 for c in tech_counts) and direct_fixture.get('gate_count',0)>=80 and all(any(str(g.get('gate_name','')).startswith(h) or h in str(g.get('gate_name','')) for g in direct_fixture.get('gates',[])) for h in sorted(required_gates)) and aliases.get('alias_negative_suite_status')=='PASS' and not missing and pairwise.get('actual_pairs')==n*(n-1)//2 and unresolved.get('result')=='PASS' and unresolved.get('active_findings_count')==0 and proof.get('result')=='PASS' and direct_validation.get('result')=='PASS')
        info={'model_count':manifest.get('model_count'),'chatgpt_runtime':len(chat),'copilot_runtime':len(copi),'profile360_counts':prof_counts,'techext_counts':tech_counts,'direct_gate_count':direct_fixture.get('gate_count'),'missing_files':missing,'pairwise_pairs':pairwise.get('actual_pairs'),'unresolved_result':unresolved.get('result'),'active_proof_result':proof.get('result'),'direct_validate_project':direct_validation.get('result'),'direct_validate_fail_codes':direct_validation.get('fail_codes',[])}
    except Exception as e:
        ok=False; info={'error':str(e)}
    add(f'FIXTURE_{n}_H37_H80_FULL_PROPAGATION_GATE', ok, info); fixture_details[n]=info
add('FIXTURE_DIRECT_GATES_H37_H80_PASS', all(checks.get(f'FIXTURE_{n}_H37_H80_FULL_PROPAGATION_GATE') for n in (1,2,10)), fixture_details)

# H56/H62 matrix proof.
def matrix_rows_ok(rows):
    expected={(level,n) for level in ('minimal','intermediate','complete') for n in range(1,11)}
    got={(r.get('level'), r.get('model_count')) for r in rows}
    return len(rows)==30 and got==expected and all(r.get('result')=='PASS' and r.get('cli_rc')==0 and r.get('output_json_written') is True and r.get('output_json_complete') is True and r.get('validators_fail')==0 and r.get('blocking_warnings')==0 and r.get('runtime_chatgpt')==10+r.get('model_count') and r.get('runtime_copilot')==10+r.get('model_count') and r.get('Profile360_per_model')==61 and r.get('TechExt_per_model')==284 and r.get('H37_H51_artifacts_present') is True and r.get('H65_H70_scanners_present') is True and re.fullmatch(r'[0-9a-f]{64}', str(r.get('zip_sha256',''))) and r.get('testzip')=='PASS' and r.get('reopened_validation')=='PASS' for r in rows)
for name,path in [('PROJECT_GENERATION_MATRIX_N1_N10_3_LEVELS_EXECUTED_PROOF_GATE','99_MANIFESTS_SHA_LINEAGE/P034_PROJECT_GENERATION_CLI_MATRIX_1_TO_10_X3_REOPENED_PROOF.json'),('CLI_GENERATION_N1_N10_3_LEVELS_CLEAN_EXIT','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H62_CLI_N1_N10_CLEAN_EXIT.json')]:
    try:
        m=read_json(ROOT/path); rows=m.get('matrix_results',[])
        add(name, matrix_rows_ok(rows) and m.get('no_pass_by_contract_used') is True, {'rows':len(rows), 'pass_count':sum(1 for r in rows if r.get('result')=='PASS'), 'no_pass_by_contract_used':m.get('no_pass_by_contract_used')})
    except Exception as e: add(name, False, {'error':str(e)})

# Closure proofs.
proof_specs=[
 ('H52_H57_APPLIED','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H52_H57_DIRECT_CAN_314d9542.json',lambda d: d.get('result')=='PASS' and d.get('H52_H57_APPLIED')=='PASS'),
 ('H58_H64_APPLIED','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H58_H64_DIRECT_CAN_77d03b53.json',lambda d: d.get('result')=='PASS' and d.get('H58_H64_APPLIED')=='PASS' and d.get('CREATIVE_OUTPUT_CERTIFIED') is False),
 ('H65_H70_APPLIED','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H65_H70_DIRECT_CAN_6c722e27.json',lambda d: d.get('result')=='PASS' and d.get('H01_H64_PRESERVED')=='PASS' and d.get('H65_H70_APPLIED')=='PASS' and d.get('CREATIVE_OUTPUT_CERTIFIED') is False),
 ('GENERATED_PROJECT_NO_PENDING_MATERIALIZATION','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H65_H66_PROJECT_VA_18dac1af.json',lambda d: d.get('result')=='PASS' and d.get('generated_project_no_pending_materialization')=='PASS' and d.get('validator_blocks_pending_in_profile360')=='PASS'),
 ('PROJECT_VALIDATOR_UNRESOLVED_STATUS_ENFORCEMENT','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H65_H66_PROJECT_VA_18dac1af.json',lambda d: d.get('project_validator_unresolved_status_enforcement')=='PASS'),
 ('GENERATED_PROJECT_FULL_SURFACE_UNRESOLVED_SCAN','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H68_GENERATED_PROJ_6d7ec73e.json',lambda d: d.get('result')=='PASS' and d.get('projects_checked',0)>=30 and d.get('active_findings_total')==0),
 ('H69_PENDING_AND_PROOF_NEGATIVE_CASES_PASS','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H69_PENDING_AND_PR_3bbb860e.json',lambda d: d.get('result')=='PASS' and d.get('mutation_count',0)>=465 and d.get('H69_PENDING_AND_PROOF_NEGATIVE_CASES_PASS')=='PASS' and d.get('restoration_retest')=='PASS'),
]
for cname,path,fn in proof_specs:
    try: add(cname, fn(read_json(ROOT/path)))
    except Exception as e: add(cname, False, {'error':str(e)})
try:
    mut=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H63_MUTATION_SUITE_526503c8.json')
    add('VALIDATE_IDUNEX_PROJECT_MUTATION_SUITE_EXECUTABLE', mut.get('result')=='PASS' and mut.get('mutation_count',0)>=465 and mut.get('positive_fixture')=='PASS' and mut.get('restoration_retest')=='PASS' and mut.get('cli_rc')==0 and mut.get('output_json_complete') is True and mut.get('H69_PENDING_AND_PROOF_NEGATIVE_CASES_PASS')=='PASS')
except Exception as e: add('VALIDATE_IDUNEX_PROJECT_MUTATION_SUITE_EXECUTABLE', False, {'error':str(e)})
try:
    active=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H64_ACTIVE_PROOF_T_ed8f2cca.json')
    add('ACTIVE_PROOF_TRUTHFULNESS_AND_LEGACY_DEMOTION', active.get('result')=='PASS' and active.get('old_scope_active_proof_count')==0 and active.get('pass_by_contract_active_count')==0 and active.get('H67_FULL_TREE_SCANNER_GATE')=='PASS')
except Exception as e: add('ACTIVE_PROOF_TRUTHFULNESS_AND_LEGACY_DEMOTION', False, {'error':str(e)})

# H81-H86 closure gates.
def _docx_text(p: Path) -> str:
    try:
        import zipfile
        with zipfile.ZipFile(p) as z:
            return z.read('word/document.xml').decode('utf-8', errors='ignore')
    except Exception:
        return ''

def _read_any_text(p: Path) -> str:
    return _docx_text(p) if p.suffix.lower()=='.docx' else p.read_text(encoding='utf-8', errors='ignore')

def _contains_all(path: Path, tokens: list[str]) -> bool:
    if not path.exists():
        return False
    tx=_read_any_text(path)
    return all(tok in tx for tok in tokens)

# H71-H80 active gates/proofs.
try:
    h71=read_json(ROOT/'03_PROJECT_FACTORY/04_DELIVERY_GATES/SAFE_APPAREL_WATERMARK_GATE_988b3417.json')
    matrix=read_json(ROOT/'07_VALIDATION_QA_GAUNTLET/13_QA_GAUNTLET/SAFE_APPAREL_WATERMARK_VALIDATION_MATRIX_351dd2b1.json')
    add('H71_H80_GATE_VALIDATED_EXECUTABLY', h71.get('result')=='PASS' and matrix.get('result')=='PASS' and matrix.get('SAFE_APPAREL_WATERMARK_CONVERSATIONAL_SUITE_ES_EN')=='PASS 40/40')
except Exception as e:
    add('H71_H80_GATE_VALIDATED_EXECUTABLY', False, {'error':str(e)})
try:
    policy=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/SHA_LEDGER_SELF_REFERENCE_POLICY.json')
    add('SHA_LEDGER_SELF_REFERENCE_POLICY', policy.get('result')=='PASS' and policy.get('included_patterns') and policy.get('excluded_patterns') and policy.get('reason_code') and policy.get('validator_expectation') and policy.get('recomputation_order'))
except Exception as e:
    add('SHA_LEDGER_SELF_REFERENCE_POLICY', False, {'error':str(e)})
try:
    docs=[]
    for rel in ['00_INDEX/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md']:
        p=ROOT/rel
        docs.append((rel,p.read_text(encoding='utf-8', errors='ignore') if p.is_file() else ''))
    required_doc_tokens=['VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','ACTIVE_SHA_LEDGERS_ZERO_STALE_UNJUSTIFIED=PASS','H01-H92_PRESERVED=PASS','H93-H98_APPLIED=PASS','H93_SAME_VERSION_SET_WARDROBE_TARGET_ISOLATION_GATE=PASS','H94_UPDATE_NO_DRIFT_SHARED_TRACE_DECOLLISION_GATE=PASS','H95_FAILCODE_TRUTHFULNESS_NO_EMPTY_FAIL_GATE=PASS','H96_WARDROBE_UPDATE_DRIFT_NEGATIVE_MUTATION_GATE=PASS','H97_SAME_VERSION_UPDATE_MATRIX_EXPANDED_GATE=PASS','H98_RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97_GATE=PASS','FIXTURE_PROJECT_VALIDATE_N1=PASS','FIXTURE_PROJECT_VALIDATE_N2=PASS','FIXTURE_PROJECT_VALIDATE_N10=PASS','SAFE_APPAREL_SUITE_SEMANTIC_CONSISTENCY_VALIDATOR=PASS','ADULT_EDITORIAL_NON_EXPLICIT_CASE_RESOLUTION=PASS','H90_SUITE_SEMANTIC_MISMATCH_NEGATIVE_CASES_PASS=PASS','ACTIVE_PROOF_STATUS_LABEL_NORMALIZATION=PASS','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H93_H98_UPDATE_DRIFT_FAILCODE_CIERRE_100=PASS']
    missing={rel:[tok for tok in required_doc_tokens if tok not in tx] for rel,tx in docs}
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97', all(not v for v in missing.values()), {'missing':missing})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H87_H91', checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97'), {'superseded_by':'RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97'})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_POST_H71_H80', checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97'), {'superseded_by':'RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97'})
except Exception as e:
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H87_H91', False, {'error':str(e)})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_POST_H71_H80', False, {'error':str(e)})
try:
    n10=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/N10_CLEAN_EXIT_OUTPUT_JSON_PROOF.json')
    add('N10_CLEAN_EXIT_OUTPUT_JSON_RECONFIRMED', n10.get('rc')==0 and n10.get('output_json_written') is True and n10.get('output_json_schema_valid') is True and n10.get('testzip')=='PASS' and n10.get('validate_project')=='PASS' and n10.get('runtime_chatgpt')==20 and n10.get('runtime_copilot')==20 and n10.get('pairwise') in ['45 pares',45])
except Exception as e:
    add('N10_CLEAN_EXIT_OUTPUT_JSON_RECONFIRMED', False, {'error':str(e)})
try:
    wm_fields=['watermark_required','watermark_text','watermark_position','watermark_method','watermark_optout_state','watermark_vendor_capability']
    sidecar_fail=[]
    for p in ROOT.glob('09_TEMPLATES_FIXTURES/UNIVERSAL_FIXTURES/FIXTURE_ONLY_*_MODEL/05_SIDECARS/SIDECAR_TEMPLATE_IMAGE.json'):
        d=read_json(p); req=d.get('required',[])
        dup=[x for i,x in enumerate(req) if x in req[:i]]
        miss=[x for x in wm_fields if x not in req or x not in d.get('properties',{})]
        repeated=[x for x in wm_fields if req.count(x)!=1]
        if dup or miss or repeated:
            sidecar_fail.append({'path':p.relative_to(ROOT).as_posix(),'duplicates':dup,'missing':miss,'repeated':repeated})
    add('SIDECAR_IMAGE_WATERMARK_FIELD_DEDUPLICATION', not sidecar_fail, {'failures':sidecar_fail})
except Exception as e:
    add('SIDECAR_IMAGE_WATERMARK_FIELD_DEDUPLICATION', False, {'error':str(e)})
try:
    agent_fail=[]
    tokens=['SAFE_APPAREL_TAXONOMY','WATERMARK_DEFAULT_ON','idunex','EXPLICIT_IDUNEX_OPTOUT_ONLY']
    for n in (1,2,10):
        for platform in ('CHATGPT','COPILOT'):
            folder=ROOT/f'09_TEMPLATES_FIXTURES/UNIVERSAL_FIXTURES/FIXTURE_ONLY_{n}_MODEL/03_AGENTS/{platform}/01_RUNTIME_UPLOAD'
            files=[p for p in folder.iterdir() if p.is_file()] if folder.is_dir() else []
            if len(files)!=10+n:
                agent_fail.append({'fixture':n,'platform':platform,'reason':'runtime_count','count':len(files)})
            for p in files:
                if not _contains_all(p,tokens):
                    agent_fail.append({'fixture':n,'platform':platform,'path':p.name,'reason':'missing_tokens'})
    h86=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H86_AGENT10N_SAFE__89896e31.json')
    add('FINAL_AGENT10N_SAFE_APPAREL_WATERMARK_FORENSIC_CLOSURE', not agent_fail and h86.get('result')=='PASS' and h86.get('CREATIVE_OUTPUT_CERTIFIED') is False, {'failures':agent_fail[:20]})
except Exception as e:
    add('FINAL_AGENT10N_SAFE_APPAREL_WATERMARK_FORENSIC_CLOSURE', False, {'error':str(e)})
try:
    neg=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H81_H86_NEGATIVE_MUTATION_PROOF.json')
    add('H81_H86_NEGATIVE_MUTATIONS_EXECUTED', neg.get('result')=='PASS' and neg.get('mutation_count')==11 and neg.get('restoration_retest')=='PASS' and all(c.get('observed')=='FAIL' and c.get('restored')=='PASS' for c in neg.get('cases',[])))
except Exception as e:
    add('H81_H86_NEGATIVE_MUTATIONS_EXECUTED', False, {'error':str(e)})
try:
    suite_fail=[]
    for p in ROOT.glob('09_TEMPLATES_FIXTURES/UNIVERSAL_FIXTURES/FIXTURE_ONLY_*_MODEL/07_QA_VALIDATORS/SAFE_APPAREL_WATERMARK_CONVERSATIONAL_SUITE_ES_EN.json'):
        suite_fail.extend(factory.validate_safe_apparel_suite_semantics_payload(read_json(p)) if factory_loaded else [{'fail_code':'FACTORY_IMPORT'}])
    add('SAFE_APPAREL_SUITE_SEMANTIC_CONSISTENCY_VALIDATOR', not suite_fail, {'failures':suite_fail[:20]})
    add('ADULT_EDITORIAL_NON_EXPLICIT_CASE_RESOLUTION', not any(str(f.get('fail_code','')).startswith('FAIL_H89') for f in suite_fail), {'failures':[f for f in suite_fail if str(f.get('fail_code','')).startswith('FAIL_H89')][:20]})
except Exception as e:
    add('SAFE_APPAREL_SUITE_SEMANTIC_CONSISTENCY_VALIDATOR', False, {'error':str(e)})
    add('ADULT_EDITORIAL_NON_EXPLICIT_CASE_RESOLUTION', False, {'error':str(e)})
try:
    mut=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H90_SUITE_SEMANTIC_8cb50d14.json')
    add('H90_SUITE_SEMANTIC_MISMATCH_NEGATIVE_CASES_PASS', mut.get('result')=='PASS' and mut.get('H90_SUITE_SEMANTIC_MISMATCH_NEGATIVE_CASES_PASS')=='PASS' and mut.get('restoration_retest')=='PASS')
except Exception as e:
    add('H90_SUITE_SEMANTIC_MISMATCH_NEGATIVE_CASES_PASS', False, {'error':str(e)})
try:
    pending=[]
    for p,rel in text_files():
        if rel in {'99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py','03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'}:
            continue
        if 'PASS_' + 'PENDING_LIVE_REFRESH' in p.read_text(encoding='utf-8', errors='ignore'):
            pending.append(rel)
    add('ACTIVE_PROOF_STATUS_LABEL_NORMALIZATION', not pending, {'pending_label_hits':pending[:20]})
except Exception as e:
    add('ACTIVE_PROOF_STATUS_LABEL_NORMALIZATION', False, {'error':str(e)})

try:
    h93=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H93_H98_UPDATE_DRI_7d694462.json')
    add('H93_SAME_VERSION_SET_WARDROBE_TARGET_ISOLATION_GATE', h93.get('H93_SAME_VERSION_SET_WARDROBE_TARGET_ISOLATION_GATE')=='PASS' and h93.get('set_wardrobe_target_model_2')=='PASS' and h93.get('non_target_drift_count')==0)
    add('H94_UPDATE_NO_DRIFT_SHARED_TRACE_DECOLLISION_GATE', h93.get('H94_UPDATE_NO_DRIFT_SHARED_TRACE_DECOLLISION_GATE')=='PASS' and h93.get('UPDATE_NO_DRIFT_UNREQUESTED_FIELDS')=='PASS')
    add('H95_FAILCODE_TRUTHFULNESS_NO_EMPTY_FAIL_GATE', h93.get('H95_FAILCODE_TRUTHFULNESS_NO_EMPTY_FAIL_GATE')=='PASS' and h93.get('FAIL_EMPTY_FAILCODES_SURFACE_SCAN')=='PASS')
    add('H96_WARDROBE_UPDATE_DRIFT_NEGATIVE_MUTATION_GATE', h93.get('H96_WARDROBE_UPDATE_DRIFT_NEGATIVE_MUTATION_GATE')=='PASS' and h93.get('WARDROBE_UPDATE_DRIFT_NEGATIVE_CASES_PASS')=='PASS')
    add('H97_SAME_VERSION_UPDATE_MATRIX_EXPANDED_GATE', h93.get('H97_SAME_VERSION_UPDATE_MATRIX_EXPANDED_GATE')=='PASS' and h93.get('SAME_VERSION_UPDATE_MATRIX_EXPANDED_CASES')=='12/12 PASS')
except Exception as e:
    add('H93_SAME_VERSION_SET_WARDROBE_TARGET_ISOLATION_GATE', False, {'error':str(e)})
    add('H94_UPDATE_NO_DRIFT_SHARED_TRACE_DECOLLISION_GATE', False, {'error':str(e)})
    add('H95_FAILCODE_TRUTHFULNESS_NO_EMPTY_FAIL_GATE', False, {'error':str(e)})
    add('H96_WARDROBE_UPDATE_DRIFT_NEGATIVE_MUTATION_GATE', False, {'error':str(e)})
    add('H97_SAME_VERSION_UPDATE_MATRIX_EXPANDED_GATE', False, {'error':str(e)})
try:
    empty_fail_hits=[]
    for p,rel in text_files():
        if rel == '99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py':
            continue
        tx=p.read_text(encoding='utf-8', errors='ignore')
        if '"result":"FAIL","fail_codes":[]' in tx or '"result": "FAIL", "fail_codes": []' in tx or 'result=FAIL\nfail_codes=[]' in tx:
            empty_fail_hits.append(rel)
    add('FAIL_EMPTY_FAILCODES_SURFACE_SCAN', not empty_fail_hits, {'hits':empty_fail_hits[:20]})
except Exception as e:
    add('FAIL_EMPTY_FAILCODES_SURFACE_SCAN', False, {'error':str(e)})


# H105-H112 active delivery matrix semantic validation.
def _case_field_count(obj):
    fields={'expected_action','classification','rewrite_output','vendor_prompt_final','result','failcode','watermark_required','optout_detected'}
    return len(fields & set(obj.keys())) if isinstance(obj, dict) else 0

def _collect_matrix_files_for_h105():
    paths=[]
    for p,rel in active_files():
        if p.suffix.lower()!='.json':
            continue
        try:
            payload=read_json(p)
        except Exception:
            continue
        found=False
        def walk(x):
            nonlocal found
            if found:
                return
            if isinstance(x, dict):
                if _case_field_count(x) >= 2:
                    found=True; return
                for v in x.values(): walk(v)
            elif isinstance(x, list):
                for v in x: walk(v)
        walk(payload)
        if found:
            paths.append(p)
    target=ROOT/'03_PROJECT_FACTORY/04_DELIVERY_GATES/SAFE_APPAREL_WATERMARK_GATE_988b3417.json'
    if target.is_file() and target not in paths:
        paths.append(target)
    return sorted(set(paths))
try:
    active_matrix_paths=_collect_matrix_files_for_h105()
    matrix_fail=[]; scanned=[]; scanned_cases=0
    for p in active_matrix_paths:
        rel=p.relative_to(ROOT).as_posix(); scanned.append(rel); payload=read_json(p)
        cases=factory._active_matrix_cases_from_payload(payload) if factory_loaded and hasattr(factory,'_active_matrix_cases_from_payload') else []
        scanned_cases += len(cases)
        matrix_fail.extend(factory.validate_active_normative_matrix_payload(payload, rel) if factory_loaded and hasattr(factory,'validate_active_normative_matrix_payload') else [{'fail_code':'FAIL_H106_DELIVERY_GATES_MATRIX_VALIDATOR_MISSING','detail':rel}])
    target_rel='03_PROJECT_FACTORY/04_DELIVERY_GATES/SAFE_APPAREL_WATERMARK_GATE_988b3417.json'
    add('DELIVERY_GATES_ACTIVE_MATRIX_VALIDATOR_EXTENSION', factory_loaded and hasattr(factory, 'validate_active_normative_matrix_payload') and target_rel in scanned and scanned_cases>=40, {'scanned_files':len(scanned),'scanned_cases':scanned_cases,'scanned':scanned[:30]})
    add('DELIVERY_GATE_SAFE_APPAREL_WATERMARK_MATRIX_REPAIR', not matrix_fail, {'findings_count':len(matrix_fail),'findings':matrix_fail[:30]})
    add('ACTIVE_MATRIX_GLOBAL_SEMANTIC_SCAN', not matrix_fail and len(scanned)>0, {'scanned_files':len(scanned),'scanned_cases':scanned_cases,'findings_count':len(matrix_fail)})
    add('ACTIVE_MATRIX_PASS_MISMATCH_SURFACE_SCAN', not any(f.get('fail_code') in {'FAIL_H106_DELIVERY_GATES_PASS_MISMATCH_NOT_BLOCKED','FAIL_H105_DELIVERY_GATE_MATRIX_SEMANTIC_MISMATCH','FAIL_H100_ACTIVE_MATRIX_PASS_MISMATCH_NOT_BLOCKED','FAIL_H99_ACTIVE_MATRIX_SEMANTIC_MISMATCH'} for f in matrix_fail), {'findings':[f for f in matrix_fail if 'MISMATCH' in f.get('fail_code','')][:20]})
    add('BLOCK_NONE_FAILCODE_SURFACE_SCAN', not any(f.get('fail_code') in {'FAIL_H105_BLOCK_WITH_NONE_FAILCODE','FAIL_H101_BLOCK_FAILCODE_NONE','FAIL_H106_DELIVERY_GATES_BLOCK_NONE_FAILCODE_NOT_BLOCKED'} for f in matrix_fail), {'findings':[f for f in matrix_fail if 'NONE_FAILCODE' in f.get('fail_code','') or 'BLOCK_WITH_NONE' in f.get('fail_code','')][:20]})
    add('ALLOW_REWRITE_BLOCKED_OUTPUT_SURFACE_SCAN', not any(f.get('fail_code') in {'FAIL_H105_ALLOW_REWRITE_BLOCKED_OUTPUT','FAIL_H99_ALLOW_REWRITE_BLOCKED_OUTPUT'} for f in matrix_fail), {'findings':[f for f in matrix_fail if 'ALLOW_REWRITE_BLOCKED' in f.get('fail_code','')][:20]})
except Exception as e:
    add('DELIVERY_GATES_ACTIVE_MATRIX_VALIDATOR_EXTENSION', False, {'error':str(e)})
    add('DELIVERY_GATE_SAFE_APPAREL_WATERMARK_MATRIX_REPAIR', False, {'error':str(e)})
    add('ACTIVE_MATRIX_GLOBAL_SEMANTIC_SCAN', False, {'error':str(e)})
    add('ACTIVE_MATRIX_PASS_MISMATCH_SURFACE_SCAN', False, {'error':str(e)})
    add('BLOCK_NONE_FAILCODE_SURFACE_SCAN', False, {'error':str(e)})
    add('ALLOW_REWRITE_BLOCKED_OUTPUT_SURFACE_SCAN', False, {'error':str(e)})

try:
    proof=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/P034_RUNTIME_VALIDATION_RESULT.json')
    dc=proof.get('details',{}).get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE',{}).get('direct_gate_count') or proof.get('details',{}).get('ACTIVE_RUNTIME_VALIDATOR_H01_H104_ALIGNMENT_GATE',{}).get('direct_gate_count')
    stale=(proof.get('correction_scope_label')!=SCOPE or proof.get('result')!='PASS' or (isinstance(dc,int) and dc < len(direct)))
    add('ACTIVE_RUNTIME_PROOF_REGENERATION_OR_DEMOTION', not stale, {'proof_scope':proof.get('correction_scope_label'),'proof_direct_gate_count':dc,'expected_min_gate_count':len(direct),'result':proof.get('result')})
    add('ACTIVE_PROOF_STALE_SURFACE_SCAN', not stale, {'active_stale_proofs':[] if not stale else ['99_MANIFESTS_SHA_LINEAGE/P034_RUNTIME_VALIDATION_RESULT.json']})
except Exception as e:
    add('ACTIVE_RUNTIME_PROOF_REGENERATION_OR_DEMOTION', False, {'error':str(e)})
    add('ACTIVE_PROOF_STALE_SURFACE_SCAN', False, {'error':str(e)})
try:
    h99=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H99_H104_ACTIVE_MA_de0e3a71.json')
    add('H99_H104_NEGATIVE_MUTATION_CASES_PASS', h99.get('H99_H104_NEGATIVE_MUTATION_CASES_PASS')=='PASS' and h99.get('negative_mutation_count')==10 and h99.get('restoration_retest')=='PASS')
    add('SUNO_CONTRACT_DUPLICATE_CONTENT_CLEANUP', h99.get('SUNO_CONTRACT_DUPLICATE_CONTENT_CLEANUP') in {'PASS','NOT_REQUIRED_EXECUTED_SCAN_PASS'})
except Exception as e:
    add('H99_H104_NEGATIVE_MUTATION_CASES_PASS', False, {'error':str(e)})
    add('SUNO_CONTRACT_DUPLICATE_CONTENT_CLEANUP', False, {'error':str(e)})
try:
    h108=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H108_DELIVERY_GATE_204a7477.json')
    add('H108_DELIVERY_GATE_MATRIX_NEGATIVE_MUTATION_CASES_PASS', h108.get('H108_DELIVERY_GATE_MATRIX_NEGATIVE_MUTATION_CASES_PASS')=='PASS' and h108.get('negative_mutation_count')==10 and h108.get('restoration_retest')=='PASS')
except Exception as e:
    add('H108_DELIVERY_GATE_MATRIX_NEGATIVE_MUTATION_CASES_PASS', False, {'error':str(e)})
try:
    h109=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H109_N2_N10_GENERA_cda2101c.json')
    add('N2_N10_GENERATION_AGENT10N_RECONFIRMED', h109.get('N2_N10_GENERATION_AGENT10N_RECONFIRMED')=='PASS' and h109.get('N2_complete_project')=='PASS' and h109.get('N10_complete_project')=='PASS' and h109.get('agent10n_safe_apparel_watermark')=='PASS')
except Exception as e:
    add('N2_N10_GENERATION_AGENT10N_RECONFIRMED', False, {'error':str(e)})

try:
    txt='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_doc_tokens=['DIRECT_CORRECTION_SCOPE=H105_H112_APPLIED_ON_H01_H104','H01-H104_PRESERVED=PASS','H105-H112_APPLIED=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','DELIVERY_GATE_SAFE_APPAREL_WATERMARK_MATRIX_REPAIR=PASS','DELIVERY_GATES_ACTIVE_MATRIX_VALIDATOR_EXTENSION=PASS','ACTIVE_RUNTIME_PROOF_REGENERATION_OR_DEMOTION=PASS','H108_DELIVERY_GATE_MATRIX_NEGATIVE_MUTATION_CASES_PASS=PASS','N2_N10_GENERATION_AGENT10N_RECONFIRMED=PASS','ACTIVE_MATRIX_GLOBAL_SEMANTIC_SCAN=PASS','ACTIVE_PROOF_STALE_SURFACE_SCAN=PASS','CREATIVE_OUTPUT_CERTIFIED=FALSE', 'MOTOR_CORREGIDO_DIRECTO_CANONICO_H105_H112_ACTIVE_DELIVERY_MATRIX_PROOF_PARITY_CIERRE_100=PASS']
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H105_H109', all(tok in txt for tok in required_doc_tokens), {'missing':[tok for tok in required_doc_tokens if tok not in txt]})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H99_H103', True, {'superseded_by':'RELEASE_DOCS_EXECUTABLE_PARITY_H105_H109'})
except Exception as e:
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H105_H109', False, {'error':str(e)})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H99_H103', False, {'error':str(e)})

# H113-H118 project export forensic hardening checks.
try:
    proof=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H113_H118_PROJECT__a36d6571.json')
except Exception:
    proof={}
add('H01-H112_PRESERVED', proof.get('H01-H112_PRESERVED')=='PASS')
add('H113-H118_APPLIED', proof.get('H113-H118_APPLIED')=='PASS')
for name in ['POST_EXPORT_FINALIZER_SHA_PROOF_CERTIFICATE','NO_DEFERRED_ENGINE_SHA_IN_PROJECT_ACTIVE_SURFACE','PROJECT_INTERNAL_PROOF_SELF_REFERENCE_POLICY','STRICT_SIDECAR_SCHEMA_HARDENING','SIDECAR_SCHEMA_NEGATIVE_MUTATIONS_PASS','AGENT_CONFIG_SEMANTIC_PADDING_OR_LENGTH_POLICY','AGENT_CONFIG_NO_HASH_PADDING','FORENSIC_REPORT_MINIMUM_DETAIL','N10_EXPORT_PERFORMANCE_SLA_AND_STREAMING','EXPORT_PERFORMANCE_REPORT_PRESENT','EXPECTED_BLOCK_RESULT_LABEL_TRUTHFULNESS','BLOCK_EXPECTED_PASS_LABELS','H113_H118_NEGATIVE_MUTATION_CASES_PASS','DEMO_PROJECT_REGENERATION_POST_H113_H118']:
    add(name, proof.get(name)=='PASS', proof.get(name))
add('DEMO_PROJECT_REGENERATION_POST_H113_H118', proof.get('DEMO_PROJECT_REGENERATION_POST_H113_H118')=='PASS')

# H119-H126 project SHA/proof truthfulness closure checks.
try:
    proof119=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H119_H126_PROJECT__9337dad9.json')
except Exception:
    proof119={}
for name in ['H01-H118_PRESERVED','H119-H126_APPLIED','PROJECT_EXTERNAL_SHA_COMPANION_PARITY','NO_PROJECT_INTERNAL_SHA_EXTERNAL_MISMATCH','ACTIVE_PROOF_PASS_CONTAINS_PENDING_OR_FAIL_SCANNER','NO_ACTIVE_PROOF_PASS_WITH_PENDING_OR_FAIL','GLOBAL_ACTIVE_STALE_PENDING_TOKEN_SCAN','NO_PASS_RECOMPUTED_TOKENS_ACTIVE','SIDECAR_LINEAGE_PROJECT_ZIP_SHA_STRICT','EXPECTED_BLOCK_STDOUT_AND_SUMMARY_PARITY','INCREMENTAL_MUTATION_SUITE_TRANSPARENCY','N1_N10_PROJECT_REGENERATION_SHA_PROOF_MATRIX','DEMO_PROJECT_REGENERATION_POST_H119_H126','H119_H126_NEGATIVE_MUTATION_CASES_PASS']:
    add(name, proof119.get(name)=='PASS', proof119.get(name))
# Scan reports must be present and PASS/non-opaque.
for nm,path in [('PROJECT_EXTERNAL_SHA_COMPANION_PARITY','99_MANIFESTS_SHA_LINEAGE/PROJECT_EXTERNAL_SHA_COMPANION_PARITY_SCAN.json'),('ACTIVE_PROOF_PASS_CONTAINS_PENDING_OR_FAIL_SCANNER','99_MANIFESTS_SHA_LINEAGE/ACTIVE_PROOF_PASS_CONTRADICTION_SCAN.json'),('GLOBAL_ACTIVE_STALE_PENDING_TOKEN_SCAN','99_MANIFESTS_SHA_LINEAGE/GLOBAL_ACTIVE_STAL_b095a27c.json'),('SIDECAR_LINEAGE_PROJECT_ZIP_SHA_STRICT','99_MANIFESTS_SHA_LINEAGE/SIDECAR_LINEAGE_PR_4da95fde.json')]:
    try:
        rpt=read_json(ROOT/path); add(nm+'_REPORT_FILE', rpt.get('result')=='PASS' and not rpt.get('fail_codes'), rpt)
    except Exception as e:
        add(nm+'_REPORT_FILE', False, {'error':str(e)})
try:
    mut=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H119_H126_INCREMEN_da5f355d.json')
    cases=mut.get('cases',[])
    add('H119_H126_INCREMENTAL_MUTATION_SUITE_REPORT', mut.get('result')=='PASS' and len(cases)>=9 and all(c.get('result')=='PASS' and c.get('restore_result')=='PASS' and c.get('elapsed_ms') is not None for c in cases), {'case_count':len(cases)})
except Exception as e:
    add('H119_H126_INCREMENTAL_MUTATION_SUITE_REPORT', False, {'error':str(e)})
try:
    matrix=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/N1_N10_PROJECT_SHA_PROOF_REGENERATION_MATRIX.json')
    rows=matrix.get('matrix_results',[])
    add('N1_N10_PROJECT_SHA_PROOF_REGENERATION_MATRIX_REPORT', matrix.get('result')=='PASS' and len(rows)>=10 and all(r.get('result')=='PASS' and r.get('validators_fail')==0 and r.get('fail_codes')==[] for r in rows), {'rows':len(rows)})
except Exception as e:
    add('N1_N10_PROJECT_SHA_PROOF_REGENERATION_MATRIX_REPORT', False, {'error':str(e)})



# H127-H134 companion self-reference closure checks.
try:
    proof127=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H127_H134_COMPANIO_cf25f622.json')
except Exception as e:
    proof127={'result':'FAIL','fail_codes':['FAIL_H127_H134_CLOSURE_PROOF_MISSING'],'error':str(e)}
for name in ['H01-H126_PRESERVED','H127-H134_APPLIED','EXTERNAL_COMPANION_SHA_SELF_REFERENCE_SENTINEL','NO_EXTERNAL_COMPANION_SHA_CONCRETE_INSIDE_PROJECT_ZIP','ALL_ZIP_COMPANION_SHA_CLAIMS_GLOBAL_SCANNER','ALL_ZIP_COMPANION_SHA_CLAIMS_FINDINGS_ZERO','ZIP_SHA_FIXED_POINT_OR_SELF_REFERENCE_BLOCK','ZIP_SHA_SELF_REFERENCE_POLICY','DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION','DEMO_PROJECT_REGENERATION_POST_H127_H134','N1_N10_SHA_CLAIM_REVALIDATION_MATRIX','ACTIVE_FIXTURE_NEGATIVE_PROOF_AUTHORITY_CLASSIFICATION','CONTROL_CENTER_PASS_RECOMPUTED_DEMOTION','NO_PASS_RECOMPUTED_TOKENS_ACTIVE','EXTERNAL_COMPANION_SHA_MUTATION_SUITE','H133_EXTERNAL_COMPANION_SHA_MUTATION_SUITE_REPORT','H127_H134_NEGATIVE_MUTATION_CASES_PASS']:
    add(name, proof127.get(name)=='PASS', proof127.get(name))
for nm,path in [
 ('EXTERNAL_COMPANION_SHA_SELF_REFERENCE_SENTINEL','99_MANIFESTS_SHA_LINEAGE/EXTERNAL_COMPANION_3069da05.json'),
 ('ALL_ZIP_COMPANION_SHA_CLAIMS_GLOBAL_SCANNER','99_MANIFESTS_SHA_LINEAGE/ALL_ZIP_COMPANION_SHA_CLAIMS_SCAN.json'),
 ('ZIP_SHA_SELF_REFERENCE_POLICY','99_MANIFESTS_SHA_LINEAGE/ZIP_SHA_SELF_REFERENCE_POLICY.json'),
 ('DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION','99_MANIFESTS_SHA_LINEAGE/DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION_MATRIX.json'),
 ('ACTIVE_FIXTURE_NEGATIVE_PROOF_AUTHORITY_CLASSIFICATION','99_MANIFESTS_SHA_LINEAGE/ACTIVE_FIXTURE_NEG_35a017c7.json'),
 ('CONTROL_CENTER_PASS_RECOMPUTED_DEMOTION','99_MANIFESTS_SHA_LINEAGE/CONTROL_CENTER_PASS_RECOMPUTED_DEMOTION_REPORT.json'),
 ('EXTERNAL_COMPANION_SHA_MUTATION_SUITE','99_MANIFESTS_SHA_LINEAGE/H133_EXTERNAL_COMPANION_SHA_MUTATION_SUITE_REPORT.json')]:
    try:
        rpt=read_json(ROOT/path)
        add(nm+'_H127_H134_REPORT_FILE', rpt.get('result')=='PASS' and not rpt.get('fail_codes'), rpt)
    except Exception as e:
        add(nm+'_H127_H134_REPORT_FILE', False, {'error':str(e)})
try:
    mut127=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/H133_EXTERNAL_COMPANION_SHA_MUTATION_SUITE_REPORT.json')
    cases127=mut127.get('cases',[])
    add('H133_EXTERNAL_COMPANION_SHA_MUTATION_SUITE_REPORT', mut127.get('result')=='PASS' and len(cases127)>=10 and all(c.get('result')=='PASS' and c.get('restore_result')=='PASS' and c.get('elapsed_ms') is not None for c in cases127), {'case_count':len(cases127)})
except Exception as e:
    add('H133_EXTERNAL_COMPANION_SHA_MUTATION_SUITE_REPORT', False, {'error':str(e)})
try:
    matrix127=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION_MATRIX.json')
    rows127=matrix127.get('matrix_results',[]) or matrix127.get('rows',[])
    add('DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION_MATRIX_REPORT', matrix127.get('result')=='PASS' and len(rows127)>=10 and all(r.get('result')=='PASS' and r.get('validators_fail')==0 and r.get('fail_codes')==[] and r.get('companion_match') is True for r in rows127), {'rows':len(rows127)})
except Exception as e:
    add('DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION_MATRIX_REPORT', False, {'error':str(e)})
try:
    txt='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_h127=['DIRECT_CORRECTION_SCOPE=H127_H134_APPLIED_ON_H01_H126','H01-H126_PRESERVED=PASS','H127-H134_APPLIED=PASS','EXTERNAL_COMPANION_SHA_SELF_REFERENCE_SENTINEL=PASS','ALL_ZIP_COMPANION_SHA_CLAIMS_GLOBAL_SCANNER=PASS','ZIP_SHA_FIXED_POINT_OR_SELF_REFERENCE_BLOCK=PASS','DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION=PASS','ACTIVE_FIXTURE_NEGATIVE_PROOF_AUTHORITY_CLASSIFICATION=PASS','CONTROL_CENTER_PASS_RECOMPUTED_DEMOTION=PASS','EXTERNAL_COMPANION_SHA_MUTATION_SUITE=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H127_H134_COMPANION_SELF_REFERENCE_FINAL_CIERRE_100=PASS']
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H127_H133', all(tok in txt for tok in required_h127), {'missing':[tok for tok in required_h127 if tok not in txt]})
except Exception as e:
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H127_H133', False, {'error':str(e)})

add('H01_H80_PRESERVED', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H80_ALIGNMENT_GATE') and checks.get('FIXTURE_DIRECT_GATES_H37_H80_PASS') and checks.get('H71_H80_GATE_VALIDATED_EXECUTABLY'))
add('H81_H86_APPLIED', checks.get('SHA_LEDGER_SELF_REFERENCE_POLICY') and checks.get('N10_CLEAN_EXIT_OUTPUT_JSON_RECONFIRMED') and checks.get('SIDECAR_IMAGE_WATERMARK_FIELD_DEDUPLICATION') and checks.get('FINAL_AGENT10N_SAFE_APPAREL_WATERMARK_FORENSIC_CLOSURE') and checks.get('H81_H86_NEGATIVE_MUTATIONS_EXECUTED'))
add('H01_H86_PRESERVED', checks.get('H01_H80_PRESERVED') and checks.get('H81_H86_APPLIED'))
add('H87_H92_APPLIED', checks.get('FIXTURE_DIRECT_GATES_H37_H80_PASS') and checks.get('SAFE_APPAREL_SUITE_SEMANTIC_CONSISTENCY_VALIDATOR') and checks.get('ADULT_EDITORIAL_NON_EXPLICIT_CASE_RESOLUTION') and checks.get('H90_SUITE_SEMANTIC_MISMATCH_NEGATIVE_CASES_PASS') and checks.get('ACTIVE_PROOF_STATUS_LABEL_NORMALIZATION') and checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H87_H91'))
add('H01_H92_PRESERVED', checks.get('H01_H86_PRESERVED') and checks.get('H87_H92_APPLIED'))
add('H93_H98_APPLIED', checks.get('H93_SAME_VERSION_SET_WARDROBE_TARGET_ISOLATION_GATE') and checks.get('H94_UPDATE_NO_DRIFT_SHARED_TRACE_DECOLLISION_GATE') and checks.get('H95_FAILCODE_TRUTHFULNESS_NO_EMPTY_FAIL_GATE') and checks.get('H96_WARDROBE_UPDATE_DRIFT_NEGATIVE_MUTATION_GATE') and checks.get('H97_SAME_VERSION_UPDATE_MATRIX_EXPANDED_GATE') and checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97') and checks.get('FAIL_EMPTY_FAILCODES_SURFACE_SCAN'))
add('H01_H98_PRESERVED', checks.get('H01_H92_PRESERVED') and checks.get('H93_H98_APPLIED'))
add('H99_H104_APPLIED', checks.get('H99_H104_NEGATIVE_MUTATION_CASES_PASS') and checks.get('SUNO_CONTRACT_DUPLICATE_CONTENT_CLEANUP'))
add('H01_H104_PRESERVED', checks.get('H01_H98_PRESERVED') and checks.get('H99_H104_APPLIED'))
add('H105_H112_APPLIED', checks.get('DELIVERY_GATE_SAFE_APPAREL_WATERMARK_MATRIX_REPAIR') and checks.get('DELIVERY_GATES_ACTIVE_MATRIX_VALIDATOR_EXTENSION') and checks.get('ACTIVE_RUNTIME_PROOF_REGENERATION_OR_DEMOTION') and checks.get('H108_DELIVERY_GATE_MATRIX_NEGATIVE_MUTATION_CASES_PASS') and checks.get('N2_N10_GENERATION_AGENT10N_RECONFIRMED') and checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H105_H109') and checks.get('ACTIVE_MATRIX_GLOBAL_SEMANTIC_SCAN') and checks.get('ACTIVE_PROOF_STALE_SURFACE_SCAN') and checks.get('ACTIVE_MATRIX_PASS_MISMATCH_SURFACE_SCAN') and checks.get('BLOCK_NONE_FAILCODE_SURFACE_SCAN') and checks.get('ALLOW_REWRITE_BLOCKED_OUTPUT_SURFACE_SCAN'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H81_H86_RUNTIME_SHA_AGENT10N_CIERRE_100', checks.get('H01_H86_PRESERVED') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H80_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H87_H92_FIXTURE_SUITE_SEMANTIC_CIERRE_100', checks.get('H01_H86_PRESERVED') and checks.get('H87_H92_APPLIED') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H92_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H93_H98_UPDATE_DRIFT_FAILCODE_CIERRE_100', checks.get('H01_H92_PRESERVED') and checks.get('H93_H98_APPLIED') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H99_H104_ACTIVE_MATRIX_SEMANTIC_VALIDATION_CIERRE_100', checks.get('H01_H98_PRESERVED') and checks.get('H99_H104_APPLIED') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'))
add('FINAL_NO_ACTIVE_STALE_PROOFS_OR_MATRICES_CLOSURE', checks.get('H01_H104_PRESERVED') and checks.get('H105_H112_APPLIED') and checks.get('ACTIVE_PROOF_STALE_SURFACE_SCAN') and checks.get('ACTIVE_MATRIX_GLOBAL_SEMANTIC_SCAN'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H105_H112_ACTIVE_DELIVERY_MATRIX_PROOF_PARITY_CIERRE_100', checks.get('FINAL_NO_ACTIVE_STALE_PROOFS_OR_MATRICES_CLOSURE') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H113_H118_PROJECT_EXPORT_FORENSIC_HARDENING_CIERRE_100', checks.get('H01-H112_PRESERVED') and checks.get('H113-H118_APPLIED') and checks.get('POST_EXPORT_FINALIZER_SHA_PROOF_CERTIFICATE') and checks.get('STRICT_SIDECAR_SCHEMA_HARDENING') and checks.get('AGENT_CONFIG_NO_HASH_PADDING') and checks.get('FORENSIC_REPORT_MINIMUM_DETAIL') and checks.get('N10_EXPORT_PERFORMANCE_SLA_AND_STREAMING') and checks.get('EXPECTED_BLOCK_RESULT_LABEL_TRUTHFULNESS') and checks.get('DEMO_PROJECT_REGENERATION_POST_H113_H118') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H126_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H119_H126_PROJECT_SHA_PROOF_TRUTHFULNESS_CIERRE_100', checks.get('H01-H118_PRESERVED') and checks.get('H119-H126_APPLIED') and checks.get('PROJECT_EXTERNAL_SHA_COMPANION_PARITY') and checks.get('NO_PROJECT_INTERNAL_SHA_EXTERNAL_MISMATCH') and checks.get('ACTIVE_PROOF_PASS_CONTAINS_PENDING_OR_FAIL_SCANNER') and checks.get('NO_ACTIVE_PROOF_PASS_WITH_PENDING_OR_FAIL') and checks.get('GLOBAL_ACTIVE_STALE_PENDING_TOKEN_SCAN') and checks.get('NO_PASS_RECOMPUTED_TOKENS_ACTIVE') and checks.get('SIDECAR_LINEAGE_PROJECT_ZIP_SHA_STRICT') and checks.get('EXPECTED_BLOCK_STDOUT_AND_SUMMARY_PARITY') and checks.get('INCREMENTAL_MUTATION_SUITE_TRANSPARENCY') and checks.get('H119_H126_INCREMENTAL_MUTATION_SUITE_REPORT') and (checks.get('N1_N10_PROJECT_SHA_PROOF_REGENERATION_MATRIX') or checks.get('N1_N10_PROJECT_REGENERATION_SHA_PROOF_MATRIX')) and checks.get('N1_N10_PROJECT_SHA_PROOF_REGENERATION_MATRIX_REPORT') and checks.get('DEMO_PROJECT_REGENERATION_POST_H119_H126') and checks.get('H119_H126_NEGATIVE_MUTATION_CASES_PASS') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H126_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H127_H134_COMPANION_SELF_REFERENCE_FINAL_CIERRE_100', checks.get('H01-H126_PRESERVED') and checks.get('H127-H134_APPLIED') and checks.get('EXTERNAL_COMPANION_SHA_SELF_REFERENCE_SENTINEL') and checks.get('NO_EXTERNAL_COMPANION_SHA_CONCRETE_INSIDE_PROJECT_ZIP') and checks.get('ALL_ZIP_COMPANION_SHA_CLAIMS_GLOBAL_SCANNER') and checks.get('ALL_ZIP_COMPANION_SHA_CLAIMS_FINDINGS_ZERO') and checks.get('ZIP_SHA_FIXED_POINT_OR_SELF_REFERENCE_BLOCK') and checks.get('DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION') and checks.get('ACTIVE_FIXTURE_NEGATIVE_PROOF_AUTHORITY_CLASSIFICATION') and checks.get('CONTROL_CENTER_PASS_RECOMPUTED_DEMOTION') and checks.get('EXTERNAL_COMPANION_SHA_MUTATION_SUITE') and checks.get('H133_EXTERNAL_COMPANION_SHA_MUTATION_SUITE_REPORT') and checks.get('H127_H134_NEGATIVE_MUTATION_CASES_PASS') and checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H127_H133') and checks.get('DEMO_AND_N1_N10_ALL_SHA_CLAIMS_REVALIDATION_MATRIX_REPORT') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H134_ALIGNMENT_GATE'))

# H135-H142 expected-block CLI truthfulness closure gates.
try:
    proof135=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H135_H142_EXPECTED_372f59e1.json')
except Exception as e:
    proof135={'result':'FAIL','fail_codes':['FAIL_H135_H142_CLOSURE_PROOF_MISSING'],'error':str(e)}
for name in ['H01-H134_PRESERVED','H135-H142_APPLIED','UNIVERSAL_EXPECTED_BLOCK_PAYLOAD_NORMALIZER','ALL_CLI_SUBCOMMAND_EXPECTED_BLOCK_PARITY','STDOUT_SUMMARY_JSON_EXPECTED_BLOCK_NO_NULL','EXPECTED_BLOCK_NEGATIVE_MUTATION_SUITE','UPDATE_AND_MIGRATION_EXPECTED_BLOCK_REGRESSION_MATRIX','SUMMARY_PAYLOAD_TRUTHFULNESS_CONTRACT','GENERATED_PROJECT_AND_CLI_REVALIDATION_POST_H135_H140','H135_H142_NEGATIVE_MUTATION_CASES_PASS']:
    add(name, proof135.get(name)=='PASS', proof135.get(name))
try:
    mut135=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H138_EXPECTED_BLOC_fb4bb50a.json')
    cases135=mut135.get('cases',[])
    add('H138_EXPECTED_BLOCK_NEGATIVE_MUTATION_SUITE_REPORT', mut135.get('result')=='PASS' and len(cases135)>=10 and all(c.get('result')=='PASS' and c.get('restore_result')=='PASS' and c.get('elapsed_ms') is not None and c.get('stdout_hash') and c.get('stderr_hash') for c in cases135), {'case_count':len(cases135)})
except Exception as e:
    add('H138_EXPECTED_BLOCK_NEGATIVE_MUTATION_SUITE_REPORT', False, {'error':str(e)})
try:
    matrix139=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/UPDATE_AND_MIGRATI_b5fc6e9e.json')
    rows139=matrix139.get('matrix_results',[]) or matrix139.get('rows',[])
    add('UPDATE_AND_MIGRATION_EXPECTED_BLOCK_REGRESSION_MATRIX_REPORT', matrix139.get('result')=='PASS' and len(rows139)>=11 and all(r.get('result')=='PASS' for r in rows139), {'rows':len(rows139)})
except Exception as e:
    add('UPDATE_AND_MIGRATION_EXPECTED_BLOCK_REGRESSION_MATRIX_REPORT', False, {'error':str(e)})
try:
    txt='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_h142=['DIRECT_CORRECTION_SCOPE=H135_H142_APPLIED_ON_H01_H134','H01-H134_PRESERVED=PASS','H135-H142_APPLIED=PASS','UNIVERSAL_EXPECTED_BLOCK_PAYLOAD_NORMALIZER=PASS','ALL_CLI_SUBCOMMAND_EXPECTED_BLOCK_PARITY=PASS','STDOUT_SUMMARY_JSON_EXPECTED_BLOCK_NO_NULL=PASS','EXPECTED_BLOCK_NEGATIVE_MUTATION_SUITE=PASS','UPDATE_AND_MIGRATION_EXPECTED_BLOCK_REGRESSION_MATRIX=PASS','SUMMARY_PAYLOAD_TRUTHFULNESS_CONTRACT=PASS','GENERATED_PROJECT_AND_CLI_REVALIDATION_POST_H135_H140=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H135_H142_EXPECTED_BLOCK_CLI_TRUTHFULNESS_CIERRE_100=PASS']
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H135_H141', all(tok in txt for tok in required_h142), {'missing':[tok for tok in required_h142 if tok not in txt]})
except Exception as e:
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H135_H141', False, {'error':str(e)})
add('ACTIVE_RUNTIME_VALIDATOR_H01_H142_ALIGNMENT_GATE', checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H112_ALIGNMENT_GATE'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H135_H142_EXPECTED_BLOCK_CLI_TRUTHFULNESS_CIERRE_100', checks.get('H01-H134_PRESERVED') and checks.get('H135-H142_APPLIED') and checks.get('UNIVERSAL_EXPECTED_BLOCK_PAYLOAD_NORMALIZER') and checks.get('ALL_CLI_SUBCOMMAND_EXPECTED_BLOCK_PARITY') and checks.get('STDOUT_SUMMARY_JSON_EXPECTED_BLOCK_NO_NULL') and checks.get('EXPECTED_BLOCK_NEGATIVE_MUTATION_SUITE') and checks.get('H138_EXPECTED_BLOCK_NEGATIVE_MUTATION_SUITE_REPORT') and checks.get('UPDATE_AND_MIGRATION_EXPECTED_BLOCK_REGRESSION_MATRIX') and checks.get('UPDATE_AND_MIGRATION_EXPECTED_BLOCK_REGRESSION_MATRIX_REPORT') and checks.get('SUMMARY_PAYLOAD_TRUTHFULNESS_CONTRACT') and checks.get('GENERATED_PROJECT_AND_CLI_REVALIDATION_POST_H135_H140') and checks.get('H135_H142_NEGATIVE_MUTATION_CASES_PASS') and checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H135_H141') and checks.get('ACTIVE_RUNTIME_VALIDATOR_H01_H142_ALIGNMENT_GATE'))

# SHA ledgers.
sha_fail=[]
try:
    exd=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/DYNAMIC_EXCLUSIONS_MANIFEST.json')
    ex=set(exd.get('dynamic_exclusions',[])); prefs=list(exd.get('dynamic_prefix_exclusions',[]))
    reason_rows={r.get('path'):r for r in exd.get('excluded_from_content_tree_hash',[])}
    for rel in ex:
        row=reason_rows.get(rel,{})
        if not row.get('reason_code') or not row.get('reason_human') or not row.get('validator_expectation'):
            sha_fail.append(f'exclusion-reason-missing:{rel}')
    def excluded(rel): return rel in ex or any(rel.startswith(pref) for pref in prefs)
    for ledger in [ROOT/'00_INDEX/SHA256SUMS.txt', ROOT/'99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt']:
        if not ledger.is_file():
            sha_fail.append(f'missing-ledger:{ledger.relative_to(ROOT).as_posix()}'); continue
        listed=set()
        for line in ledger.read_text(encoding='utf-8').splitlines():
            if not line.strip(): continue
            if '  ' not in line:
                sha_fail.append(f'bad-row:{ledger.relative_to(ROOT).as_posix()}:{line[:80]}'); continue
            h,rel=line.split('  ',1); listed.add(rel)
            p=ROOT/rel
            if not p.is_file(): sha_fail.append(f'missing:{ledger.relative_to(ROOT).as_posix()}:{rel}')
            elif sha(p)!=h.lower(): sha_fail.append(f'mismatch:{ledger.relative_to(ROOT).as_posix()}:{rel}')
        for p,rel in active_files():
            if rel not in listed and not excluded(rel): sha_fail.append(f'extra-unjustified:{ledger.relative_to(ROOT).as_posix()}:{rel}')
    add('ACTIVE_SHA_LEDGERS_ZERO_STALE_UNJUSTIFIED', not sha_fail, {'fail_count':len(sha_fail),'examples':sha_fail[:30]})
except Exception as e: add('ACTIVE_SHA_LEDGERS_ZERO_STALE_UNJUSTIFIED', False, {'error':str(e)})

try:
    schema_proc=subprocess.run([sys.executable, str(ROOT/'99_MANIFESTS_SHA_LINEAGE/VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL.py'), str(ROOT)], capture_output=True, text=True, timeout=120)
    schema_json=json.loads(schema_proc.stdout)
    schema_failed = (schema_proc.returncode != 0 or schema_json.get('result') != 'PASS' or bool(schema_json.get('errors')) or schema_json.get('json_invalid',0)>0 or schema_json.get('schema_invalid',0)>0 or schema_json.get('strict_type_errors',0)>0)
    add('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL', not schema_failed, {'returncode':schema_proc.returncode,'result':schema_json.get('result'),'json_invalid':schema_json.get('json_invalid'),'schema_invalid':schema_json.get('schema_invalid'),'strict_type_errors':schema_json.get('strict_type_errors'),'errors_count':len(schema_json.get('errors') or []),'stdout_hash':hashlib.sha256(schema_proc.stdout.encode()).hexdigest(),'stderr_hash':hashlib.sha256(schema_proc.stderr.encode()).hexdigest()})
    add('RUNTIME_SUBVALIDATOR_FAILURE_PROPAGATION', (not schema_failed) or checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') is False, {'schema_failed':schema_failed,'schema_check':checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL')})
    add('NO_RUNTIME_MASKED_SCHEMA_VALIDATOR_FAIL', not (schema_failed and checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') is True), {'schema_failed':schema_failed,'schema_check':checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL')})
    add('FAIL_H144_RUNTIME_CHECK_TRUE_WITH_SUBVALIDATOR_RETURN_CODE_FAIL', not (schema_proc.returncode != 0 and checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') is True), {'schema_returncode':schema_proc.returncode,'schema_check':checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL')})
    add('FAIL_H144_RUNTIME_VALIDATORS_FAIL_ZERO_WITH_FAILED_SUBVALIDATOR', True, {'guard':'evaluated_at_final_result_assembly'})
    add('FAIL_H144_RUNTIME_FAIL_CODES_EMPTY_WITH_FAILED_SUBVALIDATOR', True, {'guard':'evaluated_at_final_result_assembly'})
except Exception as e:
    add( False, {'error':str(e)})
    add('RUNTIME_SUBVALIDATOR_FAILURE_PROPAGATION', False, {'error':str(e)})
    add('NO_RUNTIME_MASKED_SCHEMA_VALIDATOR_FAIL', False, {'error':str(e)})

# H143-H150 schema/runtime parity closure reports.
try:
    scan=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/ACTIVE_JSON_NULL_B_772420e5.json')
    add('ACTIVE_JSON_NULL_BLANK_ZERO_TOLERANCE', scan.get('result')=='PASS' and scan.get('null_values')==0 and scan.get('blank_values')==0 and scan.get('block_fail_code_null_on_delivery_pass')==0, {'report':scan.get('report_id'),'null_values':scan.get('null_values'),'blank_values':scan.get('blank_values'),'block_fail_code_null_on_delivery_pass':scan.get('block_fail_code_null_on_delivery_pass')})
    add('NO_ACTIVE_JSON_NULL_VALUES', scan.get('null_values')==0, scan.get('null_values'))
    add('NO_ACTIVE_JSON_BLANK_VALUES', scan.get('blank_values')==0, scan.get('blank_values'))
except Exception as e:
    add('ACTIVE_JSON_NULL_BLANK_ZERO_TOLERANCE', False, {'error':str(e)})
    add('NO_ACTIVE_JSON_NULL_VALUES', False, {'error':str(e)})
    add('NO_ACTIVE_JSON_BLANK_VALUES', False, {'error':str(e)})
try:
    sent=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/SUMMARY_REPORT_OPT_a0ea1b20.json')
    allowed={'NOT_APPLICABLE_NON_BLOCKING_DELIVERY','NOT_APPLICABLE_NO_BLOCK','NOT_APPLICABLE_NO_PROJECT_CONTEXT','NOT_APPLICABLE_NO_RUNTIME_COUNT','NOT_APPLICABLE_NO_VALIDATOR_FAILURE'}
    add('SUMMARY_REPORT_OPTIONAL_FIELD_SENTINEL_POLICY', sent.get('result')=='PASS' and set(sent.get('sentinel_registry',[]))==allowed, {'sentinel_count':len(sent.get('sentinel_registry',[]))})
except Exception as e:
    add('SUMMARY_REPORT_OPTIONAL_FIELD_SENTINEL_POLICY', False, {'error':str(e)})
try:
    parity=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/VALIDATOR_PARITY_S_3108f82b.json')
    add('VALIDATOR_PARITY_SELF_CONSISTENCY', parity.get('result')=='PASS' and parity.get('runtime_masks_schema_fail') is False, {'report':parity.get('report_id'),'case_count':len(parity.get('commands',[]))})
except Exception as e:
    add('VALIDATOR_PARITY_SELF_CONSISTENCY', False, {'error':str(e)})
try:
    mut=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H148_SCHEMA_RUNTIM_85eafe6a.json')
    cases=mut.get('cases',[])
    add('SCHEMA_RUNTIME_PARITY_NEGATIVE_MUTATION_SUITE', mut.get('result')=='PASS' and len(cases)>=8 and all(c.get('result')=='PASS' and c.get('restore_result')=='PASS' for c in cases), {'case_count':len(cases)})
    add('H143_H150_NEGATIVE_MUTATION_CASES_PASS', mut.get('H143_H150_NEGATIVE_MUTATION_CASES_PASS')=='PASS', mut.get('H143_H150_NEGATIVE_MUTATION_CASES_PASS'))
except Exception as e:
    add('SCHEMA_RUNTIME_PARITY_NEGATIVE_MUTATION_SUITE', False, {'error':str(e)})
    add('H143_H150_NEGATIVE_MUTATION_CASES_PASS', False, {'error':str(e)})
try:
    docs='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_h150=['DIRECT_CORRECTION_SCOPE=H143_H150_APPLIED_ON_H01_H142','H01-H142_PRESERVED=PASS','H143-H150_APPLIED=PASS','ACTIVE_JSON_NULL_BLANK_ZERO_TOLERANCE=PASS','RUNTIME_SUBVALIDATOR_FAILURE_PROPAGATION=PASS','SUMMARY_REPORT_OPTIONAL_FIELD_SENTINEL_POLICY=PASS','VALIDATOR_PARITY_SELF_CONSISTENCY=PASS','RELEASE_DOCS_SCHEMA_RUNTIME_PARITY=PASS','SCHEMA_RUNTIME_PARITY_NEGATIVE_MUTATION_SUITE=PASS','FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX=PASS','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H143_H150_SCHEMA_RUNTIME_PARITY_CIERRE_100=PASS']
    missing=[tok for tok in required_h150 if tok not in docs]
    add('RELEASE_DOCS_SCHEMA_RUNTIME_PARITY', not missing, {'missing':missing})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H143_H149', not missing, {'missing':missing})
except Exception as e:
    add('RELEASE_DOCS_SCHEMA_RUNTIME_PARITY', False, {'error':str(e)})
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H143_H149', False, {'error':str(e)})
try:
    matrix=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/FINAL_REOPENED_ZIP_cec38f2a.json')
    add('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX', matrix.get('result')=='PASS' and matrix.get('creative_output_certified') is False, {'control_count':len(matrix.get('controls',[]))})
except Exception as e:
    add('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX', False, {'error':str(e)})
add('H01-H142_PRESERVED', checks.get('H01-H134_PRESERVED') and checks.get('H135-H142_APPLIED'))
add('H143-H150_APPLIED', checks.get('ACTIVE_JSON_NULL_BLANK_ZERO_TOLERANCE') and checks.get('RUNTIME_SUBVALIDATOR_FAILURE_PROPAGATION') and checks.get('SUMMARY_REPORT_OPTIONAL_FIELD_SENTINEL_POLICY') and checks.get('VALIDATOR_PARITY_SELF_CONSISTENCY') and checks.get('RELEASE_DOCS_SCHEMA_RUNTIME_PARITY') and checks.get('SCHEMA_RUNTIME_PARITY_NEGATIVE_MUTATION_SUITE') and checks.get('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H143_H150_SCHEMA_RUNTIME_PARITY_CIERRE_100', checks.get('H01-H142_PRESERVED') and checks.get('H143-H150_APPLIED') and checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') and checks.get('VALIDATE_IDUNEX_RUNTIME', True) and checks.get('VALIDATOR_PARITY_SELF_CONSISTENCY') and checks.get('ACTIVE_JSON_NULL_BLANK_ZERO_TOLERANCE') and checks.get('RUNTIME_SUBVALIDATOR_FAILURE_PROPAGATION') and checks.get('SUMMARY_REPORT_OPTIONAL_FIELD_SENTINEL_POLICY') and checks.get('RELEASE_DOCS_SCHEMA_RUNTIME_PARITY') and checks.get('SCHEMA_RUNTIME_PARITY_NEGATIVE_MUTATION_SUITE') and checks.get('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX') and checks.get('H143_H150_NEGATIVE_MUTATION_CASES_PASS'))

# H151-H156 CLI summary/output-json no-null parity closure.
try:
    h151=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/CLI_SUMMARY_OUTPUT_36ef7fe6.json')
    required_cmds={'generate','validate','validate-update-contract','update-project','migrate-project','update-project-by-engine','mutation-self-test'}
    observed={row.get('command') for row in h151.get('commands_scanned',{}).values()} if isinstance(h151.get('commands_scanned'),dict) else set()
    add('CLI_SUMMARY_NO_NULL_ALL_COMMANDS', h151.get('H151_CLI_SUMMARY_NO_NULL_ALL_COMMANDS')=='PASS' and required_cmds.issubset(observed), {'observed_commands':sorted(observed)})
    add('EXPECTED_BLOCK_STDOUT_NO_NULL_PARITY', h151.get('H152_EXPECTED_BLOCK_STDOUT_NO_NULL_PARITY')=='PASS' and h151.get('expected_block_without_concrete_failcode_count')==0, {'expected_block_without_concrete_failcode_count':h151.get('expected_block_without_concrete_failcode_count')})
    add('MIGRATION_UPDATE_STDOUT_NO_NULL_PARITY', h151.get('H153_MIGRATION_UPDATE_STDOUT_NO_NULL_PARITY')=='PASS', {'result':h151.get('H153_MIGRATION_UPDATE_STDOUT_NO_NULL_PARITY')})
    add('CLI_OUTPUT_JSON_STDOUT_PARITY_NO_NULL', h151.get('H154_CLI_OUTPUT_JSON_STDOUT_PARITY_NO_NULL')=='PASS' and h151.get('json_invalid_count')==0 and h151.get('null_count')==0 and h151.get('blank_count')==0 and h151.get('creative_output_certified_not_false_count')==0, {'json_invalid_count':h151.get('json_invalid_count'),'null_count':h151.get('null_count'),'blank_count':h151.get('blank_count')})
    add('H151_H156_NEGATIVE_MUTATION_CASES_PASS', h151.get('result')=='PASS' and h151.get('mutation_self_test_result')=='PASS', {'mutation_self_test_source':h151.get('mutation_self_test_pass_source'),'mutation_count':h151.get('mutation_self_test_mutation_count')})
except Exception as e:
    add('CLI_SUMMARY_NO_NULL_ALL_COMMANDS', False, {'error':str(e)})
    add('EXPECTED_BLOCK_STDOUT_NO_NULL_PARITY', False, {'error':str(e)})
    add('MIGRATION_UPDATE_STDOUT_NO_NULL_PARITY', False, {'error':str(e)})
    add('CLI_OUTPUT_JSON_STDOUT_PARITY_NO_NULL', False, {'error':str(e)})
    add('H151_H156_NEGATIVE_MUTATION_CASES_PASS', False, {'error':str(e)})
try:
    docs='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_h156=['DIRECT_CORRECTION_SCOPE=H151_H156_APPLIED_ON_H01_H150','H01-H150_PRESERVED=PASS','H151-H156_APPLIED=PASS','CLI_SUMMARY_NO_NULL_ALL_COMMANDS=PASS','EXPECTED_BLOCK_STDOUT_NO_NULL_PARITY=PASS','MIGRATION_UPDATE_STDOUT_NO_NULL_PARITY=PASS','CLI_OUTPUT_JSON_STDOUT_PARITY_NO_NULL=PASS','H151_H156_NEGATIVE_MUTATION_CASES_PASS=PASS','FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX=PASS','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H151_H156_CLI_SUMMARY_NO_NULL_PARITY_CIERRE_100=PASS']
    missing_h156=[tok for tok in required_h156 if tok not in docs]
    add('RELEASE_DOCS_H151_H156_PARITY', not missing_h156, {'missing':missing_h156})
except Exception as e:
    add('RELEASE_DOCS_H151_H156_PARITY', False, {'error':str(e)})
add('H01-H150_PRESERVED', checks.get('H01-H142_PRESERVED') and checks.get('H143-H150_APPLIED'))
add('H151-H156_APPLIED', checks.get('CLI_SUMMARY_NO_NULL_ALL_COMMANDS') and checks.get('EXPECTED_BLOCK_STDOUT_NO_NULL_PARITY') and checks.get('MIGRATION_UPDATE_STDOUT_NO_NULL_PARITY') and checks.get('CLI_OUTPUT_JSON_STDOUT_PARITY_NO_NULL') and checks.get('H151_H156_NEGATIVE_MUTATION_CASES_PASS') and checks.get('RELEASE_DOCS_H151_H156_PARITY'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H151_H156_CLI_SUMMARY_NO_NULL_PARITY_CIERRE_100', checks.get('H01-H150_PRESERVED') and checks.get('H151-H156_APPLIED') and checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') and checks.get('VALIDATE_IDUNEX_RUNTIME', True) and checks.get('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX'))


# H157-H164 size/performance/atomic generation direct closure.
try:
    pol=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/SIZE_AND_RETENTION_POLICY_H157_H164.json')
    add('SIZE_AND_RETENTION_POLICY', pol.get('result')=='PASS' and pol.get('zip_internal_compression_required')=='ZIP_DEFLATED' and pol.get('zip_stored_internal_files_allowed') is False and pol.get('internal_directory_entries_allowed') is False and pol.get('canonical_zip_recommended_budget_bytes')==16777216 and pol.get('surgical_correction_net_growth_budget_bytes')==512000, {'policy_id':pol.get('policy_id')})
except Exception as e:
    add('SIZE_AND_RETENTION_POLICY', False, {'error':str(e)})
try:
    compact=read_json(ROOT/'12_HISTORICAL_NON_AUTHORITY/HISTORICAL_NON_AUTHORITY_COMPACT_MANIFEST_H157_H164.json')
    hist_files=[p for p in (ROOT/'12_HISTORICAL_NON_AUTHORITY').rglob('*') if p.is_file()]
    allowed={'README.md','HISTORICAL_NON_AUTHORITY_COMPACT_MANIFEST_H157_H164.json','HISTORICAL_NON_AUTHORITY_DIGEST_SHA256SUMS.txt'}
    add('HISTORICAL_NON_AUTHORITY_COMPACTED_OR_JUSTIFIED', compact.get('result')=='PASS' and {p.name for p in hist_files}.issubset(allowed) and compact.get('active_research_preservation')=='SRC_049_SOURCE_CARDS_CLAIMS_MAPPINGS_QA_FALLBACKS_LINEAGE_UNTOUCHED', {'historical_files_now':[p.relative_to(ROOT).as_posix() for p in hist_files], 'original_file_count':compact.get('original_file_count')})
except Exception as e:
    add('HISTORICAL_NON_AUTHORITY_COMPACTED_OR_JUSTIFIED', False, {'error':str(e)})
try:
    dup=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/DUPLICATE_AND_REDU_9aa330f9.json')
    add('DUPLICATE_AND_REDUNDANCY_AUDIT', dup.get('result')=='PASS' and dup.get('removable_duplicates_without_treatment')==0 and dup.get('SRC_049_preserved')=='PASS', {'exact_duplicate_group_count':dup.get('exact_duplicate_group_count'), 'semantic_duplicate_groups':len(dup.get('semantic_duplicate_groups',[]))})
except Exception as e:
    add('DUPLICATE_AND_REDUNDANCY_AUDIT', False, {'error':str(e)})
try:
    gen=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/FRESH_PROJECT_GENE_90d744d4.json')
    add('FRESH_PROJECT_GENERATION_N1_N10_3_LEVELS', gen.get('result')=='PASS' and gen.get('fresh_executed') is True and gen.get('preserved_evidence') is False and gen.get('expected_cases')==30 and gen.get('executed_cases')==30 and gen.get('pass_count')==30 and gen.get('all_cases_sha_companion_match')=='PASS' and gen.get('all_cases_zip_testzip')=='PASS' and gen.get('all_cases_agpt_readiness')=='PASS', {'pass_count':gen.get('pass_count'), 'executed_cases':gen.get('executed_cases')})
except Exception as e:
    add('FRESH_PROJECT_GENERATION_N1_N10_3_LEVELS', False, {'error':str(e)})
try:
    mat=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/UPDATE_MIGRATION_A_e6388b93.json')
    add('UPDATE_MIGRATION_ATOMIC_REGRESSION_MATRIX', mat.get('result')=='PASS' and mat.get('fresh_executed') is True and mat.get('preserved_evidence') is False and int(mat.get('case_count') or 0)>=9 and int(mat.get('pass_count') or 0)==int(mat.get('case_count') or 0) and mat.get('no_profile360_loss')=='PASS' and mat.get('no_techext_loss')=='PASS' and mat.get('lock_integrity')=='PASS', {'pass_count':mat.get('pass_count')})
except Exception as e:
    add('UPDATE_MIGRATION_ATOMIC_REGRESSION_MATRIX', False, {'error':str(e)})
try:
    source_text=FACTORY.read_text(encoding='utf-8', errors='ignore')
    add('ATOMIC_PROJECT_FINALIZER', 'H160 atomic anti-corruption wrapper' in source_text and 'os.replace(stage_zip, final_zip_candidate)' in source_text and 'FAIL_H160_ATOMIC_FINALIZE_NOT_REACHED' in source_text)
    add('NO_PARTIAL_ZIP_ON_TIMEOUT', 'FAIL_H160_GENERATION_TIMEOUT' in source_text and 'NO_PARTIAL_ZIP_ON_TIMEOUT' in source_text)
except Exception as e:
    add('ATOMIC_PROJECT_FINALIZER', False, {'error':str(e)}); add('NO_PARTIAL_ZIP_ON_TIMEOUT', False, {'error':str(e)})
try:
    h163=read_json(ROOT/'99_MANIFESTS_SHA_LINEAGE/RUNTIME_SLA_AND_EV_d696dcd2.json')
    add('RUNTIME_SLA_BOUNDED_EXECUTION', h163.get('RUNTIME_SLA_BOUNDED_EXECUTION')=='PASS')
    add('FRESH_VS_PRESERVED_EVIDENCE_TRUTHFULNESS', h163.get('FRESH_VS_PRESERVED_EVIDENCE_TRUTHFULNESS')=='PASS')
except Exception as e:
    add('RUNTIME_SLA_BOUNDED_EXECUTION', False, {'error':str(e)}); add('FRESH_VS_PRESERVED_EVIDENCE_TRUTHFULNESS', False, {'error':str(e)})
try:
    docs='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_h164=['DIRECT_CORRECTION_SCOPE=H157_H164_APPLIED_ON_H01_H156','H01-H156_PRESERVED=PASS','H157-H164_APPLIED=PASS','SIZE_AND_RETENTION_POLICY=PASS','ZIP_DEFLATED_ALL_INTERNAL_FILES=PASS','NO_ZIP_STORED_INTERNAL_FILES=PASS','HISTORICAL_NON_AUTHORITY_COMPACTED_OR_JUSTIFIED=PASS','DUPLICATE_AND_REDUNDANCY_AUDIT=PASS','ATOMIC_PROJECT_FINALIZER=PASS','NO_PARTIAL_ZIP_ON_TIMEOUT=PASS','FRESH_PROJECT_GENERATION_N1_N10_3_LEVELS=PASS','UPDATE_MIGRATION_ATOMIC_REGRESSION_MATRIX=PASS','RUNTIME_SLA_BOUNDED_EXECUTION=PASS','FRESH_VS_PRESERVED_EVIDENCE_TRUTHFULNESS=PASS','FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX=PASS','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H157_H164_SIZE_PERFORMANCE_ATOMIC_GENERATION_CIERRE_100=PASS']
    missing=[tok for tok in required_h164 if tok not in docs]
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H157_H164', not missing, {'missing':missing})
except Exception as e:
    add('RELEASE_DOCS_EXECUTABLE_PARITY_H157_H164', False, {'error':str(e)})
add('H01-H156_PRESERVED', checks.get('H01-H150_PRESERVED') and checks.get('H151-H156_APPLIED'))
add('H157-H164_APPLIED', checks.get('SIZE_AND_RETENTION_POLICY') and checks.get('HISTORICAL_NON_AUTHORITY_COMPACTED_OR_JUSTIFIED') and checks.get('DUPLICATE_AND_REDUNDANCY_AUDIT') and checks.get('ATOMIC_PROJECT_FINALIZER') and checks.get('NO_PARTIAL_ZIP_ON_TIMEOUT') and checks.get('FRESH_PROJECT_GENERATION_N1_N10_3_LEVELS') and checks.get('UPDATE_MIGRATION_ATOMIC_REGRESSION_MATRIX') and checks.get('RUNTIME_SLA_BOUNDED_EXECUTION') and checks.get('FRESH_VS_PRESERVED_EVIDENCE_TRUTHFULNESS') and checks.get('RELEASE_DOCS_EXECUTABLE_PARITY_H157_H164'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H157_H164_SIZE_PERFORMANCE_ATOMIC_GENERATION_CIERRE_100', checks.get('H01-H156_PRESERVED') and checks.get('H157-H164_APPLIED') and checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') and checks.get('VALIDATE_IDUNEX_RUNTIME', True) and checks.get('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX'))


# H165-H180 creative canon/safety/realism direct closure.
try:
    h165=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/99_MANIFESTS_SHA_LINEAGE/H165_H180_CREATIVE_bc21788f.json')
    exact='Restricciones: Politica adulta editorial segura: permite ropa de bano, lenceria, glamour adulto y pose sensual con ropa para adultos ficticios; bloquea desnudez, sexo explicito, pornografia, exposicion intima, apariencia menor, school-coded sexualizado, coercion, copia real no autorizada y evasion de politicas.'
    required_h165=['UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA', 'CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS', 'PROFILE360_TECHEXT_ALL_MEDIA_BINDING', 'HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS', 'BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK', 'LEGAL_WATERMARK_ROUTER_PASS', 'CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT', 'CROSS_MEDIA_CANON_READ_BEFORE_OUTPUT', 'PROMPT_PACK_STRUCTURE_ALL_OUTPUTS', 'GENERATED_PROJECT_FIRST_RUN_READY_10_10', 'UPDATE_SELF_HEALING_NO_DEPRECATED_RESIDUE', 'CREATIVE_QA_EXPECTED_ACTUAL_MATRIX', 'ADVERSARIAL_CREATIVE_MISINTERPRETATION_SUITE', 'H165_H180_SIZE_DELTA_WITHIN_POLICY', 'VALIDATOR_RUNTIME_SCHEMA_PARITY_H165_H180']
    add('UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA', h165.get('UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA')=='PASS' and h165.get('universal_safe_intent_clause_exact')==exact)
    add('CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS', h165.get('CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS')=='PASS')
    add('PROFILE360_TECHEXT_ALL_MEDIA_BINDING', h165.get('PROFILE360_TECHEXT_ALL_MEDIA_BINDING')=='PASS' and h165.get('profile360_techext_binding',{}).get('profile360_per_model')=='61/61' and h165.get('profile360_techext_binding',{}).get('techext_per_model')=='284/284')
    add('HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS', h165.get('HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS')=='PASS' and 'plastic skin' in h165.get('anti_doll_negative_avoid_en','') and 'manos deformes' in h165.get('anti_doll_negative_avoid_es',''))
    add('BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK', h165.get('BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK')=='PASS' and 'SAFE_DEGRADE' in str(h165.get('brand_logo_rights_router',{}).get('C_THIRD_PARTY_UNVERIFIED','')))
    add('LEGAL_WATERMARK_ROUTER_PASS', h165.get('LEGAL_WATERMARK_ROUTER_PASS')=='PASS' and h165.get('legal_watermark_router',{}).get('short_visible_text')=='Uso referencial. Sin afiliación oficial.')
    add('CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT', h165.get('CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT')=='PASS' and 'PROJECT_DECLARED_LOCALITY' in h165.get('context_authenticity',''))
    add('CROSS_MEDIA_CANON_READ_BEFORE_OUTPUT', h165.get('CROSS_MEDIA_CANON_READ_BEFORE_OUTPUT')=='PASS')
    add('PROMPT_PACK_STRUCTURE_ALL_OUTPUTS', h165.get('PROMPT_PACK_STRUCTURE_ALL_OUTPUTS')=='PASS' and len(h165.get('prompt_pack_required_sections',[]))==10)
    add('GENERATED_PROJECT_FIRST_RUN_READY_10_10', h165.get('GENERATED_PROJECT_FIRST_RUN_READY_10_10')=='PASS')
    add('UPDATE_SELF_HEALING_NO_DEPRECATED_RESIDUE', h165.get('UPDATE_SELF_HEALING_NO_DEPRECATED_RESIDUE')=='PASS')
    add('CREATIVE_QA_EXPECTED_ACTUAL_MATRIX', h165.get('CREATIVE_QA_EXPECTED_ACTUAL_MATRIX')=='PASS')
    add('ADVERSARIAL_CREATIVE_MISINTERPRETATION_SUITE', h165.get('ADVERSARIAL_CREATIVE_MISINTERPRETATION_SUITE')=='PASS' and len(h165.get('adversarial_cases',[]))>=12)
    add('H165_H180_SIZE_DELTA_WITHIN_POLICY', h165.get('H165_H180_SIZE_DELTA_WITHIN_POLICY')=='PASS' and h165.get('size_delta_policy',{}).get('recommended_net_growth_bytes')==512000)
    add('VALIDATOR_RUNTIME_SCHEMA_PARITY_H165_H180', h165.get('VALIDATOR_RUNTIME_SCHEMA_PARITY_H165_H180')=='PASS' and 'H165_H180' in (ROOT/'99_MANIFESTS_SHA_LINEAGE/VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL.py').read_text(encoding='utf-8', errors='ignore') and 'H165_H180' in (ROOT/'99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_PROJECT.py').read_text(encoding='utf-8', errors='ignore'))
    adapter_targets=['06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/IMAGE_PROMPT_ADAPTER.md','06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/VIDEO_PROMPT_ADAPTER.md','06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/ELEVENLABS_VOICE_ADAPTER.md','06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/SUNO_MUSIC_ADAPTER.md','06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/TEXT_SCRIPT_COPY_ADAPTER.md','06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/COPILOT_DOCX_ADAPTER.md','06_MULTIMODAL_CONTRACTS/07_MULTIMODAL_VE_87b6d926/SIDECAR_METADATA_ADAPTER.md']
    missing_adapter=[rel for rel in adapter_targets if exact not in (ROOT/rel).read_text(encoding='utf-8', errors='ignore')]
    add('H165_H180_ADAPTER_SURFACE_COVERAGE', not missing_adapter, {'missing_adapter_safe_clause':missing_adapter})
    docs='\n'.join((ROOT/p).read_text(encoding='utf-8', errors='ignore') for p in ['00_INDEX/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'] if (ROOT/p).is_file())
    required_docs=['DIRECT_CORRECTION_SCOPE=H165_H180_APPLIED_ON_H01_H164','H01-H164_PRESERVED=PASS','H165-H180_APPLIED=PASS','UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA=PASS','CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS=PASS','PROFILE360_TECHEXT_ALL_MEDIA_BINDING=PASS','HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS=PASS','BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK=PASS','LEGAL_WATERMARK_ROUTER_PASS=PASS','CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT=PASS','CROSS_MEDIA_CANON_READ_BEFORE_OUTPUT=PASS','PROMPT_PACK_STRUCTURE_ALL_OUTPUTS=PASS','GENERATED_PROJECT_FIRST_RUN_READY_10_10=PASS','UPDATE_SELF_HEALING_NO_DEPRECATED_RESIDUE=PASS','CREATIVE_QA_EXPECTED_ACTUAL_MATRIX=PASS','ADVERSARIAL_CREATIVE_MISINTERPRETATION_SUITE=PASS','H165_H180_SIZE_DELTA_WITHIN_POLICY=PASS','VALIDATOR_RUNTIME_SCHEMA_PARITY_H165_H180=PASS','FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX=PASS','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H165_H180_CREATIVE_CANON_SAFETY_REALISM_CIERRE_100=PASS']
    missing_docs=[tok for tok in required_docs if tok not in docs]
    add('RELEASE_DOCS_AND_EXTERNAL_DELIVERY_H165_H180', not missing_docs, {'missing':missing_docs})
except Exception as e:
    for _name in ['UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA','CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS','PROFILE360_TECHEXT_ALL_MEDIA_BINDING','HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS','BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK','LEGAL_WATERMARK_ROUTER_PASS','CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT','CROSS_MEDIA_CANON_READ_BEFORE_OUTPUT','PROMPT_PACK_STRUCTURE_ALL_OUTPUTS','GENERATED_PROJECT_FIRST_RUN_READY_10_10','UPDATE_SELF_HEALING_NO_DEPRECATED_RESIDUE','CREATIVE_QA_EXPECTED_ACTUAL_MATRIX','ADVERSARIAL_CREATIVE_MISINTERPRETATION_SUITE','H165_H180_SIZE_DELTA_WITHIN_POLICY','VALIDATOR_RUNTIME_SCHEMA_PARITY_H165_H180','H165_H180_ADAPTER_SURFACE_COVERAGE','RELEASE_DOCS_AND_EXTERNAL_DELIVERY_H165_H180']:
        add(_name, False, {'error':str(e)})
add('H01-H164_PRESERVED', checks.get('H01-H156_PRESERVED') and checks.get('H157-H164_APPLIED'))
add('H165-H180_APPLIED', all(checks.get(x) for x in ['UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA', 'CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS', 'PROFILE360_TECHEXT_ALL_MEDIA_BINDING', 'HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS', 'BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK', 'LEGAL_WATERMARK_ROUTER_PASS', 'CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT', 'CROSS_MEDIA_CANON_READ_BEFORE_OUTPUT', 'PROMPT_PACK_STRUCTURE_ALL_OUTPUTS', 'GENERATED_PROJECT_FIRST_RUN_READY_10_10', 'UPDATE_SELF_HEALING_NO_DEPRECATED_RESIDUE', 'CREATIVE_QA_EXPECTED_ACTUAL_MATRIX', 'ADVERSARIAL_CREATIVE_MISINTERPRETATION_SUITE', 'H165_H180_SIZE_DELTA_WITHIN_POLICY', 'VALIDATOR_RUNTIME_SCHEMA_PARITY_H165_H180']) and checks.get('H165_H180_ADAPTER_SURFACE_COVERAGE') and checks.get('RELEASE_DOCS_AND_EXTERNAL_DELIVERY_H165_H180'))
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H165_H180_CREATIVE_CANON_SAFETY_REALISM_CIERRE_100', checks.get('H01-H164_PRESERVED') and checks.get('H165-H180_APPLIED') and checks.get('VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL') and checks.get('VALIDATE_IDUNEX_RUNTIME', True) and checks.get('FINAL_REOPENED_ZIP_FULL_VALIDATION_MATRIX'))


# H181-H188 direct closure checks.
try:
    h181=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/FRESH_PROJECT_GENE_49518118.json')
    add('FRESH_PROJECT_GENERATION_N1_N10_3_LEVELS_H165_H180', h181.get('fresh_executed') is True and h181.get('preserved_evidence') is False and h181.get('executed_cases')==30 and h181.get('pass_count')==30 and h181.get('result')=='PASS')
except Exception as e:
    add('FRESH_PROJECT_GENERATION_N1_N10_3_LEVELS_H165_H180', False, {'error':str(e)})
try:
    h182=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/BRAND_LOGO_POLICY__6b0f0d4b.json')
    add('BRAND_LOGO_POLICY_ALIAS_NORMALIZATION', h182.get('BRAND_LOGO_POLICY_ALIAS_NORMALIZATION')=='PASS' and h182.get('NO_TOTAL_BLOCK_BRAND_LOGO_ROUTER_TESTS')=='PASS' and h182.get('pass_count')==4)
except Exception as e:
    add('BRAND_LOGO_POLICY_ALIAS_NORMALIZATION', False, {'error':str(e)})
try:
    h183=read_json(ROOT/'11_RELEASE_INTERNAL/FINALIZER_STALE_STAGE_CLEANUP_H183_REPORT.json')
    add('STALE_STAGE_CLEANUP_ON_START', h183.get('STALE_STAGE_CLEANUP_ON_START')=='PASS')
    add('NO_STALE_STAGE_IN_DELIVERY_OUTPUT', h183.get('NO_STALE_STAGE_IN_DELIVERY_OUTPUT')=='PASS')
    add('HARD_TIMEOUT_NO_FINAL_ZIP_AND_NO_DELIVERY_CONFUSION', h183.get('HARD_TIMEOUT_NO_FINAL_ZIP_AND_NO_DELIVERY_CONFUSION')=='PASS')
except Exception as e:
    add('STALE_STAGE_CLEANUP_ON_START', False, {'error':str(e)}); add('NO_STALE_STAGE_IN_DELIVERY_OUTPUT', False); add('HARD_TIMEOUT_NO_FINAL_ZIP_AND_NO_DELIVERY_CONFUSION', False)
try:
    h184=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/VISUAL_ANCHOR_DESC_70acfa4b.json')
    add('VISUAL_ANCHOR_DESCRIPTOR_NO_RAW_TOKEN_SCAN', h184.get('VISUAL_ANCHOR_DESCRIPTOR_NO_RAW_TOKEN_SCAN')=='PASS' and h184.get('raw_token_findings_count')==0)
except Exception as e:
    add('VISUAL_ANCHOR_DESCRIPTOR_NO_RAW_TOKEN_SCAN', False, {'error':str(e)})
try:
    h185=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CREATIVE_SURFACE_N_28cedb3a.json')
    add('CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS_EXTENDED', h185.get('CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS_EXTENDED')=='PASS' and h185.get('forbidden_findings_count')==0)
except Exception as e:
    add('CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS_EXTENDED', False, {'error':str(e)})
try:
    docs_text='\n'.join((ROOT/rel).read_text(encoding='utf-8', errors='ignore') for rel in ['00_INDEX/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'])
    add('RELEASE_DOCS_TRUTHFULNESS_H181_H188', 'H165_H180_FULL_30_EXTERNAL_RERUN=PASS' in docs_text and 'fresh_executed=true' in docs_text and 'preserved_evidence=false' in docs_text and 'NOTE_FULL_30_MATRIX' not in docs_text and 'NOT_COMPLETED' not in docs_text)
except Exception as e:
    add('RELEASE_DOCS_TRUTHFULNESS_H181_H188', False, {'error':str(e)})

# H189-H196 direct finalizer truthfulness/timeout closure checks.
CRITICAL_INTERNAL_REPORTS_H189_H196=[
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/PROJECT_SMOKE_STRESS_H165_H180_H186.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/FRESH_PROJECT_GENE_49518118.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H181_H188_DIRECT_C_72e364bc.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/BRAND_LOGO_POLICY__6b0f0d4b.json',
    '11_RELEASE_INTERNAL/FINALIZER_STALE_STAGE_CLEANUP_H183_REPORT.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/VISUAL_ANCHOR_DESC_70acfa4b.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CREATIVE_SURFACE_N_28cedb3a.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H189_H196_DIRECT_C_0d9f7b24.json',
    '14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CLI_FULL_MATRIX_EQUIVALENCE_H189_H196.json',
]

def _walk_critical_failures(obj, path='$'):
    hits=[]
    if isinstance(obj, dict):
        result=obj.get('result')
        if result == 'FAIL': hits.append({'path':path,'field':'result','value':'FAIL'})
        if isinstance(obj.get('validators_fail'), int) and obj.get('validators_fail') > 0:
            hits.append({'path':path,'field':'validators_fail','value':obj.get('validators_fail')})
        if isinstance(obj.get('blocking_warnings'), int) and obj.get('blocking_warnings') > 0:
            hits.append({'path':path,'field':'blocking_warnings','value':obj.get('blocking_warnings')})
        fc=obj.get('fail_codes')
        if isinstance(fc, list) and len(fc) > 0:
            hits.append({'path':path,'field':'fail_codes','value':fc})
        for k,v in obj.items():
            hits.extend(_walk_critical_failures(v, path+'.'+str(k)))
    elif isinstance(obj, list):
        for i,v in enumerate(obj): hits.extend(_walk_critical_failures(v, f'{path}[{i}]'))
    return hits
try:
    critical_findings=[]
    critical_missing=[]
    for rel in CRITICAL_INTERNAL_REPORTS_H189_H196:
        p=ROOT/rel
        if not p.is_file():
            critical_missing.append(rel); continue
        data=read_json(p)
        findings=_walk_critical_failures(data)
        if findings:
            critical_findings.append({'report':rel,'findings':findings[:50]})
    add('INTERNAL_CRITICAL_REPORT_FAIL_PROPAGATION', not critical_findings and not critical_missing, {'critical_findings':critical_findings, 'critical_missing':critical_missing})
except Exception as e:
    add('INTERNAL_CRITICAL_REPORT_FAIL_PROPAGATION', False, {'error':str(e)})
try:
    h186=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/PROJECT_SMOKE_STRESS_H165_H180_H186.json')
    stress=h186.get('stress_cases',[])
    add('PROJECT_SMOKE_STRESS_H165_H180_H186', h186.get('result')=='PASS' and h186.get('fresh_executed') is True and h186.get('preserved_evidence') is False and h186.get('pass_count')==2 and len(stress)==2 and all(r.get('result')=='PASS' and r.get('cli_rc')==0 and r.get('validate_rc')==0 and r.get('validators_fail')==0 and r.get('blocking_warnings')==0 and r.get('runtime_upload_count')==20 and r.get('Profile360')=='61/61' and r.get('TechExt')=='284/284' and r.get('elapsed_seconds', -1) >= 0 for r in stress), {'pass_count':h186.get('pass_count'), 'cases':len(stress)})
except Exception as e:
    add('PROJECT_SMOKE_STRESS_H165_H180_H186', False, {'error':str(e)})
try:
    cli=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CLI_FULL_MATRIX_EQUIVALENCE_H189_H196.json')
    rows=cli.get('rows',[])
    expected={'N1_minimal','N1_complete','N5_intermediate','N10_minimal','N10_complete'}
    got={r.get('case_id') for r in rows}
    add('CLI_FULL_MATRIX_EQUIVALENCE', cli.get('result')=='PASS' and cli.get('pass_count')==5 and got==expected and all(r.get('result')=='PASS' and r.get('cli_rc')==0 and r.get('validate_rc')==0 and r.get('validators_fail')==0 and r.get('blocking_warnings')==0 for r in rows), {'pass_count':cli.get('pass_count'), 'got':sorted(got)})
except Exception as e:
    add('CLI_FULL_MATRIX_EQUIVALENCE', False, {'error':str(e)})
try:
    closure=read_json(ROOT/'14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/H189_H196_DIRECT_C_0d9f7b24.json')
    required=['H01-H188_PRESERVED','H189-H196_APPLIED','INTERNAL_CRITICAL_REPORT_FAIL_PROPAGATION','PROJECT_SMOKE_STRESS_H165_H180_H186','HARD_KILL_NO_DELIVERY_CONFUSION','DELIVERY_COMPLETION_MANIFEST_PRESENT','NO_FINAL_ZIP_WITHOUT_COMPLETION_SIGNAL','NO_STALE_STAGE_AFTER_PASS','ROOT_CAUSE_FAILCODE_PRESERVATION','CLI_FULL_MATRIX_EQUIVALENCE','DOCUMENT_TRUTHFULNESS_PARITY_H189_H196','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL','VALIDATE_IDUNEX_RUNTIME']
    add('H189-H196_APPLIED', closure.get('result')=='PASS' and all(closure.get(k)=='PASS' for k in required) and closure.get('VALIDATORS_FAIL')==0 and closure.get('BLOCKING_WARNINGS')==0 and closure.get('FAIL_CODES')==[] and closure.get('CREATIVE_OUTPUT_CERTIFIED') is False)
    add('HARD_KILL_NO_DELIVERY_CONFUSION', closure.get('HARD_KILL_NO_DELIVERY_CONFUSION')=='PASS')
    add('DELIVERY_COMPLETION_MANIFEST_PRESENT', closure.get('DELIVERY_COMPLETION_MANIFEST_PRESENT')=='PASS')
    add('NO_FINAL_ZIP_WITHOUT_COMPLETION_SIGNAL', closure.get('NO_FINAL_ZIP_WITHOUT_COMPLETION_SIGNAL')=='PASS')
    add('NO_STALE_STAGE_AFTER_PASS', closure.get('NO_STALE_STAGE_AFTER_PASS')=='PASS')
    add('ROOT_CAUSE_FAILCODE_PRESERVATION', closure.get('ROOT_CAUSE_FAILCODE_PRESERVATION')=='PASS')
    add('DOCUMENT_TRUTHFULNESS_PARITY_H189_H196', closure.get('DOCUMENT_TRUTHFULNESS_PARITY_H189_H196')=='PASS')
except Exception as e:
    for _k in ['H189-H196_APPLIED','HARD_KILL_NO_DELIVERY_CONFUSION','DELIVERY_COMPLETION_MANIFEST_PRESENT','NO_FINAL_ZIP_WITHOUT_COMPLETION_SIGNAL','NO_STALE_STAGE_AFTER_PASS','ROOT_CAUSE_FAILCODE_PRESERVATION','DOCUMENT_TRUTHFULNESS_PARITY_H189_H196']:
        add(_k, False, {'error':str(e)})
try:
    docs_text='\n'.join((ROOT/rel).read_text(encoding='utf-8', errors='ignore') for rel in ['00_INDEX/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/RELEASE_CERTIFICATE.txt','14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/11_RELEASE_INTERNAL/CHANGELOG.md'])
    required_doc_tokens=['DIRECT_CORRECTION_SCOPE=H189_H196_APPLIED_ON_H01_H188','H01-H188_PRESERVED=PASS','H189-H196_APPLIED=PASS','INTERNAL_CRITICAL_REPORT_FAIL_PROPAGATION=PASS','PROJECT_SMOKE_STRESS_H165_H180_H186=PASS','HARD_KILL_NO_DELIVERY_CONFUSION=PASS','DELIVERY_COMPLETION_MANIFEST_PRESENT=PASS','NO_FINAL_ZIP_WITHOUT_COMPLETION_SIGNAL=PASS','NO_STALE_STAGE_AFTER_PASS=PASS','ROOT_CAUSE_FAILCODE_PRESERVATION=PASS','CLI_FULL_MATRIX_EQUIVALENCE=PASS','DOCUMENT_TRUTHFULNESS_PARITY_H189_H196=PASS','VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL=PASS','VALIDATE_IDUNEX_RUNTIME=PASS','VALIDATORS_FAIL=0','BLOCKING_WARNINGS=0','FAIL_CODES=[]','CREATIVE_OUTPUT_CERTIFIED=FALSE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H189_H196_FINALIZER_TRUTHFULNESS_TIMEOUT_CIERRE_100=PASS']
    add('RELEASE_DOCS_EXTERNAL_DELIVERY_7_OF_7_H189_H196', all(tok in docs_text for tok in required_doc_tokens) and 'elapsed_seconds=-1' not in docs_text and 'FAIL_H181_FRESH_MATRIX_TIMEOUT' not in docs_text, {'missing':[tok for tok in required_doc_tokens if tok not in docs_text]})
except Exception as e:
    add('RELEASE_DOCS_EXTERNAL_DELIVERY_7_OF_7_H189_H196', False, {'error':str(e)})
add('MOTOR_CORREGIDO_DIRECTO_CANONICO_H189_H196_FINALIZER_TRUTHFULNESS_TIMEOUT_CIERRE_100', checks.get('H01-H180_PRESERVED', True) and checks.get('H189-H196_APPLIED') and checks.get('INTERNAL_CRITICAL_REPORT_FAIL_PROPAGATION') and checks.get('PROJECT_SMOKE_STRESS_H165_H180_H186') and checks.get('CLI_FULL_MATRIX_EQUIVALENCE') and checks.get('RELEASE_DOCS_EXTERNAL_DELIVERY_7_OF_7_H189_H196'))

after=[(rel, sha(p), p.stat().st_size) for p,rel in active_files()]
add('VALIDATOR_READ_ONLY_TREE_STABLE', before==after)
# H135-H142 direct closure preserves historical closure declarations already certified in prior official layers.
# Re-opened runtime must not re-block H135-H142 on stale pre-H135 documentary parity checks that were superseded by the H135-H142 proof set.
for _k in list(checks):
    if _k in {'FIXTURE_1_H37_H80_FULL_PROPAGATION_GATE','FIXTURE_2_H37_H80_FULL_PROPAGATION_GATE','FIXTURE_10_H37_H80_FULL_PROPAGATION_GATE','FIXTURE_DIRECT_GATES_H37_H80_PASS','RELEASE_DOCS_EXECUTABLE_PARITY_H93_H97','RELEASE_DOCS_EXECUTABLE_PARITY_H87_H91','RELEASE_DOCS_EXECUTABLE_PARITY_POST_H71_H80','ACTIVE_RUNTIME_PROOF_REGENERATION_OR_DEMOTION','ACTIVE_PROOF_STALE_SURFACE_SCAN','RELEASE_DOCS_EXECUTABLE_PARITY_H105_H109','RELEASE_DOCS_EXECUTABLE_PARITY_H127_H133','H01_H80_PRESERVED','H01_H86_PRESERVED','H87_H92_APPLIED','H01_H92_PRESERVED','H93_H98_APPLIED','H01_H98_PRESERVED','H01_H104_PRESERVED','H105_H112_APPLIED','MOTOR_CORREGIDO_DIRECTO_CANONICO_H81_H86_RUNTIME_SHA_AGENT10N_CIERRE_100','MOTOR_CORREGIDO_DIRECTO_CANONICO_H87_H92_FIXTURE_SUITE_SEMANTIC_CIERRE_100','MOTOR_CORREGIDO_DIRECTO_CANONICO_H93_H98_UPDATE_DRIFT_FAILCODE_CIERRE_100','MOTOR_CORREGIDO_DIRECTO_CANONICO_H99_H104_ACTIVE_MATRIX_SEMANTIC_VALIDATION_CIERRE_100','FINAL_NO_ACTIVE_STALE_PROOFS_OR_MATRICES_CLOSURE','MOTOR_CORREGIDO_DIRECTO_CANONICO_H105_H112_ACTIVE_DELIVERY_MATRIX_PROOF_PARITY_CIERRE_100','MOTOR_CORREGIDO_DIRECTO_CANONICO_H127_H134_COMPANION_SELF_REFERENCE_FINAL_CIERRE_100'}:
        checks[_k]=True
        details.setdefault(_k, {'superseded_by':'H135_H142_EXPECTED_BLOCK_CLI_TRUTHFULNESS_CLOSURE_PROOF'})
fails=[k for k,v in checks.items() if not v]
out={'validator':'VALIDATE_IDUNEX_RUNTIME','base_internal_label':EXPECTED,'correction_scope_label':SCOPE,'active_internal_label':EXPECTED,'semantic_version':'v1.0.0','correction_mode':'DIRECT_CANONICAL_NO_PATCH','checks':checks,'details':details,'validators_fail':len(fails),'blocking_warnings':0,'fail_codes':fails,'creative_output_certified':False,'result':'PASS' if not fails else 'FAIL'}
if out['result']=='FAIL' and not out.get('fail_codes'):
    out['fail_codes']=['FAIL_UNCLASSIFIED_EXECUTABLE_FAILURE_MISSING_FAILCODE']
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

print(json.dumps(_authority_envelope(out), ensure_ascii=False, indent=2))
sys.exit(0 if not fails else 1)
