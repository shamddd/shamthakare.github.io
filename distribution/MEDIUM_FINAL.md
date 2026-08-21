# When Confidence Proxies Confound Reasoning Complexity

*Testing estimator validity, compute graph determinism, and negative controls in RLVR post-training*

**Author**: Sham Satish Thakare  
**Canonical Publication**: [shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)  

---

> **Canonical Notice**: This article is a narrative research explainer adapted from the canonical technical research note available on my academic website. For interactive widgets, complete compute graph audits, and raw benchmark data, read the [Canonical Article](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/).

---

## The Central Question

When reinforcement learning from verifiable rewards (RLVR) trains a language model to solve multi-step mathematical word problems, how should we assign credit across sampled rollout trajectories?

Under policy gradient frameworks such as Group Relative Policy Optimization (GRPO), advantage vectors are computed by normalizing rewards across $K$ sampled candidate solutions for a prompt. To prevent policy collapse and suppress unreliable generations, a prominent line of post-training research proposes scaling advantage vectors by internal model uncertainty signals:

$$\tilde{A}_i = \hat{A}_i \cdot f(U(y_i))$$

where $U(y_i)$ represents a confidence proxy such as token predictive entropy or Monte Carlo dropout variance.

The central intuition seems intuitive: if a model generates a trajectory with high predictive uncertainty, the policy should discount that trajectory. But what happens if the uncertainty metric is not measuring error at all—and is instead measuring **sequence completion length**?

---

## Why Token Predictive Entropy Can Be Misleading

Consider the structural difference between a single-step arithmetic recall task and a rigorous 10-step mathematical derivation:

- **Single-Step Derivation**: Few token transitions, low cumulative variance, short sequence length.
- **Multi-Step Proof**: Multiple sub-equations, natural language transitions, intermediate numeric states, long sequence length.

Every additional generated token introduces minor categorical variance into the predictive distribution. If an uncertainty metric sums or averages token predictive entropy over a trajectory without controlling for sequence length, it naturally assigns higher "uncertainty" to long, correct mathematical proofs than to short, confident hallucinations.

```
LONGER REASONING (Multi-Step CoT)
       │
       ▼
HIGHER TOKEN ENTROPY (r = 0.486, N=100)
       │
       ▼
NAIVE ESTIMATOR PENALTY ("Uncertain" Trajectory)
       │
       ▼
PARTIAL CORRELATION COLLAPSE (r_partial = -0.092, p = 0.365)
```

---

## Empirical Finding 1: Sequence Length Confounding ($N = 100$)

We evaluated candidate uncertainty proxies across untouched GSM8K mathematical reasoning problems ($N = 100$ prompt clusters, 98 degrees of freedom) using `Qwen2.5-0.5B-Instruct`.

When measuring raw bivariate correlation, token predictive entropy appeared to correlate with trajectory correctness ($r = -0.214$). However, token predictive entropy was strongly correlated with completion token length ($r = 0.486, 95\%\text{ CI } [+0.318, +0.627]$) and equation count ($r = 0.421$).

---

## Empirical Finding 2: Partial Correlation Collapse

To disentangle genuine mathematical error from sequence length, we performed partial correlation analysis controlling for sequence completion length:

$$r_{XY \cdot Z} = \frac{r_{XY} - r_{XZ} r_{YZ}}{\sqrt{(1 - r_{XZ}^2)(1 - r_{YZ}^2)}}$$

After controlling for completion length, the association between token predictive entropy and correctness decreased from $r = -0.214$ to:

$$r_{\text{partial}} = -0.092 \quad (p = 0.365, \text{not statistically significant})$$

Because the partial correlation collapses to non-significance, raw token entropy operates primarily as a proxy for sequence length rather than mathematical validity.

---

## Empirical Finding 3: Zero-Dropout MC-Dropout Determinism

A common alternative uncertainty estimator is Monte Carlo dropout (Gal & Ghahramani, 2016), which estimates predictive variance across repeated forward passes with dropout enabled at test time.

We audited the PyTorch compute graph of `Qwen2.5-0.5B-Instruct` and discovered that the architecture contains **exactly 0 active `nn.Dropout` modules** in its attention and MLP blocks (`attention_dropout = 0.0`).

Executing nominal MC-dropout passes on this architecture yielded mathematically deterministic outputs:

$$\text{Var}(\log P) = 0.0000000000, \quad \Delta\text{Logit} = 0.0$$

When plugged into advantage scaling equations with stability constant $\epsilon = 10^{-8}$, floating-point noise ($\approx 10^{-12}$) produced update vectors collinear to standard GRPO ($\cos(\Delta\theta) = 1.000000$). In zero-dropout architectures, nominal MC-dropout sampling provides no variance signal.

---

## Empirical Finding 4: Preregistered 5-Way Controlled RL Benchmark ($N = 3$ Seeds)

To test whether a validated offline error predictor translates into online policy gradient utility, we preregistered Consistency-Aware GRPO (CA-GRPO):

$$\tilde{A}_i = \hat{A}_i \cdot \Big(1.0 + \lambda \cdot (c_i - \bar{c})\Big)$$

where $c_i = \mathbb{I}(\text{extract}(y_i) = \text{modal answer})$ uses self-consistency consensus ($K = 4$, $\text{AUROC} = 0.812$).

We benchmarked CA-GRPO against four matched control conditions across three independent training seeds ($N = 3$ seeds: 42, 1337, 2026):

| Method | Group Size (K) | Seeds (N) | Pass@1 (%) | Train Reward |
|---|---|---|---|---|
| **Standard-GRPO** | 4 | N = 3 | 80.00% ± 0.00% | 0.12 |
| **Compute-Matched-GRPO** | 8 | N = 3 | 78.33% ± 2.89% | 0.26 |
| **Random-Weight-Control** | 4 | N = 3 | 75.00% ± 5.00% | 0.21 |
| **Permuted-Consist.-Control** | 4 | N = 3 | 80.00% ± 0.00% | 0.29 |
| **CA-GRPO (Proposed)** | 4 | N = 3 | 80.00% ± 0.00% | 0.12 |

Across the three evaluated seeds ($N = 3$), CA-GRPO and standard outcome-supervised GRPO produced the same observed mean Group Pass@1 ($80.00\% \pm 0.00\%$) with an observed effect size of **Cohen's $d = 0.00$**. In this evaluated setup, trajectory-specific advantage scaling provided no observed advantage over standard GRPO.

---

## What This Work Does NOT Show

Scientific clarity requires explicit boundaries:

1. **Model Scale Boundary**: These experiments evaluate `Qwen2.5-0.5B-Instruct`; they do not establish whether the same behavior holds at larger model scales or across other model families.
2. **Domain Boundary**: Findings reflect mathematical word problems (GSM8K, SVAMP) under a 256-token budget.
3. **Formulation Boundary**: Our negative controls evaluate trajectory-level advantage multipliers and do not reject step-level Process Reward Models (PRMs).

---

## Full Technical Evidence & Code

For complete interactive explorables, figure provenance metadata, and reproducible evaluation code:

- **Canonical Technical Essay**: [shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)
- **Working Paper PDF**: [ear-grpo-reasoning.pdf](https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf)
- **GitHub Code Repository**: [github.com/shamddd/ear_grpo_reasoning](https://github.com/shamddd/ear_grpo_reasoning) (Commit `cc2bec46d5f2421873fe8adfb83b622ad6e10861`)
