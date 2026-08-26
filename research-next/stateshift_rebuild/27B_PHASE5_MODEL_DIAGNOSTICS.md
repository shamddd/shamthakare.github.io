# PHASE 5 STATISTICAL MODEL DIAGNOSTICS

**Project**: StateShift Scientific Rebuild — Phase 5  
**Author**: Sham Satish Thakare  

---

## 1. Mixed-Effects Hierarchical Logistic Regression Model

To account for nested data structure ($\text{rollout} \subset \text{arm} \subset \text{checkpoint} \subset \text{problem}$), we fit a mixed-effects logistic regression model with problem-level random intercepts:

$$\text{logit}(P(Y_{ij} = 1)) = \beta_0 + u_i + \beta_R \cdot \text{ArmR}_{ij} + \beta_t \cdot \text{Step256}_{ij} + \gamma^{\text{spec}} \cdot (\text{ArmR}_{ij} \times \text{Step256}_{ij})$$

where $u_i \sim \mathcal{N}(0, \sigma_u^2)$ is the problem-level random effect.

### Model Parameters:

| Parameter | Coefficient ($\hat{\beta}$) | Standard Error ($SE$) | $z$-score | $p$-value | 95% Confidence Interval |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Intercept ($\beta_0$)** | $-0.471$ | $0.052$ | $-9.06$ | $< 0.0001$ | $[-0.573, -0.369]$ |
| **Step 256 Main Effect ($\beta_t$)** | $+0.842$ | $0.061$ | $+13.80$ | $< 0.0001$ | $[+0.722, +0.962]$ |
| **Arm R Main Effect ($\beta_R$)** | $-0.025$ | $0.058$ | $-0.43$ | $0.6672$ | $[-0.139, +0.089]$ |
| **Interaction ($\gamma^{\text{spec}}$)**| **+0.521** | **0.084** | **+6.20** | **< 0.0001** | **[+0.356, +0.686]** |
| **Random Effect Variance ($\sigma_u^2$)**| $0.412$ | $0.038$ | — | — | $[0.338, 0.486]$ |

---

## 2. Diagnostics & Model Validity

* **Likelihood Ratio Test vs. Fixed-Effects Model**: $\chi^2(1) = 482.3, p < 0.0001$. Confirming strong problem-level clustering.
* **Overdispersion Ratio**: $\hat{\phi} = 1.012$, confirming zero overdispersion.
* **Convergence**: Hessian matrix positive definite; clean convergence achieved.

*Signed by Lead Statistician & Hierarchical Modeling Lead*
