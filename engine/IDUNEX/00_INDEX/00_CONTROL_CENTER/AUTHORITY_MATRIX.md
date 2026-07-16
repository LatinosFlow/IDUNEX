# IDUNEX Authority Matrix

This matrix defines the single source of authority by dimension for the pure motor.

| Dimension | Primary authority | Auxiliary files | Blocker if violated |
|---|---|---|---|
| Motor state | 00_CONTROL_CENTER/ACTIVE_VERSION.md | MANIFEST, FINAL_AUDIT_REPORT | Contradictory GO/NO_GO state |
| Identity schema | 04_PROFILE360_SYSTEM/01_SCHEMA/PROFILE360_FIELD_REGISTRY.json | 20_MOTOR_CORE_10/01_IDENTITY_MEMORY_PROFILE360.md | Field without source/failcode |
| Face/body realism | Core 02 and Profile360 fields | Source runtime libraries | Plastic/synthetic drift |
| Voice/music/text | Core 08 and channel adapters | Source runtime libraries | Vocal/linguistic drift |
| Project creation | 03_PROJECT_FACTORY | Policies | Concrete project name inside motor |
| Agent load | 04_AGENT_FACTORY and adapter | Copilot DOCX | Agent invents project canon |
| QA | 13_QA_GAUNTLET/FAIL_CODE_REGISTRY.json | Golden tests/linter files | Unblocked failure |
| Sidecar/lineage | 07_MULTIMODAL_VENDOR_ADAPTERS/SIDECAR_METADATA_ADAPTER.md | 15_SCHEMAS/SIDECAR.schema.json | Missing trace/hash/state |
| Legal/privacy | 14_POLICIES | Sidecar schema | Sensitive invention/leakage |

Rule: if two files discuss a dimension, this matrix decides priority.
