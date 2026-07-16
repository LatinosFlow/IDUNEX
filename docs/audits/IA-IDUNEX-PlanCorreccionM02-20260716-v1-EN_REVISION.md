# IA-IDUNEX — Plan maestro de corrección M02

**Identificador operativo:** `AUD-011`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Fecha:** 2026-07-16  
**Informe de origen:** `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`  
**Commit auditado por M02:** `9dc3aef0b5cd872399a9c123d69043296da38aee`  
**Estado del plan:** `EN_REVISION`  
**MOTOR_STATUS:** `EN_REVISION`  
**Decisión vigente:** `M02_FAIL`  
**Alcance de este cambio:** documentación de planificación únicamente

## 1. Propósito y decisión de control

Este documento define el orden, las dependencias, los riesgos, las pruebas mínimas y los criterios de aceptación para corregir los bloqueantes `B-01` a `B-08` detectados por M02 y registrados en `AUD-003` a `AUD-010`.

El plan no modifica el motor, no corrige ningún bloqueante, no genera un Proyecto Demo, no crea release ni tag, no cierra issues y no declara ni acepta un estado `PASS`. Los criterios descritos son condiciones futuras de elegibilidad para una re-auditoría independiente; no constituyen certificación ni cambian `MOTOR_STATUS=EN_REVISION`.

La decisión `M02_FAIL` permanece vigente hasta que una nueva auditoría recompute la evidencia sobre un commit final inmóvil. Ninguna evidencia autoemitida por el motor puede sustituir esa recomputación.

## 2. Autoridad y fuentes leídas

Orden de autoridad aplicado:

1. `governance/authority/REFERENCIA/Informe_Maestro_Go_07d4ad84.pdf`, leído completo, 34 páginas.
2. `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`, leído completo.
3. Issues abiertos `AUD-003` a `AUD-010` (`#4` a `#11`).
4. Estado raíz declarado por `README.md` y `GOVERNANCE_STATUS.md`: `EN_REVISION`.
5. Evidencia técnica citada por M02, utilizada para ubicar superficies probables; sus declaraciones internas de `PASS`, `10/10`, `31/31` o disponibilidad para Demo no se aceptan como autoridad.

Reglas del Informe Maestro que gobiernan este plan:

- `ENGINE_LEVEL ≠ PROJECT_LEVEL ≠ AGENT_LEVEL`.
- Proyecto Demo es una validación posterior, no un fixture, default o canon activo del motor.
- El cierre del motor exige matriz máxima, lifecycle, update/migration y mutation recomputados.
- Un comando que no retorna limpio, evidencia faltante o un `PASS` solo declarado impide la entrega.
- El SHA integral del ZIP y sus bytes absolutos requieren autoridad externa.
- El motor no debe mantener factories o validators paralelos, historial activo, bloat ni evidencia autoritativa duplicada.

## 3. Principios de ejecución de la corrección

1. **Un issue, un objetivo verificable.** La regla por defecto es un PR técnico por issue para preservar revisión, reversión y atribución de regresiones.
2. **Estado seguro primero.** La contradicción de gobierno se corrige antes de habilitar cualquier otro trabajo para que toda superficie siga indicando `EN_REVISION` y bloquee Demo/release.
3. **Baseline en dos gates.** `AUD-003` abre primero el gate de disponibilidad y procedencia del ZIP/companion, pero regenera y sella manifiestos al final, cuando el árbol técnico ya no cambiará.
4. **No regenerar ledgers prematuramente.** Cualquier cambio posterior a una regeneración invalida hashes y conteos; el sello final de `AUD-003` es el último PR técnico.
5. **Factory serializado.** `AUD-004`, `AUD-010`, `AUD-005` y `AUD-007` comparten el factory de aproximadamente 823 KB. Pueden prepararse en paralelo, pero se integran en orden y con rebase sobre el PR previo.
6. **Pruebas exactas, no instrumentadas.** La aceptación se ejecuta sobre los blobs que se pretenden auditar; no se usa monkey patch, wrapper que altere semántica ni protección temporal como evidencia de cierre.
7. **Evidencia fuera del runtime distribuible.** Resultados voluminosos de auditoría se conservan fuera del motor activo; dentro del motor solo queda lineage compacto y necesario.
8. **No cierre automático.** La integración de un PR técnico no cierra su issue ni eleva M02. El issue queda disponible para verificación independiente.

## 4. Matriz maestra de corrección

