# ANALYTICAL DERIVATION: BREAK-EVEN DEPLOYMENT HORIZON Q* & POWER-LAW CROSSOVER

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. BREAK-EVEN DEPLOYMENT HORIZON $Q^*(a, b)$

For any two interventions $a$ (e.g. $A_1$ Best-of-$N$) and $b$ (e.g. $A_3$ Full RLVR) where $C_{\text{train}}(b) > C_{\text{train}}(a)$ and $C_{\text{inference}}(a) > C_{\text{inference}}(b)$, the **Break-Even Query Horizon $Q^*(a, b)$** is:

$$Q^*(a, b) = \frac{C_{\text{train}}(b) - C_{\text{train}}(a)}{C_{\text{inference}}(a) - C_{\text{inference}}(b)}$$

Substituting our FLOP model:
$$Q^*(A_1(N), A_3) = \frac{C_{\text{train}}(A_3)}{(N - 1) \cdot C_{\text{inference}}(A_0) + N \cdot C_{\text{verifier}}}$$

### Key Crossover Insights:
* If deployment query volume $Q < Q^*$: Best-of-$N$ ($A_1$) consumes fewer total FLOPs than training full RLVR ($A_3$).
* If deployment query volume $Q > Q^*$: Training RLVR ($A_3$) amortizes its initial training cost $C_{\text{train}}(A_3)$ and becomes cheaper in total FLOPs.

---

## 2. CROSSOVER UNDER POWER-LAW INFERENCE SCALING

Assume inference-time verifier search error decays as a power law with sample count $N$:

$$\text{Error}_{A1}(N) = \alpha \cdot N^{-\beta}$$

where $\alpha > 0$ is the base error coefficient and $\beta > 0$ is the scaling exponent.

To achieve a target accuracy $U_{\text{target}}$ (or error $\epsilon = 1 - U_{\text{target}}$) using $A_1$, the required sample count is:

$$N(\epsilon) = \left( \frac{\alpha}{\epsilon} \right)^{1/\beta}$$

Substituting $N(\epsilon)$ into the total deployment cost for $A_1$:

$$C_{\text{total}}(A_1, Q, \epsilon) = Q \cdot \left[ \left( \frac{\alpha}{\epsilon} \right)^{1/\beta} \cdot \left( C_{\text{gen}} + C_{\text{verifier}} \right) \right]$$

Comparing to trained RLVR intervention $A_3$ which achieves error $\epsilon_{A3}$ at fixed single-sample inference cost:

$$C_{\text{total}}(A_3, Q) = C_{\text{train}}(A_3) + Q \cdot C_{\text{gen}}$$

### Analytical Crossover Boundary:

$$Q_{\text{crossover}}(\epsilon) = \frac{C_{\text{train}}(A_3)}{\left[ \left( \frac{\alpha}{\epsilon} \right)^{1/\beta} - 1 \right] C_{\text{gen}} + \left( \frac{\alpha}{\epsilon} \right)^{1/\beta} C_{\text{verifier}}}$$

* **High Scaling Exponent $\beta$** (Fast inference scaling): $N(\epsilon)$ remains small $\implies Q^*$ is very large $\implies A_1$ Best-of-$N$ dominates for almost all practical query volumes $Q$.
* **Low Scaling Exponent $\beta$** (Diminishing search returns / hard reasoning): $N(\epsilon)$ explodes $\implies Q^*$ shrinks rapidly $\implies$ Training RLVR ($A_3$) becomes amortized and optimal at small query volumes $Q$.

---

## 3. CONSTRAINED OPTIMIZATION FORMULATIONS

We evaluate two complementary optimization formulations:

### Formulation A: Budget-Constrained Utility Maximization
$$\max_{a \in \{A_0, A_1, A_2, A_3\}} U(a, D) \quad \text{subject to} \quad C_{\text{total}}(a, Q) \le B$$

### Formulation B: Cost-Minimized Target Utility (Cleanest Statistical Metric)
$$\min_{a \in \{A_0, A_1, A_2, A_3\}} C_{\text{total}}(a, Q) \quad \text{subject to} \quad U(a, D) \ge u_{\text{target}}$$

**Formulation B** is statistically cleaner because it compares FLOP efficiency directly at fixed performance thresholds, avoiding arbitrary utility scaling artifacts.
