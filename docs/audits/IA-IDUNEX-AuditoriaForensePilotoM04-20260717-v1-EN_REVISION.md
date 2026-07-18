# IA-IDUNEX-AuditoriaForensePilotoM04-20260717-v1

**Tipo:** Auditoría forense documental  
**ID:** AUD-020  
**Fecha:** 2026-07-17  
**Versión:** v1  
**Estado:** EN_REVISION → ver resultado final  
**Auditor:** Copilot CLI (sesión AUD-020)  
**Piloto auditado:** IDUNEX_M04_PILOTO_001  
**Referencia PR:** AUD-020 (este PR) | PR #34 (M04_PASS fusionado)

---

## 1. Contexto y alcance

Esta auditoría forense evalúa el proyecto piloto `IDUNEX_M04_PILOTO_001` generado en la fase M04 del motor IDUNEX. El alcance es exclusivamente documental: no se modifican artefactos del piloto, el motor (`engine/IDUNEX/`) ni `governance/CURRENT_STATE.json`. No se crea Proyecto 000 Demo, release, tag ni se cambia `MOTOR_STATUS` a `OFICIAL`.

### Contexto de la cadena de autoridad

| PR | Contenido | Estado |
|---|---|---|
| PR #31 | AUD-016: M02_PASS | MERGED |
| PR #32 | AUD-017: M03_PASS (adversarial) | MERGED |
| PR #33 | AUD-018: autorización M04 piloto controlado | MERGED |
| PR #34 | AUD-019: M04_PASS piloto IDUNEX_M04_PILOTO_001 | MERGED |
| Este PR | AUD-020: auditoría forense piloto M04 | BORRADOR |

---

## 2. Evidencia de entrada: estado del repositorio

### 2.1 Commit actual de main

```
SHA:   e32008d99950ecacc98c41bf4095d1c7b414add3
Fecha: 2026-07-17T19:34:08-05:00
Msg:   Merge pull request #34 from LatinosFlow/aleducase-aud-019-m04-piloto-controlado
```

**Resultado: PASS** — commit de main identificado y trazable.

### 2.2 Estado de PR #34 / M04_PASS

```json
{
  "number": 34,
  "title": "AUD-019: M04 primer proyecto piloto controlado IDUNEX",
  "state": "MERGED",
  "mergedAt": "2026-07-18T00:34:08Z",
  "mergeCommit": "e32008d99950ecacc98c41bf4095d1c7b414add3"
}
```

**Resultado: PASS** — PR #34 fusionado; M04_PASS documentado.

### 2.3 Intake Audit post-M04 en main

```json
{
  "name": "IDUNEX Intake Audit",
  "status": "completed",
  "conclusion": "success",
  "headSha": "e32008d99950ecacc98c41bf4095d1c7b414add3",
  "createdAt": "2026-07-18T00:35:35Z"
}
```

**Resultado: PASS** — Intake Audit ejecutado sobre el commit de merge PR #34 con conclusión `success`.

---

## 3. Existencia del piloto, ZIP y companion

| Artefacto | Ruta | Existe |
|---|---|---|
| Carpeta piloto | `C:\temp\idunex_m04_pilot_001\generated\IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0` | ✅ |
| ZIP | `...\IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0.zip` | ✅ |
| Companion SHA256 | `...\IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0.zip.sha256` | ✅ |

**Resultado: PASS** — Los tres artefactos existen en la ruta esperada según informe M04.

---

## 4. Verificación SHA256

| Fuente | SHA256 |
|---|---|
| Recalculado del ZIP | `88ea66ecfdf8e3160e3c0b08948ffef529cf5c90aa0781500a42b8a50a3004dc` |
| Companion `.sha256` | `88ea66ecfdf8e3160e3c0b08948ffef529cf5c90aa0781500a42b8a50a3004dc` |
| Reportado en M04 | `88ea66ecfdf8e3160e3c0b08948ffef529cf5c90aa0781500a42b8a50a3004dc` |

**Resultado: PASS** — SHA256 recalculado coincide 100% con companion y con el valor reportado en M04. Integridad del ZIP verificada.

---

## 5. Estructura del piloto

### 5.1 Carpetas raíz (13 dominios controlados)

