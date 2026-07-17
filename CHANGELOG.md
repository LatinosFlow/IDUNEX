# CHANGELOG — IDUNEX Engine

## AUD-003 — baseline físico actual, sin cambio de versión ni release

- Separado el baseline histórico recibido del árbol corregido actual.
- Preservado el ledger recibido y la reversa por commit/SHA de los manifiestos previos.
- Regenerados rutas, tamaños, tipos, extensiones y SHA256 desde `engine/IDUNEX/`.
- Agregado aggregate SHA256 determinista del árbol físico actual y scanner reproducible.
- Resultado limitado a `AUD003_SCOPE=PARTIAL_PASS`; `MOTOR_STATUS=EN_REVISION` y `M02_RESULT=M02_FAIL` permanecen vigentes.
- No se generó Proyecto Demo, release ni tag.

## v1.0.0 — EN_REVISION

- Baseline recibido desde `IDUNEX_MOTOR_v1.0.0.zip`.
- Integridad física recibida: SHA256, CRC/testzip, conteos ZIP y estructura raíz `IDUNEX/`.
- Estado funcional: pendiente de auditoría máxima independiente M02/M03.
- No declarar `OFICIAL` ni `READY_FOR_PROJECT_DEMO_GENERATION` hasta recomputar pruebas.
