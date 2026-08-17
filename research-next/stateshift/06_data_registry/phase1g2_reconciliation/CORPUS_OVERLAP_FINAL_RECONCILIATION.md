# CORPUS OVERLAP FINAL RECONCILIATION

**Audited Corpora**:
- DeepScaleR-Preview (`agentica-org/DeepScaleR-Preview-Dataset`, $N=40,315$)
- Omni-MATH (`KbsdJames/Omni-MATH`, $N=4,428$)  

---

## 1. Definitional Reconciliation & Authoritative Overlap Count

| Overlap Definition | Calculation Method | Overlap Count ($N$) | Total Unique Training Items |
| :--- | :--- | :---: | :---: |
| **`raw_exact_string_overlap`** | Un-normalized exact python string equality | **`3,501`** | `41,242` |
| **`normalized_exact_text_overlap`** | LaTeX/NFC/whitespace normalized text equality | **`3,501`** | **`41,242`** |

---

## 2. Narrative Conflict Resolution

- The draft text string `N=2,184` in `PHASE1G1_RECONCILIATION_VERDICT.md` was an un-updated draft placeholder.
- **Authoritative Seal**: The true, empirically computed direct problem statement overlap between DeepScaleR and Omni-MATH is **`3,501` items**.
- **Unique Records Searched**: Searching the combined corpus ($40,315 + 4,428 = 44,743$ records) represents searching **`41,242` unique training examples**.

---
