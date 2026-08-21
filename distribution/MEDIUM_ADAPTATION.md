# Medium Research Adaptation: When Confidence Proxies Confound Reasoning Complexity

> **Canonical Publication Note**: This article was originally published on my academic website: [Sham Satish Thakare's Research Essay](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/). For full interactive visualizations, LaTeX math equations, and complete experimental logs, please visit the canonical version.

---

# When Confidence Proxies Confound Reasoning Complexity

*A diagnostic audit exposing length confounding in token predictive entropy and why offline error predictors fail to improve online reinforcement learning for language models.*

**By Sham Satish Thakare** (August 2026)

---

In reinforcement learning from verifiable rewards (RLVR) for mathematical reasoning, Group Relative Policy Optimization (GRPO) estimates baseline-free advantages across sampled rollouts. To protect policies from reward hacking and policy collapse, researchers frequently hypothesize that weighting advantages by internal uncertainty signals—such as token predictive entropy—will suppress unreliable trajectories.

However, when we benchmark these uncertainty proxies across multi-step mathematical derivations on GSM8K, a striking empirical contradiction emerges:

> **Token predictive entropy correlates with sequence length ($r = +0.486$) rather than true mathematical error.**

Controlling for sequence length collapses the association between entropy and correctness from $r = -0.214$ to $r_{\text{partial}} = -0.092$ ($p = 0.365$). Consequently, naive uncertainty weighting inadvertently suppresses valid, multi-step exploration.

---

## 1. The Core Problem: Long Multi-Step Proofs Look "Uncertain"

A brief, direct calculation involves few token transitions and low aggregate predictive entropy. Conversely, a rigorous 10-step mathematical proof requires navigating multiple sub-equations, generating natural language transitions, and resolving intermediate numeric states. Each additional token introduces minor variance in the predictive distribution.

If a confidence proxy measures raw or mean token entropy without controlling for length, it will naturally assign higher "uncertainty" to long, correct derivations than to short, confident hallucinations.

In our **Correct-but-Complex Stress Test**, token predictive entropy misidentified correct multi-step reasoning traces as more uncertain than short incorrect errors in **42.1% of paired comparisons**.

---

## 2. Architectural Audit: The MC-Dropout Trap

Before benchmarking diagnostic proxies, we audited the internal execution graph of target open-weight causal models, specifically `Qwen/Qwen2.5-0.5B-Instruct`.

We find that the model contains **exactly 0 active `nn.Dropout` modules** in its attention and MLP blocks (`attention_dropout = 0.0`). Consequently, executing Monte Carlo dropout forward passes with `mc_dropout = True` produces mathematically deterministic passes:

$$\text{Var}(\log P) = 0.0000000000, \quad \Delta\text{Logit} = 0.0$$

When normalized in advantage scaling equations with stability constant $\epsilon = 10^{-8}$, floating-point order-of-operations noise ($\approx 10^{-12}$) yields a multiplier of $\exp(-\gamma \cdot 10^{-4}) \approx 0.999965$, producing policy update vectors strictly collinear to standard GRPO ($\cos(\Delta\theta) = 1.000000$).

---

## 3. Preregistered 5-Way Controlled RL Results

To test whether a validated offline error predictor (Self-Consistency consensus, $\text{AUROC} = 0.812$) translates into an effective online policy gradient weight, we preregistered **Consistency-Aware GRPO (CA-GRPO)**:

$$\tilde{A}_i = \hat{A}_i \cdot \Big(1.0 + \lambda \cdot (c_i - \bar{c})\Big)$$

We benchmarked CA-GRPO against four matched controls across three independent training seeds:

- **Standard GRPO (Outcome Supervised)**: $80.00\% \pm 0.00\%$ Pass@1
- **CA-GRPO (Proposed Consistency-Aware)**: $80.00\% \pm 0.00\%$ Pass@1
- **Permuted Consistency Control (Negative Control)**: $80.00\% \pm 0.00\%$ Pass@1
- **Compute-Matched GRPO ($K=8$)**: $78.33\% \pm 2.89\%$ Pass@1
- **Random Weight Control**: $75.00\% \pm 5.00\%$ Pass@1

### The Takeaway
CA-GRPO achieved an identical $80.00\%$ Pass@1 to Standard GRPO and Permuted Control, yielding an effect size of **Cohen's $d = 0.00$**. Negative controls proved that trajectory-specific advantage scaling provided no causal policy learning advantage over standard outcome-supervised GRPO.

---

## What This Means for Researchers

1. **Audit Your Architecture**: Verify that your target LLM actually contains active dropout before implementing MC-dropout uncertainty estimation.
2. **Control for Length**: Never evaluate token-level predictive entropy without controlling for sequence length via partial correlation.
3. **Run Preregistered Negative Controls**: Always include permuted and random weighting controls to verify that an advantage weighting scheme provides genuine causal utility.

---

### Links & Paper Reference

- **Full Canonical Article & Interactive Visualizations**: [https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)
- **PDF Manuscript**: [IEEE TAI Paper Submission PDF](https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf)
- **GitHub Repository**: [github.com/shamddd/ear_grpo_reasoning](https://github.com/shamddd/ear_grpo_reasoning)
