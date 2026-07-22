# GOV-IDUNEX-ActivacionPromptCanonicoProyecto000Demo-20260722-v1-EN_REVISION

**Tipo:** Activación documental de prompt canónico  
**ID:** `AUD-028-PROMPT`  
**Fecha:** `2026-07-22`  
**Versión:** `v1`  
**Estado:** `EN_REVISION`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Issue de control:** `#53`  
**Autoridad global:** `governance/CURRENT_STATE.json`  
**Motor:** `EN_REVISION`  
**CREATIVE_OUTPUT_CERTIFIED:** `false`

---

## 1. Resumen ejecutivo

Se crea un prompt canónico activo y genérico en nombre de archivo para el Proyecto 000 Demo:

`governance/authority/ACTIVO/IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt`

El prompt preserva el input del Demo, elimina declaraciones históricas de readiness y separa claramente:

- autoridad del Informe Maestro;
- autoridad técnica del motor;
- input externo del Demo;
- preflight;
- ejecución única;
- validación recomputada;
- auditoría independiente posterior.

Este documento no autoriza todavía la ejecución. `CURRENT_STATE.json` permanece en `PENDING_AUTHORIZATION` y conserva `prompt_path=null` y `prompt_sha256=null` hasta el PR separado de autorización AUD-028.

**Veredicto:**

`PROMPT_CANONICO_VALIDADO_PENDING_AUD028_AUTHORIZATION`

---

## 2. Fuente histórica preservada

Prompt anterior:

`governance/authority/REFERENCIA/IDUNEX_PROMPT_CANO_16f1f470.txt`

Clasificación:

- `SUSTITUIDO` como autoridad de ejecución;
- `REFERENCIA` para lineage;
- no modificado para preservar trazabilidad.

La sustitución se requiere porque el prompt histórico contiene una declaración de cierre/readiness que no corresponde al estado global vigente y está ubicado bajo una superficie `REFERENCIA`.

---

## 3. Prompt activo

| Campo | Valor |
|---|---|
| Ruta | `governance/authority/ACTIVO/IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt` |
| Nombre con versión | No |
| Estado documental | `VALIDADO` |
| Estado de ejecución | `PENDING_AUD028_AUTHORIZATION` |
| Bytes UTF-8 | `7,698` |
| SHA-256 | `53411b87c07cc054546d73adcc7e132d031e02d5e5d90606580abbe7f1d7d3ea` |
| Input mode | `COMPLETE` |
| Ejecución autorizada | `false` |

El SHA corresponde al contenido UTF-8 exacto con salto de línea final.

---

## 4. Input Demo preservado

- Proyecto: `Proyecto 000 Demo`;
- propietario/marca externa: `LatinosFlow`;
- modelo 1: `Valeria Rios Andrade`, alias `Vale`, mujer ficticia adulta de 20 años;
- modelo 2: `Mateo Vargas Salinas`, alias `Mateo`, hombre ficticio adulto de 30 años;
- modalidades: imagen, video, voz/audio, música/Suno, sonido, texto/copy y QA/agente;
- assets: `NO_ASSETS_SUBMITTED`;
- logo: `LOGO_ASSET_NOT_VERIFIED`;
- `CREATIVE_OUTPUT_CERTIFIED=false`.

Los nombres y la marca permanecen como input externo del Demo, nunca como defaults del motor.

---

## 5. Correcciones de gobernanza

El prompt activo declara:

- `MOTOR_ACTIVE_STATUS=EN_REVISION`;
- `READY_FOR_PROJECT_DEMO_GENERATION=FALSE`;
- `CONTROLLED_EXTERNAL_DEMO_STATUS=PENDING_AUTHORIZATION`;
- `DEMO_EXECUTION_AUTHORIZED=FALSE`;
- `CREATIVE_OUTPUT_CERTIFIED=FALSE`.

También prohíbe:

- release;
- tag;
- `OFICIAL`;
- cierre productivo;
- carga de agentes;
- `PROJECT_AUDIT_PASS` declarativo;
- certificación creativa sin QA real.

---

## 6. Contrato de tres adjuntos

La futura ejecución externa utilizará exactamente:

1. `IDUNEX_MOTOR_v1.0.0.zip`;
2. Informe Maestro vigente;
3. `IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt`.

El companion SHA, manifest y autorización se conservan como evidencia externa de preflight y auditoría; no sustituyen ninguno de los tres adjuntos operativos.

---

## 7. Ejecución y consumo

El prompt exige:

- preflight antes de consumir;
- `generate` máximo una vez;
- `validate` máximo una vez si existe ZIP final candidato;
- no reintentar después de consumo;
- no editar manualmente el ZIP generado;
- cinco artefactos externos;
- decisión limitada a generación pendiente de auditoría independiente.

La autorización efectiva solo existirá cuando un PR posterior cambie el objeto machine-readable a `AUTHORIZED_NOT_CONSUMED` y fije este prompt y SHA.

---

## 8. Archivos afectados

Creados:

1. `governance/authority/ACTIVO/IDUNEX_PROMPT_CANONICO_PROJECT_000_DEMO.txt`;
2. `docs/audits/GOV-IDUNEX-ActivacionPromptCanonicoProyecto000Demo-20260722-v1-EN_REVISION.md`.

Modificado:

3. `REPOSITORY_MANIFEST.yml`.

No modificado:

- `engine/IDUNEX`;
- `governance/CURRENT_STATE.json`;
- prompt histórico de `REFERENCIA`;
- package del motor;
- release o tag.

---

## 9. Reversión

Cerrar el PR sin fusionar o revertir sus tres archivos. La reversión no modifica el motor ni consume una autorización.

---

## 10. Estado final

- `PROMPT_CANONICO_STATUS=VALIDADO_PENDING_AUTHORIZATION`
- `PROMPT_CANONICO_SHA256=53411b87c07cc054546d73adcc7e132d031e02d5e5d90606580abbe7f1d7d3ea`
- `HISTORICAL_PROMPT_STATUS=SUSTITUIDO_REFERENCIA`
- `CONTROLLED_EXTERNAL_DEMO_STATUS=PENDING_AUTHORIZATION`
- `DEMO_EXECUTION_AUTHORIZED=false`
- `MOTOR_STATUS=EN_REVISION`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `OFICIAL_AUTHORIZED=false`
- `PRODUCTIVE_CLOSURE_AUTHORIZED=false`
- `CREATIVE_OUTPUT_CERTIFIED=false`
