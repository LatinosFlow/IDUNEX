# GOV-IDUNEX-AutorizacionRegeneracionProyecto000DemoPostPR44-20260721-v1-EN_REVISION

**Tipo:** Autorización documental de ejecución controlada  
**ID:** AUD-025  
**Fecha:** 2026-07-21  
**Versión:** v1  
**Estado:** `EN_REVISION`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**PR técnico de origen:** `#44`  
**Estado técnico de origen:** `MERGED_DECLARADO_Y_CONTENIDO_POST_MERGE_VALIDADO`  
**Commit técnico de merge:** `NO_RECUPERADO; no usado como autoridad de contenido`  
**Destino autorizado:** ChatGPT normal, fuera de GitHub

---

## 1. Resumen ejecutivo

AUD-025 autoriza una única regeneración externa y controlada del Proyecto 000 Demo después de:

1. la reauditoría externa que declaró `PROJECT_AUDIT_FAIL`;
2. la corrección de sincronización post-finalizer, fidelity hashes, padding documental, conteo de duplicados y cobertura del validator;
3. la corrección adicional del wrapper atómico H160;
4. el merge del PR #44;
5. la validación independiente del `main` descargado después del merge.

Esta autorización no declara `PROJECT_AUDIT_PASS`, no promueve el motor y no habilita carga en agentes.

---

## 2. Autoridad técnica autorizada

### Repositorio post-merge

- Archivo recibido: `IDUNEX-main.zip`
- SHA-256 del ZIP recibido: `453245673ab126ff94c2c5ba990716e0f235bc7ab9e95a71a753a99aacc6e29f`
- ZIP `testzip`: `PASS`
- Root: `IDUNEX-main`

### Motor autorizado

- Archivos: `981`
- Bytes: `47,302,063`
- Tree SHA-256:
  `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`

### Gobernanza

`CURRENT_STATE.json` SHA-256:

`4bcd514f656b804bcfe79ba9eac7d549f37fbec218d8a879a956ede700a1f2f1`

Valores obligatorios:

- `motor_status=EN_REVISION`
- `ready_for_project_demo_generation=false`
- `release_authorized=false`
- `tag_authorized=false`
- `productive_closure_authorized=false`
- `creative_output_certified=false`

### Input exacto autorizado

- Archivo:
  `IDUNEX-Project000-Demo-Input-20260717-v1-EN_REVISION.json`
- SHA-256:
  `801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`

No se autoriza modificar, reconstruir, completar ni sustituir el input.

---

## 3. Antecedentes y sustitución operativa

- AUD-023 autorizó una regeneración post PR #38.
- AUD-024 autorizó una reejecución post corrección de empaquetado.
- AUD-024 fue consumido y no puede reutilizarse.
- La entrega resultante fue reauditorada y declaró `PROJECT_AUDIT_FAIL`.
- El PR #44 corrigió los bloqueadores encontrados.
- La validación post-merge declaró `POST_MERGE_VALIDATION_PASS`.

AUD-025 es la única autorización vigente para la siguiente regeneración controlada.

---

## 4. Alcance autorizado

Después de aprobar el preflight, se autoriza:

1. Ejecutar `generate` una sola vez.
2. Capturar comando, stdout, stderr, RC y JSON de resultado.
3. Ejecutar `validate` una sola vez únicamente si existe ZIP definitivo.
4. Reabrir el ZIP final.
5. Recomutar companion SHA-256.
6. Custodiar los cinco artefactos externos canónicos.
7. Ejecutar validación recomputacional de:
   - content-tree post-finalizer;
   - fidelity hashes;
   - reporte forense sin padding;
   - duplicate allowlist y resumen;
   - H160 atómico;
   - runtime 10+N;
   - agent-load surfaces;
   - aliases;
   - MODEL_REGISTRY;
   - NO_DRIFT;
   - Profile360;
   - TechExt.
8. Preparar la entrega para una reauditoría externa independiente.

---

## 5. Preflight obligatorio sin consumo

Antes de `generate` se debe verificar:

- ZIP operativo y manifiesto: `PASS`.
- Input SHA-256 exacto.
- Motor: `981` archivos.
- Motor: `47,302,063` bytes.
- Tree SHA-256 exacto:
  `628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`.
- Ausencia de `.pyc` y `__pycache__`.
- Gobernanza operacional en raíz:
  - `governance/CURRENT_STATE.json`
  - `governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json`
  - `governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt`
- Resolver SHA devuelve exactamente el tree SHA autorizado.
- `CURRENT_STATE` conserva todos los valores no-release.
- AUD-025 está presente byte a byte en el `main` usado para armar el paquete.
- `generate=false` y `validate=false` antes de la ejecución.

