#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys, json, re
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[2]
REQUIRED_TOKENS = [
 'external_validation_required','EDITABLE_FIELDS_FOR_CUSTOM_PROJECTS','TEMPLATE_REQUIRED_FIELDS','DO_NOT_EXECUTE_TEMPLATE_WITH_PLACEHOLDERS','GENERIC_SKELETON_NON_AUTHORITY','PROJECT_FILENAME_CANON','PROJECT_NAME_SLUG','PROJECT_UID','PROJECT_OUTPUT_CONTRACT','PROJECT_STATUS_CONTRACT','PROJECT_EXTERNAL_VALIDATION_REQUIRED','PROJECT_TEMPLATE_FILL_VALIDATOR','PROJECT_NO_PLACEHOLDER_EXECUTION_GATE'
]
REQUIRED_PATHS = [
 '03_PROJECT_FACTORY/04_DELIVERY_GATES/PROJECT_NO_PLACEHOLDER_EXECUTION_GATE.json',
 '03_PROJECT_FACTORY/04_DELIVERY_GATES/GENERIC_SKELETON_NON_AUTHORITY_GATE.json',
 '03_PROJECT_FACTORY/09_H281_H310_PRO_ba690755/PROJECT_FILENAME_CANON.json',
 '03_PROJECT_FACTORY/09_H281_H310_PRO_ba690755/PROJECT_STATUS_CONTRACT.json',
 '03_PROJECT_FACTORY/09_H281_H310_PRO_ba690755/PROJECT_TEMPLATE_FILL_VALIDATOR.json',
 '03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'
]

def _active_version_v1_0_0_guard(root: Path):
    failures=[]
    text_exts={'.json','.md','.txt','.csv','.sh','.py'}
    legacy_semver='v1.' + '1.0'
    for p in sorted(root.rglob('*')):
        if not p.is_file() or p.suffix.lower() not in text_exts:
            continue
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/')):
            continue
        tx=p.read_text(encoding='utf-8', errors='ignore')
        if legacy_semver in tx:
            failures.append({'fail_code':'FAIL_ACTIVE_LEGACY_SEMVER_LITERAL_REMAINS','path':rel})
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root).as_posix()
        if rel.startswith(('14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/')):
            continue
        if legacy_semver in rel:
            failures.append({'fail_code':'FAIL_ACTIVE_LEGACY_SEMVER_PATH_REMAINS','path':rel})
    required=root/'12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json'
    if required.is_file():
        tx=required.read_text(encoding='utf-8', errors='ignore')
        for needle in ['IDUNEX_MOTOR_v1.0.0.zip','IDUNEX_MOTOR_v1.0.0.zip.sha256','IDUNEX_MOTOR_v1.0.0_RELEASE_CERTIFICATE.txt']:
            if needle not in tx:
                failures.append({'fail_code':'FAIL_ENGINE_OUTPUT_CONTRACT_V1_0_0_ARTIFACT_MISSING','path':'12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json','needle':needle})
        legacy_zip='IDUNEX_MOTOR_' + legacy_semver + '.zip'
        if legacy_zip in tx:
            failures.append({'fail_code':'FAIL_ENGINE_OUTPUT_CONTRACT_ACTIVE_LEGACY_ARTIFACT','path':'12_OUTPUT_CONTRACTS/ENGINE_OUTPUT_CONTRACT.json'})
    return failures

fail=[]
fail.extend(_active_version_v1_0_0_guard(ROOT))
missing_paths=[p for p in REQUIRED_PATHS if not (ROOT/p).is_file()]
if missing_paths: fail.append({'fail_code':'FAIL_PROMPTS_PROJECT_POLICY_PATH_MISSING','detail':missing_paths})
texts=[]
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.json','.txt','.py','.csv','.sh'}:
        texts.append(p.read_text(encoding='utf-8', errors='ignore'))
corpus='\n'.join(texts)
missing_tokens=[t for t in REQUIRED_TOKENS if t not in corpus]
if missing_tokens: fail.append({'fail_code':'FAIL_PROMPTS_PROJECT_POLICY_TOKEN_MISSING','detail':missing_tokens})
factory=(ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').read_text(encoding='utf-8', errors='ignore') if (ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').is_file() else ''
for needle in ['_project_policy_canonical_identity','PROJECT_NO_PLACEHOLDER_EXECUTION_GATE','GENERIC_SKELETON_NON_AUTHORITY','PROJECT_UID','project_filename_canon','logo_asset_policy']:
    if needle not in factory:
        fail.append({'fail_code':'FAIL_FACTORY_POLICY_LOGIC_MISSING','detail':needle})
out={'validator':'VALIDATE_PROMPTS_PROJECT_POLICY','semantic_version':'v1.0.0','result':'PASS' if not fail else 'FAIL','VALIDATORS_FAIL':len(fail),'BLOCKING_WARNINGS':0,'FAIL_CODES':[f.get('fail_code','FAIL_PROMPTS_PROJECT_POLICY') for f in fail],'failures':fail,'CREATIVE_OUTPUT_CERTIFIED':False}
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
