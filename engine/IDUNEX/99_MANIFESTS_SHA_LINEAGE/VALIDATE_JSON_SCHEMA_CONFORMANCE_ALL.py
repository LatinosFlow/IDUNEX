#!/usr/bin/env python3
"""Strict JSON and schema conformance validator for IDUNEX P034."""
from validator_subcheck_protocol import enforce_subcheck_invocation as _enforce_subcheck_invocation
_enforce_subcheck_invocation(__file__, __name__)

import json, sys, re
from pathlib import Path
sys.dont_write_bytecode = True
H165_H180_VALIDATOR_RUNTIME_SCHEMA_PARITY='PASS'
try:
    import jsonschema
except Exception:
    jsonschema = None
ROOT=Path(__file__).resolve().parents[1]
bad=[]; total=0; schema_checked=0; schema_invalid=[]

def fail(path, code, err):
    bad.append({'path':str(path.relative_to(ROOT)),'code':code,'error':str(err)})

def walk_bad_values(obj, path='$', key=None, parent=None):
    out=[]
    if obj is None:
        code='FAIL_H143_ACTIVE_JSON_NULL_VALUE'
        if key=='block_fail_code' and isinstance(parent,dict) and parent.get('human_readable_result')=='DELIVERY_PASS' and parent.get('expected_block') is False:
            code='FAIL_H143_BLOCK_FAIL_CODE_NULL_ON_DELIVERY_PASS'
        return [{'path':path,'code':code}]
    if isinstance(obj,str) and obj.strip()=='' :
        return [{'path':path,'code':'FAIL_H143_ACTIVE_JSON_BLANK_VALUE'}]
    if isinstance(obj,dict):
        for k,v in obj.items(): out.extend(walk_bad_values(v,path+'.'+str(k),k,obj))
    elif isinstance(obj,list):
        for i,v in enumerate(obj): out.extend(walk_bad_values(v,f'{path}[{i}]',None,obj))
    return out
for p in ROOT.rglob('*.json'):
    rel0=p.relative_to(ROOT).as_posix()
    if any(skip in rel0 for skip in ['12_HISTORICAL_NON_AUTHORITY/','14_HISTORICAL_NON_AUTHORITY/','12_HISTORICAL_NON_AUTHORITY/','14_HISTORICAL_NON_AUTHORITY/','UNIVERSAL_FIXTURES/','P034/','LEGACY_REPORTS/']):
        continue
    total+=1
    try:
        data=json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        fail(p,'FAIL_JSON_INVALID',e); continue
    # Active JSON data must not contain unresolved JSON null values; schema language "null" strings are allowed.
    active_nulls=walk_bad_values(data)
    if active_nulls:
        for item in active_nulls[:50]:
            fail(p,item['code'],item['path'])
    # creative_output_certified is always an explicit boolean in active proofs/runtime outputs, never null.
    def _creative_values(obj, pointer='$'):
        out=[]
        if isinstance(obj,dict):
            for k,v in obj.items():
                if k=='creative_output_certified': out.append((pointer+'.'+k,v))
                out.extend(_creative_values(v,pointer+'.'+str(k)))
        elif isinstance(obj,list):
            for i,v in enumerate(obj): out.extend(_creative_values(v,f'{pointer}[{i}]'))
        return out
    for ptr,val in _creative_values(data):
        if val is None:
            fail(p,'FAIL_CREATIVE_OUTPUT_CERTIFIED_NULL',ptr)
    # Structural contracts for every JSON schema document.
    if isinstance(data,dict) and (data.get('$schema') or 'schema' in p.name.lower() or p.name.endswith('_SCHEMA.json')):
        schema_checked+=1
        if jsonschema:
            try: jsonschema.Draft202012Validator.check_schema(data)
            except Exception as e:
                schema_invalid.append({'path':p.relative_to(ROOT).as_posix(),'error':str(e)})
        if data.get('type')=='object':
            props=set((data.get('properties') or {}).keys()); req=set(data.get('required') or [])
            if not req.issubset(props): schema_invalid.append({'path':p.relative_to(ROOT).as_posix(),'error':'required not subset of properties'})
    # Known strict content schemas.
    rel=p.relative_to(ROOT).as_posix()
    if rel.endswith('PROFILE360_CANONICAL_REGISTRY_00_60.json'):
        if data.get('section_count') not in (None,61) or len(data.get('sections',[]))!=61:
            fail(p,'FAIL_PROFILE_SCHEMA_STRICT','Profile360 must expose 61 sections')
    if rel.endswith('TECHEXT_FULL10_OFFICIAL_FIELD_REGISTRY.json'):
        fields=data.get('fields',[])
        if len(fields)!=284: fail(p,'FAIL_TECHEXT_SCHEMA_STRICT','TechExt must expose 284 fields')
        for row in fields:
            if row.get('data_type') not in {'string','number','numeric_band','number_or_numeric_band','array','integer'}: fail(p,'FAIL_TECHEXT_SCHEMA_STRICT',f"bad data_type {row.get('field_id')}")
            if row.get('value_class') not in {'MODEL_SPECIFIC_REQUIRED','MODEL_SPECIFIC_DERIVED','SHARED_POLICY_ALLOWED','PROJECT_SHARED_CONTEXT','NOT_APPLICABLE_WITH_JUSTIFICATION'}: fail(p,'FAIL_TECHEXT_VALUE_CLASS',f"bad value_class {row.get('field_id')}")
    if '/02_MODELS/' in rel and rel.endswith('TECHEXT_FULL10.json'):
        for row in data.get('fields',[]):
            vt=row.get('value_type'); av=row.get('actual_value')
            ok=(vt=='string' and isinstance(av,str)) or (vt=='number' and isinstance(av,(int,float)) and not isinstance(av,bool)) or (vt=='array' and isinstance(av,list)) or (vt=='boolean' and isinstance(av,bool)) or (vt=='object' and isinstance(av,dict))
            if not ok: fail(p,'FAIL_TECHEXT_TYPE_MISMATCH',f"{row.get('field_id')} expected {vt} got {type(av).__name__}")
            if row.get('value_class') not in {'MODEL_SPECIFIC_REQUIRED','MODEL_SPECIFIC_DERIVED','SHARED_POLICY_ALLOWED','PROJECT_SHARED_CONTEXT','NOT_APPLICABLE_WITH_JUSTIFICATION'}: fail(p,'FAIL_TECHEXT_VALUE_CLASS',f"{row.get('field_id')} missing value_class")
    if '/02_MODELS/' in rel and rel.endswith('PROFILE360_FULL60.json'):
        if len(data.get('sections',[]))!=61: fail(p,'FAIL_PROFILE_SCHEMA_STRICT','Profile payload must contain 61 sections')
if schema_invalid:
    bad.extend({'path':x['path'],'code':'FAIL_JSON_SCHEMA_INVALID','error':x['error']} for x in schema_invalid)
out={'validator':'VALIDATE_JSON_SCHEMA_CONFORMANCE_ALL','json_total':total,'json_invalid':sum(1 for x in bad if x['code']=='FAIL_JSON_INVALID'),'schema_checked':schema_checked,'schema_invalid':len(schema_invalid),'strict_type_errors':sum(1 for x in bad if x['code']=='FAIL_TECHEXT_TYPE_MISMATCH'),'techext_data_type_allowed_set':['array','integer','number','number_or_numeric_band','numeric_band','string'],'errors':bad,'result':'PASS' if not bad else 'FAIL'}
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

print(json.dumps(out,ensure_ascii=False,indent=2)); sys.exit(0 if not bad else 1)
