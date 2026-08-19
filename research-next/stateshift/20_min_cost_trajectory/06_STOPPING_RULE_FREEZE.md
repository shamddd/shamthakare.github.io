# PHASE 2B — PROSPECTIVE SEQUENTIAL STOPPING RULE FREEZE

**Milestone**: Prospective Stopping Rule Lock  

---

## 1. Frozen Stopping Criteria

$$\mathbf{STOPPING\ RULE:\ IF\ \text{CI}_{95\%}(\Gamma_{128})\ EXCLUDES\ ZERO\ \rightarrow\ STOP\ AFTER\ STAGE\ B1\ (K=3)}$$

1. **Criterion 1 (Intermediate Effect Detected)**: $\Gamma_{128} > 0$ with $p < 0.05$ (problem-blocked bootstrap 95% CI strictly above 0.000).
2. **Criterion 2 (Uncertainty Ceiling Met)**: Width of 95% CI for $\Gamma_{128} \le 0.065$.
3. **Action**: If Criterion 1 OR Criterion 2 is satisfied upon evaluating Stage B1 ($8,172$ rollouts, $\$2.57$ USD), terminate trajectory sampling and seal publication results.

*Signed by Statistical Methodologist & Scientific Integrity Auditor*
