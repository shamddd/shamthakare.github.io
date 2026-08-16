# 20-Candidate Research Project Pool & Novelty Collision Matrix

**Author / Evaluator**: Sham Thakare (Senior ML Research Scientist & PhD Portfolio Strategist)  
**Date**: August 2026  
**Evaluation Scope**: 20 Fresh Candidate Research Projects across Reinforcement Learning, Foundation Models, Mechanistic Diagnostics, AI Reliability, and Autonomous Agent Systems.

---

## 1. Evaluation Methodology & Scoring Rubric

Each candidate project is evaluated against live 2024–August 2026 literature across NeurIPS, ICML, ICLR, ACL, EMNLP, JMLR, TMLR, IEEE TAI, and arXiv preprints.

### Scoring Weight Distribution (/100)
- **Novelty (25 pts)**: Originality of scientific question; absence of direct prior work; non-obvious hypothesis.
- **Scientific Importance (20 pts)**: Fundamental relevance to core bottlenecks in ML/RL/agents; depth of conceptual insight.
- **Experimental Rigor (15 pts)**: Quality of controls, baselines, statistical validity, and reproducibility.
- **Feasibility (10 pts)**: Executability within modest compute budgets ($\le 1\text{--}2$ GPUs; 0.5B–3B parameter models; public data).
- **Falsifiability (10 pts)**: Sharp, unambiguous negative gate criteria that can cleanly prove the hypothesis false.
- **Faculty Alignment (10 pts)**: Genuine intellectual intersection with active labs at Harvard, Stanford, and MIT.
- **Publication Potential (5 pts)**: Realistic path to top-tier conference or reputable journal (JMLR, TMLR, IEEE TAI/TPAMI/TCC).
- **Portfolio Complementarity (5 pts)**: Synergistic coherence with existing identity without duplicating prior repositories.

### Collision Classification
- 🟢 **GREEN**: High novelty, clear unresolved evidence gap, defensible contribution. Proceed to selection.
- 🟡 **YELLOW**: Partial overlap with emerging 2025/2026 preprints; requires sharp boundary definition and control isolation.
- 🔴 **RED**: Substantially solved or directly anticipated in recent literature. **Immediately eliminated**.

---

## 2. 20 Candidate Projects Inventory & Collision Audit

---

### CANDIDATE 01 [GREEN]
- **Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*
- **Frontier**: Frontier A (Long-Horizon Agent Credit Assignment)
- **Scientific Question**: In multi-turn agent interactions ($T \ge 20$ steps) with external tool environments, can an unsupervised counterfactual state ablation estimator isolate the true marginal contribution of intermediate tool invocations from stochastic environment noise, outperforming uniform trajectory advantage assignment?
- **Hypothesis**: Replacing uniform trajectory advantage weighting in GRPO with a counterfactual state-ablation credit estimator reduces policy gradient variance by $\ge 40\%$ and improves task completion on long-horizon tool execution without requiring external learned PRMs.
- **Mechanism**: At training time, for an execution trace containing $K$ tool calls, the algorithm computes counterfactual sub-trajectories by ablating/swapping individual tool return payloads with null/stale tokens, estimating the empirical Shapley contribution $\hat{\Phi}(a_t)$ of each turn to terminal success, and weighting step-level policy gradient updates by $\hat{\Phi}(a_t)$.
- **Closest Prior Work**:
  1. *Turn-level Credit Policy Optimization (TCPO)* (2025)
  2. *Hindsight Credit Assignment Policy Optimization (HCAPO)* (2025/2026)
  3. *Counterfactual Shapley Credit Assignment ($\phi$-PPO)* (2026)
  4. *PURE: Process sUpervised Reinforcement lEarning* (MIT, 2025)
