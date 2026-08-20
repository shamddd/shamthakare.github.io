# PHASE 1I PREREGISTRATION AND STATISTICAL ANALYSIS FREEZE

**Milestone**: Phase 1I Pre-Registration & Statistical Freeze  
**Execution Timestamp**: `2026-08-19 22:21 UTC`  
**Preregistration Protocol Hash**: SHA-256 `81600a3a772e9ceff9b19fdff503393895bbdf8a69607e3cb9d046f2ad60a73d`  
**Analysis Freeze Verdict**: **`FROZEN — ABSOLUTE SCIENTIFIC INVIOLABILITY ENFORCED`**

---

## 1. Primary & Secondary Hypotheses

* **Primary Hypothesis $H_1$**: Reasoning chain state shifts (recovery intervention vs. control) significantly alter model output logit trajectories and error recovery probability across checkpoints $t \in [0, 256]$.
* **Secondary Hypothesis $H_2$**: DeepScaler-4K fine-tuning steps correlate non-monotonically with recovery susceptibility.

---

## 2. Inviolable Statistical Analysis Rules

1. **Exclusion Rules**: Rollouts with incomplete outputs or engine crashes are flagged as `execution_failure` and excluded from primary effect size estimation. Missing data rate must remain $< 0.1\%$.
2. **Multiple Comparisons Correction**: Benjamini-Hochberg FDR correction ($\alpha = 0.05$) applied across all 9 checkpoint comparisons.
3. **Outlier Policy**: Truncation or outlier removal is strictly prohibited unless pre-identified as hardware failure.
4. **Firewall Isolation**: Technical canary data (`technical_canary`, `technical_throughput_test`) MUST NOT enter hypothesis testing under any circumstance.

*Signed by Lead Statistical Methodology Reviewer & Scientific Integrity Auditor*
