# AGENT_RUNTIME_UPLOAD_SET_GATE

Motor: IDUNEX_MOTOR_v1.0.0
Internal label: LEGACY_NON_AUTHORITY
Status: ACTIVE_BLOCKING
Fail code: `BLOCKED_AGENT_RUNTIME_UPLOAD_SET_INVALID`

## Contract
Validates exact upload set per agent: 10 core IDUNEX + N MODEL_RUNTIME_PROFILE_FULL, max 20 files, max 10 models, no split agents, no runtime extras.

## Blocking rule
Delivery is forbidden when this gate fails. PASS requires non-empty `actual_value`, computed evidence, and no count-only shortcut.

## Fallback fixes
- Move non-runtime files to DOCUMENTATION/ or EVIDENCE/.
- Rebuild AGENT_RUNTIME_UPLOAD_SET_MANIFEST.json.
- Recalculate SHA/manifests after every packaging change.
- Reopen final ZIP and re-run this gate before delivery.
