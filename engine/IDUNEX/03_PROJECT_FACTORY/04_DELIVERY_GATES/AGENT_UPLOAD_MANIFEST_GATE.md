# H38 - AGENT_UPLOAD_MANIFEST_GATE

Status: ACTIVE_VALIDATED.

Policy: Gate is integrated into the active Project Factory runtime, not delivered as a decorative patch. Project delivery blocks on missing required materialization, trace, validator result, failcode or fallback.

Project artifact: `AGENT_RUNTIME_UPLOAD_SET_MANIFEST_CHATGPT.json`.

Validator: `Validated by validate_h37_h51_artifacts() and generate_end_to_end() inside IDUNEX_PROJECT_FACTORY_v1.0.0.py.`

Failcodes:
- `FAIL_H38_AGENT_RUNTIME_MANIFEST_MISSING`
- `FAIL_H38_AGENT_RUNTIME_FILE_COUNT_MISMATCH`
- `FAIL_H38_AGENT_RUNTIME_SHA_MISSING`
- `FAIL_H38_NON_RUNTIME_MIXED_AS_RUNTIME`
- `FAIL_H38_CHATGPT_COPILOT_UPLOAD_PARITY_BROKEN`

Fallback fixes:
- propagate explicit field to canon/profile/runtime/QA/fallback/trace
- regenerate impacted manifests/ledgers/certificates
- block official delivery when evidence is not executable or re-openable
