# DEV / Hashnode Post: Reproducing RLVR Credit Assignment Controls & MC-Dropout Audit

**Author**: Sham Satish Thakare  
**Canonical Research Link**: [https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)  

---

## Technical Overview

When engineering Reinforcement Learning from Verifiable Rewards (RLVR) pipelines using Group Relative Policy Optimization (GRPO) for reasoning LLMs, advantage scaling is defined as:

$$\hat{A}_i = \frac{R(y_i) - \mu_R}{\sigma_R + \epsilon}$$

Many recent implementations attempt to weight $\hat{A}_i$ using Monte Carlo (MC) dropout or token predictive entropy:

$$\tilde{A}_i = \hat{A}_i \cdot U(y_i)$$

This post walks through two critical engineering bugs you should audit in your post-training codebase before deploying uncertainty-weighted policy gradients.

---

## Bug 1: MC-Dropout Collapse on Zero-Dropout Compute Graphs

If you enable `mc_dropout = True` on popular open-weight models like `Qwen/Qwen2.5-0.5B-Instruct` or `Llama-3`, check your PyTorch compute graph.

Inspecting `Qwen2ForCausalLM` reveals:
```python
# attention_dropout = 0.0
# active nn.Dropout modules = 0
```

Because 0 active dropout modules exist, multiple forward passes yield **zero variance**:

$$\text{Var}(\log P) = 0.0000000000$$

Any small numerical variation is floating-point order-of-operations noise ($\approx 10^{-12}$), making the resulting advantage scaling multiplier $\approx 0.999965$ and rendering policy updates collinear to standard GRPO ($\cos(\Delta\theta) = 1.000000$).

---

## Bug 2: Token Predictive Entropy Sequence Length Confound

When computing mean token entropy $\bar{H}(y) = \frac{1}{T}\sum_{t=1}^T H(P(y_t | y_{<t}))$, long multi-step reasoning traces accumulate higher entropy simply due to token length ($r = +0.486$).

Controlling for length via partial correlation reveals that the relationship between entropy and error vanishes:

$$r_{\text{partial}} = -0.092 \quad (p = 0.365)$$

In 42.1% of paired comparisons, token entropy incorrectly penalizes valid multi-step reasoning traces while rating short incorrect answers as high confidence.

---

## Preregistered 5-Way Control Experiment

We ran a 5-way controlled RL benchmark ($N=3$ seeds) on GSM8K:

```python
results = {
    "Standard-GRPO": {"pass_at_1": "80.00% ± 0.00%", "reward": 0.12},
    "Compute-Matched-GRPO-K8": {"pass_at_1": "78.33% ± 2.89%", "reward": 0.26},
    "Random-Weight-Control": {"pass_at_1": "75.00% ± 5.00%", "reward": 0.21},
    "Permuted-Consistency-Control": {"pass_at_1": "80.00% ± 0.00%", "reward": 0.29},
    "CA-GRPO-Proposed": {"pass_at_1": "80.00% ± 0.00%", "reward": 0.12}
}
```

Effect size over standard outcome-supervised GRPO: **Cohen's $d = 0.00$**.

---

## How to Reproduce

All figures and logs are programmatically regenerable using our open-source scripts:

```bash
git clone https://github.com/shamddd/ear_grpo_reasoning.git
cd ear_grpo_reasoning
python3 scripts/generate_figures.py
```

- **Full Technical Article**: [https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/](https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/)
- **PDF Paper**: [IEEE TAI Manuscript PDF](https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf)