- **Novelty Hypothesis**: Prior work either evaluated single-turn math with external PRMs or applied classical vector Shapley values in toy RL. C3A introduces a token-efficient, forward-pass-only ablation operator for non-differentiable multi-turn tool interaction environments without learned reward models.
- **Possible Falsification**: If step-level counterfactual ablation weighting yields zero improvement in sample efficiency or task pass rate over trajectory-uniform GRPO across 3 random seeds ($\Delta \le 1.0\%$), the hypothesis is falsified.
- **Dataset**: InterCode (SQL / Bash), ToolBench (subset of 500 multi-step API tasks), WebArena-Lite.
- **Models**: Qwen2.5-1.5B-Instruct, SmolLM-1.7B.
- **Baselines**: Standard Outcome GRPO, Step-Uniform PPO, Turn-Level TCPO, Random-Credit Control.
- **Controls**: Permuted-step credit control, compute-matched rollout control, oracle ablation baseline.
- **Metrics**: Task Pass@1, Tool Selection Precision, Gradient Variance ($\mathbb{E}[\|\nabla_\theta \mathcal{L}\|^2]$), Tool Call Redundancy Rate.
- **Compute Estimate**: 1 $\times$ NVIDIA A100 / RTX 4090 (approx. 24 GPU-hours).
- **Expected Duration**: 3–4 weeks.
- **Publication Class**: Top Conference / Journal (ICML/NeurIPS/TMLR/IEEE TAI).
- **Faculty Alignment**: Kianté Brantley (Harvard); Chelsea Finn / Dorsa Sadigh (Stanford); Pulkit Agrawal (MIT).
- **Collision Verdict**: 🟢 **GREEN** (High novelty, unaddressed agent tool credit gap).
- **Score**: **93 / 100** (Novelty 24, SciImp 19, Rigor 15, Feas 9, Falsif 10, FacAlign 9, Pub 4, PortComp 5).

---

### CANDIDATE 02 [GREEN]
- **Title**: *Representation Rank Collapse as an Unconfounded Indicator of Reasoning Breakdown in Transformer Deliberation*
- **Frontier**: Frontier H (Representation-Level Failure Indicators)
- **Scientific Question**: Does the effective rank and spectral decay of attention head projection matrices across intermediate transformer layers provide an unconfounded, length-invariant predictor of logical derivation breakdown in long reasoning chains, unlike token predictive entropy?
- **Hypothesis**: The effective spectral rank ($\text{erank}(\mathbf{H}_l) = \exp(-\sum_i \tilde{\sigma}_i \ln \tilde{\sigma}_i)$) of hidden activations in intermediate layers ($l \in [0.4L, 0.7L]$) exhibits a sharp contraction ($>35\%$ drop) prior to logical bifurcation into an error state, maintaining strong partial correlation with derivation error after controlling for sequence length ($|r(\text{Error} \mid \text{Length})| > 0.40, p < 0.001$).
- **Mechanism**: Caches hidden state activations $\mathbf{H}_l \in \mathbb{R}^{B \times d}$ during autoregressive deliberation. Computes singular value decomposition (SVD) across token chunks and layer depths. Tracks the layer-wise spectral entropy and participation ratio, comparing correct derivations against subtle error injections.
- **Closest Prior Work**:
  1. *When Confidence Proxies Confound Reasoning Complexity* (2026)
  2. *Attention Head Rank Collapse during Extended Deliberation* (2025)
  3. *Q-Probe: Lightweight Reward Maximization via Representation Probing* (Harvard, ICML 2024)
  4. *The Geometry of Latent Spaces in Reasoning Models* (Stanford, 2025/2026)
