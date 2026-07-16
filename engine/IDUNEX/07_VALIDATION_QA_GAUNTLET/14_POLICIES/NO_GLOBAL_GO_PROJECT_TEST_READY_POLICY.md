# NO_GLOBAL_GO_PROJECT_TEST_READY_POLICY - HISTORICAL COMPATIBILITY BRIDGE

## Active semantics
ENGINE_GO = true
PROJECT_INSTANCE_GO = false_until_project_QA
OUTPUT_GO = false_until_output_QA_SIDECAR_HASH_LINEAGE
GLOBAL_GO is not active runtime language for the motor.

## Historical-only interpretation
`NO_GLOBAL_GO`, `PROJECT_TEST_READY_NO_GLOBAL_GO`, `global_go:false`, `GLOBAL_GO=false` and equivalent legacy text are compatibility records only and must be interpreted as `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY`. [HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY]

## Operational rule
A smoke test validates pathways only. It cannot release a project instance and cannot release an output. Release requires project QA, sidecar, hash lineage, manifests and external package hash validation.

## Validators
- `VALIDATE_NO_ACTIVE_LEGACY_NO_GO_STATE`
- `VALIDATE_STATUS_SEMANTIC_CONSISTENCY`
- `VALIDATE_SHA256_EXTERNAL_COMPANION_REAL_AND_MATCHING`

Updated: NEUTRALIZED_ACTIVE_SCOPE
