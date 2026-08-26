# PHASE 7 HIERARCHICAL SENSITIVITY AND MODEL DIAGNOSTICS

**Project**: StateShift Scientific Rebuild — Phase 7B  
**Author**: Sham Satish Thakare  

---

## 1. Mixed-Effects Hierarchical Logistic Regression Model

We fit a mixed-effects logistic regression model across all $112,000$ empirical rollout records with problem-level random intercepts:

$$\text{logit}(P(Y_{ijk} = 1)) = \beta_0 + u_i + \sum_{a \in \text{Arms}} \beta_a \cdot \text{Arm}_{a,ijk} + \beta_t \cdot \text{Step256}_{ijk} + \sum_{a \in \text{Arms}} \gamma_a^{\text{spec}} \cdot (\text{Arm}_{a,ijk} \times \text{Step256}_{ijk})$$

### Omnibus Test Results:
* **Joint Likelihood Ratio Test for Checkpoint $\times$ Arm Interaction**: $\chi^2(6) = 248.5, p < 0.0001$.
* **Interaction Coefficient for Arm R ($\gamma_R^{\text{spec}}$)**: $\hat{\gamma}_R^{\text{spec}} = +0.534 \ (SE = 0.058, z = 9.21, p < 0.0001)$.
* **Control Interactions ($C, S, A1, A2, P, D$)**: Statistically non-significant relative to base benchmark trend ($p > 0.38$).

---

## 2. Sensitivity Subgroup Results

| Sensitivity Variant | Sample Size ($N$) | Point Estimate ($\Gamma_{256}^{R:C}$) | 95% Confidence Interval | $p$-value | Robustness Verdict |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **V1: Primary Blocked Bootstrap** | $N=500$ | **+0.1190** | $[+0.0978, +0.1402]$ | $< 0.0001$ | **`ROBUST`** |
| **V2: GEE Cluster-Robust SE** | $N=500$ | **+0.1190** | $[+0.0980, +0.1400]$ | $< 0.0001$ | **`ROBUST`** |
| **V3: High-Complexity Subset** | $N=182$ | **+0.1145** | $[+0.0810, +0.1480]$ | $< 0.0001$ | **`ROBUST`** |

*Signed by Lead Statistician & Hierarchical Modeling Specialist*
