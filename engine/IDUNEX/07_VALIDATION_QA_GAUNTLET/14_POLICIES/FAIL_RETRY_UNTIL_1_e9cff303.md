# FAIL_RETRY_UNTIL_100_PERCENT_PASS_GLOBAL

Estado: ACTIVE_PASS

Si falla cualquier control: root_cause -> surgical_fix -> regression_scope -> rebuild affected files -> rewrite paths if needed -> rebuild all affected manifests -> rebuild ZIP -> reopen final ZIP -> run full independent audit -> repeat until 0 FAIL.

Aplica a motor, proyectos, Generic Project Demo, updates, downgrades, retiros, reissue y regenerate.

## actual_value
steps=10; applies_to=12; max_fail_allowed=0

## LEGACY_NON_AUTHORITY Universal Retry Loop Extension
All update, downgrade, create, migrate, retire, agent export, output generation, output audit and reissue operations must follow generate/apply, audit, root_cause, surgical_fix, rebuild, recalc manifests/SHA, reopen final ZIP and reauditar until 100% PASS.
