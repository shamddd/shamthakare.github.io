# FROZEN SCIENTIFIC CLAIMS & SCOPE BOUND LEDGER

**Date**: August 16, 2026  
**Auditor**: Lead Scientific Reviewer  

---

## 1. PRIMARY SCIENTIFIC CLAIM

> *"Across the three tested independently pretrained instruction/chat-tuned model families, the preregistered directional criterion $R_f < 1$ was observed: controlled OOD length extrapolation shifted the utility-normalized deployment-horizon frontier toward trained interventions relative to IID evaluation."*

---

## 2. PROHIBITED OVER-CLAIMS (STRICTLY BANNED)

* **NO** claims of "universal laws of reasoning".
* **NO** claims of "first ever" or "unprecedented breakthrough".
* **NO** claims that RLVR "proves" superiority over test-time search in all domains.
* **NO** claims generalizing beyond the $360	ext{M} 	ext{--} 1.1	ext{B}$ parameter range.

---

## 3. EXACT EXPERIMENTAL SCOPE BOUNDS

* **Model Families**: 3 instruction/chat-tuned models (`SmolLM2-360M-Instruct`, `Qwen2.5-0.5B-Instruct`, `TinyLlama-1.1B-Chat-v1.0`).
* **Training Seeds**: 2 independent RL seeds per family ($N=12$ training runs total).
* **Task Environment**: Synthetic controlled compositional reasoning (`ModComp-3` IID, `ModComp-5` OOD Length, `ModComp-Recomb` OOD Recombination).
* **Search Baseline**: Best-of-$N$ Pareto envelope ($N \in \{1, 2, 4, 8, 16, 32\}$ with verifier costs charged).
* **Trained Interventions**: LoRA-RLVR ($A_2$) and Full-Parameter RLVR ($A_3$) trained with 50 GRPO steps.
