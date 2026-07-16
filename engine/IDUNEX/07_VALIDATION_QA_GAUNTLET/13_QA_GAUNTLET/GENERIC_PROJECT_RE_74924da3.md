# GENERIC_PROJECT_REAUDIT_SCENARIO_PROTOCOL

Motor: IDUNEX_MOTOR_v1.0.0  
Version semantica: v1.0.0  
Internal label: LEGACY_NON_AUTHORITY

## Estado
ACTIVE_BLOCKING_GENERIC.

## Regla
Toda simulacion activa del Project Factory debe usar fixtures genericos parametrizados: `GENERIC_PROJECT_FIXTURE`, `PROJECT_X`, `MODEL_A_ADULT`, `MODEL_B_ADULT`, `ORIGIN_A` y `ORIGIN_B`.

## Alcance universal
Aplica a crear proyecto nuevo, crear proyecto demo, actualizar proyecto con motor nuevo, actualizar datos de modelos, auditar proyecto, auditar motor y retirar/archivar.

## Bloqueo
- `BLOCKED_PROJECT_SPECIFIC_HARDCODE_IN_ACTIVE_POLICY`
- `BLOCKED_GENERIC_FIXTURE_MISSING`
- `BLOCKED_POSITIVE_FIXTURE_VALIDATOR_FAIL`

## Cierre
Solo PASS si el fixture positivo generico tiene validators_fail=0, DELIVERY_ALLOWED, truthfulness PASS, SHA/manifests PASS, configs 8000 PASS y no depende de nombres de proyecto/modelo.