- **Novelty Hypothesis**: Demonstrates for the first time that while output token confidence metrics are heavily confounded with sequence length ($r \approx +0.49$), interior representation spectral rank isolates pure logical breakdown independently of derivation length.
- **Possible Falsification**: If partial correlation $r(\text{erank}, \text{Error} \mid \text{Length})$ is statistically indistinguishable from zero ($p > 0.05$) across GSM8K, MATH, and LogiQA, the hypothesis is falsified.
- **Dataset**: GSM8K ($N=500$), MATH Level 1–5 ($N=500$), LogiQA ($N=300$), synthetic length-balanced arithmetic.
- **Models**: Qwen2.5-0.5B-Instruct, Qwen2.5-Math-1.5B, DeepSeek-R1-Distill-Qwen-1.5B.
- **Baselines**: Token Predictive Entropy, Mean Token NLL, Logit Margin, Self-Consistency Consensus ($K=4$).
- **Controls**: Shuffled token activation control, random projection baseline, length-matched paired derivation control.
- **Metrics**: Error AUROC, Error AUPRC, Partial Pearson $r(\text{Metric}, \text{Error} \mid \text{Length})$, Early Warning Lead Time (tokens before syntax error).
- **Compute Estimate**: 1 $\times$ GPU (approx. 10 GPU-hours; forward-pass SVD analysis only).
- **Expected Duration**: 2–3 weeks.
- **Publication Class**: Top Conference / Theory/Diagnostic Track (ICLR/NeurIPS/JMLR/TMLR).
- **Faculty Alignment**: Sham Kakade / Boaz Barak (Harvard); Stefano Ermon / Chris Ré (Stanford); Phillip Isola / Aleksander Madry (MIT).
- **Collision Verdict**: 🟢 **GREEN** (Pioneering mechanistic diagnostic with rigorous length-confounding controls).
- **Score**: **95 / 100** (Novelty 25, SciImp 19, Rigor 15, Feas 10, Falsif 10, FacAlign 9, Pub 4, PortComp 5).

---

### CANDIDATE 03 [GREEN]
- **Title**: *Decentralized Tipping-Point Mitigation in Multi-Agent Reasoning Consensus: Phase Transitions and Epistemic Cascade Breakers*
- **Frontier**: Frontier G (Multi-Agent Emergent Failure)
- **Scientific Question**: Can decentralized epistemic diversity metrics detect the critical tipping point where multi-agent debate transitions from constructive deliberation to sycophantic consensus collapse, and can an asynchronous "cascade breaker" protocol restore collective accuracy?
- **Hypothesis**: Multi-agent reasoning debates exhibit a non-linear phase transition (tipping point) in consensus error as a function of peer confidence coupling and network clustering coefficient; an epistemic disagreement-gated intervention protocol halts cascading errors, increasing multi-agent task accuracy by $\ge 15\%$ over standard majority debate under adversarial fault injection.
- **Mechanism**: Models multi-agent debate as an opinion dynamics graph with dynamic edge weights modulated by internal representation uncertainty. When peer agreement outpaces internal verification confidence (high sycophancy risk score), the system triggers an asynchronous "devil's advocate" branch with orthogonal system priors.
- **Closest Prior Work**:
  1. *Improving Factuality in LLMs through Multiagent Debate* (Harvard/MIT, ICML 2024)
  2. *Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate* (2025)
  3. *Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate* (2025/2026)
  4. *AdaptiveReplica / QuorumShift* (2026)
