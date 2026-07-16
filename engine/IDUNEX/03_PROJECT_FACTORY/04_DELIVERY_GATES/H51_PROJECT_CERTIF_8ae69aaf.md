# H51 - PROJECT_CERTIFICATE_COMPLETENESS_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `IDUNEX_PROJECT_CERTIFICATE.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H51_PROJECT_CERTIFICATE_INCOMPLETE`
- `FAIL_H51_PROJECT_CERTIFICATE_SHA_MISSING`
- `FAIL_H51_PROJECT_CERTIFICATE_RUNTIME_COUNTS_MISSING`
- `FAIL_H51_PROJECT_CERTIFICATE_CREATIVE_STATE_MISSING`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
