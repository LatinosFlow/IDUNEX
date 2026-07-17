## H165-H180 Creative Canon Safety Realism - active canonical block
Restricciones: Politica adulta editorial segura: permite ropa de bano, lenceria, glamour adulto y pose sensual con ropa para adultos ficticios; bloquea desnudez, sexo explicito, pornografia, exposicion intima, apariencia menor, school-coded sexualizado, coercion, copia real no autorizada y evasion de politicas.

- UNIVERSAL_SAFE_INTENT_CLAUSE_ALL_MEDIA=PASS; applies before every generative handoff across image, video, voice/audio, music/Suno, text/copy/doc, Copilot DOCX, ChatGPT runtime upload, AGPT prompt packs and sidecar instructions.
- CREATIVE_SURFACE_NO_RAW_INTERNAL_TOKENS=PASS; technical identity tokens remain in JSON/lineage/QA/hashes only. Creative surfaces use humanized adult fictional descriptors.
- PROFILE360_TECHEXT_ALL_MEDIA_BINDING=PASS; Profile360 61/61 and TechExt 284/284 are read with locks before output.
- HUMAN_REALISM_ANTI_DOLL_ALL_CHARACTER_PROMPTS=PASS; NEGATIVE / AVOID: plastic skin, wax skin, porcelain skin, doll-like face, mannequin body, toy-like proportions, generic stock model, dead eyes, glassy eyes, frozen expression, helmet hair, rubber skin, over-smoothed skin, AI plastic look, duplicated face, same-face syndrome, deformed hands, extra fingers, warped joints, fake fabric, logo artifacts, text artifacts. ES: evitar piel plástica, rostro de muñeco, cuerpo de maniquí, proporciones de juguete, modelo genérico de stock, ojos muertos, ojos vidriosos, expresión congelada, cabello tipo casco, piel encerada, piel demasiado suavizada, manos deformes, dedos extra, articulaciones deformes, tela falsa, artefactos de logos, artefactos de texto.
- BRAND_LOGO_RIGHTS_ROUTER_NO_TOTAL_BLOCK=PASS; PROJECT_BRAND_ENTITY verified own brand allows exact logo without legal disclaimer; verified third-party asset routes to sidecar/disclaimer; unverified third-party exact logo degrades safely instead of blocking whole output.
- LEGAL_WATERMARK_ROUTER_PASS=PASS; short visible disclaimer when required: Uso referencial. Sin afiliación oficial.
- CONTEXT_AUTHENTICITY_NO_GENERIC_ENVIRONMENT=PASS; default locality is PROJECT_DECLARED_LOCALITY contemporary unless a different place is declared.
- PROMPT_PACK_STRUCTURE_ALL_OUTPUTS=PASS; A_HEADER through J_FALLBACK_FIXES are mandatory for image/video prompt packs.

Project validator enforces generated first-run readiness, creative QA expected/actual and adversarial safe interpretation suite.