La matriz se normaliza en dos vistas enlazadas por `issue` para mantener legibilidad sin omitir ninguno de los campos requeridos.

### 4.1 Diagnóstico, superficie y orden

| Issue | Bloqueante M02 | Severidad | Causa raíz | Archivos probables afectados | Tipo de cambio | Rama sugerida | Orden recomendado |
|---|---|---|---|---|---|---|---:|
| `AUD-003` (`#4`) | `B-01` baseline físico no reproducible y ledger desactualizado | Crítica | El remapeo físico no disparó actualización atómica de rutas, hashes y manifiestos; el ZIP fuente/companion no quedó recuperable para recomputación. | `REPOSITORY_MANIFEST.yml`; `governance/baseline/WINDOWS_PATH_SAFE_REMAP.{json,md}`; `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/{SHA256SUMS.txt,MANIFEST.txt,MANIFEST.json}`; puntero SHA interno; `tools/package/package_engine.py`; evidencia externa del ZIP/companion. | Recuperación de procedencia; reconciliación de árbol; regeneración determinista de manifiestos; sello criptográfico externo. | `fix/AUD-003-baseline-ledger-remap` | `1a` gate de evidencia; `8` sello final |
| `AUD-004` (`#5`) | `B-02` incompatibilidad Windows de `generate` | Crítica | Acceso a `signal.SIGALRM` antes de la protección y dependencia de `setitimer` Unix-only en un flujo soportado en Windows. | `engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py`; runner de matriz; pruebas de watchdog/lifecycle. | Refactor de timeout/watchdog por capacidad; manejo y cleanup multiplataforma; regresión Windows/Linux. | `fix/AUD-004-generate-windows-watchdog` | `2` |
| `AUD-005` (`#6`) | `B-03` remapeo no propagado a código y self-test | Crítica | El rename se aplicó al filesystem, no al grafo de referencias. Factory y validator aún buscan el H62 largo y otras rutas originales. | `governance/baseline/WINDOWS_PATH_SAFE_REMAP.{json,md}`; factory; `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`; `.../H62_CLI_N1_N10_CLEAN_EXIT.json`; registries, tests y manifiestos referenciadores. | Resolver único original→segura; migración de referencias; lint de integridad referencial; regeneración de evidencia H62. | `fix/AUD-005-remap-references` | `4` |
| `AUD-006` (`#7`) | `B-04` estados `PASS` contradictorios | Crítica de gobierno | Certificados y estados derivados actúan como autoridad paralela y no se invalidan ante cambio de árbol o fallo independiente. | `README.md`; `GOVERNANCE_STATUS.md`; `engine/IDUNEX/00_INDEX/00_CONTROL_CENTER/{ACTIVE_VERSION.md,VERSION_MANIFEST.json}`; `engine/IDUNEX/00_INDEX/MASTER_GOVERNANCE_MAP.json`; certificados duplicados en `00_INDEX` y `11_RELEASE_INTERNAL`; reporte de democión de control center. | Máquina de estados única; invalidación de derivados; interlock de Demo/release; detector de contradicciones. | `fix/AUD-006-governance-state-machine` | `0` |
| `AUD-007` (`#8`) | `B-05` acoplamiento activo a Demo y falso positivo | Alta, bloqueante | Excepción de proyecto incorporada a lógica ENGINE_LEVEL; el self-test afirma ausencia del patrón sin inspeccionarlo ni ejecutarlo adversarialmente. | Factory; `IDUNEX_PROJECT_MATRIX_31_RUNNER.py`; `PROJECT_DEMO_PASS_GATE.{json,md}`; `DEMO_TEMPLATE_READINESS.md`; caso de mutation `463_H27...`; registries que referencian gates Demo. | Eliminación de branch por nombre; parametrización genérica; test AST/textual y conductual negativo; matriz no-Demo de 30 casos. | `fix/AUD-007-remove-demo-hardcoding` | `5` |
| `AUD-008` (`#9`) | `B-06` no-bloat/no-history incumplidos | Alta, bloqueante | Acumulación de hitos, reportes, evidencia y copias exactas dentro del runtime activo, sin clasificación única de autoridad/retención. | `engine/IDUNEX/08_EVIDENCE_LINEAGE/`; `11_RELEASE_INTERNAL/`; `14_HISTORICAL_NON_AUTHORITY/`; delivery gates con nomenclatura H; allowlists y auditorías de duplicados; manifiestos finales. | Inventario hash; deduplicación; democión/movimiento reversible; compactación de lineage; política de retención. | `fix/AUD-008-no-bloat-history` | `7` |
| `AUD-009` (`#10`) | `B-07` validator único no demostrado | Alta, bloqueante | Se confunde un registry/orquestador con un único entrypoint; múltiples scripts activos pueden producir cierres parciales o divergentes. | `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`; scripts `VALIDATE_*.py`; `07_VALIDATION_QA_GAUNTLET/16_MASTER_GOVERNANCE/`; canonical bridge; registry QA y factory si expone validación. | Un entrypoint autoritativo; secundarios convertidos en módulos; contrato de resultado único; bloqueo de cierre global alterno. | `fix/AUD-009-validator-entrypoint` | `6` |
| `AUD-010` (`#11`) | `B-08` normalización inconsistente en update | Alta, bloqueante | Se mezclan archivos absolutos con `project_root` relativo antes de `relative_to`, dejando el resultado dependiente del CWD. | Factory, borde CLI de `update-project`, `migrate-project` y `update-project-by-engine`; pruebas de rutas. | Normalización temprana a representación absoluta/canónica; validación de pertenencia; regresión de CWD y OS. | `fix/AUD-010-cli-path-normalization` | `3` |

