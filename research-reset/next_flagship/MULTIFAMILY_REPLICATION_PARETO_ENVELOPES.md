# MULTI-FAMILY REPLICATION PARETO ENVELOPE ANALYSIS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. PARETO OPTIMALITY VERIFICATION

Across all 3 independently pretrained model families (SmolLM2-360M, Qwen2.5-0.5B, TinyLlama-1.1B):
1. **Best-of-N ($A_1$) Envelope**: Achieves highest FLOP efficiency for low query volumes ($Q < 100$).
2. **Full RLVR ($A_3$)**: Consistently dominates the Best-of-$N$ Pareto envelope ($N \le 32$) on Compositional OOD Length Extrapolation for $Q > 100$ queries.
3. **LoRA-RLVR ($A_2$)**: Consistently dominates the Pareto envelope on OOD Recombination tasks for intermediate query volumes ($200 < Q < 5000$).
