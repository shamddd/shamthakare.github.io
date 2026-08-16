# EXTERNAL BENCHMARK EXPERIMENTAL PROTOCOL (E1 vs E2)

**Date**: August 16, 2026  
**Auditor**: Benchmarking & Contamination Auditor  

---

## 1. DUAL EXPERIMENTAL SUITE DESIGN

* **Experiment E0 / E1 (Completed)**: Synthetic Controlled Compositional Environment (`ModComp-3` IID, `ModComp-5` OOD Length, `ModComp-Recomb`).
* **Experiment E2 (Proposed External Study)**: Real-world Mathematical & Algorithmic Reasoning:
  - **Dataset 1**: GSM8K (IID 8-grade math vs OOD Multi-step Operator Extension).
  - **Dataset 2**: SVAMP (Word problem semantic variation).
  - **Dataset 3**: MATH Subset (Level 1-2 IID vs Level 4-5 OOD Depth).

---

## 2. CONTAMINATION SAFEGUARDS & AUDIT PROTOCOL

* Pre-register exact test splits before training.
* Strip overlapping training prompts using 8-gram exact match filtering.
* Verifier: Exact numerical answer extraction (Regex + SymPy evaluation).
