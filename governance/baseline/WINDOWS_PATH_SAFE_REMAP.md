# IDUNEX Windows/GitHub Desktop Path-Safe Remap

**Estado:** EN_REVISION  
**Propósito:** evitar el error `Filename too long` en Windows/GitHub Desktop durante la primera carga del repositorio.

## Decisión técnica

Este paquete conserva el contenido del baseline, pero acorta rutas excesivamente largas, principalmente dentro de evidencia histórica o superficies de validación no autoritativa.

No declara release oficial ni PASS funcional. La auditoría máxima M02/M03 sigue pendiente.

## Control

- Objetivo de longitud relativa máxima: `125` caracteres.
- Rutas remapeadas: `487`.
- Manifiesto de equivalencia: `governance/baseline/WINDOWS_PATH_SAFE_REMAP.json`.

## Regla operativa

Este paquete debe usarse solo como carga inicial del repositorio GitHub en Windows. Si una auditoría posterior requiere comparar contra el ZIP original, se debe usar `IDUNEX_MOTOR_v1.0.0.zip` y su `.sha256` como evidencia externa.
