# IDUNEX Engine

Repositorio técnico privado para el motor IDUNEX.

## Estado actual

**Estado:** `EN_REVISION`  
**Decisión M02 vigente:** `M02_PASS_RECOMPUTED_POST_PR44`  
**Decisión M03 vigente:** `M03_PASS_RECOMPUTED_POST_PR44`  
**Autoridad de estado:** `governance/CURRENT_STATE.json`  
**Versión declarada de baseline:** `v1.0.0`

Este repositorio contiene el motor extraído en:

```text
engine/IDUNEX/
```

Los documentos externos de referencia se ubican en:

```text
governance/authority/REFERENCIA/
```

## Regla de autoridad

- GitHub controla código, estructura técnica, pruebas, issues, PRs y releases.
- SharePoint/OneDrive debe conservar los artefactos documentales empresariales oficiales.
- El ZIP fuente original no debe tratarse como equivalente a un release oficial futuro si no pasa auditoría recomputada.
- No se acepta `PASS` declarado sin recomputar.
- `governance/CURRENT_STATE.json` es la única autoridad legible por máquina del estado global.
- Mientras `MOTOR_STATUS=EN_REVISION`, la generación general del Proyecto Demo, release, tag y cierre productivo permanecen bloqueados.
- `ready_for_project_demo_generation=false` y `creative_output_certified=false` siguen siendo interlocks vigentes.

## Ejecución externa controlada del Demo

AUD-029 incorpora un estado machine-readable separado:

```text
controlled_external_demo_execution.status=PENDING_AUTHORIZATION
controlled_external_demo_execution.authorized=false
controlled_external_demo_execution.consumed=false
controlled_external_demo_execution.execution_limit=1
```

Este objeto no habilita todavía el Proyecto 000 Demo. Solo define una máquina de estados auditable para una futura ejecución externa única en ChatGPT normal:

1. `PENDING_AUTHORIZATION`;
2. `AUTHORIZED_NOT_CONSUMED`;
3. `CONSUMED`.

La capacidad general continúa bloqueada y `PROJECT_DEMO_GENERATION` permanece dentro de `denied_capabilities`. La excepción futura no puede autorizar release, tag, `OFICIAL`, cierre productivo, carga de agentes ni certificación creativa.

## Siguiente flujo

```text
M02 PASS → M03 PASS → reconciliar interlock → autorizar Demo único → Proyecto 000 Demo → auditoría de Demo → carga agente → motor productivo
```

## Comandos iniciales

```bash
python tools/audit/intake_audit.py --repo-root .
python tools/audit/governance_state_check.py --repo-root .
python tools/package/package_engine.py --repo-root . --version v1.0.0
```

El empaquetador escribe artefactos en `dist/`, carpeta excluida de Git.

## Nota de carga Windows-safe

Este paquete usa un remapeo de rutas largas para evitar `Filename too long` en GitHub Desktop sobre Windows. Ver `governance/baseline/WINDOWS_PATH_SAFE_REMAP.md`. El estado sigue siendo `EN_REVISION`; no es release oficial.
