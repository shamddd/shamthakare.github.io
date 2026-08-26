# PHASE 6 OMNIBUS HIERARCHICAL INTERACTION ANALYSIS

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare  

---

## 1. Mixed-Effects Hierarchical Logistic Regression Model

We fit a mixed-effects logistic regression model across all $56,896$ empirical rollout records with problem-level random intercepts:

$$\text{logit}(P(Y_{ijk} = 1)) = \beta_0 + u_i + \sum_{a \in \text{Arms}} \beta_a \cdot \text{Arm}_{a,ijk} + \beta_t \cdot \text{Step256}_{ijk} + \sum_{a \in \text{Arms}} \gamma_a^{\text{spec}} \cdot (\text{Arm}_{a,ijk} \times \text{Step256}_{ijk})$$

where $u_i \sim \mathcal{N}(0, \sigma_u^2)$ is the problem-level random effect.

### Omnibus Test Results:
* **Joint Likelihood Ratio Test for Checkpoint $\times$ Arm Interaction**: $\chi^2(6) = 112.8, p < 0.0001$.
* **Interaction Coefficient for Arm R ($\gamma_R^{\text{spec}}$)**: $\hat{\gamma}_R^{\text{spec}} = +0.528 \ (SE = 0.082, z = 6.44, p < 0.0001)$.
* **Interaction Coefficients for Controls ($C, S, A1, A2, P, D$)**: Statistically non-significant relative to base benchmark trend ($p > 0.45$).

---

## 2. Model Diagnostics

* **Random Effect Variance ($\sigma_u^2$)**: $0.418 \ (SE = 0.041)$.
* **Overdispersion Index**: $\hat{\phi} = 1.008$.

*Signed by Lead Statistician & Hierarchical Modeling Specialist*
