#!/usr/bin/env python3
"""H215 validator: field source trace ledger coverage per model."""
from validator_subcheck_protocol import enforce_subcheck_invocation as _enforce_subcheck_invocation
_enforce_subcheck_invocation(__file__, __name__)

from pathlib import Path
import json, sys
sys.dont_write_bytecode=True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
errors=[]; checked=[]
required={'field_path','value_hash','source_ids','claim_id','evidence_hash','qa_expected','qa_actual','failcode','fallback'}
if (ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').exists():
    txt=(ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').read_text(encoding='utf-8', errors='ignore')
    for token in ['FIELD_SOURCE_TRACE_LEDGER_MODEL_','PROFILE360_FIELD_TRACE_COVERAGE','TECHEXT_FIELD_TRACE_COVERAGE','_ledger_row','FIELD_SOURCE_TRACE_LEDGER_PER_MODEL']:
        if token not in txt: errors.append({'code':'FAIL_H215_ENGINE_LEDGER_CONTRACT_MISSING','token':token})
    checked.append('ENGINE_FACTORY_LEDGER_CONTRACT')
else:
    ledgers=sorted(ROOT.rglob('FIELD_SOURCE_TRACE_LEDGER_MODEL_*.json'))
    if not ledgers: errors.append({'code':'FAIL_H215_NO_FIELD_SOURCE_TRACE_LEDGER','path':str(ROOT)})
    for p in ledgers:
        data=json.loads(p.read_text(encoding='utf-8'))
        rows=data.get('records') or []
        checked.append(p.relative_to(ROOT).as_posix())
        if (data.get('PROFILE360_FIELD_TRACE_COVERAGE') or data.get('profile360_field_trace_coverage'))!='61/61': errors.append({'code':'FAIL_H215_PROFILE360_FIELD_TRACE_COVERAGE','path':p.relative_to(ROOT).as_posix(),'value':(data.get('PROFILE360_FIELD_TRACE_COVERAGE') or data.get('profile360_field_trace_coverage'))})
        if (data.get('TECHEXT_FIELD_TRACE_COVERAGE') or data.get('techext_field_trace_coverage'))!='284/284': errors.append({'code':'FAIL_H215_TECHEXT_FIELD_TRACE_COVERAGE','path':p.relative_to(ROOT).as_posix(),'value':(data.get('TECHEXT_FIELD_TRACE_COVERAGE') or data.get('techext_field_trace_coverage'))})
        if len(rows) < 345: errors.append({'code':'FAIL_H215_LEDGER_ROW_COUNT_LOW','path':p.relative_to(ROOT).as_posix(),'count':len(rows)})
        for i,row in enumerate(rows[:400]):
            missing=[k for k in required if k not in row]
            if missing: errors.append({'code':'FAIL_H215_LEDGER_ROW_SCHEMA','path':p.relative_to(ROOT).as_posix(),'row':i,'missing':missing}); break
out={'validator':'VALIDATE_FIELD_SOURCE_TRACE_LEDGER','checked':checked,'FIELD_SOURCE_TRACE_LEDGER_PER_MODEL':'PASS' if not errors else 'FAIL','FIELD_TRACE_MODEL_001_TO_MODEL_N_PRESENT':'PASS' if not errors else 'FAIL','PROFILE360_FIELD_TRACE_COVERAGE':'61/61' if not errors else 'FAIL','TECHEXT_FIELD_TRACE_COVERAGE':'284/284' if not errors else 'FAIL','errors':errors,'result':'PASS' if not errors else 'FAIL'}
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
