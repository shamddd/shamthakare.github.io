# STATESHIFT PHASE 1I.3 FINAL PRIMARY PROTOCOL

**Milestone**: Phase 1I.3 Final Primary Protocol Specification  
**Execution Timestamp**: `2026-08-19 23:26 UTC`  
**Authoritative Problem Registry**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json` ($N=454$, SHA-256 `76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478`)  
**Strict Sensitivity Registry**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json` ($N=388$, SHA-256 `667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227`)  
**Total Rollouts Planned**: **`29,056 Rollouts`**  
**Protocol Status**: **`FROZEN FINAL — READY FOR USER AUTHORIZATION`**

---

## 1. Primary Estimand Formulation

$$Y_{i,g,t,k} = \text{TARGET\_TRANSITION\_SUCCESS}_{i,g,t,k} \in \{0, 1\}$$

$$\bar{Y}_{i,g,t} = \frac{1}{16} \sum_{k=1}^{16} Y_{i,g,t,k} \quad \text{for } g \in \{R, C\} \text{ and } t \in \{0, 256\}$$

$$\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$$

Where $\mu_{g,t} = \frac{1}{454} \sum_{i=1}^{454} \bar{Y}_{i,g,t}$.

---

## 2. Execution Invariants & Model Checkpoints

* **Checkpoint $t=0$**: `Qwen/Qwen2.5-7B` (Revision `d149729398750b98c0af14eb82c78cfe92750796`)
* **Checkpoint $t=256$**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` (Revision `7667ad787966f5733fdca3d2b240452d7095ff95`)
* **Inference Engine**: `vLLM Engine (v0.7.0)` ($C=16$, `gpu_memory_utilization=0.90`)
* **Sampling Parameters**: `temperature = 0.6`, `top_p = 0.95`, `max_new_tokens = 512`
* **Master Seed**: `"20260819_stateshift_v4"`

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
