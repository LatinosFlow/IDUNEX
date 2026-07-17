#!/usr/bin/env python3
"""H225 validator: prompt pack A-J coverage with mandatory Negative/QC/Fallback sections."""
from validator_subcheck_protocol import enforce_subcheck_invocation as _enforce_subcheck_invocation
_enforce_subcheck_invocation(__file__, __name__)

from pathlib import Path
import json, sys
sys.dont_write_bytecode=True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
SECTIONS=['A_HEADER','B_SCENE','C_COMPOSITION','D_LIGHTING','E_WARDROBE_PROPS','F_CAMERA_TECH','G_NEGATIVE_AVOID','H_PARAMS','I_QC_CHECKLIST_PASS_FAIL','J_FALLBACK_FIXES']
errors=[]; checked=[]
if (ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').exists():
    txt=(ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').read_text(encoding='utf-8', errors='ignore')
    checked.append('ENGINE_FACTORY_PROMPT_PACK_TEMPLATE')
    for s in SECTIONS:
        if s not in txt: errors.append({'code':'FAIL_H225_ENGINE_PROMPT_SECTION_MISSING','section':s})
    for s in ['G_NEGATIVE_AVOID','I_QC_CHECKLIST_PASS_FAIL','J_FALLBACK_FIXES']:
        if s not in txt: errors.append({'code':'FAIL_H225_MANDATORY_SECTION_MISSING','section':s})
else:
    packs=list(ROOT.rglob('PROMPT_PACK_TEMPLATE_*.md'))+list(ROOT.rglob('*PROMPT_PACK*.md'))
    packs=[p for p in packs if '12_HISTORICAL_NON_AUTHORITY' not in p.as_posix()]
    if not packs: errors.append({'code':'FAIL_H225_NO_PROMPT_PACK_FOUND','path':str(ROOT)})
    for p in packs:
        txt=p.read_text(encoding='utf-8', errors='ignore')
        checked.append(p.relative_to(ROOT).as_posix())
        missing=[s for s in SECTIONS if s not in txt]
        if missing: errors.append({'code':'FAIL_H225_PROMPT_PACK_A_J_INCOMPLETE','path':p.relative_to(ROOT).as_posix(),'missing':missing})
        critical=[s for s in ['G_NEGATIVE_AVOID','I_QC_CHECKLIST_PASS_FAIL','J_FALLBACK_FIXES'] if s not in txt]
        if critical: errors.append({'code':'FAIL_H225_NEGATIVE_QC_FALLBACK_MISSING','path':p.relative_to(ROOT).as_posix(),'missing':critical})
out={'validator':'VALIDATE_PROMPT_PACK_STRUCTURE','checked':checked,'PROMPT_PACK_STRUCTURE_VALIDATOR':'PASS' if not errors else 'FAIL','PROMPT_PACK_A_J_COVERAGE':'100%' if not errors else 'FAIL','NEGATIVE_AVOID_PRESENT':'PASS' if not errors else 'FAIL','QC_CHECKLIST_PRESENT':'PASS' if not errors else 'FAIL','FALLBACK_FIXES_PRESENT':'PASS' if not errors else 'FAIL','errors':errors,'result':'PASS' if not errors else 'FAIL'}
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
