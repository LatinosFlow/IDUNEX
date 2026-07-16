# IA-IDUNEX — Auditoría forense independiente del motor M02

**Expediente:** `AUD-002`  
**Issue padre:** `AUD-001`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Fecha de corte:** 2026-07-16  
**Commit auditado de `main`:** `9dc3aef0b5cd872399a9c123d69043296da38aee`  
**Versión declarada:** `v1.0.0`  
**Estado del informe:** `EN_REVISION`  
**Decisión M02:** `M02_FAIL`

## 1. Resumen ejecutivo

La auditoría independiente no confirma el cierre técnico M02 del motor IDUNEX v1.0.0. La decisión es **M02_FAIL**.

El resultado se obtuvo sin aceptar los estados `PASS` contenidos en los artefactos del propio motor. Se reconstruyó el inventario desde los manifiestos, se aplicó y contrastó el remapeo Windows-safe, se inspeccionaron los blobs relevantes del commit auditado y se ejecutó una copia forense del factory exacto fuera de `engine/IDUNEX/`.

Los bloqueantes principales son:

1. El baseline declarado no es reproducible desde el commit auditado: no se dispuso del ZIP fuente ni de su companion para recalcular el SHA-256 `bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6` y ejecutar `testzip` de forma independiente.
2. El remapeo Windows-safe no fue propagado a los manifiestos ni a todas las referencias de código: las 475 rutas del motor incluidas en el mapa permanecen con el nombre original en el manifiesto y no con el nombre físico remapeado.
3. `generate` falla en Windows antes de iniciar la generación por el uso no protegido de `signal.SIGALRM`.
4. La matriz N1..N10 × tres niveles de información terminó con **0 PASS y 30 FAIL**.
5. `mutation-self-test` terminó **503/506**, con tres fallos asociados a una referencia H62 anterior al remapeo.
6. Existe lógica activa acoplada al nombre `Proyecto 000 Demo`, aunque la autoridad prohíbe nombres demo como canon activo y el propio self-test declara lo contrario.
7. Hay contradicción entre el estado raíz `EN_REVISION` y artefactos internos que declaran `31/31 PASS`, `10/10` y disponibilidad para demo.

No se modificó el motor, no se generó Proyecto Demo, no se creó release ni tag y no se cerraron issues.

## 2. Estado general

| Estado | Cantidad |
|---|---:|
| PASS | 10 |
| FAIL | 12 |
| EN_REVISION | 2 |
| Total | 24 |

Un `PASS` en esta tabla significa que el control específico pudo sostenerse con evidencia inspeccionada o ejecutada. No implica aprobación global. Cualquier control bloqueante en `FAIL` impide `M02_PASS`.

## 3. Alcance y método

### 3.1 Alcance

Se auditaron:

- la autoridad maestra bajo `governance/authority/REFERENCIA/`;
- el estado y los manifiestos de gobierno del repositorio;
- el árbol lógico del motor bajo `engine/IDUNEX/`;
- la coherencia del remapeo Windows-safe;
- factory, CLI, validadores, contratos, Profile360, TechExt, research, runtime, prompt packs, outputs, actualización y migración;
- matriz N1..N10 × `low-info`, `intermediate-info` y `full-info`;
- `mutation-self-test`.

### 3.2 Método

1. Se tomó como corte el commit de `main` indicado arriba.
2. Los archivos fueron recuperados como blobs exactos mediante la interfaz del repositorio.
3. Los PDF de autoridad fueron extraídos y renderizados para comprobación textual y visual.
4. Se reconstruyó el inventario a partir de `SHA256SUMS.txt`/`MANIFEST.txt` y se aplicaron las transformaciones declaradas en `WINDOWS_PATH_SAFE_REMAP.json`.
5. El factory y el runner se copiaron a un área de auditoría fuera de `engine/IDUNEX/`; el contenido del motor no fue editado.
6. Las ejecuciones se realizaron en Windows con Python 3.12.13 y `python-docx` 1.2.0.
7. Los resultados declarados dentro del repositorio se trataron únicamente como afirmaciones a contrastar.

### 3.3 Limitaciones