- **Novelty Hypothesis**: Formalizes the phase transition boundary of multi-agent debate collapse using statistical mechanics tools and introduces a decentralized, non-hierarchical cascade-breaker protocol that requires no trusted central oracle.
- **Possible Falsification**: If the cascade-breaker protocol fails to outperform standard majority voting under both benign and 20% Byzantine/adversarial agent corruption across 5 random seeds, the hypothesis is falsified.
- **Dataset**: StrategyQA, GSM8K, Multi-Agent Logic Benchmark (M-LogicBench), Fault-Injected Debate Suite.
- **Models**: 3–7 heterogeneous agents using Qwen2.5-0.5B, SmolLM-1.7B, Llama-3.2-1B.
- **Baselines**: Standard Multi-Agent Debate (Du et al., 2024), Majority Voting, Centralized Leader Orchestration (HACN), Static Random Interventions.
- **Controls**: Shuffled agent communication topology, confidence-blind debate baseline, homogeneous model control.
- **Metrics**: Collective Accuracy, Sycophancy Collapse Rate, Consensus Entropy, Communication Token Overhead.
- **Compute Estimate**: 1 $\times$ GPU (approx. 14 GPU-hours; batched multi-agent inference).
- **Expected Duration**: 3 weeks.
- **Publication Class**: Top Conference / Systems/AI Journal (AAMAS/ICML/NeurIPS/IEEE TAI).
- **Faculty Alignment**: Yilun Du / David Parkes (Harvard); Dorsa Sadigh / Percy Liang (Stanford); Asuman Ozdaglar (MIT).
- **Collision Verdict**: 🟢 **GREEN** (Rigorous systems/scientific synthesis bridging distributed consensus and multi-agent AI).
- **Score**: **91 / 100** (Novelty 23, SciImp 18, Rigor 15, Feas 10, Falsif 9, FacAlign 9, Pub 4, PortComp 5).

---

### CANDIDATE 04 [YELLOW]
- **Title**: *Epistemically Calibrated Model-Based Planning: Intrinsic Forward-Pass Energy Probes for World-Model Reliability*
- **Frontier**: Frontier B (World-Model Reliability)
- **Scientific Question**: Can forward-pass energy scores in generative world models detect out-of-distribution state transitions before executing MCTS tree rollouts?
- **Hypothesis**: Free-energy scoring over intermediate layer activations detects invalid environment state transitions with AUROC $> 0.85$, preventing world-model hacking in model-based RL.
- **Closest Prior Work**: *DreamZero* (Harvard/MIT, 2026), *Q-Probe* (Harvard, 2024), *Energy-based OOD Detection* (2025).
- **Collision Analysis**: Energy scoring for out-of-distribution detection is well established; adapting it to world action models has strong overlap with recent Berkeley/Stanford 2026 preprints.
- **Verdict**: 🟡 **YELLOW** (High potential, but needs sharper differentiation from standard energy OOD baselines).
- **Score**: **82 / 100**.

---

### CANDIDATE 05 [YELLOW]
- **Title**: *Null-Space Policy Gradient Surgery for Preventing Catastrophic Plasticity Loss in Multi-Distribution RLVR*
- **Frontier**: Frontier F (Distribution-Shift-Aware Post-Training)
- **Scientific Question**: Can projecting mathematical RLVR policy gradients onto the orthogonal null-space of pre-training Fisher representations preserve out-of-domain linguistic and factual capabilities?
- **Hypothesis**: Projecting GRPO updates into the null space of the top-k Fisher eigenvectors bounds non-target benchmark degradation to $< 2\%$ while retaining $> 90\%$ of target math reasoning gains.
- **Closest Prior Work**: *Training Language Models That Can Continue to Learn* (Harvard/Kempner, ICML 2026), *Gradient Surgery for Multi-Task Learning* (2023).
- **Collision Analysis**: Subspace gradient projection is heavily explored in multi-task learning; computing full Fisher null spaces in online RL is computationally expensive.
- **Verdict**: 🟡 **YELLOW** (Substantial conceptual overlap with Kakade et al. ICML 2026).
- **Score**: **84 / 100**.

---

### CANDIDATE 06 [RED - ELIMINATED]
- **Title**: *De-Biasing Binary Rewards in GRPO Pipelines via Noise Matrix Inversion*
- **Frontier**: Frontier E (Verifier Reliability)
- **Scientific Question**: Can binary verifier noise be corrected using forward-backward transition matrices in GRPO?
- **Closest Prior Work**: *De-biasing Binary Rewards in GRPO Pipelines* (2026), *Backward and Forward Reward Correction for GRPO* (2026).
- **Collision Analysis**: Directly anticipated and published in early 2026 preprints with identical mathematical formulations.
- **Verdict**: 🔴 **RED (Direct Prior-Art Collision — ELIMINATED)**.

