## Phase 3 file-level inheritance
inherits = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RESEARCH_LANDING_RULE
inherits_runtime_qa = RESEARCH_RUNTIME_GLOBAL_RULES#COMMON_RUNTIME_QA_BLOCK
research_specific_extracts_preserved = true

# SIDECAR PLACEHOLDER POLICY

TEMPLATE_ONLY permite placeholders. DRAFT permite placeholders controlados. QA_REVIEW no debe contener placeholders críticos salvo valores explícitamente marcados como test. PROJECT_TEST_READY y PROJECT_GO bloquean cualquier *_PLACEHOLDER, *_TEMPLATE_ID, HASH_INPUT_PLACEHOLDER, HASH_OUTPUT_PLACEHOLDER, REVIEWER_PLACEHOLDER o VENDOR_PLACEHOLDER.


## Phase 3 research inheritance
