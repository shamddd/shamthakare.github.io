# PHASE 1I CANONICAL CONFIRMATORY EXECUTION RECORD

**Milestone**: Phase 1I.1 Canonical Record Lock  
**Execution Timestamp**: `2026-08-19 23:03 UTC`  
**Primary Authoritative Registry**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json` ($N=454$)  
**Registry SHA-256 Hash**: `76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478`  
**Strict Secondary Registry**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json` ($N=388$)  
**Strict Registry SHA-256 Hash**: `667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227`  
**Total Planned Rollouts**: **`130,752 Rollouts`** ($454 \times 2 \times 9 \times 16$)  
**Canonical Primary Estimand**: $\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$  
**Record Status**: **`CANONICAL — ALL HISTORICAL SUPERSEDED DOCUMENTS MARKED`**

---

## 1. Authoritative Parameter Lock

* **Problem Count ($N$)**: `454`
* **Intervention States**: `control`, `recovery` ($2$)
* **Checkpoints ($t$)**: `0, 32, 64, 96, 128, 160, 192, 224, 256` ($9$)
* **Rollouts per Cell ($K$)**: `16`
* **Total Rollouts**: `130,752`
* **Inference Backend**: `vLLM Engine (v0.7.0)` ($C=16$)
* **Sampling Parameters**: `temperature = 0.6`, `top_p = 0.95`
* **Master Seed**: `"20260819_stateshift_v4"`
* **Record Type Enforcement Tag**: `empirical_confirmatory`

*Signed by Principal ML Research Scientist & Reproducibility Engineer*
