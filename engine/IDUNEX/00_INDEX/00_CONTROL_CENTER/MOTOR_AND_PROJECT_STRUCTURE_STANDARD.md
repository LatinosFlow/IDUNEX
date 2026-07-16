# MOTOR_AND_PROJECT_STRUCTURE_STANDARD - P0.2-010

Engine: IDUNEX_MOTOR_v1.0.0
Fecha: NEUTRALIZED_ACTIVE_SCOPE
Estado: ACTIVE

## Motor root namespace
La raiz canonica del motor es la lista declarada en `ROOT_DIRECTORY_CANONICAL_RENUMBERING.*`. Ningun sibling scope puede duplicar prefijo `NN_`.

## Project Core
Separar knowledge, configs, manifests, outputs y evidencias. `PROJECT_CORE` contiene reglas portables; `CHATGPT` y `COPILOT` contienen runtime/adapters especificos.

## Runtime ChatGPT/Copilot
Cada agente debe usar 10 core files + 1 Profile360 completo por modelo. Maximo operativo: 20 archivos knowledge por agente.

## Proyectos con mas de 10 modelos
Dividir agentes o bloquear un unico agente por exceso de knowledge files. Nunca resumir Profile360 FULL60 para entrar al limite de 20.
