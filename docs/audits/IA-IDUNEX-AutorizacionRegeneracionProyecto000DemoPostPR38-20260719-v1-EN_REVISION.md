# IA-IDUNEX-AutorizacionRegeneracionProyecto000DemoPostPR38-20260719-v1-EN_REVISION

**Tipo:** Addendum documental de autorización operativa controlada  
**ID:** AUD-023  
**Fecha:** 2026-07-19  
**Versión:** v1  
**Estado del documento:** `EN_REVISION`  
**Repositorio:** `LatinosFlow/IDUNEX`  
**Rama documental:** `docs/aud-023-demo-regeneration-post-pr38`  
**Destino autorizado:** ChatGPT normal, fuera de GitHub  

---

## 1. Resumen ejecutivo

AUD-023 autoriza una nueva regeneración controlada del Proyecto 000 Demo utilizando el motor IDUNEX corregido después del merge del PR #38.

La base técnica autorizada para esta ejecución es:

- Repositorio: `LatinosFlow/IDUNEX`
- Rama: `main`
- Commit: `18be3cfc4704ecff7c0187548072de6541410313`
- PR de corrección: `#38`
- Estado del PR: `MERGED`
- Motor: `EN_REVISION`
- Versión semántica: `v1.0.0`

Esta autorización no modifica `governance/CURRENT_STATE.json` ni convierte el motor en `OFICIAL`.

---

## 2. Autoridad y antecedentes

AUD-023 complementa AUD-022 exclusivamente para actualizar la identidad del snapshot técnico autorizado.

AUD-022 autorizó la preparación y ejecución controlada del Proyecto 000 Demo fuera de GitHub, pero documentó un snapshot anterior del motor.

Después de la primera auditoría externa del Proyecto 000 Demo:

1. Se declaró `PROJECT_AUDIT_FAIL`.
2. Se identificaron 14 hallazgos bloqueantes.
3. Se corrigieron factory, contratos, validators, ledgers, superficies de agentes y finalizer.
4. La corrección fue incorporada mediante el PR #38.
5. El PR #38 fue fusionado mediante squash en:

   `main@18be3cfc4704ecff7c0187548072de6541410313`

AUD-023 no sustituye la gobernanza global ni declara cierre de la auditoría externa.

---

## 3. Input exacto autorizado

La regeneración debe utilizar exactamente:

- Archivo:

  `IDUNEX-Project000-Demo-Input-20260717-v1-EN_REVISION.json`

- SHA-256:

  `801055FEB1D2BE3E932B99C71E38FEDAC612B4D106B2959439E935C5F8AF3B34`

No se autoriza:

- reconstruir el input;
- modificar sus claves o valores;
- sustituirlo por una versión inferida;
- completar información manualmente;
- usar el input temporal reconstruido de pruebas anteriores.

El input reconstruido anterior queda clasificado como `SUSTITUIDO` para la comprobación de fidelidad exacta.

---

## 4. Alcance autorizado

Se autoriza una ejecución controlada con el siguiente alcance:

1. Descargar o preparar un snapshot exacto de:

   `main@18be3cfc4704ecff7c0187548072de6541410313`

2. Ejecutar el Project Factory con el input exacto autorizado.

3. Generar una nueva entrega del Proyecto 000 Demo.

4. Ejecutar el validator canónico sobre la entrega generada.

5. Reabrir y comprobar el ZIP definitivo.

6. Emitir los cinco artefactos externos canónicos:

   - ZIP del proyecto.
   - Archivo companion `.zip.sha256`.
   - `*_RELEASE_CERTIFICATE.txt`.
   - `*_FINAL_AUDIT_REPORT.md`.
   - `*_README_FOR_HUMAN_OPERATOR.md`.

7. Preservar evidencia de:

   - aliases y pseudónimos;
   - runtime ChatGPT;
   - runtime Copilot;
   - agent-load 10/10 por agente;
   - `MODEL_REGISTRY`;
   - `NO_DRIFT_LEDGERS`;
   - Profile360;
   - TechExt;
   - fidelity ledgers;
   - hashes;
   - resultados de generate y validate;
   - artefactos externos 5/5.

8. Preparar la entrega para una nueva auditoría externa e independiente.

---

## 5. Entorno autorizado

La regeneración operativa del Proyecto 000 Demo debe realizarse en:

```text
ChatGPT normal o entorno externo controlado de ejecución