- No se localizó como blob recuperable en el commit auditado el ZIP fuente descrito por `REPOSITORY_MANIFEST.yml`, ni un companion que permitiera recalcular el baseline físico. Por la regla de evidencia faltante, el control de baseline es `FAIL`.
- No se dispuso de un checkout Git local completo. La inspección se realizó sobre blobs exactos y sobre el inventario transformado. Los controles que requerían el árbol físico completo no fueron elevados a `PASS` cuando la evidencia resultó insuficiente.
- El runner canónico contiene un caso adicional llamado `H238_DEMO_N2`. No se ejecutó porque la orden de auditoría prohíbe generar Proyecto Demo. Para la matriz requerida se utilizó una envoltura de auditoría de 30 casos que omitió exclusivamente ese caso; el factory ejecutado permaneció exacto. La nomenclatura del runner se mapeó así: `basic` = low-info, `intermediate` = intermediate-info y `complete` = full-info.
- La ejecución instrumental que protegió temporalmente `SIGALRM` se usó solo para diagnóstico y nunca como base de un `PASS`.

## 4. Autoridad y archivos revisados

### 4.1 Raíz y gobierno

- `README.md`
- `GOVERNANCE_STATUS.md`
- `REPOSITORY_MANIFEST.yml`
- `governance/baseline/WINDOWS_PATH_SAFE_REMAP.json`
- `governance/baseline/WINDOWS_PATH_SAFE_REMAP.md`
- `governance/authority/REFERENCIA/Informe_Maestro_Go_07d4ad84.pdf`
- `governance/authority/REFERENCIA/IDUNEX_MOTOR_v1_0__49f2b895.pdf`
- `governance/authority/REFERENCIA/IDUNEX_MOTOR_v1_0__91fec215.pdf`
- `governance/authority/REFERENCIA/IDUNEX_MOTOR_v1_0__29dfbebb.txt`

El Informe Maestro establece, entre otros criterios, separación estricta ENGINE/PROJECT/AGENT, ausencia de defaults propios o demo, no-bloat, no-history activo y cierre solo con CLI, matriz, update/migration y mutation en PASS.

### 4.2 Estado y manifiestos internos

- `engine/IDUNEX/ACTIVE_VERSION.md`
- `engine/IDUNEX/VERSION_MANIFEST.json`
- `engine/IDUNEX/MASTER_GOVERNANCE_MAP.json`
- `engine/IDUNEX/RELEASE_CERTIFICATE.txt`
- `engine/IDUNEX/ENGINE_PROJECT_AGENT_LEVEL_CONTRACTS.json`
- `engine/IDUNEX/SHA256SUMS_POINTER.txt`
- `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt`
- `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/MANIFEST.txt`
- `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/MANIFEST.json`

`SHA256SUMS.txt` y `MANIFEST.txt` son el mismo blob. Ambos indexan 971 archivos; `MANIFEST.json` declara seis manifiestos autoexcluidos, lo que reconcilia el total declarado de 977 entradas.

### 4.3 Implementación y contratos

- `engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py`
- runner canónico N1..N10 localizado mediante el manifiesto y el remapeo
- `engine/IDUNEX/07_QA_VALIDATION/.../VALIDATE_IDUNEX_RUNTIME.py`
- registro canónico Profile360 00..60
- registro TechExt full 10/10 remapeado
- contrato runtime ChatGPT/Copilot 10+N remapeado
- política y registros del corpus research
- protocolos de update/migration
- contratos de salida bajo `12_OUTPUT_CONTRACTS/`
- registro de validadores QA remapeado
- evidencia H62 remapeada a `H62_CLI_N1_N10_CLEAN_EXIT.json`

## 5. Matriz de auditoría M02

