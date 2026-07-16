# PROMPTPACK_IMAGE_TEST — IDUNEX smoke fixture

## HEADER
[MODEL] MODEL_TEMPLATE_SMOKE. [OUTPUT] image, 1536x1024, horizontal, photorealistic, NO TEXT unless sidecar requires metadata outside image.

## LOCKS
JSON_LOCK:ON. ANCHOR_LOCK:ON. AGE_LOCK:ON. ID_LOCK:ON. No face drift, no age drift, no body drift, no source-less inference.

## ACTIVE IDENTITY
Use only `PROFILE360_SAMPLE_MINIMAL.json` fields listed for identity, face, body, skin, hair, wardrobe, camera, sidecar and QA. The model is synthetic adult and non-real-person.

## SCENE
Neutral controlled studio smoke-test environment with plain background, soft floor contact, visible face, hands and upper body.

## COMPOSITION
Medium portrait, camera at eye height, 70mm lens equivalent, frontal view, face centered, shoulders visible, both hands relaxed in frame. Rule of thirds plus forensic landmark visibility.

## CAMERA / TECH
camera_distance=1.6m; camera_height=eye_level; lens_mm=70; aperture=f/5.6; shutter=1/125; ISO=200; WB=5300K; sensor_type=full_frame; focal_plane=eyes; depth_of_field=moderate.

## LIGHTING
Key 45° softbox, low fill, subtle rim, catchlights visible, no plastic skin, no over-smoothing.

## FACE / BODY / SKIN / HAIR / WARDROBE
Preserve declared face shape, eye spacing, nose bridge, mouth width, jaw, adult age signal, body proportions, skin undertone, hairline and textile physics.

## NEGATIVE / AVOID
same face, same body, wrong age, age drift, identity drift, beauty drift, ethnicity drift, wrong undertone, plastic skin, extra fingers, deformed hands, text artifacts, logo artifacts, brand logos, watermark unless sidecar external.

## PARAMS
seed=PROJECT_SMOKE_SEED_001; cfg_range=6-8; variation<=1%; retest_required=true.

## QC CHECKLIST
PASS requires face, age, body, hands, skin, hair, wardrobe and sidecar fields to match `PROFILE360_SAMPLE_MINIMAL.json`. FAIL triggers `FAIL_IMAGE_SMOKE_IDENTITY_LOCK` and retest.

## EXPECTED OUTPUT
A stable adult synthetic portrait with traceable sidecar and reproducible input/output hashes.

## MOCK/REAL OUTPUT EVIDENCE
See `SMOKE_OUTPUT_MOCK_RESULT.json`, `SIDECAR_OUTPUT_EXAMPLE.json`, `QA_RESULT.json` and `HASH_EVIDENCE.json`.
