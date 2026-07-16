# HASH_REGENERATION_POLICY — ACTIVE CURRENT ONLY

- Semantic version: `v1.0.0`
- Active label: `P034_PROJECT_ENTITY_BRAND_LOGO_IMAGE_DELIVERY_SAFE_APPAREL_CANONICAL_REOPEN`
- Mode: `DIRECT_CANONICAL_NO_PATCH`
- Authority: `ACTIVE_CURRENT_ONLY`

Policy:
1. Recompute active SHA ledgers after any canonical edit.
2. Exclude dynamic manifest carriers listed in the dynamic exclusion manifest.
3. Keep historical payloads only under `12_HISTORICAL_NON_AUTHORITY/`.
4. Do not cite removed historical paths from active release reports.
5. Block delivery when an active proof or report references a path absent from the reopened ZIP.

Result: `PASS`
