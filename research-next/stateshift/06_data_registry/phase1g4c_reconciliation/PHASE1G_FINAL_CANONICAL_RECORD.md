# PHASE 1G FINAL CANONICAL ACTIVE RECORD

**Milestone**: Phase 1G.4c Final Artifact Reconciliation & Prospective Human Gate  
**Timestamp (UTC)**: `2026-08-17 11:27 UTC`  

---

## 1. Authoritative Dataset & Registry Metadata

- **Primary Decontaminated Benchmark Pool**: **`N = 471`**
- **Active Confirmatory Registry Version**: `Registry V4` (`FINAL_PROSPECTIVE_STATE_REGISTRY_V4.json`)
- **Active Confirmatory Registry Size**: **`N = 468`** (`99.4%` yield)
- **Strict Sensitivity Registry Size**: **`N = 398`** (excluding `POSSIBLE_RELATED` items)
- **Authoritative Exclusion Set ($N=3$)**: `['math500_004', 'math500_273', 'math500_362']`
- **Primary Registry V4 SHA-256**: `8f2f81e31505898cf18fb81fd96914b4a1b9bea7665d649cee25a463a7961863`
- **Strict Sensitivity V4 SHA-256**: `ff57926a32b84a4e975d4d38977333662ae5b6c39b04e5613ddb9b30ed4df7f8`

---

## 2. Admissible Operator Set & Automated Invalidity Classification

- **Admissible Operator Set**: `OP_CONSTANT_PERTURB`, `OP_SIGN_FLIP`, `OP_FRACTION_FLIP` (`OP_TERM_SWAP` removed).
- **Automated Invalidity Breakdown ($N=468$)**:
  - **`SEMANTICALLY_EVALUATED_INVALID`**: **`183`** (`39.1%`) — numeric constant parameter offsets and numeric fraction ratio inversions evaluated false under context.
  - **`OPERATOR_NON_EQUIVALENT`**: **`191`** (`40.8%`) — sign flips and symbolic fraction flips provably changing expression values.
  - **`HUMAN_REVIEW_REQUIRED`**: **`94`** (`20.1%`) — complex symbolic expressions requiring human verification.

---

## 3. Human Semantic Audit Gate Status

- **Status**: **`MANUAL AUDIT PENDING`**
- **Blank Sample Sheet**: `MANUAL_SEMANTIC_AUDIT_SAMPLE.csv` ($N=60$ prospectively sampled pair IDs, Seed `20260817`, judgment columns left BLANK for true human review).
- **Prespecified Prospective Gate Criteria**:
  - Zero `MALFORMED` rows
  - $\ge 95\%$ `recovery_wrong`
  - $\ge 95\%$ `difference_local`
  - $\ge 95\%$ `structurally_recoverable`
- **Mandatory Directive**: **Scientific execution of Phase 1H is strictly prohibited until the human semantic audit gate passes.**

---

## 4. Locked Study Design & Estimand Architecture

- **Primary Estimand**: $\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$
- **Primary Endpoint**: Scalar $\Gamma_T$ at $T=256$
- **Checkpoint Trajectory**: $t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$ (`Qwen/Qwen2.5-7B` and `UWNSL/Qwen2.5-7B-deepscaler_4k_step_*`)
- **Rollout Allocation**: $K = 16$ stochastic rollouts per state per checkpoint
- **Resampling Procedure**: $B = 10,000$ problem-blocked bootstrap replicates
- **Primary Statistical Unit**: Problem/Pair $i$ ($N=468$)

---