Si cualquier control falla:

`DEMO_REGENERATION_BLOCKED`

sin ejecutar `generate`.

---

## 6. Criterios técnicos requeridos

- `generate_rc=0`
- `validate_rc=0`
- `result=PASS`
- `delivery_status=DELIVERY_ALLOWED` o contrato equivalente vigente
- `validators_fail=0`
- `blocking_warnings=0`
- `fail_codes=[]`
- ZIP `testzip=PASS`
- Companion SHA coincide
- Artefactos externos `5/5`
- Content-tree final sincronizado
- Fidelity hash mismatches `0`
- Reporte forense sin padding exacto
- Duplicate count declarado = allowlist = árbol físico
- `H160_ATOMIC_PROJECT_FINALIZER=PASS`
- Runtime ChatGPT `12`
- Runtime Copilot `12`
- Agent-load ChatGPT `10/10`
- Agent-load Copilot `10/10`
- Vale resuelve solo a Valeria Rios Andrade
- Mateo resuelve solo a Mateo Vargas Salinas
- `MODEL_REGISTRY=PASS`
- `NO_DRIFT_LEDGERS=PASS`
- Profile360 `61/61` por modelo
- TechExt `284/284` por modelo
- `CREATIVE_OUTPUT_CERTIFIED=false`

---

## 7. Restricciones duras

No se autoriza:

- modificar el motor durante la ejecución;
- modificar el input;
- modificar `CURRENT_STATE.json`;
- ejecutar `generate` más de una vez;
- repetir después de consumir la autorización;
- editar manualmente el ZIP generado;
- crear release o tag;
- declarar estado `OFICIAL`;
- declarar cierre productivo;
- declarar `PROJECT_AUDIT_PASS`;
- cargar agentes;
- declarar certificación creativa;
- reutilizar el ZIP fallido anterior;
- usar salidas temporales como entrega.

---

## 8. Evidencia obligatoria

Conservar:

1. Paquete ejecutado y SHA-256.
2. Manifiesto del paquete.
3. Evidencia de AUD-025 incorporado al `main`.
4. Preflight completo.
5. Motor, conteos y tree SHA.
6. Input y SHA.
7. Comando generate.
8. stdout, stderr y RC.
9. GenerateResult.
10. Comando validate.
11. ValidateResult.
12. ZIP final y companion.
13. Certificado, reporte y README.
14. Evidencia H283/H160.
15. Evidencia de fidelity, duplicados y reporte.
16. Resumen de ejecución.
17. Paquete para reauditoría independiente.

---

## 9. Ruta posterior

`AUD-025 MERGED → descargar main → validar incorporación → preparar paquete r3 → preflight PASS → una regeneración → validate → reauditoría externa independiente`

Solo la reauditoría externa posterior puede declarar `PROJECT_AUDIT_PASS`.

---

## 10. Decisión documental

Se autoriza:

`CONTROLLED_DEMO_REGENERATION_POST_PR44`

Límite:

`ONE`

La autorización entra en vigor únicamente cuando AUD-025 haya sido fusionado a `main` y su incorporación sea validada.

---

## 11. Estado final

- `AUD025_STATUS=EN_REVISION`
- `AUD025_PR_STATUS=PENDING_MERGE`
- `PR44_STATUS=MERGED_DECLARED_AND_CONTENT_VALIDATED`
- `POST_MERGE_VALIDATION=PASS`
- `PRIOR_AUTHORIZATION=AUD-024_CONSUMED`
- `MOTOR_STATUS=EN_REVISION`
- `CONTROLLED_EXECUTION_LIMIT=ONE`
- `DEMO_REGENERATION_AUTHORIZED=ONLY_AFTER_AUD025_MERGE`
- `AUTHORIZED_ENGINE_ZIP_SHA256=453245673ab126ff94c2c5ba990716e0f235bc7ab9e95a71a753a99aacc6e29f`
- `AUTHORIZED_ENGINE_TREE_SHA256=628985889720f83e7c4c382791192ad48025c4c54a59314e69de0207770aafb9`
- `AUTHORIZED_INPUT_SHA256=801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`
- `RELEASE_AUTHORIZED=false`
- `TAG_AUTHORIZED=false`
- `OFICIAL_AUTHORIZED=false`
- `PROJECT_AUDIT_PASS=false`
- `PROJECT_AGENT_LOAD_PASS=false`
- `CREATIVE_OUTPUT_CERTIFIED=false`
