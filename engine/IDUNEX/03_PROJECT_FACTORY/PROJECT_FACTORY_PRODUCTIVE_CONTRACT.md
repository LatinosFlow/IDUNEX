# PROJECT_FACTORY_PRODUCTIVE_CONTRACT

## Active authority clarification — 1ADD3F8D
- active_authority_target: `IDUNEX/03_PROJECT_FACTORY/05_PROJECT_FACTORY_FULL_CONTRACT.md`
- active_authority_state: PRODUCTIVE_BASE_ENGINE_ACTIVE
- forbidden_rollback: do not restore `1d0c...` or any earlier hash as runtime authority.
- parent_hash_1d0c_policy: HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY / DO_NOT_USE_AS_BASE / NOT_RUNTIME_AUTHORITY.
- input_package_sha256_before_this_surgical_patch: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`


## Propósito
Define cómo el motor convierte datos completos, parciales o mínimos en proyectos IDUNEX productivos, sin producir proyectos mínimos ni genéricos.

## Autoridad
Autoridad activa: `IDUNEX/03_PROJECT_FACTORY/05_PROJECT_FACTORY_FULL_CONTRACT.md`. Este archivo es contrato/bridge operativo, no resumen. Si existe un documento largo con el mismo dominio, este bridge define punto de entrada, ruta de carga, criterios ejecutables y bloqueo QA. No compite con PROJECT_CORE; PROJECT_CORE es autoridad superior para proyectos exportados.

## Alcance
Project creation, PROJECT_CORE, CHATGPT/COPILOT packs, manifests, QA and export readiness.. Aplica a motor base `IDUNEX_MOTOR_VERSION = v1.0.0`, Project Factory, Agent Factory, CHATGPT, COPILOT, Profile360, manifests, sidecars, validators, hash lineage y exportación productiva controlada. No autoriza PROJECT_INSTANCE_GO ni OUTPUT_GO sin QA propio.

## Inputs obligatorios
- ZIP base auditado: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`.
- Source inventory `05_SOURCE_TO_RUNTIME/01_INVENTORY/SOURCE_INVENTORY_MASTER.json`.
- Source-to-runtime map `05_SOURCE_TO_RUNTIME/02_MAPS/SOURCE_TO_RUNTIME_MASTER_MAP.json`.
- Profile360 registry `04_PROFILE360_SYSTEM/01_SCHEMA/PROFILE360_FULL60_SECTION_REGISTRY.json`.
- PROJECT_CORE, CHATGPT y COPILOT del template oficial cuando el contrato afecte agentes/proyectos.
- Sidecars, QA report y manifests cuando el contrato afecte outputs o paquetes.


## Hash authority — surgical hardening a742

- input_package_sha256_before_this_surgical_patch: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- correction_base_sha256: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- expected_correction_base_sha256: `1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60`
- FINAL_ZIP_SHA256_AUTHORITY: `EXTERNAL_COMPANION_SHA256_FILE`
- final_zip_sha256_real: `RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD`
- historical_previous_bases_policy: `HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL` / `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY` / `DO_NOT_USE_AS_BASE`
- historical_previous_bases_non_operational:
- `a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e` — PREVIOUS_SURGICAL_INPUT_LINEAGE; PARENT_PACKAGE_LINEAGE_ONLY; HISTORICAL_PARENT_NOT_OPERATIONAL_AS_CURRENT_BASE

## Outputs obligatorios
- Reglas runtime trazables hacia PROJECT_CORE / CHATGPT / COPILOT.
- Evidence object por validator: `validator_id`, `files_checked`, `rules_checked`, `expected_value`, `actual_value`, `result`, `severity`, `timestamp`.
- Sidecar fields no vacíos cuando el contrato impacte prompt, QA, fallback o output.
- Changelog y manifest/hashes regenerados cuando se modifique cualquier archivo autoridad.

## Load order
1) STATUS/ACTIVE_VERSION. 2) Source inventory. 3) Profile360 registry. 4) Project Factory full contract. 5) Export packer. 6) QA gate.

## Rutas de archivos autoridad
- `IDUNEX/00_CONTROL_CENTER/STATUS.md`
- `IDUNEX/00_CONTROL_CENTER/ACTIVE_VERSION.md`
- `IDUNEX/99_MANIFESTS_SHA_LINEAGE/VERSION_MANIFEST.json`
- `IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATION_RESULT.json`
- `IDUNEX/99_MANIFESTS_SHA_LINEAGE/QA_FINAL_REPORT.md`
- `IDUNEX/03_PROJECT_FACTORY/05_PROJECT_FACTORY_FULL_CONTRACT.md`
- `IDUNEX/03_PROJECT_FACTORY/01_TEMPLATES/IDUNEX_PROJECT_T_03c23ec2/PROJECT_CORE/`
- `IDUNEX/17_EXPORT_PACKER/EXPORT_PACKER_POLICY.md`

