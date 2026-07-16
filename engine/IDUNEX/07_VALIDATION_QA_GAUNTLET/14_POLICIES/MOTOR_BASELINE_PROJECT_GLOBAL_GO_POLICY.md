# MOTOR_BASELINE_10 / PROJECT_10 / GLOBAL_GO POLICY - HISTORICAL COMPATIBILITY BRIDGE

## Active engine semantics
ENGINE_GO = true
PROJECT_INSTANCE_GO = false_until_project_QA
OUTPUT_GO = false_until_output_QA_SIDECAR_HASH_LINEAGE
GLOBAL_GO is not an active motor status and must not be used to release the base engine, a project instance or any output.

## Historical-only legacy phrases
Any legacy phrase that contains `global_go: false`, `GLOBAL_GO=false`, `PROJECT_TEST_READY_NO_GLOBAL_GO`, `PROJECT_GO=false`, `PROJECT_10=false`, `coverage_score=10 blocked` or `coverage_score_maximum_allowed=9` is retained only as `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY`. [HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY]

## MOTOR_BASELINE_10
- Structural and semantic runtime baseline is complete for project testing.
- State: `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.
- Legacy text `global_go: false` = `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY`, not active engine policy.
- Does not authorize project instance or real output release.

## PROJECT_10
- Requires a concrete project package with real or explicitly high-fidelity output evidence.
- Requires output-level sidecar per modality, QA result, golden test result and reproducible hash.
- Not granted by the motor alone.

## GLOBAL_GO
- Forbidden at motor level as an active status.
- Replaced by the split state above.
- Requires successful project-level QA, manual approval, legal/governance review and output evidence if used historically in project documents.

## Validators
- `VALIDATE_NO_ACTIVE_LEGACY_NO_GO_STATE`
- `VALIDATE_COVERAGE_POLICY_NO_ACTIVE_MAX9_CONTRADICTION`
- `VALIDATE_STATUS_SEMANTIC_CONSISTENCY`

## Blocker rules
- FAIL_BLOCKER_GLOBAL_GO_FROM_MOTOR_BASELINE
- FAIL_BLOCKER_COVERAGE_10_WITHOUT_REAL_OUTPUT_EVIDENCE
- FAIL_BLOCKER_SELF_REFERENCE_WITHOUT_CURRENT_EXTERNAL_HASH

Updated: NEUTRALIZED_ACTIVE_SCOPE