| Carpeta | Presente | Archivos críticos |
|---|---|---|
| `00_PROJECT_INDEX` | ✅ | PROJECT_MANIFEST.json, PROJECT_STATUS_CONTRACT.json, PROJECT_LOCKS.json, PROJECT_ENTITY_PROFILE.json, PROJECT_NAMING_CANON.json, PROJECT_VERSION_LINEAGE.json, etc. |
| `01_CANON` | ✅ | PROFILE360_CANONICAL_REGISTRY_00_60.json, ENGINE_GATE_TO_PROJECT_RUNTIME_CLAUSE_MAP.json, SOURCE_RUNTIME_LEDGER_MINIFIED.json, P034_*, TECHEXT_FULL10_OFFICIAL_FIELD_REGISTRY.json, etc. |
| `02_MODELS/MODEL_D0E64DEED1_MODELO_PILOTO_UNO` | ✅ | PROFILE360_FULL60.json, TECHEXT_FULL10.json, MASTER_VISUAL_ANCHORS.json, MODEL_IDENTITY_AND_LOCKS.json, HUMAN_READABLE_VISUAL_CANON.json |
| `03_AGENTS/CHATGPT` | ✅ | 01_RUNTIME_UPLOAD (11 archivos), 02_AGENT_CONFIGURATION, 03_MANIFESTS |
| `03_AGENTS/COPILOT` | ✅ | 01_RUNTIME_UPLOAD (11 archivos .docx), 02_AGENT_CONFIGURATION, 03_MANIFESTS |
| `04_MULTIMODAL_CONTRACTS` | ✅ | Registros BRAND, PROFILE360, PAIRWISE, routing, safe apparel |
| `05_SIDECARS` | ✅ | 7 templates SIDECAR_TEMPLATE_*.json + prompt packs + manifests |
| `06_GOLDEN_TESTS` | ✅ | Prompts por modalidad, matrix, test spec |
| `07_QA_VALIDATORS` | ✅ | Suite adversarial, conversacional, densidad Profile360, closure batch |
| `08_EVIDENCE_LINEAGE` | ✅ | FIELD_SOURCE_TRACE_LEDGER, H37, evidencia índice |
| `09_MANIFESTS_SHA` | ✅ | PROJECT_PACKAGE_SHA256SUMS.txt, parity audits, finalizer report, reopened ZIP proof |
| `10_RELEASE` | ✅ | FINAL_AUDIT_REPORT.md, IDUNEX_PROJECT_CERTIFICATE.json, RELEASE_CERTIFICATE.txt, SUMMARY_REPORT.md, CHANGELOG.md |
| `11_CLOSURE_BATCH` | ✅ | PROJECT_CLOSURE_AUDIT_BATCH.md |
| `12_HISTORICAL_NON_AUTHORITY` | ✅ | README.md |
| `AGENT_FORENSIC_COMPANION` | ✅ | ACTIVE_RUNTIME_UPLOAD_MANIFEST.json, FIELD_SOURCE_TRACE_LEDGER_MODEL_001.json, prompt packs, SHA256SUMS.txt |

**Resultado: PASS** — Estructura completa con 13 carpetas de dominio + AGENT_FORENSIC_COMPANION. Sin archivos sueltos en raíz de ejecución.

### 5.2 Archivos vacíos o truncados

Escaneo recursivo de archivos con `Length == 0`: **ninguno encontrado**.

**Resultado: PASS** — Sin archivos vacíos ni truncados.

---

## 6. Coherencia de nombres, rutas, versión y estados

| Campo | Valor | Coherente |
|---|---|---|
| `project_id` | `IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0` | ✅ |
| `project_name` | `IDUNEX_M04_PILOTO_001` | ✅ |
| `semantic_version` | `v1.0.0` | ✅ |
| `engine_version` | `v1.0.0` | ✅ |
| `engine_zip_sha256` | `2fb8f9bf3e...b2eb0` | ✅ |
| `PROJECT_UID` | `C60B344DB2B3` | ✅ (metadata interna, no en filename) |
| Nombre ZIP | `IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0.zip` | ✅ |
| `internal_label` | `H391_H410_DIRECT_CANONICAL_PROJECT_FACTORY` | ✅ |
| `created_at` | `2026-07-17T19:29:46-05:00` | ✅ |

**Resultado: PASS** — Nombres, rutas, versión y estados coherentes en todo el proyecto.

---

## 7. Coherencia runtime / instrucciones / manifiestos / políticas

### 7.1 Runtime ChatGPT

- **Archivos runtime:** 11 (01-10 cores + MODEL_RUNTIME_PROFILE_FULL_MODELO_PILOTO_UNO.md)
- **Fórmula:** 10+N (N=1 modelo) = 11 ✅
- **Configuración:** `PROJECT-CONFIGURACION-AGENT.txt` con 46 cláusulas CFG (CFG-000 a CFG-046), longitud semántica dentro del rango 6500-8000 chars ✅
- **Parity audit:** `CHATGPT_RUNTIME_PARITY_AUDIT.json` — `result: PASS`, `runtime_file_count: 11` ✅

