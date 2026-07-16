# H37 - INPUT_RICH_DIRECTION_FIELDS_MATERIALIZATION_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `INPUT_PROMPT_FIDELITY_LEDGER.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H37_INPUT_FIELD_NOT_MATERIALIZED`
- `FAIL_H37_INPUT_FIELD_SUMMARIZED_AWAY`
- `FAIL_H37_INPUT_FIELD_LOST_IN_RUNTIME`
- `FAIL_H37_INPUT_FIELD_NO_QA_TRACE`
- `FAIL_H37_INPUT_FIELD_PLACEHOLDER_ACTIVE`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
