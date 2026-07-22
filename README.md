# IDUNEX Engine

Repositorio técnico privado para el motor IDUNEX.

## Estado actual

**Estado:** `EN_REVISION`  
**Decisión M02 vigente:** `NOT_RECOMPUTED_POST_AUD030`
**Decisión M03 vigente:** `NOT_RECOMPUTED_POST_AUD030`
**Autoridad de estado:** `governance/CURRENT_STATE.json`  
**Versión declarada de baseline:** `v1.0.0`

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=NOT_RECOMPUTED_POST_AUD030
M03_RESULT=NOT_RECOMPUTED_POST_AUD030
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

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
- La certificación creativa permanece bloqueada:
  `creative_output_certified=false`.
- Release, tag, `OFICIAL`, cierre productivo y carga de agentes permanecen bloqueados.
- Los PASS M02/M03 del árbol anterior son evidencia previa y no aplican al árbol modificado por AUD-030.

## Ejecución externa controlada del Demo

AUD-028 fue utilizada una sola vez y está consumida:

```text
controlled_external_demo_execution.status=CONSUMED
controlled_external_demo_execution.authorized=false
controlled_external_demo_execution.consumed=true
controlled_external_demo_execution.execution_limit=1
controlled_external_demo_execution.execution_count=1
controlled_external_demo_execution.generate_executions_allowed=0
controlled_external_demo_execution.validate_executions_allowed=0
```

Proyecto generado:

```text
IDUNEX_PROJECT_PROYECTO_000_DEMO_v1.0.0.zip
SHA-256=539cc5b7077e12025deefa0304525a9aa8bfaa627a4d408cf01127e8beb8460b
```

La validación operativa del ZIP es `PASS`, pero la auditoría independiente detectó una
desincronización bloqueante entre el content-tree final interno y dos superficies documentales
externas. Estado vigente:

```text
PROJECT_AUDIT_DECISION=PROJECT_AUDIT_FAIL_EXTERNAL_SURFACE_DESYNC
PROJECT_AGENT_LOAD_PASS=false
PROJECT_READY_FOR_PRODUCTION=false
```

No repetir `generate` ni `validate` bajo AUD-028. La corrección se controla mediante el issue #58.

## Corrección AUD-030

El factory autoritativo lee el reporte, certificado, README y las dos pruebas de content-tree
directamente desde el ZIP final reabierto. `write_external_project_artifacts()` ya no usa el
directorio materializado como autoridad documental.

La operación autoritativa de refresco es:

```text
refresh-external-artifacts <project_zip> --output-json <resultado.json>
```

Solo reemplaza atómicamente `*_RELEASE_CERTIFICATE.txt`, `*_FINAL_AUDIT_REPORT.md` y
`*_README_FOR_HUMAN_OPERATOR.md`; exige companion `<project_zip>.sha256`, valida el set externo
5/5 y falla si cambian SHA o tamaño del ZIP o del companion. No ejecuta `generate`, no modifica
gobernanza y no consume ni reactiva AUD-028.

## Siguiente flujo

```text
AUD-028 CONSUMED → AUD-030 implementado pendiente de revisión → M02/M03 post-merge → refresco externo autorizado → auditoría independiente → carga de agentes
```

## Comandos de control

```bash
python tools/audit/intake_audit.py --repo-root .
python tools/audit/governance_state_check.py --repo-root .
python tools/package/package_engine.py --repo-root . --version v1.0.0
```

El estado sigue `EN_REVISION`; no existe release oficial.