### 4.2 Dependencias, riesgos, pruebas y aceptación

| Issue | Dependencias | Riesgos principales | Pruebas mínimas | Criterio de aceptación futuro |
|---|---|---|---|---|
| `AUD-003` | Gate de estado `AUD-006`; disponibilidad del ZIP/companion original; todos los PRs que cambian árbol completados antes del sello. | Confundir SHA original con SHA del candidato corregido; regenerar sobre árbol móvil; autocertificación; cambios de EOL o modo de archivo. | SHA-256 externo; `testzip`; conteo/CRC; reconstrucción de manifiestos desde clean checkout; comparación manifiesto↔árbol; 0 rutas stale/missing; determinismo en segunda ejecución. | Procedencia documentada; ZIP y companion recuperables o decisión formal de nuevo baseline; SHA recomputable; `testzip` ejecutable; 100% de rutas indexadas existentes; 0 originales inexistentes en ledgers; manifiestos consistentes. No crea release/tag ni declara cierre. |
| `AUD-004` | `AUD-006`; para evidencia máxima posterior requiere runner no-Demo de `AUD-007` y referencias de `AUD-005`. | Watchdog sin capacidad de terminar procesos; regresión Linux; cleanup incompleto; falsos rc=0; procesos huérfanos. | Unit tests de capability detection; generate N1 en Windows y Linux; timeout cooperativo/no cooperativo; cleanup; rc/JSON/ZIP correlacionados; smoke N1/N10. | Ningún acceso no protegido a `SIGALRM`; `generate` produce salida válida y rc=0 en ambos OS cuando corresponde; timeout bloquea entrega parcial y termina limpio; no proceso huérfano. |
| `AUD-005` | `AUD-004` para recomputar H62; `AUD-007` para que mutation sea veraz; sello de manifiestos queda para `AUD-003`. | Resolver dual; rutas antiguas ocultas en JSON/MD/Python; colisiones; evidencia fabricada por override; cambios de path que rompan histórico. | Bijección/cero colisiones del mapa; lint sobre todo texto gobernado; existencia de targets; H62 por ruta segura; validator/factory contra misma tabla; mutation enfocada H18-H20. | 0 referencias activas stale; toda referencia gobernada resuelve a ruta existente; H62 se consume por la ruta segura; los tres fallos 452-454 desaparecen por evidencia real. El objetivo global 506/506 se verifica solo tras `AUD-007` y no se atribuye prematuramente a este PR. |
| `AUD-006` | Ninguna corrección técnica previa; toma `README.md`/`GOVERNANCE_STATUS.md` como estado raíz inicial. | Democión parcial; dos generadores de estado; certificados cacheados; habilitación accidental de Demo/release. | Scanner de contradicciones; mutaciones de estado; cambio de un hash que invalida derivados; búsqueda de `READY_FOR_PROJECT_DEMO_GENERATION=TRUE`, `31/31`, `10/10` y cierres activos contradictorios. | Una fuente raíz verificable mantiene `EN_REVISION`; toda superficie derivada queda no-autorizante; Demo/release permanecen bloqueados; cualquier fallo/cambio de árbol invalida certificados; detector retorna 0 contradicciones. |
| `AUD-007` | `AUD-005` para rutas/self-test consistentes; rebase posterior a `AUD-004`/`AUD-010` por factory compartido. | Eliminar solo el literal y conservar semántica Demo; romper capacidad de proyecto genérico; self-test nuevamente declarativo; generar Demo accidentalmente. | AST/token scan de branches por nombres propios; prueba negativa con nombre Demo y controles con nombres arbitrarios; inspección de gates; mutation real; runner exactamente N1..N10 × 3 sin caso Demo. | 0 comparaciones ejecutables por `Proyecto 000 Demo`; 0 canon Demo activo; políticas dependen de campos genéricos; self-test falla si se reintroduce hardcoding; la etapa no genera ningún Demo. |
| `AUD-008` | `AUD-009` debe identificar módulos/evidencia realmente necesarios; `AUD-003` sella después. | Borrar autoridad o investigación útil; romper referencias; perder trazabilidad; inflar diff y dificultar reversión. | Inventario SHA/tamaño/rol; simulación de moves; reverse manifest; lint de referencias; validación de allowlist; comparación antes/después; suite autoritativa tras limpieza. | Duplicados exactos eliminados o justificados por allowlist mínima; hitos activos reclasificados; lineage compacto; 0 referencia rota; manifiesto de movimientos/eliminaciones y reversa; políticas no-bloat/no-history quedan recomputables. |
| `AUD-009` | `AUD-005` y `AUD-007` estabilizan referencias y truthfulness; precede a `AUD-008`. | Cambiar semántica al modularizar; doble entrypoint residual; pérdida de fail codes; un módulo secundario aún emite cierre global. | Enumeración de ejecutables; invocación CLI única; import tests de módulos; paridad de resultados; mutación que intenta cierre desde secundario; registry↔módulos. | Un único comando público emite resultado global; secundarios no son CLIs de cierre; registry sincronizado; fail codes y agregación deterministas; prueba de enforcement bloquea entrypoint alterno. |
| `AUD-010` | `AUD-006`; rebase posterior a `AUD-004` si se integra después. | `resolve()` altera semántica con symlinks; traversal; diferencia Windows/Linux; normalizar tarde; cambiar update funcional. | Matriz relativa/absoluta desde varios CWD; Windows/Linux; paths con espacios; update, migrate y by-engine; pertenencia fuera de root; no-drift. | Las tres operaciones se comportan igual con rutas relativas y absolutas; representación interna única desde el borde CLI; pertenencia segura; sin regresión funcional ni dependencia del CWD. |

