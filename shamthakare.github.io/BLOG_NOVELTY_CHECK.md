# Scientific Novelty & Boundary Analysis

**Author**: Sham Satish Thakare  
**Target Paper**: *Estimator Validity, Reasoning Complexity, and Negative-Control Protocols for Uncertainty-Weighted Credit Assignment in RLVR Post-Training* (IEEE TAI Submission ID: `TAI-2026-Aug-A-01878`)  

---

## Literature Boundary & Overlap Comparison

| Prior Work | Key Claim / Method | Overlap with Our Work | Distinction & Our Novel Contribution | Wording Safety Guidelines |
|---|---|---|---|---|
| **Shao et al. (2024)** *DeepSeekMath* | Group Relative Policy Optimization (GRPO) estimates baseline-free advantages via rollout normalization. | We use standard GRPO as our foundation and outcome-supervised baseline. | We perform the first formal audit of trajectory-level uncertainty advantage weighting over standard GRPO in math reasoning. | Do not claim GRPO is ours. State clearly: *"We benchmark uncertainty advantage scaling on top of Shao et al.'s GRPO framework."* |
| **Gal & Ghahramani (2016)** *MC-Dropout* | Monte Carlo dropout forward passes approximate Bayesian posterior uncertainty. | Probing model uncertainty via dropout. | We show that MC-dropout uncertainty estimation is mathematically degenerate ($\text{Var}(\log P)=0.0$) on zero-dropout causal LLMs (`Qwen2.5-0.5B`), creating float order-of-operations artifacts. | Frame as an architectural execution audit on zero-dropout models, not a critique of Gal's theory itself. |
| **Kadavath et al. (2022)** *LM Calibration* | LMs possess internal confidence calibration for QA tasks. | Analyzing token-level entropy and logit margins. | We demonstrate that for multi-step reasoning, token entropy correlates with sequence length ($r=+0.486$), and controlling for length collapses the association ($r_{\text{partial}}=-0.092, p=0.365$). | Frame as exposing a sequence-length confound in multi-step chain-of-thought, distinct from single-step QA calibration. |
| **Wang et al. (2023)** *Self-Consistency* | Marginalizing reasoning paths via majority voting improves accuracy and provides self-consistency confidence ($U_{SC}$). | We evaluate Self-Consistency ($K=4$) as an offline confidence proxy and online RL weight. | We show $U_{SC}$ is robust to length bias ($r_{\text{partial}}=-0.569, p=8.1\times 10^{-10}, \text{AUROC}=0.812$), but online Consistency-Aware GRPO achieves $d=0.00$ over standard GRPO. | Explicitly separate offline diagnostic value from online credit assignment utility. |
| **Kuhn et al. (2023)** *Semantic Uncertainty* | Semantic clustering of natural language rollouts estimates semantic entropy. | Measuring semantic trajectory variance. | We test consistency-weighted advantage scaling under preregistered negative-control protocols (permuted & random weighting). | Highlight the negative-control protocol as our methodological contribution. |

---

## Defensible Scientific Wording Audit

- **DO NOT WRITE**: *"We are the first to solve LLM uncertainty in RL."*
- **PREFER**: *"We report a diagnostic audit and negative-control evaluation of uncertainty-weighted credit assignment in RLVR post-training."*

- **DO NOT WRITE**: *"MC-dropout is completely useless for LLMs."*
- **PREFER**: *"MC-dropout estimation becomes mathematically degenerate when executed on architectures containing zero active dropout modules in their compute graph."*

- **DO NOT WRITE**: *"Uncertainty weighting fails universally in all RL algorithms."*
- **PREFER**: *"In our preregistered 5-way controlled benchmark on GSM8K with Qwen2.5-0.5B-Instruct, trajectory-level consistency weighting yielded no causal performance advantage ($d=0.00$) over standard outcome-supervised GRPO."*
