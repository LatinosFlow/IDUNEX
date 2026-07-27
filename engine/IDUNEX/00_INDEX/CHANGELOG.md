# IDUNEX Motor v1.0.0 - Changelog

AUTHORITY_STATUS=REFERENCIA_HISTORICA_SUSTITUIDA
STATE_AUTHORITY=governance/CURRENT_STATE.json
BUILD_STATE_SNAPSHOT_AUTHORITY=FALSE
BUILD_STATE_SNAPSHOT_CLASSIFICATION=NON_AUTHORITY_BUILD_SNAPSHOT
BUILD_MOTOR_STATUS_SNAPSHOT=EN_REVISION
BUILD_M02_SNAPSHOT=NOT_RECOMPUTED_POST_AUD037
BUILD_M03_SNAPSHOT=NOT_RECOMPUTED_POST_AUD037
CURRENT_STATE_EQUALITY_REQUIRED=FALSE

SEMANTIC_VERSION=v1.0.0
VERSION_BUMP=NO
CORRECTION_MODE=DIRECT_CANONICAL_NO_PATCH
CORRECTION_SCOPE=AUD-037_GOVERNANCE_IDENTITY_CYCLE_BREAK
PREVIOUS_SCOPE_COMPATIBILITY=MUTATION_SELF_TEST_H62_MATRIX_PROOF_PARITY_AND_ACTIVE_LEDGER_EXCLUSION_CLARITY
LEGACY_SCOPE_COMPATIBILITY=DUPLICATE_GOVERNANCE_AND_ACTIVE_VALIDATOR_PARITY
CREATIVE_OUTPUT_CERTIFIED=FALSE

## 2026-07-27 - AUD-037 governance/identity cycle break
- `governance/CURRENT_STATE.json` remains the sole mutable authority.
- Internal state fields are classified as `NON_AUTHORITY_BUILD_SNAPSHOT` and never require exact equality with later M02/M03 transitions.
- The existing runtime validator enforces exact result tokens, M02-before-M03, same-tree evidence binding, AUD-028 consumption and all EN_REVISION interlocks.
- The validated M02 evidence for tree `c5cb2f4b...` is retained as superseded scoped evidence and is not reassigned to the new tree.

## 2026-07-26 - AUD-035 internal governance surface synchronization
- CURRENT_STATE is authoritative: M02 and M03 are `NOT_RECOMPUTED_POST_AUD035`, classified `EN_REVISION_M02_M03_NOT_RECOMPUTED_POST_AUD035`.
- Demo, release, tag, OFICIAL, agent loading, productive closure and creative certification remain blocked.
- The six non-self-referential internal manifests were regenerated from the canonical scanner.

## 2026-07-22 - AUD-030 external documentary emission post-H410
- The authoritative Project Factory reads the internal report, certificate, operator README and both content-tree proofs directly from the final reopened ZIP.
- `refresh-external-artifacts` refreshes only the three external documentary surfaces and fails if ZIP or companion SHA/size changes.
- AUD-028 remains consumed; no Demo generation or validation authorization was created.
- M02 and M03 are `NOT_RECOMPUTED_POST_AUD030` for the changed engine tree.
- Release, tag, OFICIAL, productive closure, agent loading and creative certification remain blocked.

## 2026-07-08 - Active surface scope drift and duplicate retention allowlist stale-pass closure
- B01_ACTIVE_SURFACE_SCOPE_DRIFT corrected: active control surfaces no longer declare the legacy duplicate-governance correction scope as vigente PASS scope.
- B02_ACTIVE_DUPLICATE_RETENTION_ALLOWLIST_STALE_PASS corrected: retention allowlist was demoted to compatibility alias non-authority and synchronized to active duplicate recomputation.
- B03_VALIDATOR_COVERAGE_GAP_SCOPE_AND_RETENTION_LEDGER corrected inside existing validators; no parallel validator was added.
- H62 proof remains previous compatible authority: mutation-self-test 506/506 and N1..N10 x low/intermediate/full matrix 31/31 preserved.
- Duplicate governance and active validator parity remains legacy compatibility metadata only, not current correction scope.

HISTORICAL_MAX_MATRIX_CURRENT_RUN=PASS
HISTORICAL_N1_TO_N10_X3_MATRIX=PASS
HISTORICAL_VALIDATORS_FAIL=0
HISTORICAL_BLOCKING_WARNINGS=0
HISTORICAL_FAIL_CODES=[]
HISTORICAL_DECLARED_SCORE=10/10
HISTORICAL_OUTPUT_EXTERNAL_EXACT_7_OF_7=PASS
CLOSURE_DECISION=BLOCKED_BY_EN_REVISION
HISTORICAL_MATRIX_CURRENT_RUN_RECOMPUTED_31_31=PASS
HISTORICAL_MUTATION_SELF_TEST=PASS_506_OF_506_RECOMPUTED
CREATIVE_OUTPUT_CERTIFIED=FALSE
PROJECT_DEMO_NEXT_PHASE_REQUIRED=FALSE

## 2026-07-08 - H62 matrix proof parity and active ledger exclusion clarity
- Scope preserved as PREVIOUS_SCOPE_COMPATIBILITY.
- B01 PASS: active H62 proof restored from H238 v1.0.0, 31/31 matrix proof.
- B02 PASS: duplicate ledger self-exception/dedup clarity applied.
- CREATIVE_OUTPUT_CERTIFIED remains FALSE.

## 2026-07-08 - CLI lifecycle and matrix version lineage parity
- Scope preserved as historical previous compatibility to H62.
- B01 PASS: H269-H280 aggregate validator runs child validators with explicit timeout, process-group kill-tree, bounded stdout/stderr capture and real rc observation.
- B02 PASS: active matrix runner derives project IDs from SEMANTIC_VERSION v1.0.0; current 31/31 matrix PASS emits v1.0.0 project IDs.
- CREATIVE_OUTPUT_CERTIFIED remains FALSE.
- 2026-07-22 — AUD-033: H113 repository current-tree identity resolution decoupled from M02 approval; identity remains non-release and governance interlocks remain authoritative.