## 5. Matriz de dependencias

La celda se lee como relación de la issue de la fila respecto de la issue de la columna. Leyenda: `D` la fila depende de la columna; `S` comparten superficie y exigen serialización/rebase; `V` requieren verificación final conjunta; `—` sin dependencia directa.

| Desde \ Hacia | 003 | 004 | 005 | 006 | 007 | 008 | 009 | 010 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `AUD-003` | — | — | `V` | `D` | — | `V` | `V` | — |
| `AUD-004` | `V` | — | `D/S` | `D` | `S` | — | `V` | `S` |
| `AUD-005` | `V` | `D/S` | — | `D` | `D/S` | `V` | `D` | `S` |
| `AUD-006` | — | — | — | — | — | — | — | — |
| `AUD-007` | `V` | `S` | `D/S` | `D` | — | — | `D` | `S` |
| `AUD-008` | `D` | — | `V` | `D` | — | — | `D` | — |
| `AUD-009` | `V` | — | `D` | `D` | `D` | — | — | — |
| `AUD-010` | `V` | `S` | `S` | `D` | `S` | — | — | — |

Lectura operativa:

- `AUD-006` es el interlock inicial y no depende de los demás.
- La recuperación externa de `AUD-003` comienza inmediatamente, en paralelo, pero el sello de árbol depende de todos los cambios que alteran contenido o rutas.
- `AUD-004` habilita la generación necesaria para recomputar H62; `AUD-005` repara la ruta y el grafo referencial que consume esa evidencia.
- `AUD-007` debe suceder a `AUD-005` para que el mutation/self-test deje de mezclar fallo de ruta con falso positivo Demo.
- `AUD-009` consolida la arquitectura cuando referencias y truthfulness ya están estabilizadas.
- `AUD-008` se integra después de `AUD-009`, porque primero debe conocerse qué módulos y evidencias son necesarios; cualquier movimiento se incluye luego en el sello de `AUD-003`.

