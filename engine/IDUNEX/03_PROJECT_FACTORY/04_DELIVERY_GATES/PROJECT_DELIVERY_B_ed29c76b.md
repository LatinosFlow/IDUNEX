# PROJECT_DELIVERY_BY_CONTRACT_NOT_COUNT_GATE

Motor: IDUNEX_MOTOR_v1.0.0  
Internal label: LEGACY_NON_AUTHORITY  
Status: ACTIVE_BLOCKING

## Regla superior
No basta PASS por conteo. `sections=61`, `techext=10`, `runtime=12`, `sidecars=4` o `validators_fail=0` son insuficientes si no existe validacion por contrato exacto del motor.

## Gates obligatorios
- `PROFILE360_REGISTRY_EXACT_MATCH_GATE` -> `BLOCKED_PROFILE360_REGISTRY_MISMATCH`: Validate exact ids 00..60, exact names, exact order and canonical count; reject P360-00 or invented names.
- `PROFILE360_SECTION_PAYLOAD_UNIQUENESS_GATE` -> `BLOCKED_PROFILE360_SECTION_PAYLOAD_CLONED`: Detect cloned/generic section payloads and identical required_fields where registry function differs.
- `PROFILE360_SECTION_DEPTH_GATE` -> `BLOCKED_PROFILE360_SECTION_UNDERFILLED`: Require sufficient section-specific materialization: values, trace, QA, sidecar and fallback.
- `TECHEXT_FIELD_LEVEL_CONTRACT_GATE` -> `BLOCKED_TECHEXT_FIELD_CONTRACT_MISSING`: Validate every official TechExt required field, not only module count.
- `MODEL_RUNTIME_PROFILE_FULL_AGENT_PARITY_GATE` -> `BLOCKED_FAKE_FULL_RUNTIME_PROFILE`: Agent-loaded per-model file must contain/materialize the FULL profile, not a summary beside a JSON full elsewhere.
- `AGENT_MODEL_FILE_FULLNESS_MINIMUM_GATE` -> `BLOCKED_AGENT_MODEL_FILE_UNDERFILLED`: Compute fullness metrics: sections, TechExt fields, anchors, source trace, sidecars, QA/fallback, field_count, parity mapping/hash.
- `CORE_NO_BOILERPLATE_SIMILARITY_GATE` -> `BLOCKED_CORE_BOILERPLATE_RUNTIME`: Validate 10 runtime core files have distinct domains and similarity avg <= 0.80.
- `PROJECT_CONFIG_8000_EXPORT_GATE` -> `BLOCKED_PROJECT_CONFIG_8000_EXPORT_FAIL`: Both ChatGPT and Copilot project configs must be exactly 8000 chars and contain required controls.
- `COVERAGE_MAP_GRANULARITY_GATE` -> `BLOCKED_COVERAGE_MAP_TOO_SHALLOW`: Coverage map must trace model -> Profile360 section/field/subfield -> TechExt module/field -> anchors/source/runtime/sidecar/QA/fail/fallback/evidence.
- `PROJECT_INTERNAL_AUDIT_DEPTH_GATE` -> `BLOCKED_PROJECT_AUDIT_DEPTH_INSUFFICIENT`: 0 validators_fail is invalid unless all deep validators exist and PASS with concrete actual_value.
- `PROJECT_FACTORY_SIMPLE_PROMPT_FULL_OUTPUT_GATE` -> `BLOCKED_SIMPLE_PROMPT_WEAK_VALIDATION`: Simple/colloquial prompts trigger the same full output and validation contract.
- `UPDATE_PROJECT_CONTRACT_VALIDATION_GATE` -> `BLOCKED_PROJECT_UPDATE_CONTRACT_REGRESSION`: Project updates/migrations apply the same deep gates and cannot preserve previous structural errors.
- `UPDATE_MODEL_DATA_CONTRACT_VALIDATION_GATE` -> `BLOCKED_MODEL_DATA_UPDATE_INCOMPLETE`: Model data updates recalculate dependent Profile360, TechExt, anchors, alias, coverage, hashes and runtime.
- `MOTOR_UPDATE_CONTRACT_VALIDATION_GATE` -> `BLOCKED_MOTOR_UPDATE_PROJECT_FACTORY_REGRESSION`: Motor updates preserve prior layers and run simple project generation regression against Project Factory.
- `TRUTHFULNESS_PROJECT_DELIVERY_GATE` -> `BLOCKED_TRUTHFULNESS_PROJECT_PASS_FALSE`: No DELIVERY_ALLOWED if any deep validator is missing, actual_value empty, PASS by count, known independent equivalent fail, or contract gate fail.
- `PROJECT_DELIVERY_BY_CONTRACT_NOT_COUNT_GATE` -> `BLOCKED_PROJECT_DELIVERY_BY_COUNT_ONLY`: Counts are evidence hints only; exact contract PASS is mandatory.

## Fallback operativo
Si cualquier gate falla: bloquear entrega, identificar root_cause, corregir solo la causa raiz, recalcular manifests/SHA, reemitir ZIP, reabrir ZIP final y reauditar todo el scope hasta PASS.
