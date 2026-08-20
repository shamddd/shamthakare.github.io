# MODEL SCALE EXTENSION DESIGN (3B -- 7B LADDER)

**Date**: August 16, 2026  
**Auditor**: Compute Allocation & Scaling Auditor  

---

## 1. STRATEGIC SCALE LADDER SPECIFICATION

To test whether the amortization shift $R_f < 1.0$ survives beyond $1.1	ext{B}$ parameters, we design a 3-tier parameter ladder:

1. **Tier 1 (Small Scale, E0)**: `SmolLM2-360M-Instruct`, `Qwen2.5-0.5B-Instruct`, `TinyLlama-1.1B-Chat-v1.0` ($360	ext{M} 	ext{--} 1.1	ext{B}$).
2. **Tier 2 (Medium Scale, Proposed E2)**: `Qwen2.5-3B-Instruct`, `Llama-3.2-3B-Instruct` ($3.0	ext{B}$).
3. **Tier 3 (Large Scale, Proposed E3)**: `Qwen2.5-7B-Instruct` ($7.0	ext{B}$).

---

## 2. COMPUTE & MPS ACCELERATOR BUDGET ESTIMATES

* Tier 2 (3B models): ~24.5 MPS Accelerator-Hours per model run.
* Tier 3 (7B models): ~58.0 MPS Accelerator-Hours per model run.
* **Status**: **UNEXECUTED / PROPOSED FOR EXTENDED RESEARCH PROGRAM**.
