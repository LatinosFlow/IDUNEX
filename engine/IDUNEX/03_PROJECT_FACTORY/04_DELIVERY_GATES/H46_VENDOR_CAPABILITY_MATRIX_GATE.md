# H46 - VENDOR_CAPABILITY_MATRIX_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `VENDOR_CAPABILITY_DECLARATION_MATRIX.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H46_VENDOR_CAPABILITY_MATRIX_MISSING`
- `FAIL_H46_UNSUPPORTED_VENDOR_FEATURE_DECLARED_PASS`
- `FAIL_H46_VENDOR_LIMITATION_NOT_EVIDENCED`
- `FAIL_H46_VENDOR_TRUTHFULNESS_BROKEN`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
