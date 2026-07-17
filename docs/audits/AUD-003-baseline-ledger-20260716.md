# AUD-003 — baseline físico, hashes y ledgers

**Issue:** `LatinosFlow/IDUNEX#4`

**Rama:** `fix/AUD-003-baseline-ledger-remap`

**Corte de partida:** `fb148d23953fe8fcb0aaeb0c739fef6db7f467f5`

**Resultado limitado:** `AUD003_SCOPE=PARTIAL_PASS`

**Estado global:** `MOTOR_STATUS=EN_REVISION`, `M02_RESULT=M02_FAIL`

## Separación de baselines

El baseline histórico recibido y el árbol corregido actual son evidencias distintas:

| Evidencia | Clasificación | Archivos | SHA256 |
|---|---|---:|---|
| ZIP `IDUNEX_MOTOR_v1.0.0.zip` | Declaración histórica; ZIP ausente por política de almacenamiento | 977 entradas declaradas | `bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6` declarado, no recomputado en AUD-003 |
| Ledger recibido preservado | Histórico, no autoridad actual | 971 rutas indexadas + 6 autoexclusiones históricas | `4b56282a87ee00d0172aa1078480255a64622886a134d4c7c702f12f19e53d99` |
| Árbol físico actual `engine/IDUNEX` | Baseline actual reproducible desde el repositorio; no release | 979 archivos, 47.227.994 bytes | `b44ce9c87249a5ab33c7cb25ef3aeb539a21ff03f481e2e6282238b2da5548e4` |

Los seis manifiestos internos se excluyen entre sí para evitar autorreferencia. El manifiesto externo de gobierno cubre los 979 archivos físicos, incluidos esos seis, y no declara exclusiones.

## Diferencia recibida → actual

El comparador aplicó las 475 transformaciones Windows-safe del motor y encadenó los 295 movimientos reversibles AUD-008 antes de comparar contenido:

- 971/971 rutas históricas resueltas físicamente;
- 873 contenidos sin cambio;
- 98 contenidos modificados;
- 0 rutas históricas faltantes después de resolver remapeo/movimientos;
- 2 archivos actuales añadidos;
- 0 colisiones de rutas.

El detalle por archivo está en `governance/baseline/IDUNEX_BASELINE_DIFF_RECEIVED_TO_CURRENT.json`. La reversa de los seis carriers previos se preserva por commit, tamaño y SHA en `governance/baseline/historical_received/AUD-003_PRE_REGENERATION_PROVENANCE.json`.

## Cobertura actual

- Rutas indexadas faltantes: **0**.
- Archivos físicos sin manifest: **0**.
- Hashes obsoletos: **0**.
- Metadatos tamaño/extensión/tipo discordantes: **0**.
- Rutas stale en manifiestos activos: **0**.
- Aggregate y companion coherentes: **sí**.

El aggregate usa SHA256 sobre registros ordenados `repo_path UTF-8 + NUL + bytes decimales + NUL + SHA256 de archivo + LF`. No es un SHA de ZIP, companion de release ni certificado.

## Validaciones ejecutadas

| Control | Resultado recomputado |
|---|---|
| IDUNEX Intake Audit | PASS, 0 failures |
| Security Lite | PASS, 0 patrones de secreto de alta confianza |
| governance_state_check | CONSISTENT, 0 contradicciones activas |
| windows_path_remap_check | PASS, 5.838 entradas verificadas, 0 missing, 0 stale |
| no_bloat_no_history_check | PASS, 0 duplicados injustificados, 0 conflictos de movimiento |
| baseline_scanner | PASS de alcance AUD-003, 979/979 cubiertos |
| demo_hardcoding_check | PASS, 0 branches activos por nombre Demo |
| validator_entrypoint_check | No existe en el árbol; no aplicable |
| Suite `tests/intake` | 26 OK, 1 skip por ausencia de primitivas Unix `SIGALRM` en Windows |
| Cambios bajo superficies Demo/release | 0 |
| Tags locales creados | 0 |

## Conclusión

El baseline físico actual queda reproducible desde el repositorio y los manifiestos activos ya no contienen rutas stale ni hashes obsoletos. Esto permite `AUD-003 PARTIAL_PASS` exclusivamente para baseline/ledger.

No se recomputó la re-auditoría M02 global, no se acepta un PASS declarado y no se autoriza Proyecto Demo, release, tag ni cierre. `M02_RESULT=M02_FAIL` permanece vigente.