---

### CANDIDATE 07 [YELLOW]
- **Title**: *Causal Provenance-Guided Working Memory Eviction for 100-Turn Autonomous Agent Contexts*
- **Frontier**: Frontier D (Agent Memory Reliability)
- **Scientific Question**: Does causal dependency graph eviction outperform sliding-window and vector RAG in preserving long-horizon execution state?
- **Closest Prior Work**: *MemGPT* (2024), *Breadcrumbs* (Harvard, 2025), *TraceMind* (2026).
- **Collision Analysis**: Overlaps with the candidate's own `tracemind` dependency DAGs and Harvard's *Breadcrumbs* (2025). Needs substantial redesign to avoid self-overlap.
- **Verdict**: 🟡 **YELLOW** (Overlaps with candidate's existing portfolio boundary).
- **Score**: **79 / 100**.

---

### CANDIDATE 08 [YELLOW]
- **Title**: *Test-Time Contrastive Gradient Adaptation without Ground-Truth Verifiers via Latent Consistency Regularization*
- **Frontier**: Frontier C (Test-Time Learning)
- **Scientific Question**: Can unsupervised latent consistency loss update weights at test time without reward hacking?
- **Closest Prior Work**: *Test-Time Training with Diffusion Models* (Stanford, 2025), *Self-Play Fine-Tuning* (2024).
- **Verdict**: 🟡 **YELLOW** (Borderline stability in small models; high risk of degenerative attractor collapse).
- **Score**: **76 / 100**.

---

### CANDIDATE 09 [GREEN]
- **Title**: *Adaptive Sibling Advantage Normalization for Heterogeneous Stochastic Tool Action Spaces in GRPO*
- **Frontier**: Frontier A (Credit Assignment / RLVR)
- **Scientific Question**: How does group advantage normalization skew exploration when rollouts invoke tools with non-stationary latencies and failure rates?
- **Verdict**: 🟢 **GREEN** (Novel mathematical formulation for stochastic tool-use RL).
- **Score**: **87 / 100**.

---

### CANDIDATE 10 [GREEN]
- **Title**: *Disentangling Mechanistic Deliberation from Autoregressive Mimicry via Latent State Activation Patching in Long-CoT Models*
- **Frontier**: Frontier H (Representation Dynamics)
- **Scientific Question**: Are reflection tokens causally necessary for downstream reasoning correction or merely superficial stylistic cues?
- **Verdict**: 🟢 **GREEN** (Clear causal mediation methodology).
- **Score**: **89 / 100**.

---

### CANDIDATE 11 [RED - ELIMINATED]
- **Title**: *World Action Models as Zero-Shot Decision Policies in Video Environments*
- **Frontier**: Frontier B (World Models)
- **Closest Prior Work**: *DreamZero: World Action Models are Zero-shot Policies* (Harvard/MIT, 2026), *Large Video Planner* (2026).
- **Collision Analysis**: Direct duplicate of Yilun Du's 2026 papers *DreamZero* and *Large Video Planner*.
- **Verdict**: 🔴 **RED (Direct Duplicate of Published Faculty Work — ELIMINATED)**.

---

### CANDIDATE 12 [YELLOW]
- **Title**: *Bayesian Belief Revision and Dynamic Trust Decay in Untrusted Agent Memory Stores*
- **Frontier**: Frontier D (Agent Memory Governance)
- **Closest Prior Work**: *Memory Poisoning Attacks against LLM Agents* (2025), *AgentGuard* (2026).
- **Verdict**: 🟡 **YELLOW** (High overlap with `agentguard-final` provenance rules).
- **Score**: **78 / 100**.

---

### CANDIDATE 13 [YELLOW]
- **Title**: *Dynamic Bayes-Risk Hybridization of Outcome Verification and Process Supervision in Reinforcement Learning*
- **Frontier**: Frontier E (Verifier Reliability)
- **Closest Prior Work**: *TCPO* (2025), *VeriGate* (2025/2026), *ARW* (2026).
- **Verdict**: 🟡 **YELLOW** (Moderate overlap with emerging multi-verifier weighting papers).
- **Score**: **83 / 100**.

---

### CANDIDATE 14 [GREEN]
- **Title**: *Adversarial Property-Based Fuzzing in the RLVR Inner Loop to Invalidate Reasoning Specification Gaming*
- **Frontier**: Frontier E (Verifier Robustness)
- **Scientific Question**: Can dynamic fuzzing environments eliminate unit-test hardcoding in code generation RLVR?
- **Verdict**: 🟢 **GREEN** (Strong algorithmic contribution to verifiable RL).
- **Score**: **88 / 100**.

---

### CANDIDATE 15 [GREEN]
- **Title**: *Spectral Fisher Information Decay across Layer Depth during Long-Horizon Generation*
- **Frontier**: Frontier H (Theory/Diagnostics)
- **Scientific Question**: Does the empirical Fisher rank decay along generation depth during multi-thousand token reasoning?
- **Verdict**: 🟢 **GREEN** (Extends pre-training Fisher theory into inference generation dynamics).
- **Score**: **88 / 100**.

---

### CANDIDATE 16 [YELLOW]
- **Title**: *Semantic Byzantine Fault Tolerance in Collaborative Agentic Reasoning Networks*
- **Frontier**: Frontier G (Multi-Agent Systems)
- **Closest Prior Work**: *Byzantine-Robust Federated Learning* (2024), *EnclaveShield / AdaptiveReplica* (2026).
- **Verdict**: 🟡 **YELLOW** (Overlaps partially with candidate's `quorumshift` distributed consensus framing).
- **Score**: **80 / 100**.

---

### CANDIDATE 17 [YELLOW]
- **Title**: *Continual Tool Schema Learning via Isolated Orthogonal Adapter Routing*
- **Frontier**: Frontier C (Continual Learning)
- **Closest Prior Work**: *Modular Continual Learning* (2025), *ToolBench* (2024).
- **Verdict**: 🟡 **YELLOW** (Engineering-heavy; lower foundational ML insight).
- **Score**: **77 / 100**.

---

### CANDIDATE 18 [GREEN]
- **Title**: *Decontaminated Isomorphic Graph Generation for Ground-Truth Reasoning Policy Generalization*
- **Frontier**: Frontier F (Evaluation Methodology)
- **Scientific Question**: Can programmatic isomorphic graph transformations prove whether RLVR learns general algorithms vs memorized templates?
- **Verdict**: 🟢 **GREEN** (High methodological and evaluation rigor).
- **Score**: **86 / 100**.

---

### CANDIDATE 19 [RED - ELIMINATED]
- **Title**: *Prefix Linear Probing for Fast Early-Exit LLM Reward Maximization*
- **Frontier**: Frontier H (Efficiency / Probing)
- **Closest Prior Work**: *Q-Probe: A Lightweight Approach to Reward Maximization for Language Models* (Harvard, ICML 2024).
- **Collision Analysis**: Direct replication of Kakade et al.'s *Q-Probe* (ICML 2024).
- **Verdict**: 🔴 **RED (Direct Prior-Art Collision — ELIMINATED)**.

---

### CANDIDATE 20 [RED - ELIMINATED]
- **Title**: *Distributional Constraints by Inference Programming in Manager-Worker Agent Teams*
- **Frontier**: Frontier G (Multi-Agent Architectures)
- **Closest Prior Work**: *DisCIPL: Distributional Constraints by Inference Programming with Language Models* (MIT, 2025).
- **Collision Analysis**: Direct overlap with MIT's *DisCIPL* framework (2025).
- **Verdict**: 🔴 **RED (Direct Prior-Art Collision — ELIMINATED)**.

---

## 3. Summary Scoring & Project Selection Matrix

```
========================================================================================================================
ID    CANDIDATE TITLE                                           STATUS     SCORE /100  SELECTION OUTCOME
========================================================================================================================
01    Causal Counterfactual Credit Assignment (C3A)             🟢 GREEN   93 / 100    SELECTED -> PROJECT A (FLAGSHIP)
02    Representation Rank Collapse as Error Indicator           🟢 GREEN   95 / 100    SELECTED -> PROJECT B (THEORY/DIAGNOSTIC)
03    Decentralized Tipping-Point Mitigation in Multi-Agent     🟢 GREEN   91 / 100    SELECTED -> PROJECT C (SYSTEMS/AGENTS)
04    Epistemically Calibrated Model-Based Planning             🟡 YELLOW  82 / 100    Reserve
05    Null-Space Policy Gradient Surgery                        🟡 YELLOW  84 / 100    Reserve
06    De-Biasing Binary Rewards in GRPO Pipelines               🔴 RED     --          ELIMINATED (Published Collision)
07    Causal Provenance Working Memory Eviction                 🟡 YELLOW  79 / 100    Reserve (Portfolio Boundary Overlap)
08    Test-Time Contrastive Gradient Adaptation                 🟡 YELLOW  76 / 100    Reserve
09    Adaptive Sibling Advantage Normalization                  🟢 GREEN   87 / 100    High-ranking Alternative
10    Disentangling Deliberation from Mimicry                   🟢 GREEN   89 / 100    High-ranking Alternative
11    World Action Models as Zero-Shot Policies                 🔴 RED     --          ELIMINATED (Duplicate of DreamZero)
12    Bayesian Belief Revision in Memory Stores                 🟡 YELLOW  78 / 100    Reserve (AgentGuard Overlap)
13    Dynamic Bayes-Risk Hybridization of Verifiers             🟡 YELLOW  83 / 100    Reserve
14    Adversarial Property-Based Fuzzing in RLVR                🟢 GREEN   88 / 100    High-ranking Alternative
15    Spectral Fisher Information Decay across Depth            🟢 GREEN   88 / 100    High-ranking Alternative
16    Semantic Byzantine Fault Tolerance                        🟡 YELLOW  80 / 100    Reserve (QuorumShift Overlap)
17    Continual Tool Schema Learning with Adapters              🟡 YELLOW  77 / 100    Reserve
18    Decontaminated Isomorphic Graph Generation                🟢 GREEN   86 / 100    High-ranking Alternative
19    Prefix Linear Probing for Fast Early-Exit                 🔴 RED     --          ELIMINATED (Duplicate of Q-Probe)
20    Distributional Constraints in Manager-Worker Teams        🔴 RED     --          ELIMINATED (Duplicate of DisCIPL)
========================================================================================================================
```

---

## 4. Final 3-Project Selection

1. **PROJECT A — FLAGSHIP (Deep ML / RL / Foundation-Model Research)**:
   **Candidate 01**: *Causal Counterfactual Credit Assignment (C3A) for Multi-Turn Tool-Using Foundation Agents*
   - Target: Potential top ML conference/journal (*ICML / NeurIPS / TMLR / JMLR / IEEE TAI*).

2. **PROJECT B — THEORY / DIAGNOSTIC (Mechanistic, Measurement & Diagnostic Probing)**:
   **Candidate 02**: *Representation Rank Collapse as an Unconfounded Indicator of Reasoning Breakdown in Transformer Deliberation*
   - Target: Potential top ML conference/journal (*ICLR / NeurIPS / JMLR / TMLR*).

3. **PROJECT C — SYSTEMS / AGENTS (Fault-Tolerant Multi-Agent Coordination & Consensus)**:
   **Candidate 03**: *Decentralized Tipping-Point Mitigation in Multi-Agent Reasoning Consensus: Phase Transitions and Epistemic Cascade Breakers*
   - Target: Potential top AI systems conference/journal (*AAMAS / ICML / IEEE TAI / ACM TIST*).