| # | Control | Estado | Evidencia recomputada |
|---:|---|---|---|
| 1 | Integridad del baseline | **FAIL** | El SHA-256 figura de forma concordante en documentos, pero no se pudo recalcular sin ZIP/companion. Además, el ledger interno conserva 475 rutas anteriores al remapeo. |
| 2 | Separación ENGINE / PROJECT / AGENT | **FAIL** | Existe contrato declarativo, pero el factory contiene una rama activa por nombre de proyecto demo y el motor conserva fixtures/evidencia de proyecto activa. |
| 3 | Versionado semántico limpio | **PASS** | `v1.0.0` y el nombre del factory usan SemVer limpio, sin sufijo de versión paralela. |
| 4 | No-bloat | **FAIL** | En el inventario activo se detectaron 18 grupos de hashes duplicados, 38 archivos implicados y al menos 215,922 bytes redundantes; además hay 169 rutas activas con nomenclatura de hitos H. |
| 5 | No-history activo | **FAIL** | Aunque 24 archivos están aislados en `14_HISTORICAL_NON_AUTHORITY`, permanecen 169 artefactos H activos fuera de esa zona, incluidos reportes y pruebas de hitos. |
| 6 | No-staging | **PASS** | Tras aplicar el remapeo a las 971 rutas indexadas no aparecen segmentos activos `staging`. |
| 7 | No-temp | **PASS** | No aparecen segmentos activos `temp`/`tmp`, `.pyc` ni ZIP internos en el inventario transformado. |
| 8 | No logs largos activos | **PASS** | No aparecen directorios `logs`/`heartbeat` ni archivos de log activos en el inventario transformado. |
| 9 | No default activo de LatinosFlow | **PASS** | No hay `LatinosFlow` en rutas del motor ni en el factory como valor por defecto activo. Las menciones de procedencia en autoridad no se trataron como default. |
| 10 | No Proyecto 000 Demo activo | **FAIL** | El factory compara de forma explícita `project_name == "Proyecto 000 Demo"`; también existen gates demo activos. |
| 11 | No nombres demo como canon activo | **FAIL** | Hay lógica y nombres demo en la ruta activa. El self-test declara que el factory opera por campos, pero la inspección del código demuestra un branch por nombre. |
| 12 | Factory único | **PASS** | Se identificó un solo `IDUNEX_PROJECT_FACTORY_v1.0.0.py`; runner y packer no son factories paralelos. |
| 13 | Validator único | **FAIL** | Hay 24 scripts Python activos fuera del histórico; 21 corresponden a validadores o implementaciones de validación. El registro declara 114 validadores y no existe un único ejecutable efectivo. |
| 14 | Profile360 | **PASS** | Registro 00..60 con 61 secciones; la validación directa N1 reportó 61/61. |
| 15 | TechExt | **PASS** | Registro full 10/10 con 284 campos; la validación directa N1 reportó 284/284. |
| 16 | Research corpus conectado | **PASS** | Política con 24 dominios y 5 punteros; el proyecto N1 de prueba produjo 49 filas de source ledger y superó su validación directa. |
| 17 | Runtime ChatGPT/Copilot 10+N | **EN_REVISION** | Contrato estructural 10+N y prueba directa N1 con 11 cargas por runtime; no se eleva a PASS porque la matriz ejecutable N1..N10 falló. |
| 18 | Prompt packs A-J | **EN_REVISION** | La prueba directa N1 validó los packs, pero la cobertura completa N1..N10 no pudo completarse por el fallo de `generate`. |
| 19 | Output contracts | **FAIL** | Existen contratos declarativos, pero el lifecycle no produce de forma fiable JSON/ZIP mediante el comando público de generación en Windows. |
| 20 | Update/migration contracts | **PASS** | `validate-update-contract`, update con rutas absolutas y SHA activo, migrate y update-by-engine completaron en PASS. El defecto de rutas relativas se registra en CLI. |
| 21 | CLI lifecycle | **FAIL** | `generate` cae por `SIGALRM`; `update-project` con rutas relativas cae por normalización inconsistente. |
| 22 | Generate, validate, update y migrate | **FAIL** | `validate`, update absoluto y migrate pasan, pero `generate` falla y update relativo produce excepción. El conjunto no puede marcarse PASS. |
| 23 | Matriz N1..N10 × tres niveles | **FAIL** | 30 casos ejecutados, 0 PASS, 30 FAIL; todos quedan sin JSON/ZIP porque el subcomando `generate` retorna código 1. |
| 24 | Mutation/self-test | **FAIL** | 506 mutaciones: 503 PASS y 3 FAIL. Resultado global FAIL y restauración PASS. |

## 6. Evidencia ejecutable

### 6.1 `generate`

El factory exacto ejecuta `signal.getsignal(signal.SIGALRM)` antes de entrar en su bloque de manejo. En Windows, `signal.SIGALRM` no existe. El comando termina con `AttributeError`, código de retorno 1 y sin JSON/ZIP final.

Impacto: bloquea el punto de entrada público de generación, el lifecycle y toda la matriz de proyecto en Windows.

### 6.2 Validación directa N1

Para distinguir un defecto de CLI de un defecto total del modelo de datos, se importó el factory exacto y se invocaron sus funciones sobre un proyecto no-demo N1 en el área de auditoría. El proyecto fue refrescado y validado. Después, el subcomando exacto `validate` terminó en PASS con:

