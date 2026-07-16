# MODEL_ALIAS_RESOLVER_AND_AUTOLOAD

## Objetivo

Resolver de forma obligatoria nombres, alias y códigos de modelo antes de cualquier respuesta IDUNEX de imagen, video, voz, Suno, texto/persona, audio, SFX, Foley, QA, sidecar o vendor handoff.

## Entradas resueltas

- Nombre corto: `Luma`, `Aren`.
- Nombre completo: `Luma Suyay Benavides`, `Aren Quilla Rojas`.
- Nombre artístico definido por proyecto.
- Código corto: `MODEL_001`, `MODEL_002`.
- Código largo: `MODEL_001_AREN`, `MODEL_002_LUMA`.
- Alias definidos por proyecto.

## Secuencia obligatoria

1. Leer archivos reales del proyecto antes de responder.
2. Resolver alias contra `PROJECT_MANIFEST`, `MODEL_INDEX`, Profile360 y Project Core.
3. Cargar 10 archivos core obligatorios del proyecto.
4. Cargar 1 Profile360 completo por modelo, nunca resumen.
5. Cargar TechExt y Master Anchors cuando la modalidad lo requiere.
6. Cargar Agent Runtime Governance, QA, sidecar/hash/lineage y vendor checklist.
7. Si falta cualquier requisito, bloquear con fail code específico.

## Bloqueos mínimos

- BLOCKED_MODEL_ALIAS_NOT_RESOLVED
- BLOCKED_PROFILE360_NOT_LOADED
- BLOCKED_TECHEXT_NOT_AVAILABLE
- BLOCKED_MASTER_ANCHORS_NOT_AVAILABLE
- BLOCKED_RUNTIME_CORE_NOT_LOADED
- BLOCKED_OUTPUT_GO_TRUE_WITHOUT_SIDECAR_HASH_LINEAGE
- BLOCKED_PROJECT_CLOSE_WITHOUT_GOLDEN_TESTS_DEFINED

## Regla de exportación Project Factory

Este resolver debe exportarse a `PROJECT_CORE/10_AGENT_RUNTIME_GOVERNANCE/` y quedar referenciado por los configs ChatGPT/Copilot de 8000 caracteres.
