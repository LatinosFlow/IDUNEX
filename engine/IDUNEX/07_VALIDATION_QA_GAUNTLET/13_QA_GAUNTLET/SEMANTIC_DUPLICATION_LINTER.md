# SEMANTIC_DUPLICATION_LINTER — Executable QA Procedure

## Purpose
Convertir política/matriz IDUNEX en procedimiento ejecutable. Este archivo no es resumen; es gate operativo.

## Input files
- Profile360 registry
- Source-to-runtime map
- Source inventory
- Schemas
- Sidecars
- Project manifests
- QA results

## Execution steps
1. Load active engine metadata and confirm `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`.
2. Validate JSON against official schemas.
3. Compare field/source/adapter/fail_code/fallback/golden_test alignment.
4. Confirm manifests and hashes are either exact or marked `self_reference_externalized`.
5. Record PASS/FAIL and required retest.

## Checks
- no field/source orphan
- no template/schema mismatch
- no inflated coverage score
- no project/output state ambiguity
- no unsupported claim of 10/10 or GLOBAL_GO

## PASS criteria
All critical files validate; evidence exists; smoke/project status remains `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.

## FAIL criteria
Any missing schema, stale hash, unverified claim, thin evidence, or GLOBAL_GO claim.

## Fail codes
- FAIL_BLOCKER_VALIDATOR_FALSE_PASS
- FAIL_BLOCKER_HASH_LINEAGE_DRIFT
- FAIL_BLOCKER_COVERAGE_SCORE_WITHOUT_EXECUTION_EVIDENCE
- FAIL_BLOCKER_SMOKE_TEST_NOT_EXECUTABLE

## Fallback fixes
Correct source file, regenerate manifests, rerun validator, rerun smoke/project evidence, keep `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`.

## Retest protocol
Run `99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py` from extracted package and inspect `VALIDATION_RESULT.json`.

## Output report format
JSON: audit_status, critical_errors, warnings, go_no_go_decision, metrics, evidence.

## Production decision
`prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE` maximum; `PROJECT_GO` and `GLOBAL_GO` require real project proof.

## Executable QA procedure — HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY former v1.0.5
Purpose: convert this QA file from summary into an executable audit protocol.

### Input files
- PROFILE360_FIELD_REGISTRY.json
- SOURCE_TO_RUNTIME_MASTER_MAP.json
- SOURCE_SEMANTIC_COVERAGE_REPORT.json
- SIDECAR schema/templates
- PROJECT_FIXTURE_VALIDATION_001 evidence bundle
- HASH_MANIFEST / FILE_MANIFEST / SHA256SUMS

### Execution steps
1. Load canonical manifests and verify file_count and hash lineage.
2. Validate field_id, runtime_domain, source_ids, adapter_targets, qa_rule_id, fail_code, fallback_fix and golden_test_id.
3. Run schema validation on all critical JSON fixtures.
4. Verify source cards and coverage are synchronized with runtime map.
5. Check sidecar by modality: adapter, vendor_params, field_ids, source_ids, hashes and production state.
6. Run modality-specific golden tests and record PASS/WARNING/FAIL.
7. Apply fallback and retest if any warning or fail is detected.

### PASS criteria
- 0 critical errors.
- No GLOBAL_GO in motor baseline.
- Coverage score never exceeds 9 without output+sidecar+QA+hash evidence.
- All failures have fail_code and surgical fallback.

### WARNING criteria
- Support-only source allowed for baseline but requires PROJECT_GO manual review.
- High-fidelity mock evidence allowed only for prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE.

### FAIL criteria
- Hash mismatch, schema mismatch, untracked source, generic golden test, adapter mismatch, fake hash, or GLOBAL_GO declaration from motor.

### Output report format
JSON object with audit_status, critical_errors, warnings, go_no_go_decision, files_checked, failed_files, fallback_actions and retest_result.

### Production decision
Motor baseline may reach prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE. PROJECT_GO/GLOBAL_GO require real project artifacts and human approval.

## Executable QA Procedure
- purpose: validate this QA dimension without interpretation drift.
- input files: project manifest, Profile360 fields, source map, fail codes, sidecars, hash evidence and modality fixtures.
- execution command: run `python IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py` and then execute the modality-specific checklist in this file.
- validation rules: JSON/schema pass; source trace present; field trace present; adapter trace present; sidecar hash present; GLOBAL_GO false.
- pass criteria: all checks pass with no critical errors and no unresolved placeholders in non-template outputs.
- warning criteria: baseline-only evidence, support-only source, coverage capped at 8/9, or manual review required before PROJECT_GO.
- fail criteria: schema mismatch, missing sidecar, missing hash evidence, adapter mismatch, GLOBAL_GO attempted from motor baseline.
- fail codes: FAIL_BLOCKER_VALIDATOR_INCOMPLETE; FAIL_BLOCKER_COVERAGE_10_WITHOUT_REAL_OUTPUT_EVIDENCE; FAIL_BLOCKER_GLOBAL_GO_FROM_MOTOR_BASELINE.
- fallback fixes: regenerate affected manifest, rerun source-to-runtime map, repair sidecar, recalculate hash, repeat test.
- retest protocol: rerun validator and produce PASS/FAIL report with timestamp and reviewer.
- output report format: JSON QA result plus Markdown summary with evidence paths and go/no-go decision.
- production decision: prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE only; PROJECT_GO/GLOBAL_GO forbidden without real project evidence.

### Example PASS report
`audit_status=PASS`, `global_go=false`, all schemas valid, sidecars present, hash evidence reproducible, coverage score <= 9. [HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY]

### Example FAIL report
`audit_status=FAIL`, schema mismatch or missing sidecar/hash, fallback listed, retest required.
