# ZERO_ACTIVE_TRACE_AFTER_REMOVAL_CHECKLIST

## Checklist PASS/FAIL

| Control | Esperado |
|---|---|
| CHANGE_ID registrado | Existe registro completo |
| Archivos activos | Sin referencias activas al cambio removido |
| Templates exportables | Sin exportar capacidad retirada |
| Validators | Sin validator activo apuntando a archivo removido |
| Sidecars | Sin campo activo removido |
| Source mappings | Sin mapping activo inconsistente |
| Docs | Solo referencia histórica si corresponde |
| Manifests | Regenerados |
| SHA/certificado | Reemitidos si ZIP cambió |
| Retest | PASS completo |

## Comando conceptual

Buscar `CHANGE_ID`, nombres de campos, validators, fail codes, sidecar fields y rutas tocadas. Toda coincidencia activa debe quedar justificada o eliminada.
