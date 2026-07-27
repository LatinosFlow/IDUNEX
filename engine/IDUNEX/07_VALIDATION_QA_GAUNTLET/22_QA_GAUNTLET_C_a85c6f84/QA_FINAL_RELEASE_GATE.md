# QA_FINAL_RELEASE_GATE

This file is a non-executable policy reference and cannot emit global closure.

`STATE_AUTHORITY=governance/CURRENT_STATE.json`, `BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE` and `BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT`. The sole validator entrypoint is `IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`; this policy neither mirrors mutable M02/M03 values nor authorizes release.

If governance later authorizes a release after independent re-audit, the external companion `IDUNEX_MOTOR_v1.0.0.zip.sha256` must exist and match the final ZIP. Inside the ZIP, `final_sha256_real` remains `RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD`.