## Reglas operativas
- Ningún PASS se acepta sin evidencia ejecutable; `DECLARED_PASS_WITHOUT_EVIDENCE = FAIL_FALSE_PASS`.
- No-loss: si una regla no llega a prompt, QA, fallback y sidecar, no cuenta como runtime.
- Anti-rollback: no usar bases anteriores, no recrear arquitectura, no borrar SRC_001-SRC_048, no borrar los dos archivos físicos SRC_049 y no degradar Copilot.
- GLOBAL_GO no es estado activo del motor; usar `ENGINE_GO = true`, `PROJECT_INSTANCE_GO = false_until_project_QA`, `OUTPUT_GO = false_until_output_QA_SIDECAR_HASH_LINEAGE`.
- Hash final del ZIP se registra solo en companion externo real; dentro del ZIP se conserva `RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD` para evitar auto-referencia imposible.

## Validators asociados
- `VALIDATE_PROJECT_CORE_EXISTS`
- `VALIDATE_PROJECT_CORE_NOLOSS`
- `VALIDATE_PROJECT_MANIFEST_TEMPLATE_MULTIMODAL`
- `VALIDATE_CANONICAL_CONTRACTS_NOT_SUMMARY_ONLY`
- `VALIDATE_SHA256_EXTERNAL_COMPANION_REAL_AND_MATCHING`

## Fail codes
- `FAIL_PROJECT_CORE_MISSING`: bloquea entrega hasta fix, evidencia y re-test.
- `FAIL_FACTORY_DEFINED_WEAK`: bloquea entrega hasta fix, evidencia y re-test.
- `FAIL_PROJECT_MANIFEST_TEMPLATE`: bloquea entrega hasta fix, evidencia y re-test.
- `FAIL_FALSE_PASS`: bloquea entrega hasta fix, evidencia y re-test.

## Fallback fixes
- Si falta ruta autoridad: detener entrega, agregar ruta exacta y re-ejecutar validator de contrato.
- Si falta sidecar field: completar campo, conectar con source_trace y revalidar hash interno.
- Si aparece resumen superficial: expandir a contrato operativo y re-test `VALIDATE_CANONICAL_CONTRACTS_NOT_SUMMARY_ONLY`.
- Si hay contradicción legacy: marcar como `HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY` o mover a política histórica.
- Si falla companion externo: regenerar ZIP, calcular SHA256 real y escribir `<sha256_final_real>  IDUNEX_MOTOR_v1.0.0.zip` fuera del ZIP.

## Sidecar fields mínimos
- `source_trace_ids`
- `profile360_sections_affected`
- `project_core_rule_id`
- `chatgpt_rule_id`
- `copilot_rule_id`
- `qa_rule_id`
- `fail_code`
- `fallback_fix`
- `hash_lineage_ref`
- `external_companion_ref`

## Source trace
Research Source -> Source Card SRC_### -> Profile360 Field ID -> Project Core Rule -> ChatGPT Agent Rule -> Copilot Agent Rule -> Model Profile Field -> Prompt / Output / QA / Fallback / Sidecar. SRC_049 mantiene alias exclusivo `ENV_PHYSICS_FULL10` y no se doble cuenta.

## QA checklist PASS/FAIL
- PASS: propósito, autoridad, alcance, inputs, outputs, load order, rutas concretas, validators, fail codes, fallback fixes, sidecar fields y source trace están presentes y verificables.
- PASS: PROJECT_CORE, CHATGPT, COPILOT, Profile360 y manifests están relacionados sin contradicción activa.
- FAIL: menos de 1,500 caracteres sin excepción técnica declarada.
- FAIL: declara PASS sin evidencia, sin archivos revisados o sin expected/actual.
- FAIL: usa base distinta a `a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e` como operativa.
- FAIL: borra o reduce source cards, mappings, Profile360, Copilot DOCX o sidecars.

## Ejemplos PASS/FAIL
- PASS: proyecto con PROJECT_CORE amplio, CHATGPT 10 MD, COPILOT 10 DOCX, config 8000, manifests y QA.
- FAIL: pack con solo prompts resumidos, sin sidecar ni SHA256SUMS reales del proyecto.

