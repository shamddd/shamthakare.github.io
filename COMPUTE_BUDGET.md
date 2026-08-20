# Compute Budget & Hardware Resource Strategy

**Total Available Budget**: **\$10.00 RunPod Credit**  
**Strategy Principle**: Zero unnecessary GPU expenditure. Maximize scientific information gain per cent spent. Utilize inference-first evaluation, public pre-trained checkpoints (Qwen2.5-0.5B/1.5B/3B, Llama-3.2-1B/3B), and local CPU simulations for non-GPU programs.

---

## 1. Resource Allocation by Program

| Program | Hardware Target | Estimated Compute Cost | Scientific Purpose |
|---|---|---|---|
| **Program 1: Calibrated Reasoning** | RunPod 1x L4 ($0.40/hr) & 1x A40 ($0.79/hr) | **\$3.50** | Baseline calibration evaluation (ECE/Brier) and process-level Brier-GRPO pilot fine-tuning across 2 model families. |
| **Program 2: Agent Reliability** | Local CPU / 1x RunPod L4 ($0.40/hr) | **$1.50** | Multi-turn agent context depth ($d=0 \to 20$) tool error propagation benchmark using open API models. |
| **Program 3: Distributed Systems** | Local CPU (Apple Silicon M1 / x86_64 8-core) | **$0.00** | C++20 Raft consensus joint-state simulator and synthetic network partition fault injector. |
| **Program 4: Observable AI Systems** | Local CPU (Apple Silicon M1 / x86_64 8-core) | **$0.00** | OpenTelemetry trace parser, topological walk graph engine, and ZK proof verification suite. |
| **Emergency Reserve** | Buffer | **$5.00** | Unforeseen re-runs, logging adjustments, or expanded ablation passes. |
| **Total** | | **$10.00** | |

---

## 2. RunPod Hardware Selection Rules

1. **L4 GPU ($0.40/hr, 24GB VRAM)**: Primary workhorse for inference calibration passes (Qwen2.5-0.5B/1.5B/3B, Llama-3.2-1B/3B) and diagnostic probing extraction.
2. **A40 GPU ($0.79/hr, 48GB VRAM)**: Reserved exclusively for multi-completion GRPO rollout batches ($G=4 \text{ or } 8$).
3. **Strict Idle Prevention**: Pods must automatically terminate via script exit handlers immediately upon experiment completion.
