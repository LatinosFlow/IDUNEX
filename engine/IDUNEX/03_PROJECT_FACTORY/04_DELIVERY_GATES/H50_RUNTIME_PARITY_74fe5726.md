# H50 - RUNTIME_PARITY_AND_MINIFICATION_SAFETY_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `CHATGPT_RUNTIME_PARITY_AUDIT.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H50_RUNTIME_PARITY_AUDIT_MISSING`
- `FAIL_H50_CHATGPT_COPILOT_PARITY_BROKEN`
- `FAIL_H50_MINIFICATION_DROPPED_CRITICAL_GATE`
- `FAIL_H50_RUNTIME_HAS_NON_RUNTIME_AUTHORITY_FILE`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
