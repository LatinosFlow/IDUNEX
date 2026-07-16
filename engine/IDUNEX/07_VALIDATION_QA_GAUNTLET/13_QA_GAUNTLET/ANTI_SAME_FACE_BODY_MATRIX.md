# ANTI_SAME_FACE_BODY_MATRIX.md

## Scope
Esta matriz valida exclusivamente anti-clonación facial, anti same-face, anti same-body y separación de identidad entre múltiples modelos. No valida adultez/voz; esa función pertenece a `ADULT_AGE_BODY_VOICE_MATRIX.md`.

## Authority
- Primary source focus: `SRC_032_Anti_same-face_anti_same-body_para_10_modelos`.
- Runtime domains: `identity_separation`, `face_uniqueness`, `body_uniqueness`, `lineup_differentiation`, `anti_clone_guardrail`.
- Required state: `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.
- Production block: `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; project_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.

## Inputs
1. `04_PROFILE360_SYSTEM/01_SCHEMA/PROFILE360_FIELD_REGISTRY.json`
2. `05_SOURCE_TO_RUNTIME/02_MAPS/SOURCE_TO_RUNTIME_MASTER_MAP.json`
3. `05_SOURCE_TO_RUNTIME/01_INVENTORY/SOURCE_INVENTORY_MASTER.json`
4. `13_QA_GAUNTLET/FAIL_CODE_REGISTRY.json`
5. Source card de `SRC_032`.
6. Sidecars y payloads de validación cuando exista lineup o roster multimodelo.

## Checks

| Check ID | Function | PASS | FAIL |
|---|---|---|---|
| ANTI_CLONE_001 | anti clonación facial | Cada modelo conserva firma facial diferenciable: estructura, proporciones, ojos, nariz, mandíbula, piel y expresión base. | Dos modelos convergen en rostro, simetría, mirada, nariz, mandíbula o expresión base. |
| ANTI_CLONE_002 | anti same-face | `same_face_blocker` rechaza similitud facial excesiva antes de generar o aprobar output. | El sistema permite caras intercambiables o indistinguibles. |
| ANTI_CLONE_003 | anti same-body | `same_body_blocker` rechaza siluetas, proporciones o presencia corporal clonadas. | Dos modelos comparten cuerpo, altura aparente, postura, masa o proporción sin justificación. |
| ANTI_CLONE_004 | diversidad controlada | La diversidad se logra sin romper identidad individual ni crear drift aleatorio. | Diferenciación basada en cambios arbitrarios que dañan identidad o coherencia. |
| ANTI_CLONE_005 | separación de roster | El lineup mantiene distancia visual por pares y evita colisiones entre identidades. | El roster presenta colisiones de identidad o cuerpos duplicados. |
| ANTI_CLONE_006 | protección contra convergencia | Rechaza outputs donde iluminación, styling o prompt reducen diferencias reales entre modelos. | Cámara, pose o wardrobe homogeneizan modelos hasta parecer clones. |
| ANTI_CLONE_007 | sidecar evidence | Sidecar registra campos/source_ids/adapter y hash reproducible para evaluación. | No hay evidencia trazable de rechazo o aceptación anti-clon. |

## Procedure
1. Cargar campos relacionados con `same_face_blocker`, `same_body_blocker`, `anti_clone_guardrail`, `facial_uniqueness_signature`, `body_uniqueness_signature`, `lineup_differentiation`, `pairwise_face_distance` y `pairwise_body_distance`.
2. Confirmar que `SRC_032` está disponible como autoridad primaria en los campos anti same-face/same-body reforzados.
3. Evaluar pares de modelos: rostro, cuerpo, pose base, presencia, wardrobe y expresión.
4. Rechazar pares con colisión visual o corporal sin esperar output final.
5. Registrar fail code, fallback y retest por cada colisión.
6. Bloquear `PROJECT_GO` si existe clonación, convergencia o evidencia insuficiente.

## Fail codes
- `FAIL_ANTI_SAME_FACE_COLLISION`
- `FAIL_ANTI_SAME_BODY_COLLISION`
- `FAIL_ROSTER_IDENTITY_COLLISION`
- `FAIL_PAIRWISE_DISTANCE_BELOW_THRESHOLD`
- `FAIL_LINEUP_CONVERGENCE`
- `FAIL_ANTI_CLONE_EVIDENCE_MISSING`

## Fallback fixes
- Reforzar marcadores faciales diferenciales por modelo.
- Separar proporciones corporales y presencia física.
- Cambiar pose/cámara/wardrobe solo como apoyo, no como sustituto de identidad.
- Recalcular distancia pairwise y repetir golden test.
- Registrar sidecar actualizado con hashes reproducibles.

## PASS criteria
- 0 colisiones de rostro.
- 0 colisiones de cuerpo.
- 0 convergencia de lineup.
- Evidencia sidecar/hash reproducible.
- `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; project_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE`, `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.
- Decisión final: `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.

## FAIL criteria
- Cualquier par de modelos indistinguible.
- Cualquier cuerpo clonado.
- Cualquier rechazo anti-clon omitido.
- Cualquier intento de escalar a `PROJECT_GO`, `PROJECT_10` o `GLOBAL_GO`.

## Output report
El reporte debe indicar pares evaluados, dimensiones diferenciadas, colisiones detectadas, fail codes, fallback aplicado, retest y decisión. La única decisión permitida para el motor base es `prior_validation_reference=NON_AUTHORITY_REFERENCE; active_validation_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.

## Production decision
Esta matriz no autoriza producción. Solo confirma separación de identidades para pruebas formales no productivas y revisión posterior de proyecto.
