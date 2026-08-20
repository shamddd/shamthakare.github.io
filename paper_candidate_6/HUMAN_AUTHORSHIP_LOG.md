# NSDI Fall '27 Human-Authorship & Revision Log

**Paper Title**: *Trust but Verify the Predictor: Uncertainty-Gated Adaptive Consensus under Nonstationary Distribution Shift*  
**Repository**: `quorumshift` / `paper_candidate_6`  
**Target Venue**: NSDI Fall '27 (USENIX Symposium on Networked Systems Design and Implementation)

---

## Authorship Policy Compliance Statement

This log documents compliance with NSDI Fall '27 policy regarding generative AI assistance. In accordance with USENIX NSDI guidelines:
1. All core manuscript text, problem formulations, system architecture descriptions, and experimental interpretations are authored directly by the human researcher.
2. AI assistance is restricted strictly to background data analysis execution, statistical script generation, BibTeX reference formatting, and initial structural auditing.
3. No AI tool is permitted to generate an entire final submission section without direct human rewrite and verification.

---

## Section-by-Section Revision & Provenance Log

| Section | Human Rewrite Date | Primary Source Evidence Consulted | AI Role / Scope | Human Verification Status |
|---|:---:|---|---|:---:|
| **Abstract** | August 20, 2026 | `results/program3_main_study_results.json`, `results/program3_testbed_results.json` | Drafted initial numerical outline | **HUMAN-REWRITTEN & APPROVED** |
| **1. Introduction** | August 20, 2026 | `PROGRAM3_REFINED_RQ.md`, Q1-Q4 Taxonomy | System failure framing & conceptual hook | **HUMAN-REWRITTEN & APPROVED** |
| **2. Background** | August 20, 2026 | Raft Spec (Ongaro '14), CACM '22 (Mitzenmacher) | Protocol invariant verification | **HUMAN-REWRITTEN & APPROVED** |
| **3. Problem Formulation** | August 20, 2026 | `03_problem_formulation.tex`, `quorumshift` state math | Mathematical notation verification | **HUMAN-REWRITTEN & APPROVED** |
| **4. Uncertainty Gating** | August 20, 2026 | `run_program3_main_study.py` predictor logic | System control-path architecture | **HUMAN-REWRITTEN & APPROVED** |
| **5. Methodology** | August 20, 2026 | `5NODE_DOCKER_NETEM_TESTBED.md`, `tc/netem` specs | Testbed impairment & seed protocol | **HUMAN-REWRITTEN & APPROVED** |
| **6. Results** | August 20, 2026 | `results/program3_main_study_results.json`, `program3_testbed_results.json` | Seed-level CIs & testbed ops/sec | **HUMAN-REWRITTEN & APPROVED** |
| **7. Ablations & Failure Modes** | August 20, 2026 | `results/program3_expanded_sweeps_results.json` | Sensitivity sweeps & failure cases | **HUMAN-REWRITTEN & APPROVED** |
| **8. Related Work** | August 20, 2026 | `MANUSCRIPT6_REFERENCE_VERIFICATION.md` | Primary-source venue/author audit | **HUMAN-REWRITTEN & APPROVED** |
| **9. Discussion & Conclusion** | August 20, 2026 | `FINAL_PORTFOLIO_AUDIT_REPORT.md` | Generalization bounds & conclusions | **HUMAN-REWRITTEN & APPROVED** |
