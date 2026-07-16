# MODEL_RUNTIME_SINGLE_AUTHORITY_GATE

Motor: IDUNEX_MOTOR_v1.0.0
Internal label: LEGACY_NON_AUTHORITY
Status: ACTIVE_BLOCKING
Fail code: `BLOCKED_MULTIPLE_ACTIVE_MODEL_PROFILE_AUTHORITIES`

## Contract
Guarantees exactly one active MODEL_RUNTIME_PROFILE_FULL authority per model per agent; summaries/previews/README are non-runtime.

## Blocking rule
Delivery is forbidden when this gate fails. PASS requires non-empty `actual_value`, computed evidence, and no count-only shortcut.

## Fallback fixes
- Move non-runtime files to DOCUMENTATION/ or EVIDENCE/.
- Rebuild AGENT_RUNTIME_UPLOAD_SET_MANIFEST.json.
- Recalculate SHA/manifests after every packaging change.
- Reopen final ZIP and re-run this gate before delivery.
