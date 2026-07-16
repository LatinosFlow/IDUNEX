# GOLDEN_TESTS_PROJECT_EXPORT_TEMPLATE

Project Factory exporta esta matriz por proyecto. Estado inicial: PROJECT_TESTS_DEFINED, no ejecutado.

| Test | Título | Evidencia |
|---|---|---|
| TEST_001_IMAGE_PORTRAIT | Imagen retrato | Face360, Skin360, Lighting360, sidecar/hash/lineage |
| TEST_002_IMAGE_FULL_BODY | Imagen cuerpo completo | Body360, Wardrobe360, Camera360, contact shadows |
| TEST_003_IMAGE_GROUP | Imagen grupo | Pairwise360, anti-merge, scale |
| TEST_004_VIDEO_CONTINUITY | Video continuidad | Motion360, Environment360, frame continuity |
| TEST_005_VOICE_PROFILE | Voz hablada | Voice360, F0, WPM, register |
| TEST_006_SUNO_MODEL_POV | Suno/model POV | Voice360, psychology, POV, song identity |
| TEST_007_TEXT_PERSONA_CHAT | Texto/persona chat | Dialogue persona, memory boundaries |
| TEST_008_ENVIRONMENT_PHYSICS | Entorno/física | Scene physics, lighting, reflections |
| TEST_009_AUDIO_SFX_FOLEY | Audio/SFX/Foley | Foley sync, acoustic realism |
| TEST_010_VENDOR_HANDOFF | Vendor handoff | Vendor checklist, settings, lineage |


# LEGACY_NON_AUTHORITY
Export templates that generate ChatGPT/Copilot runtime must output exactly 10 core IDUNEX files plus 1 MODEL_RUNTIME_PROFILE_FULL per model, require PROJECT_RUNTIME_COVERAGE_MAP, block TechExt null inheritance with BLOCKED_TECH_EXT_NULL_INHERITANCE, block missing LEGACY_NON_AUTHORITY core embedding with BLOCKED_RUNTIME_CORE_LEGACY_NON_AUTHORITY, enforce max 20 files, max 10 models, no split agents and no destructive summary.