- `validators_fail = 0`;
- `blocking = 0`;
- Profile360 = 61/61;
- TechExt = 284/284;
- runtime upload count = 11.

Esta prueba acredita componentes internos concretos, pero no compensa el fallo del comando público `generate` ni representa la matriz completa.

### 6.3 Update y migration

- `validate-update-contract`: PASS para un contrato de cambio de wardrobe.
- `update-project` con rutas relativas: FAIL por `ValueError` al comparar un archivo absoluto con un `project_root` relativo.
- `update-project` con rutas absolutas y `IDUNEX_ENGINE_ZIP_SHA256` igual al baseline declarado: PASS.
- `migrate-project` con rutas absolutas, misma versión y SHA activo: PASS.
- `update-project-by-engine`: PASS.

Impacto: las capacidades existen, pero el comportamiento depende innecesariamente de cómo el usuario exprese la ruta.

### 6.4 Matriz 30 casos

| Métrica | Resultado |
|---|---:|
| Niveles N | 10 |
| Perfiles de información | 3 |
| Casos totales | 30 |
| PASS | 0 |
| FAIL | 30 |
| Duración observada | 33.266 s |

Los treinta casos invocaron el factory exacto. El resultado uniforme fue `generate_rc = 1`, JSON faltante y ZIP faltante debido al defecto de `SIGALRM`.

### 6.5 Mutation/self-test

| Métrica | Resultado |
|---|---:|
| Mutaciones | 506 |
| PASS | 503 |
| FAIL | 3 |
| Fixture positivo | PASS |
| Restauración | PASS |
| Resultado global | FAIL |

Casos fallidos:

- 452 — H18 profile generic decollision;
- 453 — H19 precheck cloning;
- 454 — H20 adversarial N10 generic CLI.

Los tres observaron ausencia de la prueba H62. El factory todavía busca el nombre largo anterior al remapeo, mientras que el archivo físico fue remapeado a `H62_CLI_N1_N10_CLEAN_EXIT.json`.

Además, el caso `FACTORY_HARDCODED_DEMO_BRANCH_BLOCKED` se marca PASS con el texto de que el factory opera por campos y no por nombres. Esto es un falso positivo: el factory contiene la comparación literal con `Proyecto 000 Demo`.

## 7. Hallazgos bloqueantes

### B-01 — Baseline físico no reproducible y ledger desactualizado

**Evidencia por ruta**

- `README.md`
- `REPOSITORY_MANIFEST.yml`
- `governance/authority/REFERENCIA/IDUNEX_MOTOR_v1_0__29dfbebb.txt`
- `governance/baseline/WINDOWS_PATH_SAFE_REMAP.json`
- `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/SHA256SUMS.txt`

Los documentos concuerdan en el SHA declarado, pero no sustituyen el recálculo del ZIP. El mapa contiene 487 transformaciones, de las cuales 475 afectan al motor. Las 475 rutas originales aparecen en el ledger y ninguna de las 475 rutas seguras aparece allí. Una ruta original de muestra devuelve ausencia y su ruta segura existe.

**Causa raíz:** el remapeo posterior a la extracción no disparó una reescritura transaccional de rutas ni una regeneración de todos los manifiestos.

**Riesgo:** no puede demostrarse que el árbol auditado corresponde byte por byte al baseline; validadores y pruebas pueden leer rutas inexistentes.

**Corrección recomendada:** aportar el ZIP y companion originales, recalcular SHA-256 y `testzip`, regenerar manifiestos desde el árbol físico y agregar un control que exija que toda ruta indexada exista después del remapeo.

### B-02 — Incompatibilidad Windows del comando `generate`

**Evidencia por ruta**

- `engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py`

**Causa raíz:** dependencia directa de `signal.SIGALRM` sin detección de plataforma y antes del bloque de recuperación.

**Riesgo:** imposibilidad de generar proyectos mediante el CLI soportado en Windows; 30/30 casos de matriz fallan.

**Corrección recomendada:** implementar watchdog multiplataforma, proteger el acceso con detección de capacidad y agregar pruebas obligatorias en Windows y Linux.

### B-03 — Remapeo no propagado al código y al self-test

**Evidencia por ruta**

