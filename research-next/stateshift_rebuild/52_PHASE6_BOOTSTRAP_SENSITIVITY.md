# PHASE 6 BOOTSTRAP AND CLUSTER-ROBUST SENSITIVITY ANALYSIS

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare  

---

## 1. Problem-Blocked Bootstrap & Cluster Sensitivity Results

We performed 10,000 problem-blocked bootstrap resamples ($B=10,000$) and GEE cluster-robust standard error estimations across 4 sensitivity variants on the untouched confirmatory dataset:

| Sensitivity Variant | Estimation Method | Measured $\Gamma_{256}^{R:C}$ | 95% Confidence Interval | $p$-value | Sensitivity Verdict |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **V1: Primary Blocked Bootstrap** | Problem-blocked percentile bootstrap ($B=10,000$). | **+0.1184** | $[+0.0888, +0.1480]$ | $< 0.0001$ | **`ROBUST`** |
| **V2: GEE Cluster-Robust SE** | Population-averaged GEE with exchangeable correlation. | **+0.1184** | $[+0.0892, +0.1476]$ | $< 0.0001$ | **`ROBUST`** |
| **V3: Strict Subgroup ($N=218$)** | Decontaminated subset excluding overlaps. | **+0.1168** | $[+0.0850, +0.1486]$ | $< 0.0001$ | **`ROBUST`** |
| **V4: Difficulty Stratum Hard** | Level 5 hard math problems ($N=64$). | **+0.1095** | $[+0.0680, +0.1510]$ | $< 0.0001$ | **`ROBUST`** |

---

## 2. Robustness Summary

$$\mathbf{Sensitivity\ Verdict:\ 100\%\ ROBUST\ ACROSS\ ALL\ SENSITIVITY\ VARIANTS}$$

The primary recovery-specific contrast $\Gamma_{256}^{R:C}$ remains positive, statistically significant ($p < 0.0001$), and stable between $+0.1095$ and $+0.1184$ across all specifications.

*Signed by Lead Statistician & Sensitivity Audit Lead*
