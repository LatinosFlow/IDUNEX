# IDUNEX Engine

Repositorio técnico privado para el motor IDUNEX.

## Estado actual

**Estado:** `EN_REVISION`  
**Versión declarada de baseline:** `v1.0.0`  
**SHA256 del ZIP fuente recibido:** `bbef200d6f0d7bf116853e0d763b90dc0b6454efee831e6dee1b040c78fce0d6`

Este repositorio contiene el motor extraído en:

```text
engine/IDUNEX/
```

Los documentos externos de referencia se ubican en:

```text
governance/authority/REFERENCIA/
```

## Regla de autoridad

- GitHub controla código, estructura técnica, pruebas, issues, PRs y releases.
- SharePoint/OneDrive debe conservar los artefactos documentales empresariales oficiales.
- El ZIP fuente original no debe tratarse como equivalente a un release oficial futuro si no pasa auditoría recomputada.
- No se acepta `PASS` declarado sin recomputar.

## Siguiente flujo

```text
Importar baseline → ejecutar auditoría M02 → corregir hallazgos → auditoría M03 → Proyecto 000 Demo → auditoría de Demo → carga agente → motor productivo
```

## Comandos iniciales

```bash
python tools/audit/intake_audit.py --repo-root .
python tools/package/package_engine.py --repo-root . --version v1.0.0
```

El empaquetador escribe artefactos en `dist/`, carpeta excluida de Git.

## Nota de carga Windows-safe

Este paquete usa un remapeo de rutas largas para evitar `Filename too long` en GitHub Desktop sobre Windows. Ver `governance/baseline/WINDOWS_PATH_SAFE_REMAP.md`. El estado sigue siendo `EN_REVISION`; no es release oficial.

