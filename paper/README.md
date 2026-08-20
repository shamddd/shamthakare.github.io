# StateShift Manuscript Source & Publication Artifacts

**Manuscript Title**: *StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training*  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Publication Status**: Submitted to *Artificial Intelligence* (Elsevier), 2026 — Manuscript ARTINT-D-26-01491  

---

## 1. Directory Overview

This directory contains the LaTeX source files and publication assets for the StateShift manuscript:

* `main.tex`: Full LaTeX source file.
* `supplement.tex`: Supplementary Material LaTeX source file.
* `references.bib`: BibTeX bibliography file (50 verified items).
* `figures/`: High-resolution vector PDF and PNG publication figures.
* `tables/`: Data tables.

---

## 2. Compilation Instructions

If `pdflatex` or `latexmk` is installed:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Pre-compiled PDF versions are also available in `submission/aij/final_upload/01_Main_Manuscript.pdf` and `StateShift_AIJ_Final_Submission.zip`.
