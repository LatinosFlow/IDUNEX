# IA-IDUNEX — Alineación M03 con identidad vigente post-AUD033

**Estado documental:** `EN_REVISION`
**Control:** `AUD-032` / Issue #63
**Autoridad vigente:** `governance/CURRENT_STATE.json`

## Propósito

Sin ejecutar M03 ni `workflow_dispatch`, se alinean su workflow y harness con la identidad vigente del motor y se incorpora una prueba estática de paridad entre la autoridad, el baseline físico, el manifest del repositorio y ambos contratos ejecutables.

## Identidad vigente

```text
ENGINE_FILE_COUNT=981
ENGINE_BYTES=47323574
ENGINE_TREE_SHA256=58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7
M03_DECISION=NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

El workflow M03 permanece limitado a `workflow_dispatch`. La nueva prueba de Intake rechaza desalineación de SHA, bytes, conteo, autoridad, estados M02/M03, activación automática e interlocks.

## Estado e interlocks

La autoridad es `AUD-034`, `EN_REVISION`, con `M02_PASS_RECOMPUTED_POST_AUD033` y `NOT_RECOMPUTED_POST_AUD030`. Todas las autorizaciones de Demo, release, tag, cierre productivo, OFICIAL, carga de agentes y certificación creativa continúan en `false`.

AUD-028 permanece `CONSUMED`, no autorizado y sin ejecuciones generate ni validate disponibles. Esta corrección no declara evidencia M03 nueva ni autoriza una ejecución.

## Alcance y validación

El alcance se limita al workflow M03, harness M03, workflow Intake, la prueba estática y este documento. No se modifica `engine/IDUNEX` ni `governance/CURRENT_STATE.json`.

La reversa consiste en revertir el commit de AUD-032. No altera el árbol del motor ni cambia las decisiones de gobernanza.
