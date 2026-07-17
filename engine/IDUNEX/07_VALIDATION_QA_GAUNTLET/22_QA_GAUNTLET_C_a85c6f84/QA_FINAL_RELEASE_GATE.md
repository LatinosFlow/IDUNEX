# QA_FINAL_RELEASE_GATE

This file is a non-executable policy reference and cannot emit global closure.

Current state is `MOTOR_STATUS=EN_REVISION`, `M02_RESULT=M02_FAIL`, `RELEASE_AUTHORIZED=false` and `ENGINE_FINAL_RELEASE_GATE=BLOCKED`. The sole validator entrypoint is `IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`, and that technical result does not decide M02 or authorize release.

If governance later authorizes a release after independent re-audit, the external companion `IDUNEX_MOTOR_v1.0.0.zip.sha256` must exist and match the final ZIP. Inside the ZIP, `final_sha256_real` remains `RECORDED_EXTERNALLY_IN_COMPANION_AFTER_PACKAGE_BUILD`.
