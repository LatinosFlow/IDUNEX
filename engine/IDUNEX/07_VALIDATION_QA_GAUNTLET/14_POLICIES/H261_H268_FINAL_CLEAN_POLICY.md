# H261-H268 FINAL CLEAN POLICY

SEMANTIC_VERSION=v1.0.0. ROOT_UNICO=IDUNEX. CORRECTION_MODE=DIRECT_CANONICAL_NO_PATCH.

## Active scope expression
Runtime active surfaces must express previous labels only as `prior_scope_reference=NON_AUTHORITY_REFERENCE` and current authority as `active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE`.

## Retention
Exact duplicate files are allowed only when listed in `EXACT_DUPLICATE_RETENTION_ALLOWLIST.json` with a reason code and validator requirement. Human audit reports, temporary logs, staging output and test ZIPs must not be active authority.

## Truthfulness
CREATIVE_OUTPUT_CERTIFIED remains FALSE until a real asset has sidecar, hashes, reviewer, lineage, QA expected/actual and EXECUTED_PASS.
