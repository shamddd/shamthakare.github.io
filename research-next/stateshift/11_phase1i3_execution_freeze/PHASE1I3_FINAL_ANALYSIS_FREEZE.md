# PHASE 1I.3 FINAL STATISTICAL ANALYSIS FREEZE

**Milestone**: Phase 1I.3 Pre-Execution Statistical Freeze  
**Execution Timestamp**: `2026-08-19 23:29 UTC`  
**Primary Dataset**: $N = 454$ (`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json`)  
**Strict Sensitivity Dataset**: $N = 388$ (`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json`)  
**Resampling Protocol**: Problem-Blocked Bootstrap ($B = 10,000$)  

---

## 1. Frozen Primary Statistical Protocol

1. **Primary Estimand**:
   $$\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$$
2. **Inference Procedure**:
   * Problem-blocked bootstrap with $B = 10,000$ iterations.
   * Resamples entire problem units $i \in \{1, \dots, 454\}$ with replacement.
   * 95% non-parametric percentile confidence intervals $[q_{0.025}, q_{0.975}]$.
   * Two-tailed $p$-value derived from bootstrap distribution inversion.

---

## 2. Frozen Sensitivity Analysis Protocol

* **Strict Contamination Sensitivity ($N=388$)**: Re-evaluates $\Gamma_{256}$ on the strict 388-problem subset to confirm that findings persist after removing potential pre-training overlap items.
* **Sensitivity Classification**: $N=388$ is strictly a secondary sensitivity check and will **NOT** replace $N=454$ as the primary result.

*Signed by Lead Statistical Methodologist & Scientific Integrity Auditor*
