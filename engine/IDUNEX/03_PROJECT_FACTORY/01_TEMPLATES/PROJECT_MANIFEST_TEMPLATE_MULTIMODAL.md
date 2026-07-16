# Project Manifest Template - multimodal IDUNEX project

project_type = multimodal_idunex_project
model_count_min = 1
model_count_max = 10
project_core_required = true
chatgpt_core_files_exact = 10
copilot_core_files_exact = 10
agent_runtime_files_max = 20
output_modalities = image, video, voice, suno, music, audio_sfx_foley, text, dialogue, copilot_docx, promptpacks, sidecars
source_scope = ALL_ACTIVE_SOURCES_001_049
commercial_scope = PRODUCTIVE_BASE_ENGINE_PROJECT_FACTORY
real_output_policy = OUTPUT_REQUIRES_QA_SIDECAR_HASH_LINEAGE
identity_language_policy = HUMANIZED_DIGITAL_MODEL
production_state = PRODUCTIVE_BASE_ENGINE
project_instance_go = false_until_project_QA
output_go = false_until_output_QA_SIDECAR_HASH_LINEAGE
