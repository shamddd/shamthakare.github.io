# PHASE 1I PREREGISTRATION AND STATISTICAL ANALYSIS FREEZE (V2)

**Milestone**: Phase 1I.1 Statistical Analysis Freeze  
**Execution Timestamp**: `2026-08-19 22:54 UTC`  
**Preregistration Protocol Hash**: SHA-256 `81600a3a772e9ceff9b19fdff503393895bbdf8a69607e3cb9d046f2ad60a73d`  
**Analysis Freeze Verdict**: **`FROZEN V2 — PROSPECTIVE ESTIMAND & BOOTSTRAP RESAMPLING LOCKED`**

---

## 1. Authoritative Primary Hypothesis

* **Primary Hypothesis $H_1$**: The terminal checkpoint-change interaction estimand $\Gamma_{256}$ differs significantly from zero:
  $$H_0: \Gamma_{256} = 0 \quad \text{vs.} \quad H_1: \Gamma_{256} \neq 0$$
  Where $\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$.

---

## 2. Primary Uncertainty Quantification Method

* **Problem-Blocked Bootstrap ($B = 10,000$)**:
  Uncertainty for $\Gamma_{256}$ and 95% non-parametric confidence intervals are computed via problem-blocked bootstrap resampling.
  * Entire problem units $i \in \{1, \dots, N\}$ ($N=454$) are resampled with replacement.
  * All 2 states ($R, C$), 9 checkpoints ($t=0..256$), and $K=16$ rollouts belonging to problem $i$ are carried together intact as a single block to preserve intra-problem covariance structures.

---

## 3. Secondary & Exploratory Analysis Specifications

* **Secondary Endpoints**: Trajectory plots of $\Gamma_t$ for intermediate checkpoints $t \in \{32, 64, 96, 128, 160, 192, 224\}$. Pointwise 95% confidence intervals are displayed as secondary/descriptive metrics.
* **Exclusion & Missing Data Policy**: Rollouts flagged with infrastructure runtime errors (`record_type != "empirical_confirmatory"` or execution crash) are logged and excluded. Missing data rate must remain $< 0.1\%$.
* **Firewall Enforcement**: Technical canary records (`technical_canary`, `dry_run_placeholder`) are strictly excluded from statistical evaluation.

*Signed by Lead Statistical Methodologist & Scientific Integrity Auditor*
