# VOICE_TEST — IDUNEX smoke fixture

## voice_profile
Synthetic adult voice, non-celebrity, non-minor, matched to Profile360 adult identity.

## sample_script
“Este es un control de voz IDUNEX. Mantengo edad vocal adulta, timbre estable, acento controlado y respiración natural.”

## parameters
voice_age_signal=adult; timbre_signature=declared; pitch_range=medium; resonance_place=chest/head balanced; breath_pattern=natural; speaking_rate=controlled; prosody_curve=soft assertive; accent_region=neutral LatAm/PROJECT_DECLARED_COUNTRY-safe; sociolect_level=project_declared.

## emotion variants
neutral, calm confidence, mild concern. No childish tone, no celebrity imitation, no accent caricature.

## QA checklist
GT_VOICE_TIMBRE_LOCK validates age, timbre, pitch, breath, prosody, accent and speaker drift.

## fallback fixes
If accent drift: lock accent_region and reduce expressive range. If childish tone: reinforce adult vocal age and lower pitch instability. If robotic: increase breath marks and pause pattern.

## expected output
Stable adult spoken voice fixture with sidecar and hash evidence.

## mock/real output evidence
Recorded as formal mock in `SMOKE_OUTPUT_MOCK_RESULT.json`; real vendor output required before PROJECT_GO.