### 7.2 Runtime Copilot

- **Archivos runtime:** 11 (mismos cores en formato .docx + MODEL_RUNTIME_PROFILE_FULL_MODELO_PILOTO_UNO.docx)
- **Fórmula:** 10+N = 11 ✅
- **Configuración:** `PROJECT-CONFIGURACION-AGENT.txt` con 46 cláusulas CFG, diferencia semántica correcta (COPILOT prioriza clean image output vs CHATGPT que prioriza native image) ✅
- **Parity audit:** `COPILOT_RUNTIME_PARITY_AUDIT.json` — `result: PASS`, `runtime_file_count: 11` ✅

### 7.3 Paridad ChatGPT/Copilot

Ambos manifiestos de paridad confirman:
- `same_project_id: true`
- `same_model_count: true`
- `same_locks: true`
- `same_gates_critical: true`
- `same_failcodes: true`
- `same_sidecar_templates: true`
- `same_truthfulness_policy: true`
- `no_docs_no_runtime_loaded_as_runtime: true`

**Resultado: PASS** — Runtime, instrucciones y manifiestos coherentes. Paridad ChatGPT/Copilot verificada.

---

## 8. Separación ENGINE_LEVEL / PROJECT_LEVEL / AGENT_LEVEL

| Nivel | Evidencia |
|---|---|
| ENGINE_LEVEL | `engine_zip_sha256` referenciado pero no contenido dentro del proyecto. Motor identificado por hash externo. |
| PROJECT_LEVEL | `00_PROJECT_INDEX`, `01_CANON`, `02_MODELS`, manifiestos propios del proyecto. |
| AGENT_LEVEL | `03_AGENTS/CHATGPT` y `03_AGENTS/COPILOT` con su propio runtime, configuración y manifiestos. |
| Política | `motor_productive_does_not_make_project_productive: true` en PROJECT_STATUS_CONTRACT.json |
| Separación filenames | `ROOT_UNICO` por carpeta interna `IDUNEX_PROJECT_IDUNEX_M04_PILOTO_001_v1.0.0` |

**Resultado: PASS** — Separación de niveles preservada.

---

## 9. Instrucciones para ChatGPT: legibilidad y consistencia

**Evaluadas:** 46 cláusulas CFG en `03_AGENTS/CHATGPT/02_AGENT_CONFIGURATION/PROJECT-CONFIGURACION-AGENT.txt`

| Criterio | Estado |
|---|---|
| Legibilidad | ✅ Texto plano estructurado, una cláusula por línea |
| Sin contradicción crítica | ✅ CFG-027 define explícitamente diferencia ChatGPT vs Copilot |
| Política de imágenes | ✅ CFG-005: native image generation, sin auxiliar sustituto |
| Política de seguridad | ✅ CFG-000, CFG-004, CFG-013: adulto ficticio, bloqueos correctos |
| Política de certificación | ✅ CFG-021, CFG-022: CREATIVE_OUTPUT_CERTIFIED FALSE hasta asset real |
| Política SHA | ✅ CFG-031, CFG-040, CFG-045: external companion authority |
| Longitud | ✅ Rango 6500-8000 chars semánticos; HASH_PADDING_FORBIDDEN |
| Sin datos sensibles en config | ✅ |

**Resultado: PASS** — Instrucciones ChatGPT legibles, consistentes y no contradictorias.

---

## 10. Instrucciones para Copilot: legibilidad y consistencia

**Evaluadas:** 46 cláusulas CFG en `03_AGENTS/COPILOT/02_AGENT_CONFIGURATION/PROJECT-CONFIGURACION-AGENT.txt`

| Criterio | Estado |
|---|---|
| Legibilidad | ✅ Mismo esquema que ChatGPT, diferencia en header COPILOT_CLEAN_IMAGE_OUTPUT |
| Sin contradicción crítica | ✅ CFG-027 establece que Copilot prioriza clean image / sin metadata visual |
| Paridad obligaciones | ✅ Mismas 46 cláusulas con diferenciación semántica válida |
| Formato runtime | ✅ .docx para Copilot 365, .md para ChatGPT |
| Sin datos sensibles | ✅ |

**Resultado: PASS** — Instrucciones Copilot legibles, consistentes y no contradictorias.

---

## 11. Perfil 360: completitud

