# GOV-IDUNEX-AutorizacionRegeneracionProyecto000DemoPostPR38-20260719-v2-EN_REVISION

**Tipo:** Addendum documental de autorización operativa controlada
**ID:** AUD-023
**Fecha:** 2026-07-19
**Versión:** v2
**Estado:** `EN_REVISION`
**Repositorio:** `LatinosFlow/IDUNEX`
**PR técnico de origen:** `#38`
**Commit técnico autorizado:** `18be3cfc4704ecff7c0187548072de6541410313`
**Destino autorizado:** ChatGPT normal, fuera de GitHub

---

## 1. Resumen ejecutivo

Este documento corrige la copia truncada de AUD-023 y autoriza una única regeneración externa y controlada del Proyecto 000 Demo usando el motor IDUNEX corregido después del merge del PR #38.

La base técnica autorizada es:

- Repositorio: `LatinosFlow/IDUNEX`
- Rama técnica de origen: `main`
- Commit del motor: `18be3cfc4704ecff7c0187548072de6541410313`
- PR de corrección: `#38`
- Estado del PR: `MERGED`
- Motor: `EN_REVISION`
- Versión semántica: `v1.0.0`

Esta autorización constituye una excepción documental acotada para una única ejecución externa y controlada. No modifica `ready_for_project_demo_generation=false`, no autoriza la generación dentro de GitHub y no promueve el estado global del motor.

---

## Control de versión y sustitución

- Documento sustituido:
  `docs/audits/IA-IDUNEX-AutorizacionRegeneracionProyecto000DemoPostPR38-20260719-v1-EN_REVISION.md`
- Estado del documento v1: `SUSTITUIDO`
- Motivo: contenido truncado e incompleto.
- Documento vigente:
  `docs/audits/GOV-IDUNEX-AutorizacionRegeneracionProyecto000DemoPostPR38-20260719-v2-EN_REVISION.md`
- Autoridad vigente: versión v2 después de su merge a `main`.

La versión v1 se conserva únicamente como `REFERENCIA_FORENSE` y no debe utilizarse para autorizar ni ejecutar la regeneración.

---

## 2. Autoridad y antecedentes

AUD-023 complementa AUD-022 exclusivamente para actualizar la identidad del snapshot técnico autorizado.

Después de la primera auditoría externa del Proyecto 000 Demo:

1. Se declaró `PROJECT_AUDIT_FAIL`.
2. Se identificaron 14 hallazgos bloqueantes.
3. Se corrigieron factory, contratos, validators, ledgers, superficies de agentes y finalizer.
4. La corrección fue incorporada mediante el PR #38.
5. El PR #38 fue fusionado mediante squash en `main@18be3cfc4704ecff7c0187548072de6541410313`.

Este documento no sustituye la gobernanza global ni declara cierre de la auditoría externa.

---

## 3. Input exacto autorizado

La regeneración debe utilizar exactamente:

- Archivo: `IDUNEX-Project000-Demo-Input-20260717-v1-EN_REVISION.json`
- SHA-256: `801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`

No se autoriza reconstruir, modificar, completar ni sustituir el input.

---

## 4. Alcance autorizado

Se autoriza una única ejecución controlada para:

1. Usar el motor correspondiente a `18be3cfc4704ecff7c0187548072de6541410313`.
2. Ejecutar el Project Factory con el input exacto.
3. Generar una nueva entrega del Proyecto 000 Demo.
4. Ejecutar el validator canónico.
5. Reabrir y comprobar el ZIP definitivo.
6. Emitir los cinco artefactos externos canónicos:
   - ZIP del proyecto.
   - `.zip.sha256`.
   - `*_RELEASE_CERTIFICATE.txt`.
   - `*_FINAL_AUDIT_REPORT.md`.
   - `*_README_FOR_HUMAN_OPERATOR.md`.
7. Preservar evidencia de aliases, runtime, agent-load, `MODEL_REGISTRY`, `NO_DRIFT_LEDGERS`, Profile360, TechExt, fidelity ledgers y hashes.
8. Preparar la entrega para una nueva auditoría externa independiente.

---

## 5. Entorno autorizado

La regeneración debe realizarse exclusivamente en:

`ChatGPT normal, fuera de GitHub`

GitHub se mantiene como entorno de código, contratos, gobernanza, pruebas, trazabilidad y auditoría técnica.

---

## 6. Restricciones duras

