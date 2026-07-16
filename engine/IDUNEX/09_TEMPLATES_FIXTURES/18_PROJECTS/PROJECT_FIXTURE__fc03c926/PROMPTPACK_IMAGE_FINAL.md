# PROMPTPACK IMAGE FINAL — PROJECT_FIXTURE_VALIDATION_001

## HEADER
[MODEL] modelo humano digital IDUNEX de validación productiva. LOCKS: JSON_LOCK / ANCHOR_LOCK / AGE_LOCK / ID_LOCK. [OUTPUT] 1536x1024, editorial realistic, NO TEXT, NO LOGOS.

## ACTIVE IDENTITY
Use only the attached Profile360 fields. Do not invent name, age, face, ethnicity, wardrobe or biography. Require field trace and sidecar trace.

## SCENE
Controlled studio validation portrait, neutral background, PROJECT_DECLARED_LOCALITY neutral editorial context, no brand marks.

## COMPOSITION
Medium close portrait and 3/4 face check. Camera at eye height, 85mm equivalent, stable framing, face visible, hands optional but if visible must be anatomically valid.

## CAMERA / TECH
Full-frame look, 85mm, f/4, 1/160, ISO 200, WB 5300K, RAW-to-neutral grade, realistic pores and hairline.

## LIGHTING
Soft key 45 degrees, weak fill, rim light controlled, stable catchlights, no beauty-filter skin.

## FACE / SKIN / HAIR / WARDROBE CONTINUITY
Validate face_shape, undertone, hairline, wardrobe physics and adult age signals against Profile360 field IDs.

## NEGATIVE / AVOID
identity drift, same face, generic influencer face, wrong age, ethnicity drift, wrong skin undertone, wax skin, extra fingers, text artifacts, logos, watermark unless sidecar requires.

## PARAMS
cfg recommended 5-8, seed fixed by project, stylize low/medium, variation <= 1% for identity-critical markers.

## QC CHECKLIST
Identity PASS, age PASS, face landmarks PASS, skin/hair PASS, wardrobe PASS, source trace PASS, sidecar hash PASS.

## EXPECTED OUTPUT
One high-fidelity validation image or mock artifact traceable to field_ids and source_ids.

## MOCK/REAL OUTPUT EVIDENCE
Non-production high-fidelity mock record stored in HASH_EVIDENCE_REAL.json; real vendor artifact required before PROJECT_GO.

## FALLBACK FIXES
If face drifts, reinforce face landmarks and same-face negative. If skin plastic, lower smoothing and increase pore texture. If wardrobe physics fails, add fabric weight and tension points.

## REQUIRED FIELD IDS
P360_FACE_0058, P360_SKIN_0163, P360_HAIR_0178, P360_WARDROBE_0302

## REQUIRED ADAPTER
image_prompt_adapter

## GOLDEN TEST
GT_IMAGE_FRONT_IDENTITY_LOCK
