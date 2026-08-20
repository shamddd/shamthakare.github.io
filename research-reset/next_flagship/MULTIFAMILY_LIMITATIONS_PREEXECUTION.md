# PRE-EXECUTION LIMITATIONS & REVISED SENSITIVITY LANGUAGE

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. REVISED MODEL COMPARABILITY SPECIFICATION

> **Corrected Framing**: We state: **"Primary model-state category matched: instruction/chat-tuned."**

We do **NOT** claim that the three model families have equivalent prior alignment histories. Prior post-training pipeline variations are documented as family-level nuisance variables and study limitations:
* **TinyLlama-1.1B-Chat**: Pretrained on 3T tokens (Llama-2 architecture), fine-tuned on UltraChat followed by DPO on UltraFeedback.
* **Qwen2.5-0.5B-Instruct**: Pretrained on Qwen2.5 web corpus, fine-tuned via Qwen multi-stage SFT and DPO pipeline.
* **SmolLM2-360M-Instruct**: Pretrained on FineWeb-Edu, fine-tuned via Hugging Face SmolLM2 SFT and DPO pipeline.

---

## 2. REVISED SENSITIVITY & STATISTICAL POWER STATEMENTS

> **Corrected Sensitivity Statement**: *"Under the preregistered hierarchical simulation assumptions and a true family-level effect ratio $R_f \le 0.25$, the design produced directional replication in at least two of three families in 89.1% of simulations."*

### Complete Simulation Sensitivity Breakdown:
* **True Effect Ratio $R_f = 0.0632$ (Pilot Magnitude)**: Replication Probability = **`98.4%`**.
* **True Effect Ratio $R_f = 0.2500$ (Moderate Effect)**: Replication Probability = **`89.1%`**.
* **True Effect Ratio $R_f = 0.5000$ (Weak Effect)**: Replication Probability = **`76.2%`**.
* **True Effect Ratio $R_f = 1.0000$ (Null Effect $H_0$)**: False Positive Rate = **`4.8%`**.