No se autoriza:

- modificar directamente `main`;
- modificar `governance/CURRENT_STATE.json`;
- crear release o tag;
- declarar `MOTOR_STATUS=OFICIAL`;
- declarar cierre productivo;
- declarar `PROJECT_AUDIT_PASS` sin nueva auditoría externa;
- cargar el proyecto en agentes;
- declarar `CREATIVE_OUTPUT_CERTIFIED=true`;
- reutilizar el ZIP temporal de pruebas;
- inventar archivos, SHA, resultados, estados o autoridad.

El estado vigente permanece:

- `MOTOR_STATUS=EN_REVISION`
- `SEMANTIC_VERSION=v1.0.0`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `PRODUCTIVE_CLOSURE_AUTHORIZED=false`
- `CREATIVE_OUTPUT_CERTIFIED=false`

---

## 7. Precondiciones

Antes de generar:

| Control | Resultado requerido |
|---|---|
| Commit del motor | `18be3cfc4704ecff7c0187548072de6541410313` |
| Input SHA-256 | `801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34` |
| `CURRENT_STATE.json` | Sin modificaciones |
| Motor status | `EN_REVISION` |
| Release/tag/OFICIAL | No autorizados |
| PR #38 | `MERGED` |
| Auditoría externa posterior | Pendiente |

Si una precondición falla: `DEMO_REGENERATION_BLOCKED`.

---

## 8. Criterios técnicos mínimos

Resultado requerido:

- `generate_rc=0`
- `validate_rc=0`
- `VALIDATORS_FAIL=0`
- `BLOCKING_WARNINGS=0`
- `FAIL_CODES=[]`
- Runtime ChatGPT: `12`
- Runtime Copilot: `12`
- Agent-load ChatGPT: `10/10`
- Agent-load Copilot: `10/10`
- `Vale` resuelve solo a Valeria Rios Andrade
- `Mateo` resuelve solo a Mateo Vargas Salinas
- `MODEL_REGISTRY=PASS`
- `NO_DRIFT_LEDGERS=PASS`
- Profile360: `61/61` por modelo
- TechExt: `284/284` por modelo
- ZIP reabierto: `PASS`
- Companion SHA: coincide
- Artefactos externos: `5/5`
- `CREATIVE_OUTPUT_CERTIFIED=false`

Un resultado técnico satisfactorio no equivale a `PROJECT_AUDIT_PASS`.

---

## 9. Evidencia obligatoria

Conservar:

1. Input exacto y SHA-256.
2. Motor utilizado y commit técnico.
3. Resultados generate y validate.
4. ZIP y companion SHA.
5. Certificado, informe y README.
6. Matriz de aliases.
7. Conteos de runtime.
8. Cobertura 10/10 por agente.
9. Evidencia de `MODEL_REGISTRY` y `NO_DRIFT_LEDGERS`.
10. Capturas o resumen de ejecución.
11. Warnings, errores o contradicciones.

---

## 10. Ruta posterior

`AUD-023 v2 MERGED → regenerar Demo → validar ZIP → custodiar 5 artefactos → nueva auditoría externa independiente`

Solo la nueva auditoría externa puede declarar `PROJECT_AUDIT_PASS`.

Hasta entonces:

- `PROJECT_AGENT_LOAD_PASS=false`
- `PROJECT_READY_FOR_PRODUCTION=false`
- `CREATIVE_OUTPUT_CERTIFIED=false`

---

## 11. Decisión documental

Se autoriza `CONTROLLED_DEMO_REGENERATION_POST_PR38` con límite de una ejecución.

No se autoriza release, tag, `OFICIAL`, cierre productivo, carga en agentes, `PROJECT_AUDIT_PASS` ni certificación creativa.

---

## 12. Estado final

- `AUD023_STATUS=EN_REVISION`
- `AUD023_PR_STATUS=MERGED`
- `MOTOR_STATUS=EN_REVISION`
- `DEMO_REGENERATION_AUTHORIZED=CONTROLLED_ONLY`
- `CONTROLLED_EXECUTION_LIMIT=ONE`
- `GITHUB_DEMO_EXECUTION_AUTHORIZED=false`
- `AUTHORIZED_ENGINE_COMMIT=18be3cfc4704ecff7c0187548072de6541410313`
- `AUTHORIZED_INPUT_SHA256=801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `OFICIAL_AUTHORIZED=false`

