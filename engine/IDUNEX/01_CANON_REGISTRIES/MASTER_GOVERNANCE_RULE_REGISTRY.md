# IDUNEX Master Governance Rule Registry

Autoridad activa: familias estables GOV, VER, ENG, PRJ, AGT, CAN, RES, RUN, PMT, VAL, AUD, UPD, MIG, BRD, REF, SAF, ZIP, DUP, LIN, BLT y CRT.

Los hitos H quedan como lineage compacto no autoritativo. La regla estable `ZIP-EXT-001` reemplaza operativamente a `H382R_EXTERNAL_WHOLE_ZIP_AUTHORITY` sin perder trazabilidad histórica.

Regla central: si una superficie H contradice un ID estable de este registro, prevalece el ID estable y el validator maestro debe bloquear el release.


## Regla BRD-PAL-001

Bloquea leakage de paletas reales de proyecto/marca en superficies activas genéricas del motor. `PROJECT_BRAND_ENTITY` solo puede convivir con tokens semánticos `PROJECT_BRAND_*`; los valores reales se resuelven exclusivamente desde `PROJECT_BRAND_REGISTRY` del proyecto generado o input externo autorizado. La regla queda conectada a familias BRD, PRJ, BLT y VAL, y se valida mediante `VALIDATE_MASTER_GOVERNANCE_NATIVE.py` y `VALIDATE_IDUNEX_RUNTIME.py`.
