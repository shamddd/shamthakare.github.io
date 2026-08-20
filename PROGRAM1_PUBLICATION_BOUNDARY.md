# Program 1 Publication Boundary & Intellectual Property Firewall

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: Frozen & Formally Boundary-Demarcated

---

## 1. Frozen Pre-Existing Claims (Do Not Re-Use)

The following claims are permanently frozen under active journal submissions and cannot be claimed as new contributions in Program 1:

| Claim ID | Source Project / Repository | Canonical Claim Statement | Frozen Evidence / Metrics | Reusability Constraint |
|---|---|---|---|---|
| **CLM-001** | `ear_grpo_reasoning` (Submitted to IEEE TAI) | Token predictive entropy, mean NLL, and logit margin are confounded with derivation length ($r = +0.486$). | AUROC 0.618; stress test inversion rate 42.1%. | Cannot claim length confounding of token entropy as a new discovery. |
| **CLM-002** | `ear_grpo_reasoning` (Submitted to IEEE TAI) | Injecting offline self-consistency consensus weights into the inner RL loop yields 0.00% pass@1 accuracy gain over standard GRPO. | 80.00% vs 80.00% Pass@1 on GSM8K ($N=3$ matched seeds). | Cannot claim sample-level consensus weighting improves RL pass@1 accuracy. |
| **CLM-003** | `ear_grpo_reasoning` (Submitted to IEEE TAI) | Modern zero-dropout causal LLMs (Qwen2.5) render hidden-state MC-dropout probes deterministic ($\text{Var}=0.0$). | `nn.Dropout` count = 0 in attention and MLP blocks. | Cannot use MC-dropout probes on zero-dropout architectures. |
| **CLM-004** | `adaptive-rl-forge` (Submitted to JMLR) | Representation geometry probes ($\mathbf{\phi}(C_k) = [\alpha_{\text{SVD}}, \bar{H}, \sigma_g^2]^T$) predict downstream GRPO reward gain $\beta_{\text{RL}}$ with $R^2 = 0.91$. | $R^2 = 0.91$ ($p = 0.0004$), $<2\%$ compute consumption ratio. | Cannot claim representation probing for predicting RL reward gain. |

---

## 2. Prior External Work Demarcation (Prior Art Boundaries)

| Prior Art Work | Authors & Venue | Pre-empted Contribution (Prior Art) | Our Required Scientific Boundary |
|---|---|---|---|
| **Bereket & Leskovec (2025)** | Michael Bereket & Jure Leskovec (*OpenReview / arXiv 2025*) | Demonstrated that GRPO group standard normalization induces overconfidence for stochastic outcomes, and removing standard normalization restores calibration. | We **CANNOT** claim that GRPO normalization causes overconfidence. Our focus is on *how GRPO post-training breaks self-consistency agreement as a confidence proxy through trajectory homogenization and mode collapse on deterministic reasoning*. |
| **Damani et al. (ICLR 2026)** | Mehul Damani et al. (*ICLR 2026*) | Introduced RLCR adding Brier score rewards to PPO for verbalized confidence calibration. | We **CANNOT** claim adding a Brier reward to PPO for verbalized confidence is novel. Our focus is on *decoupling trajectory agreement from epistemic correctness under GRPO trajectory collapse*. |
| **Damani et al. (ICLR 2025)** | Mehul Damani et al. (*ICLR 2025*) | Formulated input-adaptive allocation of LM compute budgets. | We **CANNOT** claim basic token budget allocation is novel. Our focus is on *predicting negative flip transitions under extended reasoning*. |

---

## 3. Boundary Invariants for Program 1

1. **Focus on Trajectory Agreement Decoupling**: The new paper evaluates whether RLVR/GRPO post-training creates a **faithfulness gap between self-consistency agreement and epistemic correctness** caused by trajectory homogenization.
2. **Metric Independence**: The investigation evaluates **AURC (Area Under Risk-Coverage), Brier score, and semantic trajectory diversity**, going strictly beyond standard ECE.
3. **No Salami Slicing**: Infrastructure from `adaptive-rl-forge` is reused for evaluation, but all scientific claims are novel and distinct from `WORK-01` and `WORK-05`.
