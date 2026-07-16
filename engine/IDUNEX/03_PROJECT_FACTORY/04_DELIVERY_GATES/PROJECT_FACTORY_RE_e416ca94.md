# PROJECT_FACTORY_RETRY_LOOP_FOR_PACKAGING

Motor: IDUNEX_MOTOR_v1.0.0
Internal label: LEGACY_NON_AUTHORITY
Status: ACTIVE_BLOCKING
Fail code: `BLOCKED_PROJECT_FACTORY_RETRY_LOOP_NOT_EXECUTED`

## Contract
If a packaging gate fails, correct root cause, recalc manifests/SHA, re-emit ZIP, reopen ZIP and re-audit until 100% PASS.

## Blocking rule
Delivery is forbidden when this gate fails. PASS requires non-empty `actual_value`, computed evidence, and no count-only shortcut.

## Fallback fixes
- Move non-runtime files to DOCUMENTATION/ or EVIDENCE/.
- Rebuild AGENT_RUNTIME_UPLOAD_SET_MANIFEST.json.
- Recalculate SHA/manifests after every packaging change.
- Reopen final ZIP and re-run this gate before delivery.
