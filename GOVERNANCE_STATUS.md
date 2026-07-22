# GOV — Estado de Gobernanza del Repositorio

`governance/CURRENT_STATE.json` es la única fuente legible por máquina para el estado global vigente.

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=NOT_RECOMPUTED_POST_AUD030
M03_RESULT=NOT_RECOMPUTED_POST_AUD030
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
CONTROLLED_EXTERNAL_DEMO_EXECUTION_LIMIT=1
CONTROLLED_EXTERNAL_DEMO_EXECUTION_COUNT=1
```

| Superficie | Estado | Decisión |
|---|---|---|
| Motor | EN_REVISION | Factory corregido; M02/M03 pendientes para el nuevo árbol |
| ZIP candidato del motor | REFERENCIA PREVIA | No representa el árbol post-AUD030 |
| Informe Maestro | VALIDADO como autoridad operativa | Fijado por SHA externo |
| Prompt canónico AUD-028 | CONSUMED / EVIDENCIA | No reutilizable para otra ejecución |
| Proyecto 000 Demo | GENERADO / EN_REVISION | ZIP operativo PASS; auditoría independiente no cerrada |
| Auditoría independiente | FAIL BLOQUEANTE | `PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC` |
| Excepción externa AUD-028 | CONSUMED | Sin ejecuciones restantes |
| Release / tag / OFICIAL / cierre | BLOQUEADO | No autorizado |
| Carga de agentes | BLOQUEADO | Solo después de `PROJECT_AUDIT_PASS` |
| Corrección AUD-030 | IMPLEMENTADA / EN_REVISION | Pendiente de revisión del Draft PR y recomputación M02/M03 |

## Máquina de estados

| Estado | Authorized | Consumed | Generate permitido | Decisión |
|---|---:|---:|---:|---|
| `PENDING_AUTHORIZATION` | false | false | 0 | Preparación |
| `AUTHORIZED_NOT_CONSUMED` | true | false | 1 | Una ejecución externa |
| `CONSUMED` | false | true | 0 | Autorización agotada |

AUD-028 fue consumida al comenzar `generate` el 22 de julio de 2026. No existe reintento permitido.
El proyecto generado tiene SHA-256:

```text
539cc5b7077e12025deefa0304525a9aa8bfaa627a4d408cf01127e8beb8460b
```

La auditoría independiente recomputó el content-tree final:

```text
806a308dbefb650687b35d034bd90133997ebb5a3598ae78b41e6f5cb4dc3b35
```

Dos superficies externas conservaron el valor anterior
`f37d5c761bd389e26d3cebfe73ea379d37421dd626b193517229892c1dc70386`.
El hallazgo se controla en el issue #58.

El factory autoritativo ahora deriva las tres superficies documentales externas del ZIP final
reabierto. El subcomando `refresh-external-artifacts` refresca exclusivamente esas superficies,
verifica que ZIP y companion permanezcan byte a byte sin cambios y ejecuta el validador reabierto.
Esta implementación no corrige el ZIP histórico por sí sola, no reabre AUD-028 y no constituye una
auditoría independiente del Proyecto 000 Demo.

## Estados documentales permitidos

- OFICIAL
- VALIDADO
- BORRADOR
- EN_REVISION
- SUSTITUIDO
- ARCHIVADO
- REFERENCIA

## Regla de cierre

La integridad operativa del ZIP no sustituye la auditoría independiente del set externo completo.
No cargar agentes, no promover a producción y no declarar `PROJECT_AUDIT_PASS`. M02 y M03 deben
recomputarse para el nuevo árbol del motor después del merge; la auditoría del Proyecto 000 Demo
continúa fallida hasta un refresco autorizado y una nueva auditoría independiente.

## Corrección AUD-031

La primera recomputación M02 post-AUD030 quedó bloqueada antes de matriz y mutation por una expectativa heredada `M02_PASS` en el contrato activo de validación maestra. AUD-031 sincroniza esa superficie con `NOT_RECOMPUTED_POST_AUD030`, regenera los manifiestos canónicos y exige una nueva ejecución M02 completa.

- Run origen: `29928852782`;
- árbol previo: `8a3c191c266647acd754a56c1e5555ca1a36ab807d2e04e72a5ff21edb3e92bd`;
- árbol post-AUD031: `d6a66c316650a86c64ed20752b39e593f43f25e88b654538095124b7ebfedf8d`;
- M02/M03: `NOT_RECOMPUTED_POST_AUD030`;
- Demo, refresh real, agentes, release, tag y OFICIAL: `BLOQUEADO`.
