# Four Final Research Questions & Hypotheses

**Author**: Sham Satish Thakare  
**Purpose**: Formal specification of the primary research questions, hypotheses, mechanisms, falsifiers, and contribution levels for the 4 Primary Research Programs.

---

## Program 1: Calibrated Reasoning & Adaptive Computation

* **Research Question (RQ1)**: Does Group Relative Policy Optimization (GRPO) advantage normalization systematically degrade model calibration error (ECE / Brier score) across diverse model families (Qwen2.5, Llama-3.2, Gemma-3) and parameter scales (0.5B–7B), and does a process-level Brier score penalty restore calibration stability without degrading pass@1 reasoning accuracy?
* **Null Hypothesis ($H_0$)**: GRPO-induced calibration degradation is an artifact of specific model architectures or task distributions, and process-level Brier penalties produce no change in ECE compared to standard GRPO.
* **Alternative Hypothesis ($H_1$)**: GRPO group variance normalization induces overconfidence universally across model families ($ECE > 0.20$), and a process-level Brier penalty ($\lambda \cdot \mathcal{B}$) reduces ECE by $\ge 50\%$ while maintaining pass@1 accuracy within $\pm 1.0\%$.
* **Mechanism**: Group standard normalization $A_i = (R_i - \bar{R}) / (\sigma_R + \epsilon)$ artificially inflates advantages when group reward variance is low, forcing policy gradient step updates to sharpen token probabilities even on uncertain CoT reasoning paths.
* **Falsifier**: If ECE across Llama-3.2 and Gemma-3 under standard GRPO remains $<0.05$, or if adding a process-level Brier penalty reduces pass@1 accuracy by $>5.0\%$, $H_1$ is falsified.
* **Closest Prior Work**:
  1. Bereket & Leskovec (2025) — *Uncalibrated Reasoning: GRPO Induces Overconfidence*
  2. Damani et al. (ICLR 2026) — *Beyond Binary Rewards: Training LMs to Reason About Uncertainty*
  3. Luo et al. (2025) — *Degeneration of Model Calibration in Reinforcement Learning with Verifiable Rewards*
  4. Shao et al. (2024) — *DeepSeekMath: Pushing the Limits of Mathematical Reasoning*
  5. Thakare (2026) — *Predicting RL Plasticity of Intermediate Checkpoints* (`adaptive-rl-forge`)
* **Exact Delta**: Evaluates cross-family/cross-scale generalization of GRPO calibration collapse on deterministic math tasks and tests process-level token Brier rewards rather than sample-level credit weights.
* **Contribution Level**: **Level 1 (Phenomenon) + Level 2 (Mechanism)**.

---

## Program 2: Long-Horizon Agent Reliability, State & Tool Safety

* **Research Question (RQ2)**: Do unhandled tool execution failures (timeouts, API permission errors, malformed responses) create persistent hidden-state belief errors in tool-calling LLM agents that degrade safety alignment over context depth ($d=0 \to 20$), causing a 30%+ increase in unsafe downstream tool actions?
* **Null Hypothesis ($H_0$)**: Tool execution failures do not alter agent hidden-state safety representations over multi-turn context depth, and downstream safety rates remain invariant to preceding tool errors.
* **Alternative Hypothesis ($H_1$)**: Tool execution errors induce persistent hidden-state belief drift, increasing unsafe tool execution rates by $\ge 30\%$ at context depth $d \ge 10$ compared to cold start ($d=0$).
* **Mechanism**: Negative or malformed tool outputs shift the agent's attention key-value cache away from systemic safety policy tokens toward local error-recovery context, weakening policy adherence over extended multi-turn sessions.
* **Falsifier**: If downstream unsafe action rates following tool failures at $d=15$ are statistically indistinguishable ($p > 0.05$) from error-free sessions at $d=15$, $H_1$ is falsified.
* **Closest Prior Work**:
  1. Cold-Start Safety Gap / SODA Benchmark (2025/2026) — *The Cold-Start Safety Gap in LLM Agents*
  2. Lakkaraju et al. (2025) — *Evaluating Vulnerabilities in Multi-Turn Agent Trajectories*
  3. Thakare (2026) — *AgentGuard: Action Lineage Provenance DAGs* (`agentguard-final`)
  4. Wong et al. (2024) — *Provable Guarantees for Safe Tool Use in Agents*
  5. Bach et al. (2025) — *Reliable Tool-Using Agents under Noisy API Environments*
