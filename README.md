# IDUNEX Engine

Repositorio técnico privado para el motor IDUNEX.

## Autoridad y estado

`governance/CURRENT_STATE.json` es la única autoridad mutable del estado global. Los documentos y manifests internos de `engine/IDUNEX` conservan únicamente snapshots de build no autoritativos.

```text
STATE_AUTHORITY=governance/CURRENT_STATE.json
MOTOR_STATUS=EN_REVISION
M02_RESULT=NOT_RECOMPUTED_POST_AUD037
M03_RESULT=NOT_RECOMPUTED_POST_AUD037
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
PRODUCTIVE_CLOSURE_AUTHORIZED=FALSE
OFICIAL_AUTHORIZED=FALSE
AGENT_LOAD_AUTHORIZED=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

La frontera introducida por AUD-037 permite formalizar `M02_PASS` o `M03_PASS` en la autoridad externa, con evidencia ligada al árbol físico, sin modificar posteriormente el SHA de `engine/IDUNEX`. `NOT_RECOMPUTED` debe llevar siempre el sufijo `POST_AUDnnn` del issue vigente y los tokens PASS son exactos; una cadena que sólo contenga la palabra `PASS` no es válida.

Cada PASS exige resultado técnico, auditoría independiente, clasificación de evidencia vigente y formalización explícita de gobernanza. La decisión de origen `NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY` se conserva para trazabilidad, pero no constituye autoridad por sí sola.

La transición futura a `OFICIAL` está definida por un contrato estable dentro del motor y evidencia concreta versionada en `CURRENT_STATE`: M02/M03 para el mismo árbol, auditoría del motor, Demo generado y auditado, runtime ChatGPT, runtime Copilot PASS o limitación válida, auditoría de carga/runtime y formalización productiva. Mientras falte una capa, la transición falla cerrada.

## Interlocks

Mientras `MOTOR_STATUS=EN_REVISION`, continúan bloqueados:

- Proyecto 000 Demo y cualquier generación general;
- release, tag y estado `OFICIAL`;
- cierre productivo y carga de agentes;
- certificación de output creativo.

AUD-028 permanece `CONSUMED`, no autorizado y sin ejecuciones `generate` o `validate` disponibles.

## Evidencia M02 sustituida

El run `30194513740`, job `89773509632`, artifact `8629888949` y artifact SHA-256 `797d705d9e75317f0cb8dacebcee22e1376369bfadae05ad453943988ad14dde` constituyen evidencia técnica validada sólo para el árbol anterior `c5cb2f4bd63bc8116ad806ebffa31b135a5e61441594cbb07acf4bf7f0fe469e` (`981` archivos, `47324981` bytes). Su decisión fue `NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY`; para el árbol AUD-037 queda como `REFERENCIA_SUSTITUIDA` y `current_tree_applicability=false`.

## Flujos

M02 queda preparado para una única ejecución manual futura sobre la identidad AUD-037. M03 exige primero un `M02_PASS` formalizado para el mismo árbol, por lo que permanece bloqueado en el estado actual. Este cambio no ejecuta M02, M03, Demo, refresh real ni carga de agentes.

## Comandos de control

```bash
python -B engine/IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py engine/IDUNEX
python -B tools/audit/governance_state_check.py --repo-root .
python -B tools/audit/baseline_scanner.py --repo-root .
```

No existe release oficial.
