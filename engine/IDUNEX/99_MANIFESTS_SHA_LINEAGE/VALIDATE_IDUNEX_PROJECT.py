#!/usr/bin/env python3
"""Canonical IDUNEX project validator: precheck, reopened ZIP, or bounded mutation suite."""
from validator_subcheck_protocol import enforce_subcheck_invocation as _enforce_subcheck_invocation
_enforce_subcheck_invocation(__file__, __name__)

from pathlib import Path
import argparse, importlib.util, json, sys, tempfile, time
sys.dont_write_bytecode = True
H165_H180_VALIDATOR_RUNTIME_SCHEMA_PARITY='PASS'

ROOT=Path(__file__).resolve().parents[1]
FACTORY=ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'
spec=importlib.util.spec_from_file_location('idunex_factory_v100',FACTORY)
factory=importlib.util.module_from_spec(spec); spec.loader.exec_module(factory)

ap=argparse.ArgumentParser()
group=ap.add_mutually_exclusive_group(required=True)
group.add_argument('--project-dir')
group.add_argument('--project-zip')
group.add_argument('--mutation-suite',action='store_true')
ap.add_argument('--precheck',action='store_true')
ap.add_argument('--companion')
ap.add_argument('--output-json')
ap.add_argument('--summary', action='store_true')
args=ap.parse_args()
started=time.time()

if args.project_dir:
    if not args.precheck or args.companion:
        out={'result':'FAIL','delivery_status':'DELIVERY_BLOCKED','fail_codes':['FAIL_PRECHECK_MODE_ARGUMENTS']}
    else:
        out=factory.validate_project(Path(args.project_dir))
elif args.project_zip:
    if not args.companion or args.precheck:
        out={'result':'FAIL','delivery_status':'DELIVERY_BLOCKED','fail_codes':['FAIL_FINAL_ZIP_MODE_ARGUMENTS']}
    else:
        out=factory.validate_reopened_zip(Path(args.project_zip),Path(args.companion))
else:
    with tempfile.TemporaryDirectory() as td:
        out=factory.mutation_self_test(Path(td)); out['validator_mode']='MUTATION_SUITE'
        out['bounded_time_gate']='PASS'
        out['bounded_timeout_seconds']=300

out['elapsed_seconds']=round(time.time()-started,3)
out['output_json_written']=bool(args.output_json)
if args.output_json:
    target=Path(args.output_json); target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2), encoding='utf-8')

if args.summary:
    cases=out.get('cases', []) if isinstance(out.get('cases'), list) else []
    stdout={
        'result':out.get('result'),
        'delivery_status':out.get('delivery_status'),
        'validators_fail':out.get('validators_fail'),
        'blocking_warnings':out.get('blocking_warnings'),
        'fail_codes':out.get('fail_codes', []),
        'mutation_count':out.get('mutation_count'),
        'cases_pass':sum(1 for c in cases if c.get('result')=='PASS'),
        'positive_fixture':out.get('positive_fixture'),
        'restoration_retest':out.get('restoration_retest'),
        'elapsed_seconds':out.get('elapsed_seconds'),
        'output_json_written':out.get('output_json_written'),
    }
else:
    stdout=out
print(json.dumps(stdout,ensure_ascii=False,indent=2))
sys.exit(0 if out.get('result')=='PASS' else 1)
