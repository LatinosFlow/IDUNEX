# IDUNEX Engine

Repositorio técnico privado para el motor IDUNEX.

## Estado actual

**Estado:** `EN_REVISION`  
**Decisión M02 vigente:** `M02_PASS_RECOMPUTED_POST_PR44`  
**Decisión M03 vigente:** `M03_PASS_RECOMPUTED_POST_PR44`  
**Autoridad de estado:** `governance/CURRENT_STATE.json`  
**Versión declarada de baseline:** `v1.0.0`

Este repositorio contiene el motor extraído en `engine/IDUNEX/`. Los documentos históricos se conservan en `governance/authority/REFERENCIA/` y la autoridad operativa activa en `governance/authority/ACTIVO/`.

## Regla de autoridad

- GitHub controla código, estructura técnica, pruebas, issues, PRs y releases.
- SharePoint/OneDrive conserva los artefactos documentales empresariales oficiales.
- No se acepta `PASS` declarado sin recomputar.
- `governance/CURRENT_STATE.json` es la única autoridad legible por máquina del estado global.
- La generación general del Proyecto Demo permanece bloqueada: `ready_for_project_demo_generation=false`.
- La certificación creativa permanece bloqueada: `creative_output_certified=false`.
- Release, tag, `OFICIAL`, cierre productivo y carga de agentes permanecen bloqueados.

## Ejecución externa controlada del Demo

AUD-028 define una única ejecución externa en ChatGPT normal, sujeta íntegramente al objeto `controlled_external_demo_execution` de `CURRENT_STATE.json`.

Esta excepción no habilita generación general. Debe utilizar exactamente el paquete, Informe Maestro y prompt fijados por SHA en la autoridad machine-readable. Cuando `generate` comience, la autorización queda consumida y no puede reutilizarse.

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
