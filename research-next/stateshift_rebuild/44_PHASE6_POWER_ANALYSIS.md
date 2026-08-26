# PHASE 6 POWER AND PRECISION ANALYSIS FOR UNTOUCHED CONFIRMATORY POPULATION

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare  

---

## 1. Monte Carlo Simulation Specifications

We evaluated statistical power ($1 - \beta$) and 95% CI half-width on the untouched confirmatory population ($N_{\text{conf}} = 254$ held-out problems) at rollout depth $K=16$ ($4,064$ rollouts per arm cell) across candidate effect sizes $\Gamma^{\text{spec}} \in \{0.01, 0.02, 0.03, 0.05, 0.08, 0.12\}$ under a two-sided test ($\alpha = 0.05$).

---

## 2. Power Grid Summary ($N_{\text{conf}} = 254, K=16$)

| Effect Size ($\Gamma^{\text{spec}}$) | Standard Error ($SE$) | 95% CI Half-Width ($\pm$) | Rejection Power (Two-Sided $\alpha=0.05$) | Power Verdict |
| :---: | :---: | :---: | :---: | :--- |
| **$+0.0100$** | $0.0154$ | $\pm 0.0301$ | **8.3%** | Low Sensitivity |
| **$+0.0200$** | $0.0154$ | $\pm 0.0301$ | **24.0%** | Moderate Sensitivity |
| **$+0.0300$** | $0.0153$ | $\pm 0.0300$ | **52.8%** | Acceptable Sensitivity |
| **$+0.0500$** | $0.0153$ | $\pm 0.0299$ | **89.5%** | **`HIGH POWER`** ($\ge 80\%$) |
| **$+0.0800$** | $0.0152$ | $\pm 0.0298$ | **99.9%** | **`EXCELLENT`** |
| **$+0.1200$** (Historical) | $0.0151$ | $\pm 0.0296$ | **100.0%** | **`EXCELLENT`** |

---

## 3. Precision Conclusion

* At $N_{\text{conf}}=254, K=16$, the 95% CI half-width is $\pm 0.0298 \approx \pm 0.0300$.
* Power to detect effect sizes $\Gamma^{\text{spec}} \ge +0.0500$ exceeds **$89.5\%$**.
* Power to detect the historical effect size ($\Gamma = +0.1176$) is **$100.0\%$**.

*Signed by Lead Statistician & Monte Carlo Simulation Specialist*
