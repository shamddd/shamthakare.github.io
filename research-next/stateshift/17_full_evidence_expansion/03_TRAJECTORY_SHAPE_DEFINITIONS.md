# PHASE 2 STAGE A — TRAJECTORY SHAPE DEFINITIONS & THRESHOLDS

**Milestone**: Prospective Trajectory Property Definitions  

---

## 1. Mathematical Definitions & Predeclared Thresholds

1. **MONOTONICITY**: $\Gamma_0 \le \Gamma_{32} \le \dots \le \Gamma_{256}$ subject to tolerance $\delta = 0.005$. Requires $\ge 80\%$ Monte Carlo detection rate for STRONG claim.
2. **EMERGENCE CHECKPOINT**: The earliest checkpoint $t^* \in \{32..256\}$ where $\Gamma_{t^*} \ge 0.030$ ($p < 0.01$) and remains $\ge 0.030$ at all subsequent checkpoints.
3. **INFLECTION-LIKE DISCRETE CHANGE**: A statistically significant change in first differences $D_t = \Gamma_t - \Gamma_{t-32}$, measured by second difference $A_t = D_t - D_{t-32}$ exceeding $2 \times \text{SE}(A_t)$.
4. **LOCAL PEAK / MAXIMUM**: A checkpoint $t_{\text{peak}} \in \{32..224\}$ where $\Gamma_{t_{\text{peak}}} - \Gamma_{t_{\text{peak}}-32} > 0$ and $\Gamma_{t_{\text{peak}}+32} - \Gamma_{t_{\text{peak}}} < -0.020$ ($p < 0.05$).

*Signed by Lead Statistical Methodologist & Principal ML Research Scientist*
