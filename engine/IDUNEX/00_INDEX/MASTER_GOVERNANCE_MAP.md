# MASTER_GOVERNANCE_MAP

Este mapa convierte el Informe Maestro en gobernanza nativa del motor IDUNEX v1.0.0. No copia el PDF bruto: destila reglas, contratos, schemas, validators, policies y factory logic.

## Prioridad de autoridad
1. Registry de IDs estables GOV/VER/ENG/PRJ/AGT/CAN/RES/RUN/PMT/VAL/AUD/UPD/MIG/BRD/REF/SAF/ZIP/DUP/LIN/BLT/CRT.
2. Contratos mayores: ENGINE_OUTPUT_CONTRACT, PROJECT_OUTPUT_CONTRACT, AGENT_LOAD_CONTRACT.
3. Schemas y validators integrados.
4. Factory logic vigente.
5. Evidence lineage compacta.
6. Hitos H como lineage no autoritativo.

## Regla ZIP-EXT-001
El SHA256 y bytes absolutos del ZIP completo se certifican solo fuera del ZIP: companion `.zip.sha256`, release certificate externo y companion externo. Ningún archivo interno autocertifica el SHA integral del ZIP que lo contiene.


## Regla BRD-PAL-001

Bloquea leakage de paletas reales de proyecto/marca en superficies activas genéricas del motor. `PROJECT_BRAND_ENTITY` solo puede convivir con tokens semánticos `PROJECT_BRAND_*`; los valores reales se resuelven exclusivamente desde `PROJECT_BRAND_REGISTRY` del proyecto generado o input externo autorizado. La regla queda conectada a familias BRD, PRJ, BLT y VAL, y se valida mediante `VALIDATE_MASTER_GOVERNANCE_NATIVE.py` y `VALIDATE_IDUNEX_RUNTIME.py`.