- `governance/baseline/WINDOWS_PATH_SAFE_REMAP.json`
- factory v1.0.0
- `engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/.../H62_CLI_N1_N10_CLEAN_EXIT.json`
- `engine/IDUNEX/07_QA_VALIDATION/.../VALIDATE_IDUNEX_RUNTIME.py`

El factory y el runtime validator conservan referencias a múltiples nombres originales. El efecto fue ejecutable en los tres fallos de mutación H18-H20.

**Causa raíz:** cambio de nombres aplicado al filesystem, pero no al grafo de referencias de Python, registries, pruebas y manifiestos.

**Riesgo:** falsos faltantes, cobertura de validación incompleta y posibilidad de estados PASS producidos por overrides en lugar de evidencia disponible.

**Corrección recomendada:** construir una tabla única original→segura consumida por runtime, migrar todas las referencias y prohibir literales de rutas gobernadas mediante un lint de integridad referencial.

### B-04 — Estados PASS activos contradictorios

**Evidencia por ruta**

- `README.md` y `GOVERNANCE_STATUS.md`: `EN_REVISION`.
- `engine/IDUNEX/ACTIVE_VERSION.md`: cierre técnico PASS y ready for demo.
- `engine/IDUNEX/VERSION_MANIFEST.json`: `31/31 PASS`.
- `engine/IDUNEX/MASTER_GOVERNANCE_MAP.json`: `31/31 PASS`.
- `engine/IDUNEX/RELEASE_CERTIFICATE.txt`: ready.

**Causa raíz:** el estado autoemitido por el motor se usa como autoridad paralela sin invalidación al cambiar el baseline o fallar pruebas independientes.

**Riesgo:** habilitación prematura de demo/release y trazabilidad ambigua.

**Corrección recomendada:** establecer una sola máquina de estados gobernada desde raíz; ante cualquier cambio de árbol o fallo M02, degradar automáticamente todos los certificados derivados a `EN_REVISION`.

### B-05 — Acoplamiento activo a Demo y falso positivo de mutación

**Evidencia por ruta**

- factory v1.0.0, comparación literal `Proyecto 000 Demo`.
- gates activos `PROJECT_DEMO_PASS_GATE` y `DEMO_TEMPLATE_READINESS`.
- caso de mutación `FACTORY_HARDCODED_DEMO_BRANCH_BLOCKED`.

**Causa raíz:** una excepción demo fue incorporada al comportamiento del factory y el self-test valida una afirmación, no la ausencia real del patrón.

**Riesgo:** contaminación PROJECT_LEVEL dentro de ENGINE_LEVEL y prueba de cumplimiento engañosa.

**Corrección recomendada:** eliminar la rama por nombre propio; expresar cualquier política mediante campos genéricos y convertir la mutación en una búsqueda/ejecución negativa real.

### B-06 — No-bloat y no-history activos incumplidos

**Evidencia por ruta**

- 18 grupos de contenido duplicado activo y 38 archivos implicados.
- al menos 215,922 bytes redundantes por duplicación exacta.
- 169 rutas H activas fuera de `14_HISTORICAL_NON_AUTHORITY`.
- `08_EVIDENCE_LINEAGE` representa 27,127,210 bytes del inventario declarado.

**Causa raíz:** acumulación de pruebas de hitos, reportes y copias de autoridad dentro del runtime distribuible.

**Riesgo:** ambigüedad de autoridad, superficie de validación excesiva y deriva de contenido.

**Corrección recomendada:** conservar una sola copia canónica por artefacto, mover historia a la zona no autoritativa y generar evidencias voluminosas fuera del motor distribuible.

### B-07 — Validator único no demostrado

**Evidencia por ruta**

- registro QA que declara 114 validadores;
- 21 scripts activos de validación/implementación entre 24 scripts Python activos fuera del histórico;
- `VALIDATE_IDUNEX_RUNTIME.py` como supuesto punto principal.

**Causa raíz:** el término “validator único” se aplica a un registro/orquestador, mientras permanecen múltiples ejecutables independientes.

**Riesgo:** diferentes entradas pueden producir resultados divergentes; aumenta el riesgo de overrides y cierres parciales.

**Corrección recomendada:** exponer un único entrypoint autoritativo, convertir el resto en módulos no ejecutables y probar que ningún segundo CLI puede emitir un cierre global.

### B-08 — Normalización inconsistente de rutas en update

**Evidencia por ruta**

