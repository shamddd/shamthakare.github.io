# MODEL FAMILY COMPARABILITY AUDIT: RESOLVING CONFLICTS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. IDENTIFICATION OF CONFOUNDED DESIGN IN PREVIOUS DRAFT

> **Confounding Warning**: The previous draft proposed comparing `SmolLM2-Instruct`, `Qwen2.5-Instruct`, and `Pythia-base`. Mixing instruction-tuned models with a raw pretraining base model is a **CONFOUNDED DESIGN**. Prior SFT/alignment history introduces unmeasured heterogeneity in baseline instruction-following capabilities.

---

## 2. SELECTION OF UNCONFOUNDED DESIGN B (INSTRUCTION-TUNED REPLICATION)

We adopt **DESIGN B (INSTRUCTION-TUNED REPLICATION)** as the primary confirmatory study:
* **Requirement**: All 3 model families must begin from comparable, publicly available instruction-tuned checkpoints.
* **Pythia Replacement Requirement**: Pythia-410M lacks an official comparable instruction-tuned checkpoint. It is **OFFICIALLY REPLACED** by `TinyLlama-1.1B-Chat-v1.0`.

---

## 3. COMPARABILITY MATRIX FOR SELECTED FAMILIES

| Property | Family 1: SmolLM2 | Family 2: Qwen2.5 | Family 3: TinyLlama |
| :--- | :--- | :--- | :--- |
| **Exact Identifier** | `HuggingFaceTB/SmolLM2-360M-Instruct` | `Qwen/Qwen2.5-0.5B-Instruct` | `TinyLlama/TinyLlama-1.1B-Chat-v1.0` |
| **Status** | Instruction-Tuned | Instruction-Tuned | Instruction-Tuned |
| **Parameter Count** | $360	ext{M}$ | $490	ext{M}$ | $1.1	ext{B}$ |
| **Pretraining Lineage** | SmolLM2 Pretrained | Qwen2.5 Pretrained | Llama-2 Pretrained |
| **SFT / Alignment** | SFT + DPO | SFT + DPO | SFT + DPO |
| **License** | Apache 2.0 | Apache 2.0 | Apache 2.0 |
