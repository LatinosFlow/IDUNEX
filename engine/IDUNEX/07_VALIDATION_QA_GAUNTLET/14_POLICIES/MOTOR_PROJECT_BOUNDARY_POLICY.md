# MOTOR_PROJECT_BOUNDARY_POLICY

IDUNEX_MOTOR_v1.0.0 is an engine, not a project. The active motor defines architecture, policies, schemas, validators, factories, manifests, runtime layout, source lineage, Pairwise360, sidecars, golden tests and materialization rules.

The active motor must not define canonical project identities, concrete model names, concrete origins, concrete roles, concrete genders, concrete physical traits or final Profile360/TechExt values as motor authority.

Project data belongs only to generated project packages. Test data is allowed only when isolated and marked as FIXTURE_ONLY, NON_AUTHORITY, NOT_CANONICAL_PROJECT, NOT_CANONICAL_MODEL and NOT_FOR_RUNTIME_IDENTITY.

Factory limits: min_models=1, max_models=10, fictitious_adult_only=true, block_minors=true, block_real_people=true, block_celebrity_or_voice_imitation=true, block_alias_collisions=true.

Motor templates use schema slots or materialization contracts. Generated projects materialize actual_value with evidence, source lineage and anti-clone validation.
