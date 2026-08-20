# PHASE 2B.1 — EMPIRICAL TRAJECTORY ANALYSIS REPORT

**Milestone**: Empirical Intermediate Trajectory Completion ($t \in \{64, 128, 192\}$)  
**Execution Timestamp**: `2026-08-20 04:00 UTC`  

---

## 1. Five-Point Empirical Trajectory Summary

Combining the newly observed intermediate checkpoints ($t \in \{64, 128, 192\}$, $8,172$ rollouts) with the frozen immutable endpoint benchmarks ($t=0$ and $t=256$):

$$\mathbf{EMPIRICAL\ 5\text{-}POINT\ \Gamma_t\ VECTOR:\ [0.0000,\ +0.0337,\ +0.0748,\ +0.0976,\ +0.1176]}$$

### Complete Checkpoint Contrast Table:

| Checkpoint ($t$) | Source | $\mu_{R,t}$ | $\mu_{C,t}$ | $\Delta_{R,t}$ | $\Delta_{C,t}$ | Interaction ($\Gamma_t$) | SE | 95% Blocked Bootstrap CI | Multiplicity-Adjusted CI | $p$-value |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$t=0$** | Frozen Primary | $0.3834$ | $0.3892$ | $0.0000$ | $0.0000$ | **`$0.0000$`** | — | — | — | — |
| **$t=64$** | **`Phase 2B.1 New`** | $0.4537$ | $0.4258$ | $+0.0703$ | $+0.0366$ | **`$+0.0337$`** | $0.0138$ | **`[+0.0081, +0.0610]`** | **`[+0.0022, +0.0657]`** | $0.0050$ |
| **$t=128$** | **`Phase 2B.1 New`** | $0.5609$ | $0.4919$ | $+0.1775$ | $+0.1027$ | **`$+0.0748$`** | $0.0149$ | **`[+0.0462, +0.1025]`** | **`[+0.0364, +0.1085]`** | $<0.0001$ |
| **$t=192$** | **`Phase 2B.1 New`** | $0.6571$ | $0.5653$ | $+0.2737$ | $+0.1761$ | **`$+0.0976$`** | $0.0141$ | **`[+0.0695, +0.1252]`** | **`[+0.0657, +0.1304]`** | $<0.0001$ |
| **$t=256$** | Frozen Primary | $0.7039$ | $0.5921$ | $+0.3205$ | $+0.2029$ | **`$+0.1176$`** | $0.0113$ | **`[+0.0955, +0.1400]`** | — | $<0.0001$ |

---

## 2. Claim Enablement Classification

1. **INTERMEDIATE EFFECT**: **`ENABLED`**. All intermediate checkpoints ($t=64, 128, 192$) display statistically significant state-selective interactions ($\Gamma_t > 0, p < 0.01$).
2. **COARSE LOCALIZATION**: **`ENABLED`**. State-selective transition contrast becomes statistically detectable as early as step 64 ($\Gamma_{64} = +0.0337$, Bonferroni 95% CI $[+0.0022, +0.0657]$).
3. **BROAD SAMPLED TRAJECTORY CHARACTERIZATION**: **`ENABLED`**. Across the 5 sampled checkpoints, state-selective interaction increases monotonically from $0.0000 \to +0.0337 \to +0.0748 \to +0.0976 \to +0.1176$.
4. **STRICT MONOTONICITY / INFLECTION / PEAK**: **`NOT ENABLED`** (requires dense sampling $K \ge 8$).

*Signed by Principal ML Research Scientist & Statistical Methodologist*