## 6. Orden técnico de corrección

### Fase 0 — Contención de gobierno

1. **`AUD-006/B-04`.** Crear la máquina de estados y degradar toda superficie derivada a `EN_REVISION` o estado no-autorizante. El gate de Demo y release queda cerrado por defecto.

### Fase 1 — Gate de evidencia y recuperación paralela

2. **`AUD-003/B-01`, tramo A.** Localizar el ZIP fuente y companion fuera del motor, registrar custodia, distinguir el SHA original del futuro candidato corregido y demostrar que puede recomputarse. Si la evidencia original no existe, documentar el bloqueo y preparar la declaración formal de un nuevo baseline candidato; nunca reutilizar silenciosamente el SHA original.

Este trabajo de recuperación puede continuar en paralelo con las correcciones independientes, pero `AUD-003` no se acepta ni cierra en este tramo.

### Fase 2 — Recuperación del lifecycle CLI

3. **`AUD-004/B-02`.** Sustituir la dependencia Unix-only por un watchdog multiplataforma con cleanup y semántica de error explícita.
4. **`AUD-010/B-08`.** Normalizar paths en el borde CLI. Puede desarrollarse en paralelo con `AUD-004`, pero se rebasa y se integra después para evitar un merge ambiguo en el factory.

### Fase 3 — Integridad referencial y separación ENGINE/PROJECT

5. **`AUD-005/B-03`.** Introducir el resolver único de remapeo, migrar referencias y recomputar la evidencia H62 mediante el `generate` ya corregido.
6. **`AUD-007/B-05`.** Eliminar la excepción Demo, retirar el caso Demo del runner de cierre técnico y reemplazar el falso positivo de mutation por una prueba real.

### Fase 4 — Arquitectura de validación y limpieza

7. **`AUD-009/B-07`.** Establecer un único entrypoint global y modularizar validadores secundarios sin pérdida de fail codes.
8. **`AUD-008/B-06`.** Deduplicar y demover historia con inventario, reverse manifest y validación de referencias.

### Fase 5 — Sello final del baseline candidato

9. **`AUD-003/B-01`, tramo B.** Congelar el árbol, regenerar manifiestos/hashes desde un clean checkout, verificar la segunda ejecución determinista y producir el companion externo del candidato. Este tramo ocurre después de todo cambio de archivos o rutas.

### Fase 6 — Re-auditoría independiente

10. Ejecutar la estrategia de la sección 10 sobre el commit exacto resultante. Hasta que termine, el estado permanece `EN_REVISION` y la decisión vigente sigue siendo `M02_FAIL`.

## 7. Qué puede hacerse junto y qué debe aislarse

### 7.1 Trabajo concurrente permitido

- Recuperación del ZIP/companion de `AUD-003` puede ejecutarse en paralelo con todo el tren técnico.
- `AUD-004` y `AUD-010` pueden desarrollarse en paralelo después del interlock de `AUD-006`, pero no deben fusionarse simultáneamente: ambos modifican el mismo factory y requieren rebase y pruebas después del merge previo.
- Inventario read-only de duplicados para `AUD-008` puede prepararse mientras se diseña `AUD-009`; los cambios de árbol se integran solo después de consolidar validator.

### 7.2 Combinación condicional

`AUD-003` y `AUD-005` forman una unidad transaccional de rutas/manifiestos. Solo podrían compartir un PR si ya existe evidencia externa verificable y el mismo PR:

1. migra todas las referencias;
2. verifica 0 rutas stale y 0 colisiones;
3. regenera manifiestos una sola vez sobre el árbol final;
4. separa con claridad el SHA original del SHA del candidato corregido.

La recomendación por defecto es mantenerlos en PRs separados y usar `AUD-003` como sello final.

### 7.3 Correcciones que deben ir aisladas

- `AUD-006`: cambia autoridad y controles de transición.
- `AUD-004`: cambia concurrencia, timeout y cleanup.
- `AUD-010`: cambia semántica de paths y pertenencia.
- `AUD-007`: cambia la frontera ENGINE/PROJECT y el truthfulness del self-test.
- `AUD-009`: cambia la arquitectura de validación global.
- `AUD-008`: contiene movimientos/eliminaciones de alto volumen y requiere reversión propia.

No se recomienda un PR ómnibus para `B-01` a `B-08`.

## 8. Secuencia recomendada de PRs técnicos

