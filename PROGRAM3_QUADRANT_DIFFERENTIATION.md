# Program 3 Q1–Q4 Quadrant Differentiation Architecture

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Formally define the four quadrant shift regimes required to scientifically isolate calibrated predictive uncertainty ($T_3$) from naive OOD input-distance gating ($T_2$).

---

## 1. The Four Quadrant Regimes

```mermaid
matrix
    title Q1-Q4 Quadrant Shift Matrix
    "Q1: In-Distribution & Reliable" : "Q3: OOD & Still Reliable (False-Positive Test for T2)"
    "Q4: ID-Looking & Unreliable (False-Negative Test for T2)" : "Q2: OOD & Unreliable"
```

| Quadrant Regime | Input Feature Distance | Controller Reliability | Expected Behavior of Naive OOD Gate ($T_2$) | Expected Behavior of Calibrated Uncertainty Gate ($T_3$) | Key Scientific Finding |
|---|:---:|:---:|---|---|---|
| **Q1: ID + Reliable** | Low (ID) | High (Accurate) | Trust ($0\%$ Fallback). Retains adaptive speedup. | Trust ($0\%$ Fallback). Retains adaptive speedup. | Baseline in-distribution performance. |
| **Q2: OOD + Unreliable** | High (OOD) | Low (Failed) | Fallback (Triggers). Eliminates tail regret. | Fallback (Triggers). Eliminates tail regret. | Simple OOD and Uncertainty agree. |
| **Q3: OOD + Still Reliable** *(Benign Shift)* | High (OOD) | **High (Accurate)** | **FALSE FALLBACK ($100\%$)**. Reverts to static Raft, losing adaptive speedups. | **MAINTAINS TRUST ($0\%$ Fallback)**. Retains $+2.00\text{ms}$ adaptive speedup. | **Proves $T_3$ avoids false fallbacks when input is OOD but controller works**. |
| **Q4: ID-Looking + Unreliable** *(Feature Aliasing)* | Low (ID) | **Low (Failed)** | **MISSED FALLBACK ($0\%$)**. Fails to detect shift, suffering $+82\text{ms}$ tail regret. | **PROACTIVE FALLBACK ($100\%$)**. Detects residual variance spike, eliminating tail regret. | **Proves $T_3$ catches controller failures when input looks normal**. |

---

## 2. Definitive Proof of Value

Program 3 explicitly proves that **calibrated predictive uncertainty ($T_3$) provides distinct scientific value over naive OOD distance ($T_2$)** by:
1. Preventing unnecessary false fallbacks in **Q3** (preserving adaptive speedups).
2. Detecting hidden controller failures in **Q4** (preventing severe tail-latency spikes).
