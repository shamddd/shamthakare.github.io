# TRAINING CORPUS LINEAGE & OVERLAP RECONCILIATION

**Audited Corpora**:
1. `DeepScaleR-Preview-Dataset` (`agentica-org/DeepScaleR-Preview-Dataset`, $N=40,315$)
2. `Omni-MATH Benchmark` (`KbsdJames/Omni-MATH`, $N=4,428$)  

---

## 1. Lineage Findings & Provenance Analysis

- **Direct Corpus Overlap**: Exactly **`3501` problem statements** in Omni-MATH are present word-for-word in the DeepScaleR-Preview dataset.
- **Corpus Lineage Confirmation**: As documented in the DeepScaleR technical release notes, Omni-MATH is an explicit sub-source used during the construction of the DeepScaleR RL fine-tuning dataset.
- **Unique Records Searched**:
  - Total Raw Items Downloaded: $40,315 + 4,428 = 44,743$ records.
  - Total Unique Training/Lineage Examples: $40,315 + 4,428 - 3501 = \mathbf{41,242}$ unique items.

---

## 2. Manuscript Wording Lock

> [!IMPORTANT]
> **Rhetorical Precision Rules**:
> 1. Do NOT describe the audit as searching "44,743 independent training sources".
> 2. Always describe the audit search space as **"44,743 total records across the DeepScaleR-Preview dataset ($N=40,315$) and Omni-MATH benchmark lineage ($N=4,428$)"**.

---