| PR | Issue | Rama | Base requerida | Alcance y gate de merge |
|---:|---|---|---|---|
| 0 | `AUD-006` | `fix/AUD-006-governance-state-machine` | `main` | Interlock de `EN_REVISION`; no habilita Demo/release. |
| 1 | `AUD-004` | `fix/AUD-004-generate-windows-watchdog` | `main` con PR 0 | Watchdog Windows/Linux; pruebas de timeout y cleanup. |
| 2 | `AUD-010` | `fix/AUD-010-cli-path-normalization` | `main` con PR 1 | Paths relativos/absolutos y CWD; rebase obligatorio por factory compartido. |
| 3 | `AUD-005` | `fix/AUD-005-remap-references` | `main` con PR 2 | Resolver único, H62 seguro, lint referencial; manifiestos aún no se sellan. |
| 4 | `AUD-007` | `fix/AUD-007-remove-demo-hardcoding` | `main` con PR 3 | Sin branch Demo; self-test real; runner técnico de 30 casos no-Demo. |
| 5 | `AUD-009` | `fix/AUD-009-validator-entrypoint` | `main` con PR 4 | Único entrypoint; secundarios como módulos. |
| 6 | `AUD-008` | `fix/AUD-008-no-bloat-history` | `main` con PR 5 | Dedupe/democión reversible; cero pérdida de autoridad. |
| 7 | `AUD-003` | `fix/AUD-003-baseline-ledger-remap` | `main` con PR 6 | Sello final de árbol, manifests, hashes, ZIP/companion y determinismo. |

Cada rama debe partir del `main` ya actualizado por el PR anterior. Si se usan PRs apilados durante el desarrollo, deben marcarse como tales y retargetearse/rebasarse antes de revisión final. Ningún título o cuerpo de PR debe usar `Fixes`, `Closes` o equivalente para `AUD-003` a `AUD-010`; los issues no se cierran por merge.

## 9. Criterios de aceptación detallados por issue

### 9.1 `AUD-003` / `B-01`

- El ZIP fuente original y su companion tienen ubicación externa, custodia y hash documentados, o existe una decisión explícita y revisada de crear un nuevo baseline candidato.
- El SHA `bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6` no se atribuye a bytes corregidos sin recomputación.
- `testzip` y CRC se ejecutan sobre el artefacto exacto correspondiente.
- Los manifiestos se generan desde el árbol físico final y una segunda ejecución sin cambios produce el mismo resultado.
- Toda ruta indexada existe; no queda ninguna ruta original inexistente después del remapeo; no hay colisiones.
- `MANIFEST.txt`, `SHA256SUMS.txt`, `MANIFEST.json`, punteros y companion son coherentes con su contrato y exclusiones explícitas.
- El resultado solo queda elegible para re-auditoría; no crea release/tag ni cambia el estado global.

### 9.2 `AUD-004` / `B-02`

- La detección de capacidad ocurre antes de acceder a `SIGALRM`, `ITIMER_REAL` o APIs equivalentes.
- Windows y Linux completan `generate` con rc=0 únicamente cuando JSON, ZIP y validación final son válidos.
- El camino de timeout bloquea entrega parcial, limpia staging/heartbeat y termina procesos cooperativos y no cooperativos dentro del límite documentado.
- La restauración de handlers solo ocurre cuando la plataforma los soporta.
- N1 y N10 cubren éxito, error y timeout; no quedan procesos huérfanos.

### 9.3 `AUD-005` / `B-03`

- Existe una única fuente consumible de resolución original→Windows-safe.
- Factory, validator, registries, tests y manifiestos dejan de contener literales activos a targets originales inexistentes.
- H62 se lee mediante `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/H62_CLI_N1_N10_CLEAN_EXIT.json` o mediante el resolver autoritativo equivalente.
- El lint demuestra 0 referencias stale, 0 targets faltantes y 0 colisiones.
- Los casos 452, 453 y 454 dejan de fallar por ausencia de H62 y observan evidencia recomputada, no override.
- El objetivo 506/506 se evalúa nuevamente después de `AUD-007`; un conteo limpio no compensa un self-test falso.

### 9.4 `AUD-006` / `B-04`

- `README.md`/`GOVERNANCE_STATUS.md` o el registro raíz formalmente designado son la única fuente de estado global.
- `ACTIVE_VERSION`, `VERSION_MANIFEST`, governance maps y certificados internos no declaran cierre, `10/10`, `31/31` ni disponibilidad para Demo mientras el root está `EN_REVISION`.
- `READY_FOR_PROJECT_DEMO_GENERATION` queda falso/bloqueado.
- Cualquier fallo, evidencia faltante o cambio del árbol invalida automáticamente los derivados.
- Un scanner de consistencia detecta una mutación contradictoria y reporta 0 contradicciones en el árbol corregido.

