# PROMPTPACK_VIDEO_TEST — IDUNEX smoke fixture

## HEADER
[MODEL] MODEL_TEMPLATE_SMOKE. [OUTPUT] 5 second video smoke test, 16:9, no text/logo overlays.

## LOCKS
JSON_LOCK:ON. ANCHOR_LOCK:ON. AGE_LOCK:ON. ID_LOCK:ON. Frame continuity lock active.

## SCENE
Controlled studio, same wardrobe and lighting as image test.

## SHOT PLAN
Frame start: frontal medium shot. Frame mid: small head turn and natural blink. Frame end: return to neutral pose. No camera rotation greater than 8°.

## FRAME START / MID / END
Validate face_shape, eye spacing, nose bridge, jaw, body proportions, wardrobe, skin tone, hairline and adult age signal at start/mid/end.

## CAMERA PATH
Locked tripod with micro push-in only. No sudden background shifts.

## MOTION
motion_cadence=slow; gesture_timing=controlled; breathing_visibility=subtle; blink_rate=natural adult range.

## MORPH BLOCKERS
face_morph_blocker, body_morph_blocker, hand_morph_blocker, wardrobe_continuity_lock, lighting_continuity_lock.

## NEGATIVE / AVOID
face morphing, body morphing, hand deformation, wardrobe mutation, lighting jump, background drift, wrong age, text artifacts.

## QC CHECKLIST
Compare start/mid/end. PASS only if identity and wardrobe are stable and sidecar includes video adapter evidence.

## FALLBACK FIXES
If morphing appears: shorten shot, reduce camera motion, strengthen face/body locks, use fixed light and stable wardrobe.

## EXPECTED OUTPUT / MOCK EVIDENCE
Formal mock evidence recorded in `SMOKE_OUTPUT_MOCK_RESULT.json` and `GOLDEN_TEST_RESULTS.md`.