## Criterios de bloqueo
Bloquea entrega si falla cualquier validator asociado, si el companion externo no existe, si el SHA final no coincide, si hay `global_go:false` como estado activo, si el contrato es resumen, si hay rollback, si falta no-loss o si el reporte final no conserva evidencia.

## Relación operativa
PROJECT_CORE es fuente de verdad del proyecto; CHATGPT y COPILOT heredan reglas, no las inventan. Profile360 llena campos FACTORY_DEFINED hasta aprobación USER_APPROVED_LOCKED.

## Política no-loss
Todo cambio debe preservar contenido útil existente, mantener byte-level cuando no sea necesario modificar y registrar antes/después en `99_MANIFESTS_SHA_LINEAGE/CHANGELOG_IMPLEMENTATION_DELTA.md`.

## Política anti-rollback
Base operativa única: `a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e`. Las versiones previas no se usan como fuente, no se importan como fallback y no pueden sobrescribir contenido corregido.


## B259 correction-base normalization

correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
expected_correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
historical_previous_base_sha256 = a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e
historical_previous_base_policy = HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL
internal_prepackage_validation = PASS_INTERNAL_PREPACKAGE
external_companion_validation = REQUIRED_POST_PACKAGE
delivery_policy = DELIVERY_REQUIRES_EXTERNAL_COMPANION_VALIDATION
updated_at = NEUTRALIZED_ACTIVE_SCOPE

## Historical previous bases — non-operational

- `8c9cac03080a16947bf74d580fc423d605e97643498da50bca09722e396a7d35` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE
- `b259fb10bd9d69e8885b2f6896864d56dcc0edbf4f799f339bc533eb894e046b` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE
- `c6e7ab123ab6e0f70838da426c30114bd27e6809c24df73469e8ce5f47b838db` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE
- `ca146a322d59d0eb413756ef4fb7cde6a039bf796490473a7cff4cfb61514adf` — HISTORICAL_PREVIOUS_BASE_NOT_OPERATIONAL; HISTORICAL_ONLY_NOT_ACTIVE_ENGINE_POLICY; DO_NOT_USE_AS_BASE


## Surgical lineage patch — POSTPACKAGE_11F6F033_INPUT

- base_sha256_validated_before_patch = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- expected_correction_base_sha256 = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- input_package_sha256_before_this_surgical_patch = 1add3f8d3757d65bea5bcb848060a21a24523f297902639c4cffb7c184197b60
- current_input_base_status = ACTIVE_CORRECTION_INPUT_BASE_NOT_HISTORICAL_NOT_DO_NOT_USE
- parent_package_lineage = a7424ad2f7808162495c7c7f8aeba55a6e9160226e57e83cac7bd23b91c2666e — PREVIOUS_SURGICAL_INPUT_LINEAGE / PARENT_PACKAGE_LINEAGE_ONLY / HISTORICAL_PARENT_NOT_OPERATIONAL_AS_CURRENT_BASE
- FINAL_ZIP_SHA256_AUTHORITY = EXTERNAL_COMPANION_SHA256_FILE
- final_sha256_real = RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD
- EXTERNAL_VALIDATION_MODE = RUN_VALIDATOR_WITH_IDUNEX_PACKAGE_ZIP
- validator_hardening_added = VALIDATE_CURRENT_INPUT_BASE_NOT_MARKED_HISTORICAL_OR_DO_NOT_USE; VALIDATE_CURRENT_CORRECTION_BASE_NOT_MARKED_HISTORICAL_OR_DO_NOT_USE; VALIDATE_REPORT_HEADINGS_MATCH_ACTIVE_INPUT_BASE_PREFIX; VALIDATE_HISTORICAL_AUDITS_EXPLICITLY_NON_OPERATIONAL; VALIDATE_NO_DUPLICATE_CURRENT_BASE_IN_HISTORICAL_LISTS; VALIDATE_EXTERNAL_VALIDATION_SUMMARY_MATCHES_COMPANION_SHA; VALIDATE_VALIDATOR_FALSE_PASS_GUARD_FOR_BASE_STATUS_CONTRADICTIONS

## P0 lifecycle additions

Project creation uses PROJECT_CREATE_INPUT_MODES_4WAY. Project update, retirement, archived readonly and engine-update migrations must follow the lifecycle protocols in 03_PROJECT_FACTORY/03_LIFECYCLE.
