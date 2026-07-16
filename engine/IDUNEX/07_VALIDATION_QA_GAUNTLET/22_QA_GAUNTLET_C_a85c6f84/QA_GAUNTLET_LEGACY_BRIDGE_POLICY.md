# QA_GAUNTLET_LEGACY_BRIDGE_POLICY

22_QA_GAUNTLET_CANONICAL_BRIDGE is canonical. 13_QA_GAUNTLET is retained as physical evidence and legacy-compatible evidence layer.
Do not delete 13_QA_GAUNTLET.
Do not split authority: 08 defines order and pass/fail gates; 09 stores fail-code evidence, historical QA payloads and reports consumed by validators.

Bridge PASS requires:
- 08 has canonical index, execution order, validator registry and bridge policy.
- 09 has physical evidence, fail code registry and/or golden test evidence.
- Runtime validator lists the strict bridge validator.
- Reports cite validators and fail codes.
