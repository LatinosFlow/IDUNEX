# H48 - CONVERSATIONAL_AGENT_TEST_HARNESS_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `CONVERSATIONAL_TEST_SUITE_ES_EN.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H48_CONVERSATIONAL_TEST_SUITE_MISSING`
- `FAIL_H48_REQUIRED_CONVERSATIONAL_CASE_MISSING`
- `FAIL_H48_PROMPT_SHORT_LOWERED_DEPTH`
- `FAIL_H48_FALSE_CERTIFICATION_NOT_BLOCKED`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
