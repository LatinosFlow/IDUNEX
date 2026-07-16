## Resumen

Describe el cambio y el hallazgo/issue relacionado.

## Tipo de cambio

- [ ] Corrección de defecto
- [ ] Prueba/regresión
- [ ] Documentación
- [ ] Gobernanza
- [ ] Release tooling

## Issue relacionado

Closes #

## Criterios de aceptación

- [ ] No crea factory paralelo.
- [ ] No crea validator paralelo.
- [ ] No introduce bloat, staging, temp, logs largos ni ZIPs intermedios.
- [ ] No introduce defaults de marca/proyecto/modelo.
- [ ] Mantiene ENGINE_LEVEL / PROJECT_LEVEL / AGENT_LEVEL separados.
- [ ] Incluye prueba de reproducción si corrige defecto.
- [ ] Incluye prueba de regresión.
- [ ] `python tools/audit/intake_audit.py --repo-root .` PASS.

## Evidencia

Pega logs, comandos y resultados relevantes.

## Riesgo residual

Indica riesgos, limitaciones o validaciones pendientes.
