# ADR-0002 — Secuencia Motor → Demo → Proyectos

## Estado

EN_REVISION

## Decisión

No se crearán proyectos futuros hasta cerrar la secuencia:

```text
Motor auditado PASS → Proyecto 000 Demo generado PASS → Demo auditado PASS → Runtime cargado/probado → Motor productivo
```

## Regla

Si el Demo revela una falla de motor, se corrige el motor y se repite el ciclo. No se arrastra PASS desde una capa a otra.
