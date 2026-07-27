# HASH_REGENERATION_POLICY — AUD-003 CURRENT PHYSICAL TREE

- Semantic version: `v1.0.0`
- Current manifest: `governance/baseline/IDUNEX_CURRENT_TREE_MANIFEST.json`
- Current aggregate: `governance/baseline/IDUNEX_CURRENT_TREE_SHA256.txt`
- Mode: `DIRECT_CANONICAL_NO_PATCH`
- Authority: `CURRENT_REPOSITORY_TREE_NOT_RELEASE`

Policy:
1. Recompute active SHA ledgers after any canonical edit.
2. Exclude dynamic manifest carriers listed in the dynamic exclusion manifest.
3. Keep historical payloads only under `14_HISTORICAL_NON_AUTHORITY/` or `governance/baseline/historical_received/`.
4. Resolve Windows-safe paths and AUD-008 movements before comparing the received ledger.
5. Require zero missing indexed paths, zero unmanifested physical files and zero hash mismatches.
6. Record `STATE_AUTHORITY=governance/CURRENT_STATE.json`, `BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE` and `BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT`; manifest regeneration is never a state transition or release decision.

Verification entrypoint: `python tools/audit/baseline_scanner.py --repo-root .`
