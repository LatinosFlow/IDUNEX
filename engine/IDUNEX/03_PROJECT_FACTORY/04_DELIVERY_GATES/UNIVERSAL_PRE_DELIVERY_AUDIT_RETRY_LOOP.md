# Universal Pre Delivery Audit Retry Loop - LEGACY_NON_AUTHORITY

Applies to update motor, downgrade motor, create project, update project, migrate project, retire project, create agent, generate output, audit output and reissue package.

Flow: generate/apply, audit, root_cause if fail, surgical_fix, rebuild, recalc manifests/SHA, reopen final ZIP, reauditar and repeat until 100% PASS.
