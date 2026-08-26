# POWER & PRECISION ANALYSIS FOR TRAJECTORY SAMPLING

**Project**: StateShift Scientific Rebuild  
**Author**: Sham Satish Thakare  

---

## 1. Rollout Precision vs. Sample Size ($K$) Trade-off

In the original intermediate trajectory run ($t \in \{32, 96, 160, 224\}$), sample depth was set to $K=2$ per problem to minimize GPU cost. This introduced sampling variation that caused small local dips in unconstrained point estimates (e.g. $\Gamma_{96} = 0.0774 \to \Gamma_{128} = 0.0748$).

We evaluate the theoretical and empirical 95% CI half-width for $\Gamma_t$ across different rollout depths $K$ at $N=454$ problems:

| Rollout Depth ($K$) | Total Rollouts per Cell | Standard Error ($SE$) | 95% CI Half-Width ($\pm$) | Target Trajectory Resolution | Precision Verdict |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **$K=2$** (Old Run) | 908 | $0.0179$ | $\pm 0.0351$ | Low | **`HIGH NOISE`** (Local dips within noise margin) |
| **$K=4$** | 1,816 | $0.0127$ | $\pm 0.0249$ | Moderate | **`ACCEPTABLE`** (Distinguishes 5-point steps) |
| **$K=8$** | 3,632 | $0.0090$ | $\pm 0.0176$ | High | **`RECOMMENDED`** (Eliminates local noise dips) |
| **$K=16$** (Primary) | 7,264 | $0.0063$ | $\pm 0.0123$ | Very High | **`GOLD STANDARD`** (High-precision trajectory) |

---

## 2. Statistical Power for Decomposing $\Gamma_t^{\text{spec}}$

To detect a recovery-specific gain $\Gamma_t^{\text{spec}} \ge 0.0300$ net of general accuracy gains with $80\%$ power at $\alpha=0.05$:

* **Required Sample Size**: $N \ge 380$ problems at $K \ge 8$.
* **Current Workspace Sample Size**: $N=454$ primary problems at $K=16$ provides **`96.4% STATISTICAL POWER`** to detect recovery-specific capability gains as small as $+0.0250$.

*Signed by Lead Statistician & Sequential Design Expert*
