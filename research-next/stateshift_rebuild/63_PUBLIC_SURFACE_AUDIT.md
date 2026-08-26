# PUBLIC SURFACE AUDIT AND PUBLICATION STATUS REPAIR

**Project**: StateShift Scientific Rebuild — Phase 7A  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Audit Timestamp**: `2026-08-27T00:17:00+05:30` (IST)  
**Canonical Repository**: `https://github.com/shamddd/stateshift`  

---

## 1. Audit Table of Public Surfaces

We audited all public-facing repository surfaces to remove obsolete references to active AIJ submission (`ARTINT-D-26-01491`) and replace them with conservative, accurate working paper language:

| Target File | Historical / Obsolete Statement | Corrected Publication Status Claim | Reason for Modification |
| :--- | :--- | :--- | :--- |
| `README.md` | "Submitted to Artificial Intelligence (Elsevier), 2026 — Manuscript ARTINT-D-26-01491" | "Working Paper, 2026 — Research repository accompanying an ongoing manuscript revision" | AIJ submission rejected; public status repaired to reflect working paper. |
| `paper/README.md` | "Submitted to Artificial Intelligence (Elsevier), 2026 — Manuscript ARTINT-D-26-01491" | "Working Paper, 2026 — Research repository accompanying an ongoing manuscript revision" | Public repository header alignment. |
| `CITATION.cff` | "Submitted to Artificial Intelligence (Elsevier), 2026" | "Working Paper, 2026" | CFF metadata alignment for GitHub citation parser. |
| `CITATION.bib` | "Submitted to Artificial Intelligence (Elsevier)" | "Working Paper" | BibTeX entry alignment. |
| `paper/main.tex` | "Submitted to Artificial Intelligence" (Internal TeX comment) | "Working Paper, 2026" | Internal TeX header alignment. |

---

## 2. Public Status Policy Standard

* **Active Status Line**: `Working Paper, 2026 — Ongoing Manuscript Revision`
* **Historical Provenance**: All historical AIJ submission documents remain preserved in `submission/aij/` as archival internal evidence only, marked `SUPERSEDED / NOT EMPIRICAL / DO NOT CITE`.

*Signed by Principal Release Engineer & Scientific Integrity Auditor*
