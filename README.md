# IDUNEX Engine

Repositorio técnico privado para el motor IDUNEX.

## Estado actual

**Estado:** `EN_REVISION`  
**Decisión M02 vigente:** `M02_PASS_RECOMPUTED_POST_PR44`  
**Decisión M03 vigente:** `M03_PASS_RECOMPUTED_POST_PR44`  
**Autoridad de estado:** `governance/CURRENT_STATE.json`  
**Versión declarada de baseline:** `v1.0.0`

El motor está extraído en `engine/IDUNEX/`. Los documentos históricos se conservan en
`governance/authority/REFERENCIA/` y la autoridad operativa activa en
`governance/authority/ACTIVO/`.

## Regla de autoridad

- GitHub controla código, estructura técnica, pruebas, issues, PRs y releases.
- SharePoint/OneDrive conserva los artefactos documentales empresariales oficiales.
- No se acepta `PASS` declarado sin recomputar.
- `governance/CURRENT_STATE.json` es la única autoridad legible por máquina del estado global.
- La generación general del Proyecto Demo permanece bloqueada:
  `ready_for_project_demo_generation=false`.
- Release, tag, `OFICIAL`, cierre productivo, carga de agentes y certificación creativa
  permanecen bloqueados.

## Ejecución externa controlada del Demo

AUD-028 autoriza una única ejecución externa en ChatGPT normal:

```text
controlled_external_demo_execution.status=AUTHORIZED_NOT_CONSUMED
controlled_external_demo_execution.authorized=true
controlled_external_demo_execution.consumed=false
controlled_external_demo_execution.execution_limit=1
controlled_external_demo_execution.generate_executions_allowed=1
controlled_external_demo_execution.validate_executions_allowed=1
```

Esta excepción no habilita generación general. Debe utilizar exactamente el paquete, Informe Maestro
y prompt fijados por SHA en `CURRENT_STATE.json`. Cuando `generate` comience, la autorización queda
consumida y no puede reutilizarse.

## Siguiente flujo

```text
AUD-028 autorizado → ejecución externa única → marcar CONSUMED → auditoría independiente del Demo → carga agente → evaluación productiva
```

## Comandos de control

```bash
python tools/audit/intake_audit.py --repo-root .
python tools/audit/governance_state_check.py --repo-root .
python tools/package/package_engine.py --repo-root . --version v1.0.0
```

El estado sigue `EN_REVISION`; no existe release oficial.
