# QA_GAUNTLET_LEGACY_BRIDGE_POLICY

22_QA_GAUNTLET_CANONICAL_BRIDGE is canonical. 13_QA_GAUNTLET is retained as physical evidence and legacy-compatible evidence layer.
Do not delete 13_QA_GAUNTLET.
Do not split executable authority: the canonical bridge defines registry/order only; `99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py` is the single global validator entrypoint. The physical layer stores fail-code evidence, historical QA payloads and reports consumed as non-authoritative inputs.

Bridge local consistency requires:
- 08 has canonical index, execution order, validator registry and bridge policy.
- 09 has physical evidence, fail code registry and/or golden test evidence.
- The authoritative runtime entrypoint lists the strict bridge check.
- Reports cite validators and fail codes.

Bridge consistency is not M02_PASS and cannot authorize Demo, release, tag or productive closure.
