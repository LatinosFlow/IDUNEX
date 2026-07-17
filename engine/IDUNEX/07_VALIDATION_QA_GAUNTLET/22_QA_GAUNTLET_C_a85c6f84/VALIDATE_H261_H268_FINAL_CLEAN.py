#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path as _AuthorityPath
import sys as _authority_sys
_authority_root = next(parent for parent in _AuthorityPath(__file__).resolve().parents if parent.name == "IDUNEX")
_authority_sys.path.insert(0, str(_authority_root / "99_MANIFESTS_SHA_LINEAGE"))
from validator_subcheck_protocol import enforce_subcheck_invocation as _enforce_subcheck_invocation
_enforce_subcheck_invocation(__file__, __name__)

from pathlib import Path
import hashlib, json, re, sys, zipfile
from collections import defaultdict

TEXT_EXT={'.md','.txt','.json','.py','.csv'}
ALLOWED_DATE_PREFIXES=('12_HISTORICAL_NON_AUTHORITY/','11_RELEASE_INTERNAL/','99_MANIFESTS_SHA_LINEAGE/')
ALLOWED_DATE_FILES={'00_INDEX/RELEASE_CERTIFICATE.txt','00_INDEX/CHANGELOG.md'}
ACTIVE_SKIP_PREFIXES=('12_HISTORICAL_NON_AUTHORITY/',)
DUPLICATE_ALLOWLIST_SELF_FILES={
 # DUP-EXA-001 / LIN-MAN-001: active duplicate allowlist files and
 # non-self-referential internal manifest ledgers are dynamically excluded
 # from duplicate governance parity. They are validated by their own
 # lineage/truthfulness gates and must not be forced into stale allowlists.
 '99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json',
 '99_MANIFESTS_SHA_LINEAGE/EXACT_DUPLICATE_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.json',
 '07_VALIDATION_QA_GAUNTLET/14_POLICIES/EXACT_DUPLICATE_RETENTION_ALLOWLIST.md',
 '99_MANIFESTS_SHA_LINEAGE/FILE_MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/FINAL_TREE_MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/HASH_MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/MANIFEST.json',
 '99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt',
 '99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt',
}

VALIDATORS=[
 'VALIDATE_ACTIVE_SURFACE_HISTORICAL_METADATA_SCRUB',
 'VALIDATE_PROJECT_VALIDATOR_FILESCHECKED_TRUTHFULNESS',
 'VALIDATE_CANONICAL_LABEL_HARMONIZATION',
 'VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST',
 'VALIDATE_H245_H260_SINGLE_SOURCE_CANON_REFERENCE',
 'VALIDATE_ACTIVE_DATE_NEUTRALIZATION',
 'VALIDATE_MATRIX_RUNNER_STREAMING_PROGRESS_AND_RESUME',
 'VALIDATE_FINAL_CLEAN_10_10_GATE',
]

def sha(p: Path) -> str:
    h=hashlib.sha256(); h.update(p.read_bytes()); return h.hexdigest()

def rels(root: Path):
    for p in sorted(root.rglob('*')):
        if p.is_file():
            yield p.relative_to(root).as_posix(), p

def load_json(p: Path):
    return json.loads(p.read_text(encoding='utf-8'))

