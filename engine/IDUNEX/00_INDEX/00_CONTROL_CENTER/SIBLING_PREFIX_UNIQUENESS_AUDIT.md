# SIBLING_PREFIX_UNIQUENESS_AUDIT - P0.2-008

Engine: IDUNEX_MOTOR_v1.0.0
Fecha: NEUTRALIZED_ACTIVE_SCOPE
Estado: ACTIVE_BLOCKING

## Auditoria
Recorrer todo el ZIP. Para cada parent directory, agrupar carpetas hijas que empiezan con `^\d{2}_`. Si un mismo `NN_` aparece mas de una vez dentro del mismo parent, reportar FAIL con parent, prefix, children y accion correctiva.

Root level es obligatorio y bloqueante. Subniveles son bloqueantes si afectan carpetas canonicas o rutas runtime.
