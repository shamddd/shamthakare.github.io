# TOP 3 RESEARCH FLAGSHIP CANDIDATES (AUDITED PORTFOLIO)

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## CANDIDATE 1: INTERVENTION EFFICIENCY FRONTIERS UNDER MATCHED COMPUTE

* **Precise Question**: Under strictly matched total compute budgets $C_{\text{total}}(Q) = C_{\text{train}} + Q \cdot C_{\text{inference}}$, where does increasing parameter intervention capacity ($A_0 \to A_5$) yield Out-of-Distribution reasoning generalization ($D_{\text{OOD}}$) that cannot be matched by Best-of-$N$ verifier search ($A_1$) or low-dimensional prefix steering ($A_3$)?
* **Closest Three Papers**:
  1. *SAGE* (Lee et al., May 2026; `arXiv:2605.18864`)
  2. *Echo Chamber* (Zhao et al., COLM 2025; `arXiv:2411.07643`)
  3. *Parameter-Efficient RL (PERL)* (Zhang et al., ICLR 2026; `arXiv:2403.10704`)
* **Remaining Distinction**: Constructs the complete Pareto frontier across parameter intervention levels ($A_0 \to A_5$) parameterised by query volume $Q$ and evaluated on compositional OOD rule generalization ($D_{\text{OOD}}$) under strict FLOP matching.
* **Falsifiable Hypothesis**: $H_1$: For query volumes $Q > 10^4$, parameter-efficient RLVR ($A_3$) achieves higher OOD compositional accuracy than Best-of-$N$ ($A_1$) under equal total FLOPs, but Full RLVR ($A_5$) provides zero non-redundant gain over $A_3$.
* **Smallest Kill Experiment**: Benchmark `SmolLM2-360M` on a synthetic 4-step modular composition task (ModComp-4) comparing $A_1$ (Best-of-100), $A_3$ (Prefix-RLVR), and $A_5$ (Full RLVR) under equal total FLOP budget ($C = 5 \times 10^{15} \text{ FLOPs}$).
* **Estimated Compute**: **$6.2 \text{ GPU-Hours}$** (SmolLM2-360M on Apple Silicon MPS).
* **Risk of Collision**: **Moderate**. High literature density around RLVR, but matched-compute Pareto formulation across $A_0 \to A_5$ is unclaimed.
* **Theory Opportunity**: High (Information-theoretic parameter efficiency, compute allocation dynamics, query amortization bounds).
* **Kakade Alignment**: **High** (Aligns with foundational research on learning dynamics, scaling limits, and post-training optimization).
* **Independence Score**: **8/10** (Substantively distinct formulation focusing on query-amortized compute efficiency rather than support expansion).

---

## CANDIDATE 2: AUTONOMOUS TEST-TIME COMPUTE ALLOCATION UNDER HEAVY-TAILED VERIFICATION LATENCY

* **Precise Question**: For autonomous AI agents facing heavy-tailed verification latency, does a dynamic Gittins-index stopping rule outperform static Best-of-$N$ budget allocation in total inference compute required per solved problem?
* **Closest Three Papers**:
  1. *Scaling LLM Test-Time Compute Optimally* (Snell et al., 2024; `arXiv:2408.03314`)
  2. *Adaptive Computation Time for Recurrent Neural Networks* (Graves, 2016)
  3. *Q-Probe* (Li et al., ICML 2024)
* **Remaining Distinction**: Applies multi-armed bandit optimal stopping theory (Gittins index) to dynamic code execution verifier latency rather than assuming constant cost per sample.
* **Falsifiable Hypothesis**: $H_2$: Gittins-index dynamic verification reduces total inference FLOPs by $> 30\%$ over optimal fixed Best-of-$N$ at identical accuracy on Python execution benchmarks.
* **Smallest Kill Experiment**: Test dynamic stopping on 200 HumanEval execution tasks under synthetic heavy-tailed execution timeouts (10ms to 5s).
* **Estimated Compute**: **$2.5 \text{ GPU-Hours}$**.
* **Risk of Collision**: **Low/Moderate**.
* **Theory Opportunity**: High (Multi-armed bandits, dynamic programming, optimal search theory).
* **Kakade Alignment**: **High** (Autonomous agents, decision making, bandit theory).
* **Independence Score**: **8/10** (Strong theoretical connection between bandit theory and LLM test-time search).

---

## CANDIDATE 3: SELF-REFINING MULTI-AGENT VICKREY-CLARKE-GROVES AUCTIONS FOR CONTEXT ALLOCATION

* **Precise Question**: Does a VCG auction mechanism for prompt context allocation reduce token redundancy and agent communication collapse in non-cooperative multi-agent reasoning tasks?
* **Closest Three Papers**:
  1. *AutoGen* (Wu et al., 2023)
  2. *Multi-Agent RL and Game Theory* (Shoham & Leyton-Brown, 2008)
  3. *Communicating Agents in LLMs* (Chen et al., 2024)
* **Remaining Distinction**: Replaces heuristic chat orchestration with formal VCG auctions to allocate context window tokens among autonomous agents based on marginal utility bids.
* **Falsifiable Hypothesis**: $H_3$: VCG prompt allocation reduces total prompt token consumption by $> 35\%$ while matching multi-agent problem-solving accuracy.
* **Smallest Kill Experiment**: Simulate 3 LLM agents solving multi-step logic puzzles under VCG token bidding vs standard round-robin chat.
* **Estimated Compute**: **$3.8 \text{ GPU-Hours}$**.
* **Risk of Collision**: **Low**.
* **Theory Opportunity**: High (Algorithmic mechanism design, auction theory, multi-agent systems).
* **Kakade Alignment**: **High** (Multi-agent decision making, game theory, autonomous systems).
* **Independence Score**: **8/10**.
