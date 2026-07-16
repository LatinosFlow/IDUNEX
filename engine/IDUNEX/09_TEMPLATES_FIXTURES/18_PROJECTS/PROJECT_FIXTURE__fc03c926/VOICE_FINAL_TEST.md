# VOICE FINAL TEST — PROJECT_FIXTURE_VALIDATION_001

## VOICE PROFILE
Adult synthetic voice only. No celebrity imitation. Voice must match age signal, culture boundary and Profile360 personality fields.

## SAMPLE SCRIPT
"Esta es una prueba técnica IDUNEX. Confirmo identidad sintética adulta, acento estable, prosodia natural y trazabilidad de fuente."

## PARAMETERS
voice_age_signal: adult. timbre_signature: stable. pitch_range: declared. resonance_place: controlled. breath_pattern: natural. speaking_rate: medium. prosody_curve: non-flat. accent_region: Latam/PROJECT_DECLARED_COUNTRY neutral only if project declares it. sociolect_level: non-caricature.

## EMOTION VARIANTS
neutral, calm confidence, light concern; no childlike voice, no overacting, no accent drift.

## QA CHECKLIST
adult vocal age, timbre lock, pitch lock, accent lock, breathing realism, speaker drift blocker, sidecar source trace.

## EXPECTED OUTPUT
Audio artifact or formal technical mock with hash_input/hash_output recorded.

## FALLBACK FIXES
If childlike tone appears, raise adult vocal age and lower brightness. If accent drifts, lock accent_region and phoneme stress. If robotic, add breath marks and micro-pauses.

## REQUIRED FIELD IDS
P360_VOICE_0007, P360_VOICE_0211, P360_VOICE_0216, P360_VOICE_0223

## REQUIRED ADAPTER
elevenlabs_voice_adapter

## GOLDEN TEST
GT_VOICE_TIMBRE_LOCK
## RETEST PROTOCOL
If vocal age, timbre, accent or prosody fails, rerun with reduced emotional range, explicit adult voice_age_signal, locked accent_region, and phoneme stress notes. Record before/after hashes and keep prior_scope_reference=NON_AUTHORITY_REFERENCE; active_scope=H261_H268_RUNTIME_TRUTHFULNESS_SCOPE; global_creative_output_certification=FALSE_UNTIL_ASSET_EVIDENCE.

## PRODUCTION REJECTION CONDITIONS
Reject if voice sounds minor, celebrity-like, robotic, inconsistent with Profile360, or if sidecar/hash evidence is missing.
