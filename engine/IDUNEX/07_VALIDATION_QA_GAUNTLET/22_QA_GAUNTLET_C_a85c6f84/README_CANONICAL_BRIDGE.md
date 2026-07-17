# 22_QA_GAUNTLET_CANONICAL_BRIDGE

Puente canónico de registry, orden y evidencia hacia la batería QA. La numeración legacy 13_QA_GAUNTLET se conserva por compatibilidad. Esta capa no es un executable ni puede emitir cierre global.

El único entrypoint autoritativo es `IDUNEX/99_MANIFESTS_SHA_LINEAGE/VALIDATE_IDUNEX_RUNTIME.py`. Los scripts secundarios solo pueden ejecutarse por delegación de ese entrypoint y sus resultados tienen alcance `LOCAL_SUBCHECK_ONLY`.

Estado vigente: `MOTOR_STATUS=EN_REVISION`, `M02_RESULT=M02_FAIL`. Este bridge no decide M02 ni autoriza Proyecto Demo, release, tag o cierre productivo.

Validators obligatorios: productivo, source cards, source-to-runtime, Profile360, configs 8000, Scene Physics, manifests, hashes, companion externo y false-pass guard.