def main() -> int:
    root=Path(sys.argv[1]) if len(sys.argv)>1 else Path.cwd()
    fails=[]; results={v:'PASS' for v in VALIDATORS}
    def fail(v, code, detail):
        results[v]='FAIL'; fails.append({'validator_id':v,'fail_code':code,'detail':str(detail)})
    # H261/H266 scrub.
    stale_tokens=['historical' + '_production_decision','historical' + '_validation_state=HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY','AGENT_RUNTIME' + '_CONFIG_8000.txt']
    active_date_re=re.compile(r'(?<!H)(?<!SRC_)(?<!MODEL_)(?:' + '2026' + r'-06-[0-9]{2}|' + '2026' + r'-07-0[1-3])')
    for rel,p in rels(root):
        if rel.startswith(ACTIVE_SKIP_PREFIXES) or p.suffix.lower() not in TEXT_EXT:
            continue
        txt=p.read_text(encoding='utf-8', errors='ignore')
        for tok in stale_tokens:
            if tok in txt:
                vid='VALIDATE_PROJECT_VALIDATOR_FILESCHECKED_TRUTHFULNESS' if tok==('AGENT_RUNTIME' + '_CONFIG_8000.txt') else 'VALIDATE_ACTIVE_SURFACE_HISTORICAL_METADATA_SCRUB'
                fail(vid,'FAIL_STALE_ACTIVE_TOKEN',f'{rel}:{tok}')
        if not (rel in ALLOWED_DATE_FILES or rel.startswith(ALLOWED_DATE_PREFIXES)):
            if active_date_re.search(txt):
                fail('VALIDATE_ACTIVE_DATE_NEUTRALIZATION','FAIL_ORPHAN_LEGACY_DATE',rel)
    # H263 label harmonization: active label must be singular; legacy labels may appear only in lineage/release/historical/fixture contexts.
    label_file=root/'04_AGENT_FACTORY/10_AGENT_EXECUTI_7c69c542/H245_H260_SINGLE_S_dfaad80a.json'
    if not label_file.is_file():
        fail('VALIDATE_H245_H260_SINGLE_SOURCE_CANON_REFERENCE','FAIL_CANON_REFERENCE_MISSING',label_file)
    else:
        canon=load_json(label_file)
        if canon.get('canonical_source_path')!='04_AGENT_FACTORY/10_AGENT_EXECUTI_7c69c542' or len(str(canon.get('canonical_section_bundle_sha256','')))!=64:
            fail('VALIDATE_H245_H260_SINGLE_SOURCE_CANON_REFERENCE','FAIL_CANON_REFERENCE_INVALID',label_file)
    factory=root/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py'
    ftxt=factory.read_text(encoding='utf-8', errors='ignore') if factory.is_file() else ''
    if 'H391_H410_DIRECT_CANONICAL_PROJECT_FACTORY' not in ftxt:
        fail('VALIDATE_CANONICAL_LABEL_HARMONIZATION','FAIL_ACTIVE_INTERNAL_LABEL_MISSING','factory')
    if 'H391_H410_RUNTIME_VALIDATOR_SCOPE_MARKERS' not in ftxt:
        fail('VALIDATE_CANONICAL_LABEL_HARMONIZATION','FAIL_H261_SCOPE_NOT_ATTACHED','factory')
    # H267 runner.
    runner=root/'03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_MATRIX_31_RUNNER.py'
    rtxt=runner.read_text(encoding='utf-8', errors='ignore') if runner.is_file() else ''
    for tok in ['--resume','--stream-progress','H238_FULL_31_PROJECT_MATRIX_PARTIAL.json','resume_supported','streaming_progress']:
        if tok not in rtxt:
            fail('VALIDATE_MATRIX_RUNNER_STREAMING_PROGRESS_AND_RESUME','FAIL_RUNNER_STREAM_RESUME_MISSING',tok)
    # H264 exact duplicates. Active schema authority is `groups`; `duplicate_groups`
    # is accepted only as a legacy fallback when the active key is absent.
    allow_path=root/'99_MANIFESTS_SHA_LINEAGE/ENGINE_EXACT_DUPLICATE_ALLOWLIST.json'
    allow={}
    schema_required={'sha256','paths','reason_code','authority_path','mirror_paths','consumer','retention_rule','blocking_if_missing'}
    if not allow_path.is_file():
        fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_MISSING',allow_path)
    else:
        data=load_json(allow_path)
        raw_groups=data.get('groups')
        if raw_groups is None:
            raw_groups=data.get('duplicate_groups',[])
        if not isinstance(raw_groups, list):
            fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_GROUPS_NOT_LIST',allow_path)
            raw_groups=[]
        for g in raw_groups:
            if not isinstance(g, dict):
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_GROUP_NOT_OBJECT',g)
                continue
            missing=[k for k in schema_required if k not in g]
            if missing:
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_SCHEMA_FIELD_MISSING',{'sha256':g.get('sha256'),'missing':missing})
                continue
            h=g.get('sha256')
            paths=g.get('paths')
            authority_path=g.get('authority_path')
            mirror_paths=g.get('mirror_paths')
            if not (isinstance(h,str) and re.fullmatch(r'[0-9a-f]{64}', h)):
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_SHA256_INVALID',h)
                continue
            if not isinstance(paths,list) or not paths or not all(isinstance(x,str) and x for x in paths):
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_PATHS_INVALID',h)
                continue
            if not isinstance(authority_path,str) or authority_path not in paths:
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_AUTHORITY_PATH_INVALID',h)
                continue
            if not isinstance(mirror_paths,list) or set(paths)!={authority_path,*mirror_paths}:
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_AUTHORITY_MIRROR_SET_MISMATCH',h)
                continue
            if not isinstance(g.get('blocking_if_missing'), bool):
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_BLOCKING_FLAG_INVALID',h)
                continue
            for field in ['reason_code','consumer','retention_rule']:
                if not isinstance(g.get(field), str) or not g.get(field).strip():
                    fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_SCHEMA_FIELD_BLANK',{'sha256':h,'field':field})
            for rel_path in paths:
                fp=root/rel_path
                if not fp.is_file():
                    fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_PATH_MISSING',{'sha256':h,'path':rel_path})
                elif sha(fp)!=h:
                    fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_ALLOWLIST_PATH_SHA_MISMATCH',{'sha256':h,'path':rel_path,'observed':sha(fp)})
            allow[h]=set(paths)
    groups=defaultdict(list)
    for rel,p in rels(root):
        if rel.startswith('12_HISTORICAL_NON_AUTHORITY/') or rel.startswith('14_HISTORICAL_NON_AUTHORITY/') or rel in DUPLICATE_ALLOWLIST_SELF_FILES:
            continue
        groups[sha(p)].append(rel)
    for h,paths in groups.items():
        if len(paths)>1:
            if set(paths)!=allow.get(h):
                fail('VALIDATE_EXACT_DUPLICATE_RETENTION_ALLOWLIST','FAIL_DUPLICATE_WITHOUT_EXACT_ALLOWLIST',{'sha256':h,'paths':paths})
    # H268 active temp outputs/staging/test ZIPs.
    for rel,p in rels(root):
        low=rel.lower()
        if any(tok in low for tok in ['.tmp','.staging','/staging/','runtime_upload_test_output','test_output.zip']):
            fail('VALIDATE_FINAL_CLEAN_10_10_GATE','FAIL_ACTIVE_TEMP_OR_STAGING',rel)
        if low.endswith('.zip'):
            fail('VALIDATE_FINAL_CLEAN_10_10_GATE','FAIL_ACTIVE_INTERNAL_ZIP',rel)
    # Final gates.
    critical = len(fails)==0
    out={
        'scope':'H261_H268_APPLIED_ON_H01_H260',
        'validators':results,
        'VALIDADORES_H261_H268_PASS':'PASS' if critical else 'FAIL',
        'validators_fail':len(fails),
        'blocking_warnings':0 if critical else 1,
        'fail_codes':[f['fail_code'] for f in fails],
        'failures':fails,
        'CREATIVE_OUTPUT_CERTIFIED':False,
        'result':'PASS' if critical else 'FAIL'
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if critical else 1

if __name__=='__main__':
    raise SystemExit(main())