* **Exact Delta**: Isolates the causal effect of *tool-failure belief persistence* over context depth ($d=0 \to 20$) rather than evaluating static single-turn jailbreaks or initial prompt warm-up.
* **Contribution Level**: **Level 1 (Phenomenon) + Level 2 (Mechanism)**.

---

## Program 3: Learning-Augmented Fault-Tolerant Distributed Systems

* **Research Question (RQ3)**: Can a confidence-aware fallback reliability envelope prevent linearizability violations and latency spikes in learning-augmented Raft consensus control when online workload or node failure distributions undergo nonstationary distribution shift?
* **Null Hypothesis ($H_0$)**: Learned adaptive quorum controllers adapt smoothly to nonstationary distribution shifts without requiring fallback mechanisms, and confidence envelopes provide zero reduction in tail latency under distribution shift.
* **Alternative Hypothesis ($H_1$)**: Unhedged learned quorum controllers exhibit catastrophic tail latency spikes ($>500\text{ms}$) under distribution shift; a confidence-aware fallback envelope bounds p99 latency to $<25\text{ms}$ while guaranteeing zero stale reads ($S_{\text{stale}}=0$).
* **Mechanism**: Online ML predictors suffer uncalibrated variance under out-of-distribution failure spikes; monitoring predictor uncertainty triggers an immediate fallback to conservative majority Raft joint-consensus before stale state is committed.
* **Falsifier**: If unhedged learned controllers maintain latency $<30\text{ms}$ under out-of-distribution network partitioning, or if fallback triggers cause $S_{\text{stale}} > 0$, $H_1$ is falsified.
* **Closest Prior Work**:
  1. Thakare (2026) — *AdaptiveReplica: Dynamic Quorum Adaptation* (`quorumshift`)
  2. Alizadeh et al. (2024) — *Learning-Augmented Systems & Systems Predictability*
  3. Kraska et al. (2023) — *Guaranteed Fallback Envelopes for Learned Data Structures*
  4. Lloyd et al. (2024) — *Consensus Performance under Asymmetric Network Partitioning*
  5. Weatherspoon et al. (2025) — *Safe Reconfiguration of Distributed Storage Systems*
* **Exact Delta**: Shifts from proposing dynamic Raft adaptation (`quorumshift`) to formulating formal *reliability envelopes* and *fallback bounds* for learned controllers under distribution shift.
* **Contribution Level**: **Level 2 (Mechanism) + Level 3 (Intervention)**.

---

## Program 4: Verifiable, Private & Observable AI Systems

* **Research Question (RQ4)**: Can zero-knowledge execution provenance DAGs provide complete auditability for dynamic multi-step LLM agent tool traces while bounding verification overhead to $<5\%$ and preventing sensitive context leakage?
* **Null Hypothesis ($H_0$)**: Constructing zero-knowledge provenance proofs for agent tool execution streams incurs $>100\%$ latency overhead, rendering private auditability impractical for real-time agents.
* **Alternative Hypothesis ($H_1$)**: ZK provenance DAG proofs verify execution trace policy compliance in $<5.0\text{ms}$ per tool step while guaranteeing zero leakage of private prompt context ($H(C \mid \text{Proof}) = H(C)$).
* **Mechanism**: Merkle-tree commitment schemes over topological tool execution DAGs allow proving that an agent adhered to safety policy invariants without disclosing private payload parameters.
* **Falsifier**: If ZK proof generation per tool step exceeds $50\text{ms}$, or if policy compliance verification fails on valid execution traces, $H_1$ is falsified.
* **Closest Prior Work**:
  1. Thakare (2026) — *TraceMind: Graph-Constrained Causal Reasoning* (`tracemind`)
  2. Thakare (2026) — *EnclaveShield: Zero-Knowledge Memory Attestation* (`enclaveshield`)
  3. Solar-Lezama & Zeldovich (2025) — *Verifiable Enclave Execution for AI Workloads*
  4. Mickens et al. (2024) — *Confidential Audit Provenance in Distributed Enclaves*
  5. Mittal et al. (2025) — *Privacy-Preserving Execution Tracing for Neural Agents*
* **Exact Delta**: Unifies graph-constrained trace observability (`tracemind`) with zero-knowledge attestation (`enclaveshield`) to enable auditable agent provenance.
* **Contribution Level**: **Level 2 (Mechanism) + Level 3 (Intervention)**.
