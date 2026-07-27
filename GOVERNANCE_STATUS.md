# GOV — Estado de Gobernanza del Repositorio

La autoridad global vigente es externa al motor y mutable sin alterar su identidad:

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
CONTROLLED_EXTERNAL_DEMO_STATUS=CONSUMED
CONTROLLED_EXTERNAL_DEMO_AUTHORIZED=FALSE
CONTROLLED_EXTERNAL_DEMO_CONSUMED=TRUE
CONTROLLED_EXTERNAL_DEMO_GENERATE_ALLOWED=0
CONTROLLED_EXTERNAL_DEMO_VALIDATE_ALLOWED=0
```

| Superficie | Clasificación | Efecto |
|---|---|---|
| `governance/CURRENT_STATE.json` | AUTORIDAD MUTABLE ÚNICA | Formaliza estado y evidencia M02/M03 |
| Contrato maestro interno | CONTRATO ESTABLE | Valida esquema, transiciones e interlocks; no replica el estado actual |
| Documentos y manifests internos | `NON_AUTHORITY_BUILD_SNAPSHOT` | Trazabilidad de build sin poder de gobernanza |
| Evidencia M02 run `30194513740` | `REFERENCIA_SUSTITUIDA` | Sólo aplica al árbol `c5cb2f4b…`; no aplica al árbol AUD-037 |
| AUD-028 | `CONSUMED` | No reutilizable; contadores de ejecución en cero |
| M03 | BLOQUEADO | Requiere M02 formalizado para el mismo árbol |
| Demo, release, tag, OFICIAL, cierre, agentes | BLOQUEADO | Interlock `EN_REVISION` |

## Reglas de transición

- Sólo se aceptan tokens exactos del esquema estable; no se busca la subcadena `PASS`.
- `M03_PASS` exige `M02_PASS`.
- Cada PASS exige run, job, artifact, artifact SHA, commit e identidad completa del árbol físico.
- Las evidencias M02 y M03 deben corresponder al mismo SHA, file count y byte count.
- Cambiar el estado externo no exige actualizar ninguna superficie de `engine/IDUNEX`.

## AUD-028

La autorización fue consumida el 22 de julio de 2026. Continúan exactamente:

```text
status=CONSUMED
authorized=false
consumed=true
generate_executions_allowed=0
validate_executions_allowed=0
```

## Estado AUD-037

M02 y M03 no fueron ejecutados. No se ejecutó Proyecto 000 Demo, `refresh-external-artifacts`, carga de agentes, release, tag ni promoción a `OFICIAL`. `CREATIVE_OUTPUT_CERTIFIED=FALSE`.
