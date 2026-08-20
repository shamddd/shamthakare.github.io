# E0 MISSING EVIDENCE LEDGER

**Date**: August 16, 2026  

---

## 1. UNAVAILABLE OR UNLOCATED HISTORICAL ARTIFACTS

| Artifact | Expected Purpose | Why Unavailable | Impact on Reproducibility |
| :--- | :--- | :--- | :--- |
| `raw_model_checkpoints/*.pt` | Fine-tuned PyTorch model weights | Storage constraint (intermediate weights deleted) | Low (reproducible via preregistered RL training configs & seeds) |
| `raw_vllm_traces/*.jsonl` | Token-level latency traces | Not logged in original pilot harness | Low (FLOP and sample count accounting complete) |

*Summary*: All raw empirical evaluation output JSONs, analysis scripts, audit logs, and claim ledgers are fully preserved.
