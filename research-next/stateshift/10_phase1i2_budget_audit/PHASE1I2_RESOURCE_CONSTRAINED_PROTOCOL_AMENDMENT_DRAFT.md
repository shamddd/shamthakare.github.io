# PHASE 1I.2 RESOURCE-CONSTRAINED PROTOCOL AMENDMENT DRAFT

**Milestone**: Phase 1I.2 Prospective Protocol Amendment Draft  
**Draft Timestamp**: `2026-08-19 23:23 UTC`  
**Status**: **`UNACTIVATED DRAFT — WAITING FOR USER APPROVAL`**  
**Execution Count Pre-Amendment**: **`0 confirmatory rollouts executed ($0 spent)`**  

---

## 1. Amendment Rationale & Proposed Changes

* **Original Planned Design**: Full 9-Checkpoint Design ($N=454, 9 \text{ checkpoints}, K=16 \to 130,752 \text{ rollouts}$, estimated budget $\$30.70 \text{ USD}$).
* **Proposed Amended Design**: Endpoint-Only Design B ($N=454, 2 \text{ checkpoints } \{0,256\}, K=16 \to 29,056 \text{ rollouts}$, estimated budget **`$6.82 USD`**).
* **Exact Reason for Amendment**: Mathematical proof demonstrates that estimation and identification of the primary estimand $\Gamma_{256}$ depend exclusively on $t=0$ and $t=256$. Intermediate checkpoints consume $77.8\%$ of compute while contributing zero statistical precision to $\Gamma_{256}$. Moving to the endpoint design reduces compute cost from $\$30.70$ to $\$6.82$, allowing the entire primary confirmatory study to execute within the existing RunPod balance ($9.43 \text{ USD}$) without requiring additional user funding.

---

## 2. Claim Retention & Relinquishment Ledger

* **Retained Primary Claims**:
  1. Primary interaction estimand $\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$ remains 100% intact with full statistical power ($1.000$).
  2. Matched recovery vs. control contrast ($N=454$) remains 100% intact.
  3. Contamination sensitivity analysis ($N=388$) remains 100% intact.
* **Relinquished Secondary Claims**:
  1. Intermediate trajectory evolution (monotonicity / non-monotonicity across $t=32..224$) is relinquished.
  2. Trajectory inflection point timing is relinquished.

---

## 3. Financial & Resource Justification

* **Original Budget Needed**: $\$30.70 \text{ USD}$ (Deficit of $\$22.27 \text{ USD}$)
* **Amended Budget Needed**: **`$6.82 USD`** (Base compute $\$5.69$ + 20% reserve $\$1.13$)
* **Financial Solvency**: Solvent within existing $\$9.43$ RunPod account balance ($2.61 \text{ USD}$ buffer remaining).

*Signed by Principal ML Research Scientist & Reproducibility Auditor*
