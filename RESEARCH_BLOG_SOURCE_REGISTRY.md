# Research Blog Source Registry

**Author**: Sham Satish Thakare  
**Research Theme**: Reliable Adaptive Intelligent Systems  
**Last Verified Date**: August 21, 2026  

---

## Portfolio Summary Matrix

| ID | Project Name | Paper Title | Status | Venue / ID | Primary Research Area | Verified Key Finding |
|---|---|---|---|---|---|---|
| **P1** | `ear_grpo_reasoning` | *Estimator Validity, Reasoning Complexity, and Negative-Control Protocols for Uncertainty-Weighted Credit Assignment in RLVR Post-Training* | **Submitted** | IEEE TAI (TAI-2026-Aug-A-01878) | LLM Reasoning, RL, Uncertainty & Calibration | Token predictive entropy correlates with sequence length ($r=+0.486$), collapsing to $p=0.365$ under partial correlation; CA-GRPO shows $d=0.00$ over standard GRPO online. |
| **P2** | `MediRush-SafeAgent` | *MediRush-SafeAgent: A Policy-Constrained Multi-Stage Defense Framework for Reliable Healthcare-Commerce LLM Tool Execution* | **Submitted** | Elsevier AIIM (ARTINT-S-26-02059) | AI Agent Reliability, Tool Safety, Policy Enforcement | Multi-stage runtime interception achieves $STCR=100.0\%$, $PVR=0.0\%$ on 24-scenario benchmark. |
| **P3** | `recovery_eval` | *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning* | **Submitted** | IEEE BigData 2026 (BigD497) | Reasoning Evaluation, Causal Observability | State-matched continuation evaluation isolates true error recovery delta ($D_{\text{recovery}} = -0.1100$). |
| **P4** | `CARLS / StateShift` | *When Should Language Models Learn from Reinforcement? Predicting Plasticity and Adaptively Scheduling Reinforcement Learning During Foundation-Model Training* | **Submitted** | JMLR (MS#: 262622(1)) | Adaptive Computation, RL, Foundation Model Pre-training | Gradient alignment ($r=0.838$) and entropy ($r=0.744$) predict RL plasticity zero-shot ($R^2=0.7632$ on distilgpt2); CARLS saves 18.7% FLOPs. |
| **P5** | `quorumshift` | *Failure-Domain Aware Consensus Quorum Adaptation* | **Spec / WIP** | USENIX NSDI Track | Distributed Systems, Reliable Intelligent Infrastructure | Reliability trust gating eliminates false fallback in Q3 and prevents 80.99 ms p99 tail-latency regret in Q4 under network shift. |
| **P6** | `Diabetes_ML` | *Diabetes Prediction Using Machine Learning* | **Published** | IJNRD Vol 9 Issue 5 (IJNRD2404398) | Machine Learning, Healthcare Classification | Random Forest achieved highest classification accuracy among 6 evaluated classifiers on Pima dataset. |
| **P7** | `SCRE-Align` | *Self-Correcting Reasoning Engine Framework* | **Codebase** | Open-Source Framework | LLM Alignment, PRMs, MCTS | Modular PRM and DPO step-trainer for tree-search guided self-correction. |
| **P8** | `Boomerang / SSM` | *Boomerang Distillation & SSM Copying Benchmarks* | **Repo / Reference** | ICLR / arXiv References | Model Compression, State Space Models | Layer-stitching zero-shot model size interpolation and Mamba vs Transformer copy evaluation. |

---

## Detailed Project Entries

### Project 1: `ear_grpo_reasoning` (Flagship Selection)
* **Project Name**: `01_IEEE_TAI_2026` / `ear_grpo_reasoning`
* **Exact Paper Title**: *Estimator Validity, Reasoning Complexity, and Negative-Control Protocols for Uncertainty-Weighted Credit Assignment in RLVR Post-Training*
* **Research Area**: LLM Reasoning, Reinforcement Learning, Uncertainty & Calibration, Credit Assignment
* **Publication / Submission Status**: **Submitted** (IEEE Transactions on Artificial Intelligence, Paper ID: `TAI-2026-Aug-A-01878`)
* **Primary Research Question**: Does trajectory-level uncertainty weighting improve online Group Relative Policy Optimization (GRPO) for reasoning LLMs, or are internal token confidence proxies confounded by reasoning complexity?
* **Core Hypotheses**:
  1. *Architectural Validity ($C1$)*: MC-dropout uncertainty probing produces mathematically deterministic passes ($\text{Var}(\log P) = 0.0$) on zero-dropout architectures.
  2. *Diagnostic Validity ($C2$)*: Token-level predictive entropy correlates with sequence length ($r=+0.486$) rather than true error. Controlling for length collapses the association ($r_{\text{partial}}=-0.092, p=0.365$).
  3. *Algorithmic Validity ($C3$)*: Validated offline error predictors (Self-Consistency) do not causally improve online GRPO policy updates over standard outcome-supervised baselines ($d=0.00$).
* **Dataset(s)**: GSM8K ($N=100$ prompt clusters, 98 degrees of freedom), SVAMP
* **Model/System**: Qwen/Qwen2.5-0.5B-Instruct
* **Baselines**: Standard GRPO ($K=4$), Compute-Matched GRPO ($K=8$), Random-Weight Control, Permuted-Consistency Control
* **Experimental Scale**: $N=3$ independent training seeds, 256-token generation budget, $K=4$ and $K=8$ rollout groups.
* **Main Metric(s)**: Group Pass@1 (%), Train Reward, AUROC, Pearson correlation $r$, Partial correlation $r_{\text{partial}}$, Cohen's $d$.
* **Verified Findings**:
  - MC-dropout on zero-dropout model: $\text{Var}(\log P) = 0.0000000000$, $\cos(\Delta\theta) = 1.000000$.
  - Token Predictive Entropy correlates with sequence length ($r = +0.486, 95\%\text{ CI } [+0.318, +0.627]$) and equation count ($r = +0.421$).
  - Partial correlation controlling for length collapses token entropy association from $r = -0.214$ to $r_{\text{partial}} = -0.092$ ($p = 0.365$).
  - Stress Test: Token entropy misidentifies correct multi-step reasoning traces as more uncertain than short incorrect errors in 42.1% of paired comparisons.
  - Self-Consistency ($K=4$): Robust to length ($r=+0.114$, $r_{\text{partial}}=-0.569, p=8.1\times 10^{-10}$, $\text{AUROC}=0.812$).
  - Consistency-Aware GRPO (CA-GRPO): Group Pass@1 $= 80.00\% \pm 0.00\%$ matching Standard GRPO ($80.00\% \pm 0.00\%$) and Permuted Control ($80.00\% \pm 0.00\%$), with Cohen's $d = 0.00$.
* **Main Limitation**: Evaluated on $N=3$ seeds, focused on math reasoning (GSM8K/SVAMP) with Qwen2.5-0.5B-Instruct, tests specific advantage weighting formulas.
* **Manuscript Location**: [TAI-2026-Aug-A-01878_Main_Manuscript.pdf](file:///Users/shamthakare/Downloads/filewhen/TAI-2026-Aug-A-01878_Main_Manuscript.pdf)
* **Code Location**: [ear_grpo_reasoning scripts](file:///Users/shamthakare/Downloads/filewhen/)
* **Results Location**: [FINAL_CANONICAL_RESULTS.json](file:///Users/shamthakare/Downloads/filewhen/)
* **Figure Assets**: `hero-concept.svg`, `assumption-vs-reality.svg`, `zero-dropout-audit.svg`, `experiment-pipeline.svg`, `correlation-length-entropy.svg`, `auroc-benchmark.svg`, `rl-control-results.svg`, `stress-test-failure.svg`, `limitations-boundary.svg`
* **GitHub URL**: `https://github.com/shamddd/ear_grpo_reasoning`
* **Public Paper URL**: `https://shamddd.github.io/shamthakare.github.io/papers/ear-grpo.html`

---

### Project 2: `MediRush-SafeAgent`
* **Project Name**: `02_Elsevier_AI_in_Medicine_MediRush` / `medirush`
* **Exact Paper Title**: *MediRush-SafeAgent: A Policy-Constrained Multi-Stage Defense Framework for Reliable Healthcare-Commerce LLM Tool Execution*
* **Research Area**: AI Agent Reliability, Tool-Use Safety, Policy Enforcement, Healthcare AI
* **Publication / Submission Status**: **Submitted** (*Artificial Intelligence in Medicine*, Elsevier, Manuscript: `ARTINT-S-26-02059`)
* **Primary Research Question**: How to guarantee policy-constrained, authorized, and reliable tool execution for LLM agents in healthcare-commerce workflows under prompt injection and unauthorized user attempts?
* **Core Hypothesis**: Multi-stage runtime interception (pre-execution domain policy engine + scope authorization + post-execution state verifier + dynamic human escalation) guarantees zero policy violations without sacrificing task completion.
* **Dataset(s) / Benchmark**: MediRushBench (24 standardized scenarios across 12 operational & security categories)
* **Model/System**: MediRush-SafeAgent
* **Baselines**: Unconstrained LLM Agent, Prompt-Guardrail LLM Agent
* **Main Metric(s)**: Safe Task Completion Rate ($STCR$), Policy Violation Rate ($PVR$), Unauthorized Tool Interception Rate ($UTIR$)
* **Verified Findings**:
  - MediRush-SafeAgent: $STCR = 100.0\%$, $PVR = 0.0\%$.
  - Unconstrained LLM Baseline: $STCR = 83.33\%$, $UTIR = 16.67\%$.
  - Prompt-Guardrail Baseline: $STCR = 95.83\%$.
* **Main Limitation**: Rules engine tailored to structured healthcare-commerce schemas; requires domain policy definition.
* **Manuscript Location**: [manuscript.pdf](file:///Users/shamthakare/Desktop/Submitted_Journals_and_Conferences_Package/02_Elsevier_AI_in_Medicine_MediRush/manuscript.pdf)
* **Code Location**: `/Users/shamthakare/.gemini/antigravity/scratch/medirush/`
* **GitHub URL**: `https://github.com/shamddd/medirush-safeagent`
* **Public Paper URL**: `https://shamddd.github.io/shamthakare.github.io/papers/medirush.html`

---

### Project 3: `recovery_eval`
* **Project Name**: `03_IEEE_BigData_2026` / `recovery_eval`
* **Exact Paper Title**: *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning*
* **Research Area**: LLM Reasoning, Causal Observability, Evaluation & Reliability
* **Publication / Submission Status**: **Submitted** (11th IEEE Special Session on Machine Learning on Big Data / IEEE BigData 2026, Paper ID: `BigD497`)
* **Primary Research Question**: How can we causally evaluate whether language models recover from intermediate reasoning errors using state-matched continuation interventions?
* **Core Hypothesis**: Unmatched continuation evaluations conflate distribution drift with error recovery capacity; state-matched contrastive rollouts isolate true recovery.
* **Dataset(s)**: GSM8K, MATH reasoning traces
* **Model/System**: recovery_eval framework
* **Main Metric(s)**: State-contrast recovery metric $D_{\text{recovery}} = -0.1100$.
* **Verified Findings**: Demonstrates that models exhibit significantly lower error recovery ($D_{\text{recovery}} = -0.1100$) when controlling for state covariates than naive rollout evaluation suggests.
* **Manuscript Location**: [Paper Submission bigdata.pdf](file:///Users/shamthakare/Desktop/Submitted_Journals_and_Conferences_Package/03_IEEE_BigData_2026/Paper%20Submission%20bigdata.pdf)
* **Code Location**: `https://github.com/shamddd/recovery_eval`
* **Public Paper URL**: `https://shamddd.github.io/shamthakare.github.io/papers/recovery-eval.html`

---

### Project 4: `CARLS / StateShift`
* **Project Name**: `04_JMLR_StateShift` / `05_RL_Foundation_Models_Plasticity`
* **Exact Paper Title**: *When Should Language Models Learn from Reinforcement? Predicting Plasticity and Adaptively Scheduling Reinforcement Learning During Foundation-Model Training*
* **Research Area**: Adaptive Computation, Reinforcement Learning, Foundation Model Optimization
* **Publication / Submission Status**: **Submitted / Working Paper** (Journal of Machine Learning Research, JMLR MS#: `262622(1)`)
* **Primary Research Question**: Can pre-RL state signals predict RL plasticity across intermediate checkpoints, and can compute be dynamically scheduled among NTP, SFT, and RL objectives?
* **Core Hypothesis**: Pre-RL gradient alignment $\cos(\mathbf{g}_{\text{NTP}}, \mathbf{g}_{\text{RL}})$ ($r=0.838, p<10^{-16}$) and policy entropy ($r=0.744, p<10^{-11}$) predict subsequent RL gains before compute expenditure; CARLS dynamic controller improves compute efficiency.
* **Dataset(s)**: Arithmetic, Logic, Code reasoning tasks
* **Model/System**: SmolLM-135M (predictive model), distilgpt2 (zero-shot transfer evaluation)
* **Baselines**: Standard Sequential NTP $\to$ SFT $\to$ RL training pipeline
* **Main Metric(s)**: Zero-shot $R^2$, Spearman $\rho$, Pass@4 (%), Capability retention score, Training FLOPs reduction (%)
* **Verified Findings**:
  - Linear model trained on SmolLM-135M predicts RL plasticity zero-shot on distilgpt2 ($R^2 = 0.7632$, Spearman $\rho = 0.8247$).
  - CARLS achieves superior compute-normalized performance (64.04% Pass@4 vs 56.46% sequential) and capability retention (0.94 vs 0.85) while saving 18.7% training FLOPs.
* **Manuscript Location**: [main.pdf](file:///Users/shamthakare/Desktop/Submitted_Journals_and_Conferences_Package/05_RL_Foundation_Models_Plasticity/main.pdf)
* **Code Location**: `https://github.com/shamddd/carls-plasticity`
* **Public Paper URL**: `https://shamddd.github.io/shamthakare.github.io/papers/rl-plasticity.html`

---

### Project 5: `quorumshift`
* **Project Name**: `06_USENIX_NSDI_Track` / `quorumshift`
* **Exact Paper Title**: *Failure-Domain Aware Consensus Quorum Adaptation (quorumshift)*
* **Research Area**: Distributed Systems, Reliable Intelligent Infrastructure, Verification
* **Publication / Submission Status**: **Specification Package / Work in Progress** (USENIX NSDI Track)
* **Primary Research Question**: Under nonstationary network conditions, can predictive uncertainty distinguish harmful adaptive-consensus decisions from benign distribution shift better than input-distance OOD gating?
* **Core Hypothesis**: Decision-reliability trust gating preserves adaptive quorum tail-latency benefits under OOD-but-reliable states (Q3) and prevents false adoption in ID-looking-but-harmful states (Q4).
* **Dataset(s)**: Telemetry sweeps, 5-node containerized Raft execution testbed
* **Model/System**: `quorumshift` (C++20 dynamic Raft consensus controller)
* **Baselines**: Static Raft, Input-Distance OOD Gating ($T2$)
* **Main Metric(s)**: Tail latency regret (ms), Missed failure rate (%), Throughput (ops/s)
* **Verified Findings**:
  - Q3 simulator: $T2$ false fallback 50% vs $T3$ (predictive reliability) 0% over 20 independent seeds.
  - Q4 simulator: $T2$ missed failure 100% (+80.99 ms p99 regret) vs $T3$ 0% missed failure and 0 ms regret over 20 seeds.
  - 5-node containerized Raft testbed: $T3$ improved throughput from 58.5 to 64.2 ops/s.
* **Manuscript Location**: [RESEARCH_CONTRIBUTION_SPEC.md](file:///Users/shamthakare/Desktop/Submitted_Journals_and_Conferences_Package/06_USENIX_NSDI_Track/RESEARCH_CONTRIBUTION_SPEC.md)
* **Code Location**: `/Users/shamthakare/.gemini/antigravity/scratch/quorumshift/`
* **Public Paper URL**: `https://shamddd.github.io/shamthakare.github.io/papers/quorumshift.html`

---

### Project 6: `Diabetes_ML`
* **Project Name**: `07_IJNRD_Diabetes_ML`
* **Exact Paper Title**: *Diabetes Prediction Using Machine Learning*
* **Research Area**: Machine Learning, Healthcare Classification
* **Publication / Submission Status**: **Peer-Reviewed & Published** (*International Journal of Novel Research and Development*, Vol 9 Issue 5, June 2024, Paper ID: `IJNRD2404398`)
* **Primary Research Question**: Which machine learning classification and ensemble technique achieves highest accuracy for early diabetes prediction?
* **Dataset(s)**: Pima Indians Diabetes Dataset
* **Model/System**: Random Forest, Gradient Boosting, Decision Tree, SVM, KNN, Logistic Regression
* **Verified Findings**: Random Forest ensemble classifier achieved highest predictive accuracy among tested models.
* **Manuscript Location**: [IJNRD2404398 Sham thakare.pdf](file:///Users/shamthakare/Desktop/Submitted_Journals_and_Conferences_Package/07_IJNRD_Diabetes_ML/IJNRD2404398%20Sham%20thakare.pdf)
* **Public Paper URL**: Published (IJNRD, June 2024)

---

### Project 7: `SCRE-Align`
* **Project Name**: `08_SCRE_Align_Framework` / `scre-align`
* **Exact Paper Title**: *Self-Correcting Reasoning Engine (SCRE-Align Framework)*
* **Research Area**: LLM Alignment, Process Reward Models (PRMs), Step-DPO, MCTS Verification
* **Publication / Submission Status**: **Open-Source Codebase / Framework**
* **Primary Research Question**: How can process reward models and step-level DPO be integrated into Monte Carlo Tree Search for self-correcting LLM reasoning?
* **Code Location**: [scre-align](file:///Users/shamthakare/Desktop/scre-align/)

---

### Project 8: `Boomerang / SSM` (Reference & Prior Work)
* **Project Name**: `boomerang-distillation` & `transformers_ssm_copy`
* **Research Area**: Model Compression, State Space Models vs Transformers, Sequence Copying
* **Publication / Submission Status**: **Reference Repositories** (ICLR 2026 / arXiv:2402.01032)
* **Code Location**: `/Users/shamthakare/boomerang-distillation`, `/Users/shamthakare/transformers_ssm_copy`
