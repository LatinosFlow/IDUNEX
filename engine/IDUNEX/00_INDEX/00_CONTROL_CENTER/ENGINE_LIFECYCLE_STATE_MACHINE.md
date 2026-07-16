# ENGINE_LIFECYCLE_STATE_MACHINE

## Estados

- ENGINE_PRE_CLOSURE_PATCHABLE: permite corrección P0 quirúrgica manteniendo `IDUNEX_MOTOR_v1.0.0`.
- ENGINE_RELEASE_CANDIDATE_BLOCKED: estado prohibido para este paquete; no usar RC.
- ENGINE_FINAL_RELEASE_GATE_PENDING: auditorías ejecutándose.
- ENGINE_FINAL_RELEASE_GATE_PASS: solo con 0 FAIL y companion externo coincidente.
- ENGINE_FINAL_RELEASE_GATE_BLOCKED: cualquier evidencia faltante o inválida.
- ENGINE_ARCHIVED_READONLY: línea histórica consultable, no modificable.

## Transiciones

`PRE_CLOSURE_PATCHABLE -> FINAL_RELEASE_GATE_PENDING -> FINAL_RELEASE_GATE_PASS` solo si no hay pérdida de canon y todos los P0 pasan.

`FINAL_RELEASE_GATE_PENDING -> BLOCKED` si un validator, JSON, config 8000, hash, manual o certificado falla.
