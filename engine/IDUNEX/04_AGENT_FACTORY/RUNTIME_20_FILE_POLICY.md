# Runtime 20-File Policy - LEGACY_NON_AUTHORITY

- One ChatGPT agent per project.
- One Copilot agent per project.
- Maximum 20 files per agent.
- Maximum 10 models per project/agent.
- Runtime = 10 core IDUNEX files + 1 MODEL_RUNTIME_PROFILE_FULL per model.
- 1 model = 11 files; 2 models = 12 files; 5 models = 15 files; 10 models = 20 files.
- If 11+ models: BLOCKED_MAX_MODEL_COUNT_OR_AGENT_FILE_LIMIT.
- No split agents. No destructive summary. Digest is evidence only.
