# STATISTICAL ANALYSIS & INFERENCE DOCUMENTATION

**Project**: StateShift  

---

## 1. Problem-Blocked Bootstrap ($B=10,000$)

To account for problem-level difficulty variation and intra-problem rollout correlation, all confidence intervals are computed using **problem-blocked bootstrap resampling** ($B=10,000$ iterations). Entire problem clusters ($p \in \{1..N\}$) are resampled with replacement, preserving rollout structure within each sampled problem.

---

## 2. Multiplicity Adjustments

For intermediate trajectory checkpoints, Bonferroni multiplicity adjustments are applied to control the family-wise error rate across intermediate comparisons. At step 32, the multiplicity-adjusted 95% CI is $[+0.0011, +0.0655]$, confirming that target-transition contrast is statistically detectable at $t=32$.

---

## 3. Order-Restricted Analysis (PAVA)

Because unconstrained intermediate point estimates exhibit small sampling fluctuations at $K=2/3$ (e.g., $\Gamma_{96}=0.0774 \to \Gamma_{128}=0.0748$), we evaluate global trend consistency using the prespecified Pooled Adjacent Violators Algorithm (PAVA). The isotonic regression fit confirms that the trajectory is consistent with a non-decreasing trend across post-training.

*Signed by Lead Statistical Methodologist*
