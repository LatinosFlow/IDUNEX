# GOV-IDUNEX — Corrección de emisión externa post-H410

Fecha: 2026-07-22
Versión documental: v1
Estado: EN_REVISION
Control: AUD-030 / issue #58
Base: `fb13a4f5d4bd559b4f1268103630a735b53c8999`

## Decisión

Se corrige el factory autoritativo existente para que las tres superficies documentales externas
se deriven exclusivamente de miembros leídos desde el ZIP final reabierto. El directorio de
proyecto materializado deja de ser autoridad documental para esa emisión.

Se añade al mismo factory la operación `refresh-external-artifacts`. Esta operación no ejecuta
`generate`, no escribe dentro del ZIP, no cambia el companion, no modifica
`governance/CURRENT_STATE.json` y no crea un factory o validator paralelo.

Esta corrección no declara `PROJECT_AUDIT_PASS`, no audita de nuevo el Proyecto 000 Demo, no carga
agentes y no autoriza release, tag, `OFICIAL` o cierre productivo.

## Causa

H410 puede actualizar el ZIP in-place durante la convergencia final. El wrapper atómico publicaba
después las copias externas llamando a `write_external_project_artifacts()` con el directorio de
proyecto ya materializado. Ese directorio podía conservar el reporte y el certificado anteriores a
la última convergencia del ZIP.

La auditoría independiente observó:

- ZIP final SHA-256: `539cc5b7077e12025deefa0304525a9aa8bfaa627a4d408cf01127e8beb8460b`;
- content-tree final interno: `806a308dbefb650687b35d034bd90133997ebb5a3598ae78b41e6f5cb4dc3b35`;
- content-tree obsoleto externo: `f37d5c761bd389e26d3cebfe73ea379d37421dd626b193517229892c1dc70386`.

El ZIP final no se modifica en AUD-030. Esas identidades se conservan únicamente como evidencia del
hallazgo que motivó el cambio de factory.

## Flujo anterior

```text
H410 converge ZIP final
→ wrapper mueve ZIP, companion y directorio materializado
→ write_external_project_artifacts(root, ZIP, companion, validation)
→ reporte/certificado/README externos se copian desde root
→ una superficie root anterior puede reaparecer fuera del ZIP final
```

## Flujo corregido

```text
ZIP final reabierto
→ testzip
→ validación de rutas, duplicados, ambigüedad y root interno único
→ lectura directa de cinco miembros internos
→ igualdad exacta de cuatro claims content_tree_sha256
→ construcción de tres payloads externos con headers fail-closed
→ temporales en el mismo directorio
→ os.replace atómico de cada superficie
→ validación externa 5/5 contra el ZIP reabierto
```

Los cinco miembros fuente obligatorios son:

- `10_RELEASE/FINAL_AUDIT_REPORT.md`;
- `10_RELEASE/RELEASE_CERTIFICATE.txt`;
- `00_PROJECT_INDEX/README_FOR_HUMAN_OPERATOR.md`;
- `09_MANIFESTS_SHA/POST_EXPORT_FINALIZER_REPORT.json`;
- `09_MANIFESTS_SHA/CONTENT_TREE_PROOF_NOT_FINAL_ZIP_SHA.json`.

El mismo `content_tree_sha256` debe aparecer en reporte, certificado, reporte del finalizador y
prueba de content-tree. Una fuente faltante, ilegible, insegura o divergente bloquea la emisión.

## Subcomando autoritativo

```text
refresh-external-artifacts <project_zip> --output-json <resultado.json>
```

El companion se resuelve únicamente como `<project_zip>.sha256`. La operación captura SHA-256 y
tamaño del ZIP y del companion antes del refresco, valida companion y ZIP, reemplaza solo las tres
superficies documentales externas, ejecuta `validate_reopened_zip()` y vuelve a medir ambos archivos.

El resultado JSON incluye identidades antes/después, content-tree, paths externos, fallos,
warnings, failcodes, `ZIP_UNCHANGED`, `COMPANION_UNCHANGED` y
`CREATIVE_OUTPUT_CERTIFIED=false`. El path de `--output-json` no puede ser el ZIP, companion ni una
de las cinco superficies externas protegidas.

## Invariantes de no mutación

