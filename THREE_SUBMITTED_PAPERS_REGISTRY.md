# Three Submitted Papers Registry

**Author**: Sham Satish Thakare (Independent Researcher)  
**Date**: August 2026  
**Purpose**: Immutable canonical registry of all 3 submitted research manuscripts. Establishes a permanent firewall against self-plagiarism, claims duplication, and salami-slicing.

---

## MANUSCRIPT 1: IEEE TAI Submission (`WORK-05`)

* **Exact Title**: *When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning*
* **Manuscript ID**: Submitted to *IEEE Transactions on Artificial Intelligence* (IEEE TAI), August 2026.
* **Current Status**: `Submitted / Under Review`
* **Submission Date**: August 2026
* **Associated Repository**: [`ear_grpo_reasoning`](file:///Users/shamthakare/.gemini/antigravity/scratch/ear_grpo_reasoning)
* **Primary Research Question**: Does uncertainty-weighted credit assignment improve LLM reinforcement learning (GRPO) on multi-step reasoning tasks?
* **Hypotheses**: 
  - $H_1$: Weighting or regularizing policy gradient advantages by trajectory uncertainty prevents policy collapse and filters noisy exploration traces. (Falsified).
* **Claimed Novelty**: First empirical falsification of online sample-level uncertainty-weighted GRPO credit assignment, exposing length confounding in token entropy.
* **Methodology**: 5-way controlled RL matrix (Standard-GRPO, Compute-Matched-GRPO, Random-Weight-Control, Permuted-Control, Consistency-Aware GRPO / CA-GRPO). Architectural dropout audit across Transformer blocks.
* **Datasets**: GSM8K ($N=100$ held-out prompt clusters), SVAMP.
* **Models**: `Qwen/Qwen2.5-0.5B-Instruct`
* **Experiments**: Architectural dropout audit, diagnostic proxy benchmark ($N=100$), 5-way controlled RL matrix across 3 matched seeds.
* **Baselines**: Standard unweighted GRPO, Compute-Matched GRPO ($G=8$), Random Gaussian advantage weighting, Permuted consensus weighting.
* **Metrics**: Error AUROC, Error AUPRC, Partial Correlation $r(\text{Corr} \mid \text{Length})$, Pass@1 accuracy, Policy Entropy, KL divergence.
* **Primary Results**:
  - Token predictive entropy ($r = +0.486$), mean NLL ($r = +0.432$), logit margin ($r = +0.495$) track derivation length, misidentifying correct complex derivation as uncertain in 42.1% of cases.
  - CA-GRPO achieves 80.00% Pass@1 accuracy, matching standard unweighted GRPO (0.00% delta across 3 matched seeds).
* **Negative Findings**: Sample-level consensus weighting yields zero online RL policy gain ($\Delta = 0.00\%$) over standard outcome-supervised GRPO.
* **Limitations**: Evaluated on $N=3$ matched seeds, small model scale (Qwen2.5-0.5B), linear weighting functions.
* **Future Work Statements**: Explore process-level step calibration (not sample-level credit weighting).
* **Code Used**: `src/rl/grpo_trainer.py`, `experiments/run_phase7_cagrpo_matrix.py`
* **Data Used**: `results/FINAL_CANONICAL_RESULTS.json`

---

## MANUSCRIPT 2: IEEE BigData 2026 / MLBD 2026 Submission (`BigD497`)

* **Exact Title**: *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning*
* **Manuscript ID**: `BigD497`
* **Venue**: *11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026)* / *IEEE BigData 2026*
* **Current Status**: `Submitted / Under Review`
* **Submission Date**: August 17, 2026
* **Associated Repository**: [`submission_bigdata2026_main_v3`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_bigdata2026_main_v3)
* **Primary Research Question**: Do post-trained language model checkpoints exhibit a specialized error-recovery advantage beyond their baseline generation fluency improvements?
* **Hypotheses**: Post-trained instruction checkpoints possess specialized mechanisms for detecting and recovering from intermediate arithmetic errors. (Falsified).
* **Claimed Novelty**: First data-centric evaluation protocol pairing verifier-defined recovery states with prospectively matched reference control states using frozen structural covariates and append-only exposure ledgers.
* **Methodology**: Verifier-defined recovery state perturbations vs matched reference-control state evaluation; exposure governance ledger and BPE token provenance tracking.
* **Datasets**: GSM8K 20 prospectively isolated evaluation problems (400 genuine neural continuations).
* **Models**: `Qwen2.5-Math-1.5B` (Base vs Instruct checkpoints).
* **Experiments**: 400-rollout empirical continuation evaluation across matched recovery/control state pairs.
* **Baselines**: Unmatched recovery comparison, baseline Base checkpoint vs Instruct checkpoint.
* **Metrics**: Matched recovery-specific contrast $D_{\text{recovery}} = \mathbb{E}[V_{\pi}(s_R) - V_{\pi_0}(s_R)] - \mathbb{E}[V_{\pi}(s_C) - V_{\pi_0}(s_C)]$, 95% problem-level bootstrap CIs.
* **Primary Results**: Instruct checkpoint improved on both recovery ($+0.4300$) and control ($+0.5400$) states, yielding a matched recovery-specific contrast of $D_{\text{recovery}} = -0.1100$ ($95\% \text{ CI } [-0.240, +0.030]$).
* **Negative Findings**: Post-trained checkpoint accuracy gains do not translate into a detectable recovery-specific advantage; aggregate benchmark gains obscure state-specific behavior.
* **Limitations**: Evaluated on 20 GSM8K problems and Qwen2.5-Math 1.5B models.
* **Future Work Statements**: State-matched diagnostics across scaling axes.
* **Code Used**: `src/eval/matching.py`, `src/governance/ledger.py`
* **Data Used**: `data/matched_states.json`, `results/continuations.json`