### 9.5 `AUD-007` / `B-05`

- No existe una condición ejecutable basada en `project_name == "Proyecto 000 Demo"` ni equivalentes normalizados.
- Cualquier política especial se expresa con campos genéricos de input y es válida para nombres arbitrarios.
- `PROJECT_DEMO_PASS_GATE` y `DEMO_TEMPLATE_READINESS` dejan de actuar como canon activo o se reclasifican como contrato externo posterior.
- El caso `FACTORY_HARDCODED_DEMO_BRANCH_BLOCKED` inspecciona/ejecuta la condición real y falla si el patrón se reintroduce.
- El runner de cierre técnico contiene exactamente 30 casos N1..N10 × tres niveles y no genera Demo.

### 9.6 `AUD-008` / `B-06`

- Cada grupo de hash duplicado tiene una copia canónica o una justificación de retención explícita y mínima.
- Los hitos H activos se convierten a reglas estables o se demueven a `14_HISTORICAL_NON_AUTHORITY`.
- La evidencia extensa se conserva fuera del runtime o se compacta sin perder pointers necesarios.
- Todo movimiento/eliminación dispone de manifest de antes/después y plan de reversa.
- No se elimina investigación canónica ni evidencia requerida por el validator único.
- Los controles no-bloat/no-history se recomputan sobre el árbol final; el plan no anticipa su decisión.

### 9.7 `AUD-009` / `B-07`

- Existe exactamente un entrypoint público capaz de emitir el resultado global del motor.
- Los validadores secundarios son módulos importables o tareas internas y no pueden emitir cierre global por ejecución directa.
- El registry QA enumera cada módulo, dependencia, fail code y orden de agregación sin duplicidad.
- La misma entrada produce resultado y fail codes deterministas desde el entrypoint.
- Una prueba adversarial que intenta usar un secundario como CLI de cierre queda bloqueada.

### 9.8 `AUD-010` / `B-08`

- `--project`, `--update`, `--output` y paths relacionados se normalizan una sola vez en el borde CLI.
- `update-project` produce el mismo resultado con path absoluto y relativo desde al menos dos CWD.
- `migrate-project` y `update-project-by-engine` preservan su comportamiento con ambas formas de path.
- Paths con espacios y separadores Windows/Linux están cubiertos.
- Un path fuera del root o traversal se rechaza de forma explícita; no se cambia la semántica del update ni el no-drift contract.

## 10. Estrategia de re-auditoría posterior

### 10.1 Precondiciones

- Todos los PRs técnicos están integrados y el árbol está congelado en un commit exacto.
- El checkout de auditoría es nuevo, limpio y no reutiliza outputs de desarrollo.
- El ZIP/companion correspondiente al candidato se obtiene desde autoridad externa y no desde una copia autocertificada dentro del motor.
- El auditor no usa resultados internos como decisión; los recomputa.
- El runner técnico no contiene ni ejecuta un caso Demo.

### 10.2 Capas de recomputación

1. **Autoridad y estado:** root `EN_REVISION`, sin certificados contradictorios ni habilitación de Demo/release.
2. **Baseline:** SHA-256, `testzip`, CRC, stored count, conteos y reconciliación bidireccional manifiesto↔árbol.
3. **Integridad referencial:** mapa Windows-safe, 0 colisiones, 0 stale paths, 0 targets faltantes y H62 resuelto.
4. **Higiene:** no-bloat, no-history, duplicados, staging/temp/logs, defaults y separación ENGINE/PROJECT/AGENT.
5. **CLI por plataforma:** `generate`, `validate`, `update-project`, `migrate-project` y `update-project-by-engine` en Windows y Linux con rutas relativas/absolutas.
6. **Matriz máxima técnica:** N1..N10 × low/intermediate/full, 30 casos no-Demo, con rc, JSON, ZIP, companion, `testzip`, runtime 10+N, Profile360, TechExt y prompt packs recomputados.
7. **Mutation/self-test:** 506 casos con restauración; además se inspecciona que cada caso negativo sea conductual y no una afirmación fija.
8. **Validator único:** enumeración de entrypoints y mutación que intente un cierre alterno.
9. **Repetibilidad:** una segunda ejecución desde clean checkout debe reproducir manifiestos y resultados deterministas salvo campos volátiles declarados y excluidos.

