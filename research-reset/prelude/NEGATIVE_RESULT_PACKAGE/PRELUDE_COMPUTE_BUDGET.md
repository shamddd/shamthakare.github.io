# PRELUDE V1: STATISTICAL POWER ANALYSIS & MEASURED COMPUTE CALIBRATION PROTOCOL

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Subject**: Statistical Power, Sample Size Engineering, and Hardware Calibration for PRELUDE v1

---

## 1. THE STATISTICAL UNIT PROBLEM & POWER ANALYSIS

### The Statistical Vulnerability of Naive Experimental Designs:
If an experiment tests 6 models $\times$ 2 datasets $\times$ 2 seeds = 24 runs, the effective statistical sample size for predicting performance is **$N = 12$ independent $(M, D)$ pairs**.

* **Why $N=12$ is Fatal for Deep Meta-Regressors**:
  A multi-layer neural network with hundreds of parameters trained on 12 data points will severely overfit, memorizing the specific base model identities rather than discovering true representation-to-RL transfer laws.
* **Statistical Power Calculation**:
  For $N = 12$, detecting a true rank correlation of $\tau = 0.50$ at significance level $\alpha = 0.05$ has a statistical power of only $1 - \beta \approx 0.42$ (a $58\%$ false negative risk).

---

## 2. THE RIGOROUS TWO-PRONGED STATISTICAL SOLUTION

To resolve the statistical power deficit while preserving computational feasibility, PRELUDE v1 implements two complementary safeguards:

```
+----------------------------------------------------------------------------------------------------+
|                                    STATISTICAL DESIGN ARCHITECTURE                                 |
+----------------------------------------------------------------------------------------------------+
| PRONG 1: DELIBERATELY LOW-CAPACITY STATISTICAL MODELS                                              |
|   - Non-parametric Rank Correlation (Kendall's tau, Spearman's rho) with exact permutation p-vals |
|   - Bivariate L2-penalized Logistic Regression for binary event Y = 1[Delta_RLVR > epsilon]        |
|   - Leave-One-Model-Family-Out Cross-Validation (LOMFO-CV) to strictly prevent identity memorization|
+----------------------------------------------------------------------------------------------------+
| PRONG 2: TRAJECTORY & DIFFICULTY DATASET EXPANSION (N = 12 -> N = 48 Data Points)                  |
|   - Pretraining Trajectory Checkpoints: Instead of evaluating only terminal weights, evaluate      |
|     intermediate checkpoints along public training curves (e.g., Pythia-410M at step 10k, 50k,     |
|     143k; SmolLM2 intermediate checkpoints). Each checkpoint M_t has distinct rank & support.      |
|   - Task Difficulty Stratification: Stratify GSM8K into Easy (1-2 reasoning steps) and Hard (4+    |
|     steps), alongside SVAMP.                                                                       |
|   - Expanded Sample Size: 12 Checkpoints x 4 Task Subsets = N = 48 distinct (M_t, D_k) data points |
|   - Statistical Power at N = 48: Power 1 - beta >= 0.88 for detecting tau >= 0.40 at alpha = 0.05 |
+----------------------------------------------------------------------------------------------------+
```

---

## 3. MEASURED GRPO COMPUTE CALIBRATION PROTOCOL

We explicitly reject unverified static estimates. Because GRPO runtime depends heavily on model size, generation length ($L_{\text{gen}}$), rollout count ($G$), and VRAM batching, compute must be **empirically calibrated before launching the full matrix**.

### Step 0 Hardware Calibration Benchmark:
Before committing to full runs, execute a standardized 10-step calibration probe on the target hardware (e.g., $1\times$ NVIDIA RTX 4090 / A100):

```
                        CALIBRATION TELEMETRY PROFILING
+------------------------------------------------------------------------------+
| 1. Rollout Generation Phase:                                                 |
|    Measure: Tokens/sec, GPU VRAM peak, generation latency for G=8, L=256     |
| 2. Reference Model Evaluation Phase:                                         |
|    Measure: Forward pass time for computing reference log-probabilities      |
| 3. Policy Optimization Phase:                                                |
|    Measure: Backward pass time and gradient step latency under BF16 / FlashAttn|
+------------------------------------------------------------------------------+
```

### Parametric Runtime Model Derived from Calibration:
$$\text{Estimated Runtime (Hours)} = \sum_{i=1}^M \left[ N_{\text{steps}}^{(i)} \cdot \left( T_{\text{gen}}(P_i, G, L) + T_{\text{ref}}(P_i, G, L) + T_{\text{bwd}}(P_i, G, L) \right) \right] + T_{\text{eval}}$$

### Target Configuration for Calibration:
* **Models for Calibration**: SmolLM2-360M (Low anchor) and Pythia-1.4B / Qwen-2.5-1.5B (High anchor).
* **Rollout Configuration**: $G = 8$ generations per prompt, temperature $T = 0.7$, max generation length $L_{\text{gen}} = 256$ tokens.
* **RLVR Steps**: 150 optimization steps with mini-batch size $B = 8$.

---

## 4. GATE 3 STATUS & PRE-REGISTRATION POLICY

1. **Gate 3 Condition**: No full training matrix will be launched until the Step 0 Calibration Benchmark outputs a verified hardware profiling table with exact measured seconds per step.
2. **Reproducibility Guarantee**: Every training run must log its hardware telemetry, PyTorch random seeds, CUDA memory allocations, and per-step reward curves to permanent disk storage.