| Métrica | Valor esperado | Valor real | Estado |
|---|---|---|---|
| Profile360 secciones / modelo | 61 | 61 | ✅ PASS |
| TechExt campos / modelo | 284 | 284 | ✅ PASS |
| Visual anchors / modelo | 10 | 10 (MASTER_VISUAL_ANCHORS.json presente) | ✅ PASS |
| Pairwise pairs (N=1) | 0 | 0 | ✅ PASS (correcto para modelo único) |
| Model ID | MODEL_D0E64DEED1_MODELO_PILOTO_UNO | Coincide en locks, profile, techext | ✅ PASS |

**Resultado: PASS** — Perfil 360 completo. Sin vacíos bloqueantes.

---

## 12. Trazabilidad forense

| Elemento | Presente | Detalle |
|---|---|---|
| SHA256 del ZIP | ✅ | Companion externo; self-reference policy activa |
| Content tree SHA | ✅ | `15bdb7e9e7fe0d766b67a60963ab8e504f881aa2e434339a479e44952b89e3fe` |
| Engine ZIP SHA | ✅ | `2fb8f9bf3e13b2f27f9bbddd39b3aa1aaceb2ff5456a8f72a6e349038f3b2eb0` |
| POST_EXPORT_FINALIZER_REPORT | ✅ | gate H113_H127, result PASS |
| PROJECT_PACKAGE_SHA256SUMS.txt | ✅ | 30484 bytes — inventario de hashes internos |
| DELIVERY_ATOMIC_COMPLETION_MANIFEST | ✅ | Presente en 09_MANIFESTS_SHA |
| CREATIVE_CERTIFICATION_TRUTHFULNESS | ✅ | CREATIVE_OUTPUT_CERTIFIED=FALSE declarado |
| FIELD_SOURCE_TRACE_LEDGER | ✅ | Presente en 08_EVIDENCE_LINEAGE y AGENT_FORENSIC_COMPANION |
| H51-H118 gates | ✅ | Todos PASS según IDUNEX_PROJECT_CERTIFICATE.json |
| PROJECT_MATRIX_COMPLETION_PROOF | ✅ | MATRIX_CASES_PASS: 1, FAIL: 0 |
| ACTIVE_RUNTIME_UPLOAD_MANIFEST | ✅ | En 09_MANIFESTS_SHA y AGENT_FORENSIC_COMPANION |
| Parity audits ChatGPT/Copilot | ✅ | Ambos result PASS |

**Resultado: PASS** — Trazabilidad forense suficiente. Manifiestos, hashes, evidencia y control de estado presentes.

---

## 13. Referencias indebidas a Demo productivo

Escaneo de todos los archivos `.json`, `.md`, `.txt` del piloto buscando:
- `Proyecto 000`
- `MOTOR_STATUS=OFICIAL`
- `CREATIVE_OUTPUT_CERTIFIED=TRUE`
- `production release authorized`

**Resultado: PASS** — Sin referencias indebidas a Demo productivo. Sin autorización implícita de release, tag ni OFICIAL.

---

## 14. Datos sensibles

Escaneo de patrones sensibles (`password`, `token`, `api_key`, `secret`, `Bearer`, `sk-`, `ghp_`, `Authorization` con valor largo):

**Resultado: PASS** — Sin datos sensibles, secretos, tokens, claves ni información innecesaria.

---

## 15. Validación contra M02, M03, AUD-018 y M04

