# STATISTICAL PLAN — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Primary Endpoints & Metrics

1. **Held-Out Task Pass@1 ($P_{\text{pass}}$)**: Proportion of held-out test episodes that satisfy the environment terminal unit tests / assertions.
2. **Tool Selection Precision ($P_{\text{tool}}$)**: Ratio of causally necessary tool calls to total executed tool calls:
   $$\text{Precision} = \frac{|\mathcal{T}_{\text{causal}} \cap \mathcal{T}_{\text{executed}}|}{|\mathcal{T}_{\text{executed}}|}$$
3. **Policy Gradient Empirical Trace Variance ($V_{\nabla}$)**:
   $$\hat{V}_{\nabla} = \frac{1}{B} \sum_{i=1}^B \|\nabla_\theta \mathcal{L}_i - \bar{\nabla}_\theta \mathcal{L}\|^2$$
4. **Tool Call Redundancy Index**: Average number of non-contributory tool calls per solved task.

---

## 2. Statistical Significance Testing & Sample Size

- **Independent Seeds**: $N=3$ fully independent training runs initialized with seeds `42`, `1337`, `2026`.
- **Test Set Size**: $N_{\text{test}} = 200$ independent prompt episodes per benchmark.
- **Statistical Tests**:
  - Primary Pass@1 comparison between C3A and Standard GRPO: **Two-tailed Welch's t-test** (accounting for unequal variance) and non-parametric **Mann-Whitney U test**.
  - Alpha threshold: $\alpha = 0.05$ (Bonferroni-corrected for multiple pairwise baseline comparisons: $\alpha_{\text{adjusted}} = 0.05 / 4 = 0.0125$).
  - Effect Size Metric: **Cohen's $d$** (Target: $d \ge 0.8$, indicating a large effect size).
  - Confidence Intervals: 95% bootstrap confidence intervals computed via 10,000 resamples.

---

## 3. Stopping Rule & Preregistered Exclusion Protocol

- **Stopping Rule**: Training terminates exactly at 1,000 gradient updates ($\approx 16,000$ episodes). No early stopping based on test-set peeking.
- **Data Exclusion**: An episode is excluded from evaluation **only** if the external API environment throws an unhandled socket crash or hardware timeout ($>60$ seconds); all other runtime tool errors (e.g., HTTP 400/500, SQL syntax error) are retained as valid environment signals.
