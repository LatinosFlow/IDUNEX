# AUD-008 — Ledger de corrección no-bloat/no-history

Fecha: 2026-07-16
Issue: #9
Rama: `fix/AUD-008-no-bloat-history`

## Autoridad e interlock

La corrección se ejecutó contra el Informe Maestro de `governance/authority/REFERENCIA/`, el informe y plan M02, y `governance/CURRENT_STATE.json`.

- `MOTOR_STATUS=EN_REVISION` se mantiene sin cambios.
- `M02_RESULT=M02_FAIL` se mantiene sin cambios.
- Este ledger no declara ni acepta `M02_PASS`.
- No se generó Proyecto Demo, release ni tag.
- No se cerró el issue ni se modificaron manifiestos finales/baselines para hacerlos coincidir con el árbol corregido.
- No se modificó la lógica de generación, rutas CLI ni remapeo funcional. Las referencias derivadas fueron actualizadas únicamente para seguir rutas reclasificadas.

## Inventario reproducible

El inventario inicial fue recalculado sobre `main` en `4b4193a` y excluye `14_HISTORICAL_NON_AUTHORITY` del conjunto activo.

| Métrica | Antes | Después | Resultado |
| --- | ---: | ---: | --- |
| Archivos activos | 953 | 747 | -206 |
| Bytes activos | 46,593,879 | 18,351,717 | -28,242,162 (-60.6 %) |
| Grupos de duplicados exactos activos | 21 | 2 | -19 |
| Archivos en grupos duplicados | 46 | 6 | -40 |
| Duplicados exactos activos no justificados | 21 | 0 | corregido |
| Rutas H por nombre de archivo | 167 | 0 | corregido |
| Rutas H por cualquier componente de ruta | 205 | 0 | corregido |
| Evidencia histórica con autoridad activa | no conforme | 0 | corregido |

Los dos grupos exactos restantes pertenecen exclusivamente a manifiestos finales congelados: cuatro copias JSON equivalentes y dos copias de checksums equivalentes en `99_MANIFESTS_SHA_LINEAGE`. Se justifican como excepción no autoritativa porque la regla de alcance prohíbe corregir esos manifiestos en AUD-008. El scanner exige exactamente esas rutas y rechazará cualquier grupo adicional.

## Clasificación y tratamiento

El manifiesto registra 295 movimientos individualmente, con las cinco clases exigidas:

| Clasificación | Elementos |
| --- | ---: |
| Autoridad activa | 78 |
| Evidencia requerida | 62 |
| Histórico no autoritativo | 81 |
| Duplicado exacto | 10 |
| Referencia sustituida | 64 |

Se reclasificaron 208 archivos (28,219,941 bytes) bajo `engine/IDUNEX/14_HISTORICAL_NON_AUTHORITY/AUD_008_ACTIVE_HISTORY/`. Otros 87 elementos conservaron condición activa con nombres semánticos estables, sin marcador H.

Movimientos principales:

- `08_EVIDENCE_LINEAGE`: 53 artefactos históricos voluminosos, 27,059,971 bytes; queda un índice compacto activo.
- `11_RELEASE_INTERNAL`: 64 artefactos históricos, 440,265 bytes; queda únicamente un README no autoritativo.
- `99_MANIFESTS_SHA_LINEAGE`: 72 artefactos históricos, 670,275 bytes; los manifiestos finales congelados no fueron regenerados.
- Las rutas H activas restantes de `00`, `01`, `03`, `04`, `06`, `07` y `10` fueron reclasificadas o recibieron nombre estable según su función.

Las referencias derivadas estrictamente necesarias se actualizaron en 25 archivos, con 267 sustituciones de ruta. La comprobación de remapeo encadena los nombres congelados del baseline a través del manifiesto AUD-008, sin reescribir el baseline.

## Manifest de reversa

El archivo `docs/audits/AUD-008-movement-reversal-manifest.json` contiene, por cada movimiento:

- origen y destino;
- SHA-256 antes y después;
- razón e impacto;
- clasificación y autoridad posterior;
- operación de reversa y condición SHA previa a la reversa.

La reversa es verificable y conservadora: solo debe mover `destination` a `origin` cuando el archivo de destino mantenga `sha256_after` y el origen continúe ausente. Los elementos cuyo contenido cambió por una referencia derivada conservan SHA distintos antes/después de forma explícita. No se eliminó evidencia sin ruta de reversa.

## Scanner y pruebas

Se agregó `tools/audit/no_bloat_no_history_check.py` y su suite de mutación. El scanner recalcula hashes sobre el árbol activo y valida:

- cero duplicados exactos activos no justificados;
- cero rutas H activas fuera de la zona histórica;
- cero evidencia histórica marcada con autoridad activa;
- integridad SHA y reversibilidad de los 295 movimientos;
- `EN_REVISION` y `M02_FAIL` como interlock vigente.

Resultados ejecutados:

| Control | Resultado |
| --- | --- |
| `no_bloat_no_history_check.py` | PASS: 0 duplicados no justificados, 0 rutas H, 0 conflictos de autoridad histórica |
| Suite AUD-008 | 5/5 OK |
| Suite `tests/intake` | 23 OK, 1 omitido por plataforma |
| `governance_state_check.py` | CONSISTENT; `EN_REVISION`, `M02_FAIL`, release/tag false |
| `windows_path_remap_check.py` | PASS; 487 mappings, 0 colisiones, 0 targets faltantes, 0 referencias obsoletas activas |
| `intake_audit.py` | PASS |
| `demo_hardcoding_check.py` | PASS; 0 ramas Demo y 0 literales prohibidos |
| Validador maestro | FAIL preexistente/de alcance superior: `FAIL_RELEASE_SURFACE_SCOPE_SYNC`, `FAIL_DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY` |
| Entry point runtime canónico | FAIL esperado bajo `M02_FAIL`: `ACTIVE_VALIDATORS_EXACT_SET`, `DOCUMENT_TRUTHFULNESS_PARITY_H245_H260`, `DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY`, `FAIL_INTERNAL_MANIFEST_STALE_OR_INCOMPLETE` |

No existe un script independiente llamado `validator_entrypoint_check.py` en el repositorio; por ello se ejecutó el entry point canónico `99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`. Sus fallos restantes exigen paridad con certificados PASS/release, el set histórico de validadores H o regeneración de manifiestos finales. Forzarlos en AUD-008 violaría los interlocks y las reglas de alcance, por lo que quedan registrados y no maquillados.

## Conclusión acotada

AUD-008 corrige exclusivamente bloat, duplicación exacta injustificada e historia activa fuera de zona. El resultado no cambia la decisión M02, no habilita release y no constituye aceptación del motor.
