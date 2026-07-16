# SUNO_TEST — IDUNEX smoke fixture

## music_identity
Synthetic character song identity; not a celebrity imitation; not generic pop.

## structure
[Intro] spoken texture, [Verse 1] identity motif, [Pre-Chorus] tension, [Chorus / Hook] concise hook, [Verse 2] controlled detail, [Bridge] emotional turn, [Final Hook], [Outro].

## parameters
genre_primary=alt latin cinematic pop; genre_secondary=spoken rhythmic; BPM=88-96; key_mood=minor-warm; vocal_mode=adult; spoken_vs_sung_ratio=60/40; hook_style=minimal; verse_density=medium; instrument_palette=soft percussion, bass pulse, atmospheric guitar/synth.

## lyrics_sample
“Respiro lento, vuelvo al centro, mi voz no cambia de lugar.”

## negative music tags
no generic pop, no childish voice, no wrong accent, no over-autotune unless requested, no celebrity imitation, no random English, no unrelated biography.

## QA checklist
GT_SUNO_LYRIC_PERSONALITY validates genre, BPM, voice age, lyric personality and negative tags.

## fallback fixes
If generic: reinforce BPM, palette, emotional arc and lyric personality. If accent wrong: lock language_variant and accent_policy.

## expected output / evidence
Formal mock evidence only; real Suno output required before PROJECT_GO.
