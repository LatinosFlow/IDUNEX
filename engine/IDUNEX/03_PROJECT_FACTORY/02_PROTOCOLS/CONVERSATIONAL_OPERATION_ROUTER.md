# Conversational Operation Router - LEGACY_NON_AUTHORITY

## Purpose
Detect natural language operations without requiring long technical prompts.

## Supported intents
- `CREATE_PROJECT_AUTO`: crear proyecto demo, que el motor defina todo, crear un proyecto demo generico con dos modelos adultos ficticios.
- `CREATE_PROJECT_BASIC_GUIDED`: personalizar básico, solo edad rol estilo, plantilla corta.
- `CREATE_PROJECT_DETAILED`: definir cada rasgo, detalle rostro cuerpo voz ropa movimiento.
- `CREATE_PROJECT_FROM_REFERENCE_SET`: crear desde set referencia, usar referencia activa.
- `UPDATE_PROJECT_WITH_NEW_ENGINE`: actualiza este proyecto con el nuevo motor, migrar proyecto a motor nuevo.
- `UPDATE_PROJECT_ONLY`: actualiza solo proyecto, corregir proyecto sin tocar motor.
- `UPDATE_ENGINE_SURGICAL`: aplicar corrección quirúrgica al motor, patch motor.
- `DOWNGRADE_ENGINE`: downgrade motor, remover cambio del motor.
- `DOWNGRADE_PROJECT`: downgrade proyecto, volver proyecto a estado anterior.
- `RETIRE_PROJECT`: retira este proyecto, archivar proyecto.
- `AUDIT_ENGINE`: audita motor, audita si el motor está 10/10.
- `AUDIT_PROJECT`: audita proyecto, audita si está 10/10.
- `GENERATE_OUTPUT`: genera una imagen de Nara, haz una canción desde Dante, prompt/output con sidecar.
- `AUDIT_OUTPUT`: audita output, validar imagen/video/audio generado.
- `REISSUE_PACKAGE`: reemite paquete, reissue package.
- `MIGRATE_PROJECT`: migra proyecto, migrar no-loss.

## Required routing result
Every conversational intake must produce: detected_intent, operation_mode, required_user_inputs, fields_engine_can_autofill, should_ask, should_generate, blockers and gates.

## Fallback fixes
- If prompt asks for more than 10 models, return BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT.
- If alias is unresolved, return BLOCKED_MODEL_ALIAS_NOT_RESOLVED.
- If output 10/10 is claimed without asset, sidecar, hashes, QA, reviewer and lineage, return BLOCKED_OUTPUT_REAL_10_10_WITHOUT_ASSET.
