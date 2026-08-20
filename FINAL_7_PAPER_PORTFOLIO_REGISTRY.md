# Final 7-Paper Portfolio Registry

**Author**: Sham Satish Thakare (Independent Researcher)  
**Date**: August 2026  
**Purpose**: Canonical, immutable scientific registry for all 3 submitted manuscripts and 4 frozen new paper candidates.

---

## 1. Complete Portfolio Inventory

| Paper ID | Canonical / Working Title | Repository Path | Current Status | Primary Research Area | Main Models / Systems | Datasets / Workloads | Primary Metric | Primary Claim / Contribution |
|---|---|---|---|---|---|---|---|---|
| **`PUB-001`** | *When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning* | [`submission_ieee_tai`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_ieee_tai) | Submitted (IEEE TAI, Aug 2026) | LLM RL & Uncertainty | Qwen-2.5-Math, DeepSeek-R1-Distill | GSM8K, MATH500 | Pass@1 Gain, Token Entropy | Token predictive entropy is length-confounded ($r=+0.486$), causing $0.00\%$ Pass@1 gain for sample-level consensus GRPO. |
| **`PUB-002`** | *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning* | [`submission_bigdata2026_main_v3`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_bigdata2026_main_v3) | Submitted (IEEE BigData / MLBD 2026, ID: `BigD497`) | Reasoning Error Recovery | Llama-3-8B, Qwen-2.5-Math | Single-step Arithmetic & Logic | Matched Recovery Contrast ($D_{\text{recovery}}$) | Matched recovery contrast $D_{\text{recovery}} = -0.1100$; Instruct models display no recovery-specific advantage over Base models on single-step arithmetic prefixes. |
| **`PUB-003`** | *Amortized Intervention Frontiers for Language-Model Reasoning: When Does Training Beat Search?* | [`submission/tmlr`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission/tmlr) | Submitted (TMLR / NeurIPS Workshop, Aug 2026) | Compute Economics & Search | Llama-3.1-8B, DeepSeek-R1 | MATH500, AIME2024 | Break-even Query Volume ($R_f$) | Cost model $C_{\text{total}} = C_{\text{train}} + Q \cdot C_{\text{inference}}$; OOD length extrapolation systematically shifts break-even crossover ($R_f \approx 0.0618$). |
| **`CANDIDATE #4`** (Program 1) | *Capability-Conditioned RLVR Self-Consistency Calibration Study* | [`adaptive-rl-forge`](file:///Users/shamthakare/.gemini/antigravity/scratch/adaptive-rl-forge) | Frozen Candidate | RL Calibration Boundaries | Qwen-2.5-Math-1.5B Lineage | GSM8K, MATH500 | Brier Score ($\downarrow 0.2255$), AURC ($\downarrow 0.0995$) | Task capability is a critical boundary condition: on capable models ($>1.0\%$ baseline), GRPO RLVR improves accuracy ($+10.0\%$) and self-consistency calibration without confidence collapse. |
| **`CANDIDATE #5`** (Program 2) | *Temporal Post-Recovery Persistence in Multi-Turn Tool-Calling Agents* | [`agentguard-final`](file:///Users/shamthakare/.gemini/antigravity/scratch/agentguard-final) | Frozen Candidate | Agent State Failure & Recovery | AgentGuard, Tool LLMs | Multi-turn Tool Benchmarks | Counterfactual Action Divergence ($D(d)$) | Transient tool state restoration induces 1-step counterfactual action divergence ($D(d=1)=1.0, D(d=2)=0.0$) and policy violations ($36\%$), eliminated ($0\%$) via explicit restoration notice. |
| **`CANDIDATE #6`** (Program 3) | *Learning-Augmented Fault-Tolerant Consensus with Uncertainty-Aware Trust Gates* | [`quorumshift`](file:///Users/shamthakare/.gemini/antigravity/scratch/quorumshift) | Frozen Candidate | Learning-Augmented Distributed Systems | C++ / Python Raft Engine | 5 Nonstationary Network Shift Regimes | p99 Excess Latency Regret ($\text{Regret}_{\text{p99}}$) | Calibrated uncertainty trust gates ($T_3$) distinguish OOD-but-safe from ID-looking-but-harmful states better than naive OOD distance ($T_2$), eliminating p99 tail regret while preserving adaptive speedups. |
| **`CANDIDATE #7`** (Program 4) | *Verifiable, Private & Observable AI Systems via Zero-Knowledge Provenance Graph Proofs* | [`scratch`](file:///Users/shamthakare/.gemini/antigravity/scratch/run_program4_main_study.py) | Frozen Candidate | Cryptographic AI Trace Verification | SHA-256 Merkle Engine, Tool Receipts | 72 Agent Workflows ($N=64\dots512$) | Constraint Blow-up, Compliance Accuracy | Zero-knowledge authorization-path compliance verification over tool-signed Merkle provenance graphs ($B_3$-G) achieves $100\%$ accuracy, $0\%$ attribute disclosure, and 13.68x constraint reduction over $B_2$-L+ at scale ($N=512$). |

---

## 2. Global Decontamination & Scientific Boundary Summary

* **No Duplicated Primary Claims**: Every candidate addresses an isolated scientific question with distinct primary endpoints, datasets, and mechanism claims.
* **Preserved Lineage**: Shared infrastructure (e.g. Qwen model checkpoints, agent state loggers, Raft simulation engines) is explicitly disclosed and attributed.
