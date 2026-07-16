# H42 - SOURCE_RUNTIME_LEDGER_MINIFIED_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `SOURCE_RUNTIME_LEDGER_MINIFIED.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H42_SOURCE_LEDGER_MINIFIED_MISSING`
- `FAIL_H42_SOURCE_ID_USED_WITHOUT_TRACE`
- `FAIL_H42_SOURCE_HASH_MISSING`
- `FAIL_H42_SOURCE_AUTHORITY_STATUS_MISSING`
- `FAIL_H42_SOURCE_RUNTIME_REFERENCE_MISSING`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
