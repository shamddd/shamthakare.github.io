# Paper Candidate #6: Learning-Augmented Fault-Tolerant Consensus with Uncertainty-Aware Trust Gates

**Canonical Title**: *Trust but Verify the Predictor: Uncertainty-Gated Adaptive Consensus under Nonstationary Distribution Shift*  
**Author**: Sham Satish Thakare (Independent Researcher)  
**Target Venue**: USENIX NSDI Fall '27 Research Track  
**Date**: August 2026  
**Status**: **STRENGTHENED & SUBMISSION READY (NSDI REWRITE AUDIT COMPLETE)**

---

## 1. Directory Structure

* [`main.tex`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/main.tex): Main LaTeX document assembling all manuscript sections.
* [`sections/`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/sections): Section-by-section LaTeX sources (`00_abstract.tex` through `09_discussion_conclusion.tex`).
* [`references.bib`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/references.bib): 100% primary-source verified BibTeX database.
* [`MANUSCRIPT6_CLAIM_LEDGER_FINAL.csv`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/MANUSCRIPT6_CLAIM_LEDGER_FINAL.csv): Canonical claim-to-raw-data traceability matrix.
* [`MANUSCRIPT6_REFERENCE_VERIFICATION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/MANUSCRIPT6_REFERENCE_VERIFICATION.md): Primary-source bibliographic verification ledger.
* [`HUMAN_AUTHORSHIP_LOG.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/HUMAN_AUTHORSHIP_LOG.md): NSDI Fall '27 human-authorship compliance & section rewrite log.
* [`NSDI_RESEARCH_TRACK_SPECIFICATION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/paper_candidate_6/NSDI_RESEARCH_TRACK_SPECIFICATION.md): Systems problem, control-path architecture, and bounded claim specification for NSDI.

---

## 2. Compilation Instructions

To compile the LaTeX source locally using `pdflatex`:
```bash
cd paper_candidate_6
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
