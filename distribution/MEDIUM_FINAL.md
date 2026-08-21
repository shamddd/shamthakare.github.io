# When Confidence Proxies Confound Reasoning Complexity

*What negative controls revealed about entropy, MC-dropout, and uncertainty-weighted RLVR*

**Author**: Sham Satish Thakare  
**Research Series**: *Reliable Adaptive Intelligent Systems — Research Notes*  
**Publication Status**: Working Paper / Research Note  
**Canonical Research Source**: [shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)  

---

> **Canonical Notice**: This article is a narrative research explainer adapted from the canonical technical research note available on my academic website. For interactive explorables, compute graph audits, and raw benchmark data, read the [Canonical Article](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/).

---

## The Question

When a language model produces a longer reasoning trace, should we interpret higher predictive entropy as greater uncertainty?

Not necessarily.

In reinforcement learning from verifiable rewards (RLVR) for mathematical reasoning, policy gradient algorithms such as Group Relative Policy Optimization (GRPO) compute baseline-free advantages across sampled candidate rollouts. To protect policies from policy collapse, researchers frequently hypothesize that scaling advantage vectors by internal model confidence signals—such as token predictive entropy or Monte Carlo dropout variance—will suppress unreliable trajectories:

$$\tilde{A}_i = \hat{A}_i \cdot f(U(y_i))$$

The intuition seems straightforward: if a model generates a trajectory with high predictive uncertainty, the policy should discount that trajectory. But what happens if the uncertainty metric is not measuring error at all—and is instead measuring **sequence completion length**?

---

## Why This Matters

Consider the structural difference between a single-step arithmetic recall task and a multi-step mathematical derivation:

- **Short Single-Step Response**: Few token transitions, low cumulative variance, short sequence length.
- **Long Multi-Step Proof**: Multiple sub-equations, natural language transitions, intermediate numeric states, long sequence length.

Every additional generated token introduces minor categorical variance into the predictive distribution. If an uncertainty metric sums or averages token predictive entropy over a trajectory without controlling for sequence length, it naturally assigns higher "uncertainty" to long, correct mathematical proofs than to short, confident hallucinations.

If an RL policy gradient algorithm scales advantage vectors by a length-confounded confidence proxy $U(y_i)$, it alters credit assignment. Trajectories with detailed multi-step reasoning receive reduced advantage weights simply because they are long. Over thousands of RLVR gradient steps, this induces length penalty distortion, pushing the policy toward concise shortcuts and penalizing the exploratory chain-of-thought derivations necessary for complex reasoning tasks.

