# 22_QA_GAUNTLET_CANONICAL_BRIDGE

Puente canónico de registry, orden y evidencia hacia la batería QA. La numeración legacy 13_QA_GAUNTLET se conserva por compatibilidad. Esta capa no es un executable ni puede emitir cierre global.

El único entrypoint autoritativo es `IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`. Los scripts secundarios solo pueden ejecutarse por delegación de ese entrypoint y sus resultados tienen alcance `LOCAL_SUBCHECK_ONLY`.

`STATE_AUTHORITY=governance/CURRENT_STATE.json`, `BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE` y `BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT`. Este bridge no replica ni decide M02/M03, y no autoriza Proyecto Demo, release, tag o cierre productivo.

Validators obligatorios: productivo, source cards, source-to-runtime, Profile360, configs 8000, Scene Physics, manifests, hashes, companion externo y false-pass guard.
