# H39 - GATE_TO_RUNTIME_CLAUSE_MAP_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `ENGINE_GATE_TO_PROJECT_RUNTIME_CLAUSE_MAP.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H39_GATE_WITHOUT_RUNTIME_CLAUSE`
- `FAIL_H39_GATE_WITHOUT_TEST_CASE`
- `FAIL_H39_GATE_WITHOUT_FALLBACK`
- `FAIL_H39_GATE_TRACE_NOT_PROJECT_MATERIALIZED`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
