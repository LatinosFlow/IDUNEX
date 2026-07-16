# Colloquial Fuzz Suite - LEGACY_NON_AUTHORITY

- `crear un proyecto demo generico con dos modelos adultos ficticios` -> CREATE_PROJECT_AUTO / mode=AUTO / ask=False / generate=True / expected=none
- `que el motor defina todo` -> CREATE_PROJECT_AUTO / mode=AUTO / ask=False / generate=True / expected=none
- `quiero personalizar básico` -> CREATE_PROJECT_BASIC_GUIDED / mode=BASIC_GUIDED / ask=True / generate=False / expected=needs_basic_template
- `quiero definir cada rasgo` -> CREATE_PROJECT_DETAILED / mode=DETAILED / ask=True / generate=False / expected=needs_detailed_template
- `crear proyecto con 11 modelos` -> CREATE_PROJECT_AUTO / mode=AUTO / ask=False / generate=False / expected=BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT
- `exportar agente con 10 modelos` -> GENERATE_OUTPUT / mode=AUTO / ask=False / generate=True / expected=20_files_exact
- `exportar agente con 2 modelos` -> GENERATE_OUTPUT / mode=AUTO / ask=False / generate=True / expected=12_files_exact
- `TechExt citado pero no embebido` -> AUDIT_PROJECT / mode=AUTO / ask=False / generate=False / expected=BLOCKED_TECH_EXT_NOT_MATERIALIZED
- `core compactado sin coverage map` -> AUDIT_PROJECT / mode=AUTO / ask=False / generate=False / expected=BLOCKED_RUNTIME_COVERAGE_MAP_MISSING
- `alias extendido no resuelto` -> AUDIT_PROJECT / mode=AUTO / ask=False / generate=False / expected=BLOCKED_MODEL_ALIAS_NOT_RESOLVED
- `modelo legacy fuera de namespace` -> AUDIT_PROJECT / mode=AUTO / ask=False / generate=False / expected=BLOCKED_LEGACY_MODEL_OUTSIDE_NAMESPACE
- `PROJECT_CORE con prefijos duplicados` -> AUDIT_PROJECT / mode=AUTO / ask=False / generate=False / expected=BLOCKED_PROJECT_CORE_PREFIX_DUPLICATE
- `actualiza este proyecto con el nuevo motor` -> UPDATE_PROJECT_WITH_NEW_ENGINE / mode=AUTO / ask=True / generate=False / expected=classify_variables
- `OUTPUT_REAL_10_10 sin asset` -> AUDIT_OUTPUT / mode=AUTO / ask=False / generate=False / expected=BLOCKED_OUTPUT_REAL_10_10_WITHOUT_ASSET
- `PASS con auditoría independiente FAIL` -> AUDIT_ENGINE / mode=AUTO / ask=False / generate=False / expected=BLOCKED_TRUTHFULNESS_INDEPENDENT_FAIL
