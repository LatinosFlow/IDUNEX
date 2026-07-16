# Project Intake Decision Tree - LEGACY_NON_AUTHORITY

Minimum fields: project_id/name, model_count 1-10, general purpose, and adult fictional/non-real/non-celebrity requirement when applicable.

Decision tree:
- Sufficient data + AUTO authorization: generate.
- Missing critical non-inferable data: ask only what is required.
- Basic personalization: use BASIC_GUIDED template.
- Detailed personalization: use DETAILED template.
- Lock or safety conflict: block or request correction.
- More than 10 models: BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT.