| Informe | Piloto coherente |
|---|---|
| M02_PASS (PR #31) | ✅ Motor v1.0.0 referenciado correctamente; engine SHA en piloto coincide con motor auditado |
| M03_PASS / AUD-017 (PR #32) | ✅ Sin regresiones adversariales; safe apparel, watermark, sidecar strict schema presentes |
| AUD-018 (PR #33) | ✅ Piloto es `internal` / `controlled pilot`, no productivo; PROJECT_READY_FOR_PRODUCTION=false |
| M04_PASS / AUD-019 (PR #34) | ✅ SHA del ZIP coincide; estructura y resultados gates H51-H118 documentados; runtime 11/11 ChatGPT y Copilot |

**Resultado: PASS** — El piloto no contradice los informes precedentes.

---

## 16. Readiness para futura prueba con Proyecto 000 Demo

| Requisito | Estado |
|---|---|
| Piloto generado y validado | ✅ |
| SHA verificable externamente | ✅ |
| Runtime ChatGPT/Copilot completo | ✅ |
| Profile360 61/61 + TechExt 284/284 | ✅ |
| Instrucciones legibles sin contradicción | ✅ |
| Separación ENGINE/PROJECT/AGENT | ✅ |
| Sin autorización de producción prematura | ✅ (`PROJECT_READY_FOR_PRODUCTION: false`) |
| Motor en EN_REVISION | ✅ (gobernanza no modificada) |
| Próximo paso requerido | Agente ChatGPT o Copilot cargue el piloto y ejecute prueba controlada |

**Nota:** La creación de Proyecto 000 Demo requiere autorización separada post-AUD-020 y está **bloqueada** hasta que se declare formalmente por governance.

---

## 17. Hallazgos

### H-AUD020-001 — Informativo (no bloqueante)

**Hallazgo:** `governance/CURRENT_STATE.json` (`schema_version: 1`, `issue: AUD-006`) muestra `m02_result: "M02_FAIL"`, que refleja el estado original de AUD-006 y no fue actualizado tras PR #31 (M02_PASS).

**Impacto:** `motor_status: "EN_REVISION"` es correcto. El piloto no modifica ni depende de este campo. La autoridad de M02_PASS está documentada en PR #31. Este archivo no es modificado por esta auditoría (regla dura).

**Clasificación:** INFORMATIVO — No bloquea AUD-020_PASS. Proponer issue para alinear `governance/CURRENT_STATE.json` con M02_PASS en fase separada.

### H-AUD020-002 — Informativo (esperado)

**Hallazgo:** `09_MANIFESTS_SHA/PROJECT_REOPENED_ZIP_PROOF.json` muestra varios campos como `EXTERNAL_COMPANION_REQUIRED_AFTER_FINALIZER` y result `CONTENT_TREE_PROOF_PRECHECK_EXTERNAL_AUTHORITY_PENDING`.

**Impacto:** Comportamiento esperado y correcto según `ZIP_SHA_SELF_REFERENCE_POLICY.json` (`WHOLE_ZIP_SHA256_AUTHORITY_EXTERNAL_COMPANION`). El ZIP no puede contener su propio SHA integral. La autoridad es el companion externo, verificado y coincidente.

**Clasificación:** ESPERADO — Correcto. No bloquea.

---

## 18. Issues derivados propuestos

| ID propuesto | Descripción | Prioridad |
|---|---|---|
| ISS-AUD020-001 | Actualizar `governance/CURRENT_STATE.json` para reflejar m02_result=M02_PASS tras PR #31 | Media |
| ISS-AUD020-002 | Autorizar y documentar fase de prueba controlada del piloto con agente ChatGPT o Copilot | Alta (prerrequisito Proyecto 000 Demo) |

---

## 19. Matriz de resultados AUD-020

| Criterio | Resultado | Notas |
|---|---|---|
| SHA del ZIP coincide con companion y M04 | ✅ PASS | Triple coincidencia exacta |
| Estructura del piloto completa | ✅ PASS | 13 carpetas + AGENT_FORENSIC_COMPANION |
| Canon coherente | ✅ PASS | Profile360 61/61, TechExt 284/284, anchors 10/10 |
| Perfil 360 completo | ✅ PASS | Sin vacíos bloqueantes |
| Archivos runtime/instrucciones consistentes | ✅ PASS | 11 archivos × 2 plataformas |
| Instrucciones ChatGPT interpretables sin contradicción | ✅ PASS | 46 cláusulas CFG |
| Instrucciones Copilot interpretables sin contradicción | ✅ PASS | 46 cláusulas CFG |
| Separación ENGINE/PROJECT/AGENT preservada | ✅ PASS | |
| Trazabilidad forense suficiente | ✅ PASS | Hashes, manifiestos, evidencia |
| Sin datos sensibles indebidos | ✅ PASS | |
| Sin Demo, release, tag ni OFICIAL | ✅ PASS | |
| Sin cambios en engine/IDUNEX/ | ✅ PASS | Diff limpio |
| Sin cambios en governance/CURRENT_STATE.json | ✅ PASS | Inmutable en este PR |
| Solo informe documental agregado | ✅ PASS | Este archivo únicamente |
| Sin archivos vacíos ni truncados | ✅ PASS | |
| Sin artefactos del piloto en el repo | ✅ PASS | Piloto en C:\temp\ externo |

---

## 20. Resultado final

```
AUD-020_PASS
```

Todos los criterios de `AUD-020_PASS` se cumplen. El piloto `IDUNEX_M04_PILOTO_001` conserva el canon IDUNEX completo, el perfil 360 íntegro, la coherencia documental/runtime/instrucciones y la preparación correcta para interpretación por agentes ChatGPT/Copilot.

**No se autoriza:**
- Proyecto 000 Demo (requiere fase separada)
- Release o tag
- Cambio de `MOTOR_STATUS` a `OFICIAL`

**Estado del motor:** `EN_REVISION` (sin cambio)

---

*Generado por Copilot CLI — sesión AUD-020 | Rama: aleducase-aud-020-forensic-audit-m04-pilot*
