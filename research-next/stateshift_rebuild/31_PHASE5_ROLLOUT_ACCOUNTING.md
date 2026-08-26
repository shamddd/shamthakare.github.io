# PHASE 5 ROLLOUT ARITHMETIC RECONCILIATION

**Project**: StateShift Scientific Rebuild — Phase 5X  
**Author**: Sham Satish Thakare  

---

## 1. Absolute Rollout Identity & Counting Verification

We reconcile the exact mathematical rollout counts across all raw empirical storage artifacts in the repository:

### A. Empirical Endpoint Rollouts (`artifacts/endpoint/controlled_endpoint_outcomes.csv`)
* **Problems ($N$)**: 454 decontaminated `MATH-500` problems.
* **Rollout Depth ($K$)**: $K=16$ per cell.
* **Empirical Arms**: 2 Arms (`control` and `recovery`).
* **Empirical Checkpoints**: 2 Checkpoints ($t=0$ and $t=256$).
* **Row Count Calculation**: $454 \times 16 \times 2 \times 2 = \mathbf{29,056\ rows}$.

### B. Empirical Trajectory Rollouts (`artifacts/trajectory/intermediate_rollouts.jsonl`)
* **Problems ($N$)**: 454 problems.
* **Rollout Depth ($K$)**: $K=2$ per cell.
* **Empirical Arms**: 2 Arms (`control` and `recovery`).
* **Empirical Checkpoints**: 4 Checkpoints ($t=32, 96, 160, 224$).
* **Row Count Calculation**: $454 \times 2 \times 2 \times 4 = \mathbf{7,264\ rows}$.

### C. Empirical Natural Recovery Rollouts (`artifacts/natural_recovery/natural_error_episodes.csv`)
* **Problems ($N$)**: 200 problems.
* **Rollout Depth ($K$)**: $K=16$ unprompted rollouts at $t=256$.
* **Row Count Calculation**: $200 \times 16 = \mathbf{3,200\ rows}$.

$$\mathbf{Total\ Empirical\ Model\ Rollouts\ in\ Repository:\ 29,056 + 7,264 + 3,200 = 39,520\ rollouts}$$

---

## 2. Retraction & Reclassification of Non-Empirical Arms

The Phase 5 report previously mentioned "43,584 total rollouts" for a 6-arm design ($454 \times 16 \times 6 = 43,584$).

### Formal Retraction Statement:
We explicitly **RETRACT** the claim that Arms S (Shuffled Reasoning), I (Irrelevant Prose), A (Alternate Math Error), and D (Direct Decoding) were generated as raw model rollouts from LLM inference runs.

* **Arm R (Recovery)**: **`RAW EMPIRICAL`** ($14,528$ endpoint rows).
* **Arm C (Matched Control)**: **`RAW EMPIRICAL`** ($14,528$ endpoint rows).
* **Arm S, I, A, D**: **`DERIVED / SIMULATED`** (Constructed analytically for prospective estimator null simulation).

*Signed by Scientific Integrity Auditor & Lead Statistician*
