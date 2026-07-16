# AUD-006 - Ledger de corrección de estado y certificación

**Issue:** `AUD-006` / `#7`
**Fecha:** 2026-07-16
**Alcance:** gobierno, estado y certificación
**MOTOR_STATUS vigente:** `EN_REVISION`
**M02_RESULT vigente:** `M02_FAIL`

## Autoridad aplicada

- `governance/authority/REFERENCIA/Informe_Maestro_Go_07d4ad84.pdf`.
- `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`.
- Issue `AUD-006` / `#7`.

`governance/CURRENT_STATE.json` queda designado como fuente única legible por máquina para el estado global vigente.

## Clasificación de estados

| Clase | Tratamiento AUD-006 | Autoridad vigente |
|---|---|---|
| PASS histórico o declarativo | `REFERENCIA_HISTORICA_SUSTITUIDA` o `REFERENCIA_SUSTITUIDA` | Ninguna |
| PASS recomputado interno previo | Evidencia acotada de una ejecución anterior; no puede cerrar el motor | Ninguna |
| Estado actual del repositorio | `EN_REVISION` con `M02_FAIL` | `governance/CURRENT_STATE.json` |

## Superficies corregidas

1. Estado raíz: `README.md`, `GOVERNANCE_STATUS.md`, `REPOSITORY_MANIFEST.yml` y `governance/CURRENT_STATE.json`.
2. Control center: `ACTIVE_VERSION`, `STATUS`, ambos `VERSION_MANIFEST`, `PRODUCTIVE_BASE_ENGINE_STATUS`, contratos de niveles y mapa maestro.
3. Certificación: certificados duplicados de `00_INDEX` y `11_RELEASE_INTERNAL`.
4. Evidencia anterior: changelogs, reportes de auditoría final, resúmenes de máquina/matriz y estados finales bajo `11_RELEASE_INTERNAL` y `99_MANIFESTS_SHA_LINEAGE`, marcados como referencia sustituida.
5. Contrato de validación de gobierno: actualizado para exigir el interlock `M02_FAIL`.

Todas las superficies vigentes expresan:

```text
MOTOR_STATUS=EN_REVISION
M02_RESULT=M02_FAIL
READY_FOR_PROJECT_DEMO_GENERATION=FALSE
RELEASE_AUTHORIZED=FALSE
TAG_AUTHORIZED=FALSE
PRODUCTIVE_CLOSURE_AUTHORIZED=FALSE
CREATIVE_OUTPUT_CERTIFIED=FALSE
```

## Regla de interlock

Si existe `M02_FAIL` vigente, ningún certificado interno ni evidencia derivada puede habilitar Proyecto Demo, release, tag o cierre productivo.

## Control automatizado

El comando autoritativo de consistencia es:

```bash
python tools/audit/governance_state_check.py --repo-root .
```

El resultado esperado para este estado es `CONSISTENT`, con `active_contradiction_count=0`. Las pruebas de mutación verifican que una habilitación de Demo bajo `M02_FAIL` sea rechazada.

## Fuera de alcance preservado

- No se generó Proyecto Demo.
- No se modificó factory/generate ni `SIGALRM`.
- No se modificó el remapeo Windows-safe.
- No se limpió bloat ni historia.
- No se consolidaron validadores.
- No se creó release ni tag.
- No se cerró ningún issue.

Este ledger no certifica el motor ni altera la decisión independiente `M02_FAIL`.