### 10.3 Evidencia mínima de la re-auditoría

- commit SHA auditado;
- OS, Python y dependencias;
- comandos exactos y rc;
- hashes de inputs/outputs;
- tabla de los 24 controles M02;
- tabla de 30 casos;
- tabla de 506 mutaciones;
- reporte de paths stale/collisions;
- reporte de duplicados/historia;
- registro de entrypoints;
- discrepancias y limitaciones sin ocultamiento.

### 10.4 Regla de decisión

Si falta evidencia, existe una sola falla, aparece un workaround, un proceso no termina limpio o una superficie mantiene una contradicción, el motor conserva `EN_REVISION`, los issues permanecen abiertos y no se autoriza M03, Proyecto Demo, release ni tag.

Solo la re-auditoría independiente puede emitir una nueva decisión M02. Este plan no anticipa ni delega esa decisión a los PRs de corrección.

## 11. Registro de riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| ZIP/companion original no recuperable | Alta | Crítico | Gate `AUD-003` temprano; custodia externa; decisión formal de nuevo baseline sin reutilizar SHA. |
| Regenerar manifiestos antes del último cambio | Alta | Crítico | Sello `AUD-003` al final; freeze y segunda ejecución determinista. |
| Conflictos o regresiones en el factory grande | Alta | Alto | PRs separados; merge serial; rebase y pruebas completas tras cada integración. |
| Watchdog funciona solo en un OS | Media | Crítico | CI Windows/Linux y pruebas de timeout cooperativo/no cooperativo. |
| Cleanup de bloat elimina evidencia necesaria | Media | Crítico | Clasificación de autoridad, reverse manifest y `AUD-009` antes de `AUD-008`. |
| Validator único cambia fail codes o orden | Media | Alto | Paridad de outputs, registry explícito y mutaciones de entrypoint alterno. |
| Estado vuelve a derivar a `PASS` por artefactos cacheados | Media | Crítico | Máquina de estados fail-closed, invalidación por hash y scanner de contradicción. |
| Self-test mantiene falsos positivos | Alta | Crítico | Tests conductuales/AST y revisión de cada caso que actualmente contiene resultado fijo. |
| EOL, permisos o normalización alteran hashes | Media | Alto | Clean checkout por OS, reglas de canonicalización explícitas y hashes por bytes. |
| Matriz máxima excede tiempo/recursos | Media | Alto | Presupuesto y timeout por caso; sharding solo si conserva evidencia completa; ningún timeout se convierte en éxito. |
| Movimiento de rutas rompe remapeo Windows-safe | Media | Alto | Validar límite, colisiones y existencia antes y después; resolver único. |
| Merge de un PR cierre issues o habilite release | Baja | Crítico | Sin keywords de cierre; branch protection; checklist explícito; estado raíz `EN_REVISION`. |

## 12. Controles del PR documental `AUD-011`

Este documento debe publicarse en la rama:

```text
docs/AUD-011-plan-correccion-m02
```

El PR asociado debe permanecer en borrador y modificar únicamente:

```text
docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md
```

Validaciones de alcance:

- 0 archivos modificados bajo `engine/IDUNEX/`;
- 1 archivo documental agregado;
- `MOTOR_STATUS=EN_REVISION` preservado;
- ninguna declaración de aprobación global;
- ningún issue cerrado;
- ningún Proyecto Demo generado;
- ningún release o tag creado.

## 13. Próximo paso operativo

1. Revisar y fusionar el PR documental `AUD-011` sin cerrar issues.
2. Abrir el PR técnico aislado de `AUD-006` para instalar el interlock de gobierno.
3. En paralelo, iniciar la recuperación/custodia del ZIP y companion requerida por el tramo A de `AUD-003`.
4. Ejecutar el tren técnico en el orden de la sección 8, manteniendo cada issue abierto para re-auditoría.
5. Solicitar una nueva M02 solo después del sello final de `AUD-003`; no avanzar a M03 ni Proyecto Demo antes de una decisión independiente.

---

**Declaración de control:** este archivo es un artefacto de planificación. No modifica el motor, no corrige los bloqueantes y no convierte ninguna afirmación interna en evidencia aceptada. `MOTOR_STATUS=EN_REVISION` y `M02_FAIL` permanecen vigentes.

