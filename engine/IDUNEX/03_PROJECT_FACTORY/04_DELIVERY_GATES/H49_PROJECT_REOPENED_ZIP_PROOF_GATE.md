# H49 - PROJECT_REOPENED_ZIP_PROOF_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `PROJECT_REOPENED_ZIP_PROOF.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H49_PROJECT_REOPENED_ZIP_PROOF_MISSING`
- `FAIL_H49_PROJECT_ZIP_TESTZIP_FAIL`
- `FAIL_H49_PROJECT_SHA_COMPANION_MISMATCH`
- `FAIL_H49_REOPENED_VALIDATION_NOT_EXECUTED`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
