# IA-IDUNEX - Alineacion M03 con identidad vigente post-AUD033

**Estado documental:** `EN_REVISION`
**Control:** `AUD-032` / Issue #63
**Autoridad vigente:** `governance/CURRENT_STATE.json`

## Proposito

Sin ejecutar M03 ni `workflow_dispatch`, se alinean su workflow y harness con la identidad vigente del motor y se incorpora una prueba estatica de paridad entre la autoridad, el baseline fisico, el manifest del repositorio y ambos contratos ejecutables.

## Identidad vigente

```text
ENGINE_FILE_COUNT=981
ENGINE_BYTES=47323574
ENGINE_TREE_SHA256=58454565d354e0f641c1fc4954e867822fd90d4b316c803922a087cd4e7601c7
M03_DECISION=NOT_DECLARED_WORKFLOW_EVIDENCE_ONLY
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

El workflow M03 permanece limitado a `workflow_dispatch`. La prueba de Intake rechaza desalineacion de SHA, bytes, conteo, autoridad, estados M02/M03, activacion automatica e interlocks.

## Estado e interlocks

La autoridad es `AUD-034`, `EN_REVISION`, con `M02_PASS_RECOMPUTED_POST_AUD033` y `NOT_RECOMPUTED_POST_AUD030`. Todas las autorizaciones de Demo, release, tag, cierre productivo, OFICIAL, carga de agentes y certificacion creativa continuan en `false`.

AUD-028 permanece `CONSUMED`, no autorizado y sin ejecuciones generate ni validate disponibles. Esta correccion no declara evidencia M03 nueva ni autoriza una ejecucion.

## Correccion de seguimiento del Draft PR #69

La revision independiente del head `be43ac1b80eb240dc4721b27e52d60562be7b9f1` confirmo `SUCCESS` en Intake (run `30188388173`) y Security (run `30188388184`). Detecto tres brechas: el preflight runtime M03 no verificaba expresamente AUD-028, las mutaciones negativas no aislaban cada divergencia y H113 esperaba el M02 anterior.

El alcance controlado pasa de cinco a seis archivos. El workflow M03 ahora reporta valores requeridos, actuales y mismatches de `controlled_external_demo_execution`, y falla con `FAIL_AUD028_CONSUMED_INTERLOCK` ante cualquier diferencia. La prueba estatica verifica el contrato activo y muta identidad, autoridad, triggers y los cinco campos AUD-028. H113 exige AUD-034 y la autoridad vigente sin alterar su generacion N1 temporal ni las comprobaciones ZIP, companion y certificado.

No hay cambios en `engine/IDUNEX`; M03, `workflow_dispatch`, Demo, release, tag y carga de agentes no se ejecutan. `CREATIVE_OUTPUT_CERTIFIED=FALSE`.

## Reversa

La reversa consiste en revertir el commit correctivo de AUD-032. No altera el arbol del motor ni cambia las decisiones de gobernanza.
