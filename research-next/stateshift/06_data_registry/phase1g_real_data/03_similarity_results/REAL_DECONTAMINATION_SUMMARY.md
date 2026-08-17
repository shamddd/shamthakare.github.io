# REAL DATASET DECONTAMINATION FORENSICS SUMMARY

**Benchmark Analyzed**: MATH-500 Canonical Evaluation Split ($N=500$)  
**Training Corpora Audited**:
- DeepScaleR RL Training Dataset (`agentica-org/DeepScaleR-Preview-Dataset`, $N=40,315$)
- Omni-MATH Benchmark/Lineage Dataset (`KbsdJames/Omni-MATH`, $N=4,428$)  
**Audit Protocol**: Phase 1F Immutable Decontamination Lock  
**Date**: `2026-08-17 05:45 UTC`  

---

## 1. Quantitative Decontamination Findings

| Classification Category | Definition & Criteria | Item Count ($N$) | Percentage (%) | Action in Primary Pool |
| :--- | :--- | :---: | :---: | :--- |
| **EXACT_DUPLICATE** | Exact normalized text SHA-256 match (preserving numerics) | `3` | `0.6%` | **EXCLUDED** |
| **NEAR_DUPLICATE_HIGH_CONFIDENCE** | Token 3-gram Jaccard $\ge 0.85$ or Edit Ratio $\ge 0.88$ | `14` | `2.8%` | **EXCLUDED** |
| **STRUCTURAL_NUMERIC_VARIANT** | Identical numeric-erased structure with altered numbers | `12` | `2.4%` | **EXCLUDED** |
| **POSSIBLE_RELATED** | Moderate overlap ($0.60 \le \text{Jaccard} < 0.85$) | `70` | `14.0%` | **FLAGGED / RETAINED** |
| **NO_MEANINGFUL_MATCH** | No significant textual or structural overlap | `401` | `80.2%` | **RETAINED (CLEAN)** |
| **TOTAL BENCHMARK** | Full canonical MATH-500 evaluation set | **500** | **100.0%** | `Primary Pool N = 471` |

---

## 2. Source-Level Overlap Attribution

- **DeepScaleR Direct Overlap**: `29` items identified in DeepScaleR-Preview training dataset.
- **Omni-MATH Overlap**: `12` items share structural lineage with Omni-MATH contest sub-corpora.

---

## 3. Manuscript-Grade Methodological Caveat & Boundary Statement

> [!IMPORTANT]
> **RL-Stage Overlap Audit vs. Base-Model Pretraining Exposure Boundary**:
> This decontamination audit rigorously identifies and excludes all items present in public **RL-stage fine-tuning datasets** (specifically DeepScaleR-Preview and Omni-MATH). However, passing this audit **does NOT guarantee zero pretraining exposure** in the foundational base models (e.g., Qwen-2.5-Base), whose exact web-crawl and pretraining corpora remain undisclosed. 
> 
> Therefore, in the StateShift manuscript, this evaluation pool MUST be formally described as:
> *"A decontaminated evaluation pool stripped of verified RL-stage training data collisions and structural variants, bounding post-pretraining contamination risk."*

---
*Certified by Decontamination Forensics Lead*
