#!/usr/bin/env python3
"""H213 validator: strict active runtime clause schema for IDUNEX generated projects or engine contract."""
from pathlib import Path
import json, re, sys
sys.dont_write_bytecode=True
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path.cwd().resolve()
CLAUSE_RE=re.compile(r'^CLAUSE\|(?P<id>[A-Z0-9_]+)\|(?P<body>.+)\|FAIL=(?P<fail>[A-Z0-9_]+)\|FALLBACK=(?P<fallback>.+)$')
BANNED_FIXTURE_TERMS={'demo_'+'model_a','demo_'+'model_b','post_engine_'+'demo_project_slug'}
PROJECT_CANONICAL_TERMS=set()
errors=[]; clauses=[]; scanned=[]

def add(code,path,msg): errors.append({'code':code,'path':str(path),'detail':msg})

def load_project_canonical_terms(root):
    terms=set()
    for rel in ["00_PROJECT_INDEX/PROJECT_MANIFEST.json", "00_PROJECT_INDEX/PROJECT_MODEL_INDEX.json"]:
        p=root/rel
        if p.is_file():
            try: data=json.loads(p.read_text(encoding="utf-8"))
            except Exception: continue
            for m in data.get("models", []) if isinstance(data, dict) else []:
                if isinstance(m, dict):
                    for k in ["name","model_name","display_name","model_code","code","model_id"]:
                        v=m.get(k)
                        if isinstance(v,str): terms.add(v.lower())
    return terms

def scan_lines(path, lines):
    seen={}
    for lineno,line in enumerate(lines,1):
        t=line.strip()
        if not t.startswith('CLAUSE|'):
            continue
        scanned.append(str(path))
        if t.startswith('CLAUSE|ID='):
            add('FAIL_H213_CLAUSE_ID_EQUALS_FORMAT',path,f'line {lineno}')
            continue
        m=CLAUSE_RE.match(t)
        if not m:
            add('FAIL_H213_CLAUSE_NOT_PARSEABLE',path,f'line {lineno}: {t[:160]}')
            continue
        cid=m.group('id')
        if not m.group('fail').startswith('FAIL'):
            add('FAIL_H213_FAILCODE_INVALID',path,f'line {lineno}: {cid}')
        if not m.group('fallback'):
            add('FAIL_H213_FALLBACK_MISSING',path,f'line {lineno}: {cid}')
        low=t.lower()
        for term in BANNED_FIXTURE_TERMS:
            if term in low and term not in PROJECT_CANONICAL_TERMS:
                add('FAIL_H213_FIXTURE_DEPENDENT_CLAUSE',path,f'line {lineno}: {cid}')
        prior=seen.get(cid)
        if prior and prior!=t:
            add('FAIL_H213_DUPLICATE_CONFLICTING_CLAUSE',path,f'line {lineno}: {cid}')
        seen[cid]=t
        clauses.append({'id':cid,'path':str(path),'line':lineno})

def project_scan(root):
    for p in root.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.md','.txt'}:
            rel=p.relative_to(root).as_posix()
            if any(x in rel for x in ['12_HISTORICAL_NON_AUTHORITY/','UNIVERSAL_FIXTURES/']):
                continue
            try: scan_lines(rel, p.read_text(encoding='utf-8', errors='ignore').splitlines())
            except Exception as e: add('FAIL_H213_READ_ERROR',rel,str(e))

def engine_scan(root):
    factory=root/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'
    txt=factory.read_text(encoding='utf-8', errors='ignore') if factory.is_file() else ''
    for token in ['VISUAL_CLAUSES','FAIL_H234_FIRST_VISUAL_ROUTING_BLOCKED','DO_NOT_REQUEST_IMAGE_FOR_FICTIONAL_MODEL','STRICT_CLAUSE_RE']:
        if token not in txt: add('FAIL_H213_ENGINE_CONTRACT_MISSING',factory.as_posix(),token)
    for raw in re.findall(r"'([A-Z0-9_]+\|[^']+?\|FAIL=[A-Z0-9_]+\|FALLBACK=[A-Z0-9_]+)'", txt):
        scan_lines('ENGINE_VISUAL_CLAUSES',[f'CLAUSE|{raw}'])

if (ROOT/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py').exists(): engine_scan(ROOT)
else:
    PROJECT_CANONICAL_TERMS.update(load_project_canonical_terms(ROOT))
    project_scan(ROOT)
out={'validator':'VALIDATE_AGENT_RUNTIME_MARKDOWN_STRICT','root':str(ROOT),'clauses_checked':len(clauses),'bad_runtime_clauses':len(errors),'CLAUSE_FAIL_FALLBACK_COVERAGE':'100%' if not errors and clauses else '0%','AGENT_RUNTIME_MARKDOWN_STRICT_CLAUSE_SCHEMA':'PASS' if not errors and clauses else 'FAIL','errors':errors,'result':'PASS' if not errors and clauses else 'FAIL'}
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

print(json.dumps(out, ensure_ascii=False, indent=2)); sys.exit(0 if out['result']=='PASS' else 1)
