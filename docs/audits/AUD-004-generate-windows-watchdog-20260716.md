# AUD-004 - Ledger de corrección del watchdog de `generate` en Windows

**Issue:** `AUD-004` / `#5`  
**Fecha:** 2026-07-16  
**Alcance:** compatibilidad multiplataforma del watchdog de `generate`  
**MOTOR_STATUS vigente:** `EN_REVISION`  
**M02_RESULT vigente:** `M02_FAIL`

## Autoridad aplicada

- Informe Maestro bajo `governance/authority/REFERENCIA/`.
- `docs/audits/IA-IDUNEX-AuditoriaMotorM02-20260716-v1-EN_REVISION.md`.
- `docs/audits/IA-IDUNEX-PlanCorreccionM02-20260716-v1-EN_REVISION.md`.
- `governance/CURRENT_STATE.json`.
- Issue `AUD-004` / `#5`.

## Causa raíz

`generate_end_to_end` evaluaba `signal.SIGALRM` en `signal.getsignal(signal.SIGALRM)` antes de entrar al bloque protegido. Windows no expone `SIGALRM`, por lo que el worker terminaba con `AttributeError` antes de iniciar el flujo controlado de generación.

## Corrección aplicada

- La capacidad del timer interno se detecta con `getattr` antes de usar `SIGALRM` o `ITIMER_REAL`.
- El timer Unix se instala y restaura únicamente si también existen `getsignal`, `signal` y `setitimer`.
- Linux conserva el handler y `ITIMER_REAL` existentes cuando la plataforma los soporta.
- En plataformas sin esas primitivas, el watchdog H205 del proceso padre continúa controlando el worker mediante polling, timeout y terminación de proceso.
- El contrato funcional, los códigos de retorno y la política de no entrega parcial no cambian.

## Prueba de regresión

`tests/intake/test_generate_windows_watchdog.py` cubre:

1. `generate_end_to_end` con un módulo `signal` simulado sin `SIGALRM` ni `ITIMER_REAL`.
2. El comando público `generate` en una plataforma nativa sin `SIGALRM`.
3. Retorno controlado mediante un input de bloqueo temprano, sin ZIP ni materialización de proyecto.
4. Ausencia de `AttributeError` por `SIGALRM`.

El input de prueba contiene un sentinel inválido y queda bloqueado antes de crear cualquier proyecto. No se genera Proyecto Demo.

## Evidencia ejecutada

Entorno: Windows, Python 3.11 del runtime de Codex.

```text
python -m py_compile engine/IDUNEX/03_PROJECT_FACTORY/02_PROTOCOLS/IDUNEX_PROJECT_FACTORY_v1.0.0.py tests/intake/test_generate_windows_watchdog.py
rc=0

python -m unittest tests/intake/test_generate_windows_watchdog.py -v
2 pruebas Windows PASS; prueba Unix preservada y omitida por capacidad ausente; rc=0

python tools/audit/governance_state_check.py --repo-root .
result=CONSISTENT; active_contradiction_count=0; MOTOR_STATUS=EN_REVISION; M02_RESULT=M02_FAIL; rc=0
```

## Fuera de alcance preservado

- No se modificó el remapeo Windows-safe.
- No se limpió bloat ni historia.
- No se consolidaron validadores.
- No se creó release ni tag.
- No se cerró ningún issue.
- No se declaró ni aceptó `M02_PASS`.
- No se modificó `governance/CURRENT_STATE.json`; permanecen `EN_REVISION` y `M02_FAIL`.

Este ledger documenta una corrección técnica acotada y no certifica el motor.
