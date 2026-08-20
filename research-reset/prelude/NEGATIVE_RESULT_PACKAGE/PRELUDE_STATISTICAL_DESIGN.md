# PRELUDE V1: SIMULATION-BASED STATISTICAL DESIGN & POWER SPECIFICATION

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Subject**: Hierarchical Data Structure, Monte Carlo Power Simulation, and Model Comparison Protocol

---

## 1. THE HIERARCHICAL OBSERVATIONAL TREE

Intermediate checkpoints from the same pretraining trajectory and evaluations across tasks on the same model architecture are correlated. To prevent pseudo-replication and inflated degrees of freedom, we model data generation as a **5-Level Nested Hierarchy**:

```
+----------------------------------------------------------------------------------------------------+
|                               5-LEVEL HIERARCHICAL OBSERVATION TREE                                |
+----------------------------------------------------------------------------------------------------+
| Level 1: Model Family         [ SmolLM2, Pythia, Qwen2.5 ]                                         |
|    |                                                                                               |
|    +---> Level 2: Model Scale [ 360M, 410M, 0.5B, 1.4B, 1.7B ]                                      |
|             |                                                                                      |
|             +---> Level 3: Checkpoint Step [ Step 10k, Step 50k, Final Checkpoint ]                |
|                      |                                                                             |
|                      +---> Level 4: Task Condition [ GSM8K-Easy, GSM8K-Hard, SVAMP ]              |
|                               |                                                                    |
|                               +---> Level 5: Seed [ Seed 42, Seed 1337 ]                           |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. MONTE CARLO POWER SIMULATION AS A FUNCTION OF EFFECT SIZE

We purged all universal static power claims (e.g., "power $\ge 0.81$"). Effective sample size with intra-cluster correlation ($\rho_{\text{family}} \approx 0.35, \rho_{\text{ckpt}} \approx 0.50$) on $K=3$ model families yields $N_{\text{eff}} \approx 7.68$ independent clusters.

We executed a 500-iteration Monte Carlo hierarchical simulation (`research/prelude_v1/analysis/simulate_power.py`) evaluating Leave-One-Model-Family-Out (LOMFO-CV) paired prediction error between **Model BHI** and **Model BH**:

```
+----------------------------------------------------------------------------------------------------+
|                       MONTE CARLO HIERARCHICAL POWER SIMULATION RESULTS                            |
+--------------------+-------------------------+-----------------------+-----------------------------+
| Incremental Effect | Mean Incremental ΔR²    | Mean Incremental ΔMAE | Empirical Statistical Power |
+--------------------+-------------------------+-----------------------+-----------------------------+
| Small Effect       | ΔR² ≈ 0.011 (1.1%)      | ΔMAE = 0.0010         | 0.062 (6.2%)                |
| Moderate Effect    | ΔR² ≈ 0.070 (7.0%)      | ΔMAE = 0.0065         | 0.108 (10.8%)               |
| Large Effect       | ΔR² ≈ 0.219 (21.9%)     | ΔMAE = 0.0255         | 0.304 (30.4%)               |
+--------------------+-------------------------+-----------------------+-----------------------------+
```

### Critical Takeaway:
On small pilot sample sizes ($K=3$ families, 12–24 runs), statistical power to detect small or moderate incremental gains is low ($6\%\text{--}11\%$). A large effect ($\Delta R^2 \ge 0.20$) achieves $30.4\%$ power. Consequently:
1. **Stage B0 pilot runs are mandatory** to estimate empirical variance components before fixing the confirmatory sample size.
2. **Confirmatory matrix size cannot be arbitrarily fixed to $N=48$** without post-B0 variance estimation.

---

## 3. PRIMARY MODEL COMPARISON & METRICS

We fit low-capacity models (Ridge / ElasticNet) across three nested feature sets:

$$\begin{aligned}
\text{Model } B: \quad \hat{\Delta}_{\text{RLVR}} &= f(B) \\
\text{Model } BH: \quad \hat{\Delta}_{\text{RLVR}} &= f(B, H) \\
\text{Model } BHI: \quad \hat{\Delta}_{\text{RLVR}} &= f(B, H, I)
\end{aligned}$$

* **Primary Scientific Test**: **Model BHI vs. Model BH** (evaluating whether internal features $I$ explain residual variance unexplained by behavioral baselines $B$ and headroom/history $H$).
* **Primary Outcomes**:
  1. Held-out-family Mean Absolute Error ($\text{MAE}_{\text{BHI}}$ vs. $\text{MAE}_{\text{BH}}$)
  2. Held-out-family rank correlation (Spearman $\rho$, Kendall $\tau$)
  3. Sign accuracy for marginal gain ($\text{sign}(\hat{\Delta}) == \text{sign}(\Delta)$)
  4. Regret in selecting whether to execute RLVR under fixed budget
  5. Paired prediction-error difference ($\text{MAE}_{\text{BH}} - \text{MAE}_{\text{BHI}}$)
* **Secondary Outcome**: Incremental $\Delta R^2 = R^2_{\text{BHI}} - R^2_{\text{BH}}$ (reported with cluster-bootstrap confidence intervals).
