# GOV-IDUNEX — Corrección de resolución de identidad H113

Fecha: 2026-07-22
Versión documental: v1
Estado: EN_REVISION
Control: AUD-033 / issue #64

## Hallazgo validado

El run M02 `29936388876` obtuvo 0/30. El diagnóstico sintético `29937730988` aisló `FAIL_H113_DEFERRED_ENGINE_SHA_ACTIVE` con detalle `certificate engine sha invalid`.

La causa fue una dependencia circular en `resolve_engine_zip_sha256()`: la identidad AUD-003 del repositorio solo se aceptaba cuando `M02_RESULT=M02_PASS`, aunque M02 necesita generar la matriz antes de recomputar ese resultado.

## Corrección

La identidad no-release se acepta únicamente cuando coinciden el companion AUD-003, el manifiesto físico y `engine_change_control` en SHA, conteo y bytes; además el motor debe permanecer `EN_REVISION` y release/tag deben seguir bloqueados.

Identidad criptográfica no equivale a autorización operativa. Demo, generación general, agentes, release, tag, OFICIAL y cierre productivo continúan bloqueados.

## Evidencia requerida

- prueba integral sintética N1;
- certificado sin sentinel diferido;
- ZIP y companion válidos;
- baseline, governance, intake, security y runtime validator PASS;
- M02 y M03 no recomputados hasta ejecuciones completas nuevas.

## Reversión

Revertir el commit correctivo completo. No se modifica el ZIP real del Proyecto 000 Demo.
## Hallazgo secuencial de contrato externo

Después de resolver H113, la prueba integral alcanzó la emisión externa y detectó `FAIL_EXTERNAL_ARTIFACT_CONTENT` con detalle `release_certificate:validation headers`. La causa era duplicación de `VALIDATORS_FAIL` y `BLOCKING_WARNINGS`: una vez en el envelope externo y otra dentro del certificado interno embebido.

La corrección conserva íntegra la autoridad interna salvo esas dos líneas de contador, que se emiten una sola vez en el envelope externo. El validator sigue exigiendo exactamente una ocurrencia de cada header y derivación byte-exacta desde el ZIP reabierto.