- No se abre el ZIP en modo escritura.
- No se extrae el ZIP para construir documentos externos.
- No se escribe el companion.
- El SHA-256 y tamaño del ZIP deben coincidir antes y después.
- El SHA-256 y tamaño del companion deben coincidir antes y después.
- Cualquier divergencia produce `FAIL_EXTERNAL_ARTIFACT_REFRESH_ZIP_MUTATED` o
  `FAIL_EXTERNAL_ARTIFACT_REFRESH_COMPANION_MUTATED`.
- Las escrituras documentales usan temporales locales y reemplazo atómico.

## Failcodes principales

- `FAIL_EXTERNAL_ARTIFACT_INTERNAL_SOURCE_MISSING`;
- `FAIL_EXTERNAL_ARTIFACT_INTERNAL_CONTENT_TREE_MISMATCH`;
- `FAIL_EXTERNAL_ARTIFACT_CONTENT_TREE_MISMATCH`;
- `FAIL_EXTERNAL_ARTIFACT_REFRESH_ZIP_MUTATED`;
- `FAIL_EXTERNAL_ARTIFACT_REFRESH_COMPANION_MUTATED`;
- `FAIL_EXTERNAL_ARTIFACT_ZIP_UNSAFE`;
- `FAIL_EXTERNAL_ARTIFACT_REFRESH_OUTPUT_PATH_PROTECTED`.

## Pruebas sintéticas

`tests/intake/test_external_artifact_refresh.py` cubre derivación desde ZIP, divergencia interna,
content-tree externo obsoleto, fuente faltante, companion incorrecto, no mutación de ZIP, no
mutación de companion, set externo 5/5, ruta no canónica `NOT_APPLICABLE` y miembros duplicados o
ambiguos. `tests/intake/test_post_audit_truthfulness.py` conserva el gate canónico sin invocar
`generate`.

No se versiona ni se abre el ZIP real del Demo y no se ejecutan M02 30/30, mutation 506/506 ni M03
completo localmente.

Validación local final:

- `tests.intake.test_post_audit_truthfulness`: 10/10 PASS;
- `tests.intake.test_external_artifact_refresh`: 11/11 PASS;
- `tests.intake.test_governance_state`: 10/10 PASS;
- `governance_state_check.py`: CONSISTENT, cero contradicciones activas;
- `intake_audit.py`: PASS;
- `security_lite_scan.py`: PASS;
- `baseline_scanner.py`: PASS, manifiestos y companion sincronizados;
- `git diff --check`: PASS.

## Identidad del motor

Identidad previa:

- archivos: `981`;
- bytes: `47,302,063`;
- tree SHA-256: `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`.

Identidad post-AUD030, recalculada por `tools/audit/baseline_scanner.py --write`:

- archivos: `981`;
- bytes: `47,321,777`;
- tree SHA-256: `8a3c191c266647acd754a56c1e5555ca1a36ab807d2e04e72a5ff21edb3e92bd`.

Los seis manifiestos internos no autorreferenciales, el manifiesto físico externo, el companion del
árbol y el diff de baseline fueron regenerados por esa herramienta canónica.

## Gobernanza resultante

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=NOT_RECOMPUTED_POST_AUD030
M03_RESULT=NOT_RECOMPUTED_POST_AUD030
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
AUD-028=CONSUMED
GENERATE_EXECUTIONS_ALLOWED=0
VALIDATE_EXECUTIONS_ALLOWED=0
PROJECT_AUDIT_STATUS=PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC
PROJECT_AGENT_LOAD_PASS=FALSE
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
OFICIAL_AUTHORIZED=FALSE
PRODUCTIVE_CLOSURE_AUTHORIZED=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

Los PASS M02/M03 del árbol anterior permanecen solo como evidencia previa. Las suites deberán
recomputarse sobre el nuevo tree SHA mediante GitHub Actions después del merge. AUD-028 permanece
consumido; no existe reintento ni nueva autorización de ejecución.

## Estado del proyecto y agentes

El Proyecto 000 Demo continúa `PROJECT_GENERATED_NOT_AUDITED` con decisión vigente
`PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC`. Esta implementación no refresca el artefacto real, no
repite auditoría independiente y no habilita carga de agentes.

## Reversión

La reversión consiste en revertir el commit AUD-030 completo, nunca en editar el ZIP del Demo ni el
companion. Después de una reversión se deben regenerar nuevamente los manifiestos mediante el
scanner canónico y mantener M02/M03 como no vigentes para cualquier árbol resultante hasta su
recomputación. El stash local previo a esta tarea no forma parte del cambio ni del PR.
