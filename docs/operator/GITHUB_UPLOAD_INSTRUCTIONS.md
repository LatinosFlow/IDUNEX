# Instrucciones para cargar este paquete a GitHub

Repositorio existente: `idunex`

## Opción recomendada: Git CLI

1. Descomprime este ZIP.
2. Entra a la carpeta `idunex/`.
3. Ejecuta:

```bash
git init
git branch -M main
git add .
git commit -m "chore(import): register IDUNEX v1.0.0 baseline for review"
git remote add origin https://github.com/<OWNER>/idunex.git
git push -u origin main
```

## Después de subir

1. Activa protección de rama `main`.
2. Exige Pull Request para cambios.
3. Exige GitHub Actions PASS.
4. Usa Issues para cada hallazgo.
5. No declares release oficial hasta auditoría máxima.

## Prohibido

- Subir credenciales.
- Subir ZIPs intermedios.
- Crear ramas con motores alternativos permanentes.
- Publicar Proyecto Demo antes de cierre técnico del motor.