---

## MANUSCRIPT 3: TMLR / NeurIPS Workshop Submission

* **Exact Title**: *Amortized Intervention Frontiers for Language-Model Reasoning: When Does Training Beat Search?*
* **Manuscript ID**: `TMLR-Sub-2026` / NeurIPS Workshop Submission
* **Venue**: *Transactions on Machine Learning Research (TMLR)* / NeurIPS Workshop
* **Current Status**: `Submitted / Under Review`
* **Submission Date**: August 2026
* **Associated Repository**: [`submission/tmlr`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission/tmlr) & [`submission_package`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_package)
* **Primary Research Question**: At what query volume $Q$ does up-front post-training (RLVR) amortize its training cost $C_{\text{train}}$ compared to inference-time search (Best-of-$N$), and how does compositional distribution shift alter the frontier crossover $Q^*_{\text{frontier}}$?
* **Hypotheses**: 
  - $H_1$: Compositional out-of-distribution (OOD) length extrapolation systematically shifts the deployment horizon crossover point $Q^*_{\text{frontier}}$ toward up-front training interventions ($R_f = Q^*_{\text{OOD}} / Q^*_{\text{IID}} < 1.0$). (Supported).
* **Claimed Novelty**: Formalization of Deployment-Amortized Intervention Frontiers ($Q^*_{\text{frontier}}$) trading off training compute against dynamic inference search volume $Q$ under distribution shift.
* **Methodology**: Total deployment cost modeling $C_{\text{total}}(a, Q) = C_{\text{train}}(a) + Q \cdot C_{\text{inference}}(a)$; multi-model RLVR training and Best-of-$N$ search sweeps; sensitivity analysis over protocol ceiling overruns.
* **Datasets**: `ModComp-3` (IID), `ModComp-5` (OOD Length Extrapolation), `ModComp-Recomb` (OOD Recombination).
* **Models**: `SmolLM2-360M-Instruct`, `Qwen2.5-0.5B-Instruct`, `TinyLlama-1.1B-Chat-v1.0` ($N=12$ trained models total across 2 RL seeds).
* **Experiments**: BO-N search ($N \in \{1..32\}$) vs LoRA-RLVR vs Full-parameter RLVR across IID and OOD tasks; protocol deviation sensitivity filtering (Dataset A vs Dataset B).
* **Baselines**: Base single-sample generation ($A_0$), Best-of-$N$ search ($A_1$), LoRA-RLVR ($A_2$).
* **Metrics**: $Q^*_{\text{cost}}$, $Q^*_{\text{utility}}$, Frontier Crossover Ratio $R_f = Q^*_{\text{OOD}} / Q^*_{\text{IID}}$, Execution MPS hours.
* **Primary Results**:
  - $R_f < 1.0$ observed across all 3 model families ($R_{\text{SmolLM2}} = 0.0632$, $R_{\text{Qwen}} = 0.0648$, $R_{\text{TinyLlama}} = 0.0576$; geometric mean $\bar{R}_f = 0.0618$).
  - Up-front RLVR amortizes training compute in $<100$ queries on OOD tasks vs $>1,200$ queries on IID tasks.
* **Negative Findings**: Best-of-$N$ search scaling rapidly becomes compute-inefficient under severe OOD length extrapolation compared to up-front RLVR.
* **Limitations**: Models $<1.5\text{B}$ parameters, synthetic modular arithmetic tasks, Apple Silicon MPS execution environment.
* **Future Work Statements**: Scaling frontier analysis to 7B+ parameter reasoning models.
* **Code Used**: `src/frontier/amortization.py`, `experiments/run_frontier_sweep.py`
* **Data Used**: `results/frontier_canonical.json`