![Figure 1: Reasoning Complexity Confound Overview](https://shamddd.github.io/shamthakare.github.io/assets/research/rlvr-reasoning/hero-concept.svg)
*Figure 1: Reasoning Complexity Confound Overview ($N = 100$ prompt clusters, `Qwen2.5-0.5B-Instruct`). Longer multi-step reasoning leads to higher token entropy ($r = 0.486$), causing naive estimators to misidentify valid derivations as uncertain.*

---

## Experiment 1 — Does Entropy Track Sequence Length?

We evaluated candidate uncertainty proxies across untouched GSM8K mathematical reasoning problems ($N = 100$ prompt clusters, 98 degrees of freedom) using `Qwen2.5-0.5B-Instruct`.

When measuring raw bivariate correlation, token predictive entropy appeared to correlate with trajectory correctness ($r = -0.214$). However, token predictive entropy was positively correlated with completion token length:

$$r = 0.486, \quad 95\%\text{ CI } [+0.318, +0.627], \quad N = 100$$

and equation count ($r = 0.421$). Longer reasoning derivations naturally accumulate higher aggregate predictive entropy.

![Figure 2: Sequence Length vs Token Predictive Entropy](https://shamddd.github.io/shamthakare.github.io/assets/research/rlvr-reasoning/correlation-length-entropy.svg)
*Figure 2: Sequence Length Confounding ($N = 100$ prompt clusters). Token predictive entropy increases systematically with sequence token count ($r = 0.486$).*

---

## Controlling for Length

To disentangle mathematical error from sequence completion length, we performed partial correlation analysis controlling for sequence token length:

$$r_{XY \cdot Z} = \frac{r_{XY} - r_{XZ} r_{YZ}}{\sqrt{(1 - r_{XZ}^2)(1 - r_{YZ}^2)}}$$

After controlling for completion length, the association between token predictive entropy and correctness decreased from $r = -0.214$ to:

$$r_{\text{partial}} = -0.092 \quad (p = 0.365, \text{not statistically significant})$$

Intuitively, partial correlation measures the relationship between two variables after removing the linear influence of a third variable (sequence length). Because the partial correlation collapses to non-significance ($p = 0.365$), raw token entropy operates primarily as a proxy for sequence length rather than mathematical validity.

![Figure 3: Error Discrimination AUROC Benchmark](https://shamddd.github.io/shamthakare.github.io/assets/research/rlvr-reasoning/auroc-benchmark.svg)
*Figure 3: Error Discrimination AUROC Benchmark ($N = 100$). Self-Consistency consensus achieved AUROC = 0.812, whereas token-level proxies clustered around 0.60–0.62 due to sequence length bias.*

---

## A Useful Stress Test

In the Correct-but-Complex Stress Test ($N = 100$ prompt clusters), we paired short incorrect derivations against long, multi-step correct derivations.

Token predictive entropy misidentified correct multi-step reasoning traces as more uncertain than short incorrect errors in **42.1% of paired comparisons**.

When an estimator misranks pairs 42.1% of the time, applying it as a multiplicative weight in policy gradients inadvertently penalizes the very exploratory reasoning chains necessary for multi-step problem solving.

---

## What Happened with MC-Dropout?

A common alternative uncertainty estimator is Monte Carlo dropout (Gal & Ghahramani, 2016), which estimates predictive variance across repeated forward passes with dropout enabled at test time.

We audited the PyTorch compute graph of `Qwen2.5-0.5B-Instruct` and discovered that the architecture contains **exactly 0 active `nn.Dropout` modules** in its attention and MLP blocks (`attention_dropout = 0.0`).

Executing nominal MC-dropout passes on this architecture yielded mathematically deterministic outputs:

$$\text{Var}(\log P) = 0.0000000000, \quad \Delta\text{Logit} = 0.0$$

When plugged into advantage scaling equations with stability constant $\epsilon = 10^{-8}$, floating-point order-of-operations noise ($\approx 10^{-12}$) produced update vectors collinear to standard GRPO ($\cos(\Delta\theta) = 1.000000$). In zero-dropout architectures, nominal MC-dropout sampling provides no variance signal. This highlights the importance of auditing architecture configurations before assuming an estimator functions as intended.

![Figure 4: Compute Graph Audit of Zero-Dropout Model](https://shamddd.github.io/shamthakare.github.io/assets/research/rlvr-reasoning/zero-dropout-audit.svg)
*Figure 4: Compute Graph Audit of Zero-Dropout Architecture. Zero active dropout modules collapse MC-dropout variance to 0.0, rendering uncertainty multipliers collinear to standard GRPO ($\cos(\Delta\theta) = 1.000000$).*

---

## Negative Controls

In empirical research, negative controls verify whether an observed effect is truly caused by the hypothesized mechanism or by uncaptured confounding variables.

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

Across the three evaluated seeds ($N = 3$), CA-GRPO and standard outcome-supervised GRPO produced the same observed mean Group Pass@1 ($80.00\% \pm 0.00\%$) with an observed effect size of **Cohen's $d = 0.00$**. Permuted consistency controls likewise yielded $80.00\% \pm 0.00\%$. In this evaluated experimental setup, trajectory-specific advantage scaling provided no observed performance advantage over standard outcome-supervised GRPO.

![Figure 5: Preregistered 5-Way Controlled RL Results](https://shamddd.github.io/shamthakare.github.io/assets/research/rlvr-reasoning/rl-control-results.svg)
*Figure 5: Preregistered 5-Way Controlled RL Results ($N = 3$ seeds). Proposed CA-GRPO achieved an observed 80.00% Pass@1, showing zero observed performance delta ($d = 0.00$) over standard outcome-supervised GRPO and permuted controls.*

---

## What I Learned

1. **Validate the Estimator Before Optimizing**: Offline metric correlation does not guarantee online policy gradient utility. Always test whether an estimator measures the target variable or a sequence-length proxy.
2. **Audit Architecture Assumptions**: Check model execution graphs explicitly. Nominal sampling loops on zero-dropout models yield deterministic passes.
3. **Negative Controls Are Essential**: Permuted and random controls prevent attributing performance changes to a mechanism when baseline variance or reward structures explain the outcome.
4. **Disentangle Nuisance Variables**: Use partial correlation or controlled counterfactuals to isolate genuine error signals from sequence length and reasoning complexity.

---

## What This Study Does NOT Establish

Scientific credibility requires explicit boundaries:

- **Model Boundary**: These experiments evaluate `Qwen2.5-0.5B-Instruct`; they do not establish whether the same behavior holds at larger model scales or across other model families.
- **Domain Boundary**: Diagnostic benchmarks reflect mathematical word problems (GSM8K, SVAMP) under a 256-token generation budget.
- **Seed Limitation**: RL evaluations were conducted across $N = 3$ independent training seeds. Observed equality reflects this evaluated sample size and does not constitute a formal statistical proof of universal non-inferiority.
- **Formulation Boundary**: Our negative controls evaluate trajectory-level advantage multipliers and do not reject step-level Process Reward Models (PRMs).

---

## Exploring the Research

The broader question is not whether uncertainty estimation should be abandoned, but which estimators remain informative after controlling for nuisance factors such as sequence length, architecture configurations, and sampling procedures.

For complete interactive explorables, figure provenance metadata, and reproducible evaluation code:

- 🌐 **Canonical Technical Essay**: [shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)
- 📄 **Working Paper PDF**: [ear-grpo-reasoning.pdf](https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf)
- 💻 **GitHub Code Repository**: [github.com/shamddd/ear_grpo_reasoning](https://github.com/shamddd/ear_grpo_reasoning) (Commit `cc2bec46d5f2421873fe8adfb83b622ad6e10861`)
