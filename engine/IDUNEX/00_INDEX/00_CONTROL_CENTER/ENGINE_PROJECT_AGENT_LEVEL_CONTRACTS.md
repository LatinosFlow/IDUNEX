# ENGINE / PROJECT / AGENT LEVEL CONTRACTS

`GOV-LVL-001`: ENGINE_LEVEL != PROJECT_LEVEL != AGENT_LEVEL.

- El motor gobierna.
- El proyecto materializa.
- El agente ejecuta.

Bloqueos activos: Proyecto Demo como fixture activo, LatinosFlow como default, paletas/logos/clientes/modelos demo como defaults, y agentes leyendo el motor completo en lugar del runtime 10+N de proyecto.


## BRD-PAL-001 - Paleta de marca sin leakage activo

Las superficies genéricas del ENGINE_LEVEL deben usar únicamente tokens `PROJECT_BRAND_PRIMARY_COLOR`, `PROJECT_BRAND_SECONDARY_COLOR`, `PROJECT_BRAND_ACCENT_COLOR`, `PROJECT_BRAND_TEXT_COLOR`, `PROJECT_BRAND_BACKGROUND_COLOR` y `PROJECT_BRAND_CONTRAST_PAIR_AA`. Los valores reales se resuelven solo en PROJECT_LEVEL mediante `PROJECT_BRAND_REGISTRY` autorizado o input externo explícito. Queda bloqueada la materialización de paletas reales bajo `PROJECT_BRAND_ENTITY` como default activo.
