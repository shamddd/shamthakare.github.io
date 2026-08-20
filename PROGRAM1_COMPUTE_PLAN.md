# Program 1 Compute Allocation & Cost Ledger

**Author**: Sham Satish Thakare  
**Total Available Budget**: \$10.00 RunPod Credit  
**Checkpoint 2 Spend**: **\$0.00**  
**Pilot Target Spend**: **\$0.00** (Local CPU / MPS execution)

---

## 1. Cost Schedule by Phase

| Phase | Description | Hardware | Estimated Time | Cost Ceiling | Status |
|---|---|---|---|---|---|
| **Checkpoint 2 Audit** | Literature audit, boundary definition, preregistration | N/A (Local Text/Files) | — | **\$0.00** | **COMPLETED** |
| **Minimum Viable Pilot (MVP)** | 800 rollout completions across $N=50$ GSM8K prompts | Local CPU / MPS | 2.5 hours | **\$0.00** | **PLANNED** |
| **Main Study Phase 1** | Matched pre/post-RLVR inference sweep ($N=200$ GSM8K, $K=16$) | RunPod 1x L4 ($0.40/hr) | 2.0 hours | **\$0.80** | **GATE-HOLD** |
| **Main Study Phase 2** | MATH-500 difficulty sweep ($N=200$, $K=16$) | RunPod 1x L4 ($0.40/hr) | 2.0 hours | **\$0.80** | **GATE-HOLD** |
| **Reserve Buffer** | Unforeseen re-runs or sensitivity temperature sweeps | RunPod 1x L4 ($0.40/hr) | — | **\$8.40** | **RESERVED** |
| **Total** | | | | **\$10.00** | |

---

## 2. Idle Prevention Invariants

1. **Local-First Execution**: The MVP pilot will execute locally using PyTorch CPU/MPS backend, incurring zero cloud GPU cost.
2. **Batch Inference Optimization**: Main experiment runs will use PyTorch `vLLM` or HuggingFace batched inference to complete $N=200, K=16$ rollouts in $<2.0$ hours per benchmark.
3. **Automated Auto-Shutdown**: RunPod instances will launch via python scripts with explicit `--auto-destroy` flags upon process exit.
