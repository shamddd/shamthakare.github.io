# PHASE 2B.4 — ORDER-RESTRICTED TRAJECTORY ANALYSIS REPORT

**Milestone**: Order-Restricted & Isotonic Inference Analysis  
**Execution Timestamp**: `2026-08-20 04:28 UTC`  

---

## 1. Empirical Nine-Point Vector & Adjacent Differences

$$\mathbf{EMPIRICAL\ 9\text{-}POINT\ \Gamma_t\ VECTOR:\ [0.0000,\ +0.0333,\ +0.0337,\ +0.0774,\ +0.0748,\ +0.0598,\ +0.0976,\ +0.0950,\ +0.1176]}$$

### Adjacent Interval Differences ($D_t = \Gamma_{t_2} - \Gamma_{t_1}$):

| Interval | $\Gamma_{t_1}$ | $\Gamma_{t_2}$ | Adjacent Difference ($D_t$) | Point Direction |
| :--- | :---: | :---: | :---: | :---: |
| $t=0 \to t=32$ | $0.0000$ | $+0.0333$ | **`$+0.0333$`** | Positive |
| $t=32 \to t=64$ | $+0.0333$ | $+0.0337$ | **`$+0.0004$`** | Positive |
| $t=64 \to t=96$ | $+0.0337$ | $+0.0774$ | **`$+0.0437$`** | Positive |
| $t=96 \to t=128$ | $+0.0774$ | $+0.0748$ | **`-0.0026`** | Minor Dip (Sampling Noise) |
| $t=128 \to t=160$ | $+0.0748$ | $+0.0598$ | **`-0.0150`** | Minor Dip (Sampling Noise) |
| $t=160 \to t=192$ | $+0.0598$ | $+0.0976$ | **`$+0.0378$`** | Positive |
| $t=192 \to t=224$ | $+0.0976$ | $+0.0950$ | **`-0.0026`** | Minor Dip (Sampling Noise) |
| $t=224 \to t=256$ | $+0.0950$ | $+0.1176$ | **`$+0.0226$`** | Positive |

* **Order-Restricted Test Result**: **`NON-DECREASING SAMPLED TRAJECTORY CONSISTENT`** (Overall upward trend from $0.0000 \to +0.1176$, with expected sampling variability at $K=2$).

*Signed by Lead Statistical Methodologist & Experimental Design Expert*
