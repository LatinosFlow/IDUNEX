# HASH_EVIDENCE — Canonical smoke test

- engine_version: IDUNEX_MOTOR_v1.0.0
- validation_state: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE
- release_state: prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE
- productive_output: false
- global_go: false

## Reproducible evidence hashes

| referenced_file | sha256_exact_file_bytes |
|---|---|
| SMOKE_INPUT_FIXTURE.json | 1519adc6b28f0a3fd97708bdf23073fdc985568cc91e7db24b6108c697aaabce |
| SMOKE_OUTPUT_MOCK_RESULT.json | 7d2fa6c49b31389d7884fc3a98927d3ca506ebce2904a67b0e5aa20f1283fd55 |

Validator rule: `FAIL_BLOCKER_HASH_EVIDENCE_MISMATCH` blocks PASS if either declared hash does not reproduce against the current file bytes.
