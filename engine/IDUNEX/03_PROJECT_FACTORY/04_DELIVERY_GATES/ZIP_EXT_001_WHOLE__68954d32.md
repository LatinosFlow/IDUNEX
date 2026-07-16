# ZIP-EXT-001 - Whole ZIP external authority

Origen histórico: `H382R_EXTERNAL_WHOLE_ZIP_AUTHORITY`.

Estado: integrado al canon estable activo.

Regla: el SHA256 integral y los bytes absolutos del ZIP final solo tienen autoridad fuera del ZIP: `.zip.sha256`, certificado externo y companion externo. Ningún archivo interno autocertifica el SHA integral del ZIP que lo contiene.
