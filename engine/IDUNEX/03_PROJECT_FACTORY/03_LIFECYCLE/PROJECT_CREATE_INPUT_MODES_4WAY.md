# PROJECT_CREATE_INPUT_MODES_4WAY

## Regla central

Project Factory acepta cuatro modos de creación. Ninguno puede dejar campos requeridos en blanco. Todo dato completado por fábrica se marca `FACTORY_DEFINED_PROPOSED`; todo dato exacto aprobado por usuario se marca `USER_APPROVED_LOCKED`.

## Modos

| Modo | Ejemplo | Tratamiento |
|---|---|---|
| PROJECT_CREATE_MINIMAL | Crear 2 hombres y 2 mujeres para proyecto X | La fábrica propone todo, sin blanks, con FACTORY_DEFINED_PROPOSED |
| PROJECT_CREATE_SEMI_SPECIFIED | Crear una mujer project-declared de 29 años, ejecutiva | Respeta lo dado y completa brechas como FACTORY_DEFINED_PROPOSED |
| PROJECT_CREATE_FULL_SPECIFIED | JSON/perfiles completos | Datos del usuario pasan a USER_APPROVED_LOCKED |
| PROJECT_CREATE_FROM_REFERENCE_SET | anchors, presets, fotos, JSON_LOCK, identidad bloqueada | No modificar identidad, edad, rasgos, cabello, accesorios ni locks |

## Amarre Profile360/TechExt

Cada modo debe producir Profile360 FULL60 y TechExt FULL10 completos por modelo. Si un campo requerido no puede inferirse responsablemente, usar `MISSING_REQUIRED_TECH_FIELD` y bloquear cierre/output hasta corrección.
