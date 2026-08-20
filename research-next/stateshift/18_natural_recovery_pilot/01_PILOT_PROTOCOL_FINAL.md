# PHASE 2 STAGE C0 — NATURAL RECOVERY FEASIBILITY PILOT PROTOCOL

**Study Title**: StateShift Natural Post-Error Recovery Feasibility Pilot (`StateShift-NaturalRecovery-Pilot`)  
**Execution Timestamp**: `2026-08-20 03:04 UTC`  
**Scientific Objective**: Measure the natural error incidence (NEI) and natural post-error recovery rate (NRR) in unperturbed LLM reasoning rollouts.  

---

## 1. Experimental Invariants

* **Model / Checkpoint**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` (Commit `50bdcb5a`).
* **Problem Population**: $N=200$ challenging math reasoning problems sampled from the frozen confirmatory registry (`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json`).
* **Rollouts per Problem ($K$)**: $K=16$ independent unperturbed rollouts per problem.
* **Total Planned Rollouts**: $200 \times 16 = 3,200$ rollouts.
* **Sampling Parameters**: `max_new_tokens=512, temperature=0.6, top_p=0.95, seed_base=4200`.
* **Zero External Injection Rule**: Zero error injection, zero hint, zero critique, zero recovery instructions. The model decodes freely.
* **Hard Compute Ceiling**: **`$1.00 USD`** maximum compute exposure.

*Signed by Principal ML Research Scientist & Lead LLM Reasoning Researcher*
