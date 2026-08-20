# PHASE 2 STAGE A — TRAJECTORY POWER REQUIREMENT & DESIGN SELECTION

**Milestone**: Phase 2 Stage A Prospective Trajectory Power Analysis  
**Simulation Engine**: $B = 10,000$ zero-GPU Monte Carlo replicates per candidate $K$  
**Target Checkpoints**: $t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$  

---

## 1. Monte Carlo Simulation Power Matrix

| Candidate $K$ | Additional Rollouts | Simulated SE ($\text{SE}_{\Gamma_t}$) | Pointwise 95% CI Width | Monotonicity Detection (Scenario A) | False Reversal Rate | Required Budget (USD) | Claim Strength Classification |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$K=16$** | 101,696 | `0.0083` | `0.0325` | `70.15%` | `1.05%` | **`$19.92`** | **MODERATE** ($\ge 65\%$) |
| **$K=24$** | **152,544** | **`0.0068`** | **`0.0266`** | **`87.07%`** | **`0.19%`** | **`$29.88`** | **STRONG** ($\ge 80\%$) |
| **$K=32$** | 203,392 | `0.0059` | `0.0230` | `93.90%` | `0.01%` | **`$39.85`** | **STRONG** ($\ge 80\%$) |
| **$K=48$** | 305,088 | `0.0048` | `0.0188` | `99.18%` | `0.00%` | **`$59.77`** | **STRONG** ($\ge 80\%$) |
| **$K=64$** | 406,784 | `0.0041` | `0.0163` | `99.70%` | `0.00%` | **`$79.69`** | **STRONG** ($\ge 80\%$) |

---

## 2. Minimum Design Recommendation

* **Minimum Design for Strong Monotonicity Claim ($\ge 80\%$ reliability)**: **`$K=24$`** ($152,544$ intermediate rollouts, **`$29.88 USD`** compute cost).
* **Current Account Balance**: **`$3.74 USD`**.
* **Additional Funding Required**: **`$26.14 USD`**.

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