- factory v1.0.0, flujo `update-project` y función de reemplazos semánticos limitados.

**Causa raíz:** mezcla de `Path` absoluto para archivos con `project_root` relativo al calcular pertenencia.

**Riesgo:** fallos dependientes del directorio de trabajo y UX no determinista.

**Corrección recomendada:** resolver y normalizar todas las rutas en el borde del CLI y mantener una única representación interna.

## 8. Hallazgos no bloqueantes y observaciones positivas

### NB-01 — El remapeo es estructuralmente seguro, pero incompleto

Al transformar las 971 rutas indexadas se obtienen 971 rutas únicas, sin colisiones; la longitud relativa máxima observada es 111 y ninguna supera el límite declarado de 125. El impacto del remapeo es, por tanto, **correctivo en nombres físicos pero bloqueante en integridad referencial**.

### NB-02 — Componentes internos validados de forma aislada

Profile360, TechExt, research y el runtime N1 mostraron resultados funcionales al evitar el punto de fallo del CLI. Son activos recuperables para la corrección, pero no autorizan el cierre.

### NB-03 — Controles de higiene básicos

El inventario transformado no muestra staging, temp, logs activos, `.pyc` ni ZIP internos. Tampoco se detectó un default activo de LatinosFlow en factory/rutas.

## 9. Causa raíz consolidada

La causa sistémica es una ruptura entre cuatro capas que deberían cambiar de forma atómica:

1. árbol físico remapeado;
2. manifiestos y hashes;
3. referencias ejecutables y self-tests;
4. estado de gobierno/certificación.

A esto se suman dos defectos independientes: un watchdog Unix-only en una ruta soportada para Windows y normalización tardía de rutas en update. La acumulación de evidencia histórica dentro del motor amplifica las contradicciones y dificulta identificar la autoridad efectiva.

## 10. Recomendaciones de corrección

Orden propuesto:

1. Congelar cualquier activación de demo, release o tag.
2. Restaurar una fuente física verificable del baseline o declarar formalmente un nuevo baseline después de la corrección.
3. Hacer transaccional el remapeo: filesystem, manifiestos, hashes, referencias Python, registries y pruebas.
4. Corregir `generate` con un watchdog multiplataforma y probarlo en Windows/Linux.
5. Normalizar rutas CLI a absolutas al inicio de cada comando.
6. Eliminar toda lógica por nombre demo y reparar la mutación que hoy da falso positivo.
7. Consolidar validator y deduplicar evidencia/historia activa.
8. Invalidar certificados PASS derivados y mantener `EN_REVISION` hasta una nueva auditoría.
9. Reejecutar, sobre blobs finales exactos: baseline SHA/`testzip`, los 24 controles, matriz 30/30, update/migration y mutation 506/506.

## 11. Recomendación de versionado

No crear release ni tag del estado auditado.

Si `v1.0.0` nunca fue publicado como release oficial, puede mantenerse como candidato `v1.0.0` mientras se corrige, con `EN_REVISION` en un campo de estado separado y no como sufijo SemVer. No debe presentarse como estable hasta aprobar M02.

Si `v1.0.0` ya fue distribuido externamente como versión oficial, las correcciones de compatibilidad Windows, rutas y validación deben publicarse como mínimo en `v1.0.1`, después de superar una nueva M02. No se recomienda reescribir silenciosamente una versión ya publicada.

## 12. Decisión final

**M02_FAIL**

La evidencia disponible y las pruebas ejecutadas impiden certificar M02. Los estados PASS declarados dentro del motor quedan refutados para el commit auditado.

## 13. Próximo paso

Abrir una corrección técnica separada para los bloqueantes B-01 a B-08, mantener `AUD-001` y `AUD-002` abiertos y el motor en `EN_REVISION`, y solicitar una nueva ejecución M02 únicamente cuando existan:

- baseline físico recalculable;
- manifiestos coherentes con el remapeo;
- `generate` funcional en Windows;
- matriz 30/30 PASS sin caso demo;
- mutation/self-test 506/506 PASS;
- un único estado de gobierno sin certificados contradictorios.

---

**Declaración de independencia:** este informe no adopta como evidencia concluyente ningún PASS autoemitido por IDUNEX. Sus conclusiones provienen de la inspección de archivos reales del commit auditado, recálculos de inventario y pruebas ejecutables descritas en el propio informe.

