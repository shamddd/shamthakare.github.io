# NEGATIVE CONTROLS — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Mandatory Scientific Negative Controls

In accordance with strict scientific methodology, a proposed method beating a weak baseline is insufficient to prove causal mechanism validity. C3A requires 4 rigorous negative and calibration controls:

```
====================================================================================================
CONTROL MATRIX
====================================================================================================
Control 1: Permuted-Credit Control (Shuffled Step Weights)
   └── Validates whether advantages require true temporal-causal alignment.
Control 2: Random-Weight Advantage Control (Gaussian Noise Scaling)
   └── Validates whether improvements stem from regularization noise vs causal signal.
Control 3: Compute-Matched Rollout Control (Increased Sample Budget)
   └── Validates whether gains persist when baseline GRPO is allocated equal FLOPs.
Control 4: Oracle Causal DAG Control (Synthetic Ground-Truth)
   └── Establishes the theoretical upper bound on synthetic benchmark environments.
====================================================================================================
```

---

## 2. Control Specifications

### Control 1: Permuted-Credit Control ($\text{C3A}_{\text{perm}}$)
- **Design**: For every generated trajectory $\tau$, compute the true C3A counterfactual turn weights $[\hat{\Phi}_1, \hat{\Phi}_2, \dots, \hat{\Phi}_K]$. Then, randomly permute the weights across turns: $\tilde{\Phi} = \text{Permute}(\hat{\Phi})$. Apply $\tilde{\Phi}$ to the policy gradient.
- **Scientific Rationale**: If $\text{C3A}_{\text{perm}}$ matches or beats true C3A, the performance gains are an artifact of random gradient scaling or magnitude variance rather than temporal causal credit attribution.
- **Pass Criterion**: True C3A must statistically significantly outperform $\text{C3A}_{\text{perm}}$ ($p < 0.01$).

### Control 2: Random-Weight Control ($\text{C3A}_{\text{rand}}$)
- **Design**: Replace $\hat{\Phi}(s_t, a_t)$ with independent Gaussian noise $\epsilon_t \sim \mathcal{N}(1.0, \sigma^2)$ matching the empirical mean and variance of true C3A weights.
- **Scientific Rationale**: Disproves the alternative hypothesis that advantage noise acts as an implicit entropy regularizer preventing policy collapse.
- **Pass Criterion**: True C3A must achieve higher Pass@1 and lower gradient variance than $\text{C3A}_{\text{rand}}$.

### Control 3: Compute-Matched GRPO ($G=8$)
- **Design**: Standard GRPO is given $G=8$ rollouts per prompt (matching the total forward-pass FLOPs consumed by C3A's ablation evaluations).
- **Scientific Rationale**: Ensures that C3A is not merely benefiting from extra forward-pass computation.
- **Pass Criterion**: C3A ($G=4$ + ablation) must outperform Compute-Matched GRPO ($G=8$).

### Control 4: Oracle Causal DAG Control ($\text{C3A}^*$)
- **Design**: On the synthetic `CausalTool-Env`, policy gradients are weighted by the true mathematical Shapley values derived from the known underlying ground-truth DAG.
- **Scientific Rationale**: Establishes the empirical gap between our unsupervised ablation estimator $\hat{\Phi}$ and the theoretical oracle $\Phi^*$.
- **Target**: C3A should achieve $\ge 85\%$ of the oracle performance gap.
