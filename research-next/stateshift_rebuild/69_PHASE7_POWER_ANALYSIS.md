# PHASE 7 MONTE CARLO POWER AND PRECISION ANALYSIS

**Project**: StateShift Scientific Rebuild — Phase 7A  
**Author**: Sham Satish Thakare  

---

## 1. Simulation Results ($N_{\text{new}} = 500$ Untouched `GSM8K` Problems)

We evaluated statistical power ($1 - \beta$) and 95% CI half-width for detecting recovery-specific capability gains ($\Gamma_t^{\text{spec}}$) on the untouched `GSM8K` test dataset ($N=500, K=16$, $8,000$ rollouts per arm cell) under a two-sided test ($\alpha = 0.05$):

| Effect Size ($\Gamma^{\text{spec}}$) | Standard Error ($SE$) | 95% CI Half-Width ($\pm$) | Rejection Power (Two-Sided $\alpha=0.05$) | Power Verdict |
| :---: | :---: | :---: | :---: | :--- |
| **$+0.0100$** | $0.0109$ | $\pm 0.0214$ | **14.0%** | Low Sensitivity |
| **$+0.0200$** | $0.0109$ | $\pm 0.0214$ | **44.4%** | Moderate Sensitivity |
| **$+0.0300$** | $0.0109$ | $\pm 0.0214$ | **78.7%** | **`HIGH POWER`** ($\approx 80\%$) |
| **$+0.0500$** | $0.0109$ | $\pm 0.0213$ | **99.6%** | **`EXCELLENT`** ($\ge 99\%$) |
| **$+0.0800$** | $0.0108$ | $\pm 0.0212$ | **100.0%** | **`EXCELLENT`** |
| **$+0.1200$** | $0.0108$ | $\pm 0.0211$ | **100.0%** | **`EXCELLENT`** |

---

## 2. Power & Precision Conclusion

* At $N_{\text{new}}=500, K=16$, 95% CI half-width narrows to **$\pm 0.0213$**.
* Power to detect an effect as small as $\Gamma^{\text{spec}} = +0.0300$ reaches **$78.7\%$**.
* Power to detect effects $\ge +0.0500$ is **$99.6\%$**.

*Signed by Lead Statistician & Simulation Specialist*
