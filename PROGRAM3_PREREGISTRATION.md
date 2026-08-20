# Program 3 Experimental Preregistration Document

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PRE-PILOT PREREGISTERED SPECIFICATION**

---

## 1. Formal Hypotheses

* **Null Hypothesis ($H_0$)**: Controller uncertainty provides no practically useful information about future controller regret under nonstationary shift, and uncertainty-aware fallback does not materially reduce high-tail SLO regret relative to always-adaptive control.
* **Alternative Hypothesis ($H_1$)**: Controller uncertainty contains predictive information about future regret under nonstationary shift, and a preregistered uncertainty-aware fallback reduces high-tail SLO regret relative to always-adaptive control.

---

## 2. Trust Gate Baselines

1. **$T_0$ (No Gate / Always Adaptive)**: Un-gated dynamic weight adaptation (`AdaptiveReplica`).
2. **$T_1$ (Simple Residual Threshold)**: Trigger fallback when recent prediction error $e_t > \tau_{\text{res}}$.
3. **$T_2$ (OOD Distance Threshold)**: Trigger fallback when Mahalanobis distance to training distribution exceeds $\tau_{\text{dist}}$.
4. **$T_3$ (Calibrated Uncertainty Gate - Ours)**: Trigger fallback when prediction variance $\text{Var}(\hat{L}) > \tau_{\text{trust}}$.
5. **$T_4$ (Oracle Gate)**: Revert to static Raft majority ($R=5$) whenever $\text{Regret}_{\text{p99}} > 0$ (Analysis bound).

---

## 3. Primary & Secondary Endpoints

* **Primary Endpoint**: High-tail empirical excess latency regret $\text{Regret}_{\text{p99}}(r)$ across nonstationary shift regimes.
* **Secondary Endpoints**: Detection delay (ms), false fallback rate (%), time in fallback (%), Oracle Gap Captured (%).
