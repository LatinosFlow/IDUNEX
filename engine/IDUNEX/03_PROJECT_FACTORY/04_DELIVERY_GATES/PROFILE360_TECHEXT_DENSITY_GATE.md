# H40 - PROFILE360_TECHEXT_DENSITY_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `PROFILE360_FIELD_DENSITY_AUDIT_ALL_MODELS.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H40_PROFILE360_DENSITY_LOW`
- `FAIL_H40_TECHEXT_DENSITY_LOW`
- `FAIL_H40_COUNT_ONLY_PASS_ATTEMPT`
- `FAIL_H40_GENERIC_FIELD_VALUE`
- `FAIL_H40_FIELD_NOT_PROMPT_USABLE`
- `FAIL_H40_FIELD_NOT_QA_USABLE`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
