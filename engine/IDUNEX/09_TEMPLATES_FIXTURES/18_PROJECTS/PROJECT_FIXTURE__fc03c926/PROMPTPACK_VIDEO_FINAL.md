# PROMPTPACK VIDEO FINAL — PROJECT_FIXTURE_VALIDATION_001

## HEADER
[MODEL] modelo humano digital IDUNEX de validación productiva. LOCKS: JSON_LOCK / ANCHOR_LOCK / AGE_LOCK / ID_LOCK. [OUTPUT] 6-8 seconds, realistic video, no text/logos.

## SHOT PLAN
Frame start: neutral pose. Frame mid: slight head turn and controlled hand gesture. Frame end: return to neutral expression. No identity morph.

## FRAME START / MID / END
Compare face, age, body, hands, wardrobe and lighting across start, mid and end. Require stable field trace.

## CAMERA PATH
Slow locked dolly or static tripod. No orbit that hides face or causes morphing.

## MOTION
Controlled breathing, blink rate, gesture timing, walking_weight_shift only if full body is used.

## MORPH BLOCKERS
face_morph_blocker, body_morph_blocker, hand_morph_blocker, wardrobe_continuity_lock, lighting_continuity_lock.

## NEGATIVE / AVOID
morphing, face swap, body swap, changing wardrobe, flickering light, extra fingers, melted hands, background mutation, text/logo artifacts.

## QC CHECKLIST
Frame start/mid/end identity, adult age signal, hands, wardrobe, light, background and sidecar trace.

## EXPECTED OUTPUT
One high-fidelity video fixture or formal mock with frame comparison evidence.

## FALLBACK FIXES
If morphing appears, shorten shot, reduce camera motion, use frontal/3-4 angle, lock light and wardrobe.

## REQUIRED FIELD IDS
P360_VIDEO_0027, P360_VIDEO_0086, P360_VIDEO_0152, P360_ACTING_0068

## REQUIRED ADAPTER
video_prompt_adapter

## GOLDEN TEST
GT_VIDEO_FRAME_START_MID_END_LOCK
