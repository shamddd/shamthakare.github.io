# PHASE 2 STAGE C0.1 — PROBLEM CLUSTERING & BOOTSTRAP AUDIT REPORT

**Milestone**: Problem-Level Uncertainty & Clustering Analysis  

---

## 1. Naive vs. Problem-Blocked Bootstrap Comparison ($B=10,000$)

| Estimand Metric | Sample Value | Naive Wilson 95% CI | Problem-Blocked Bootstrap 95% CI | Clustering Materiality |
| :--- | :---: | :---: | :---: | :---: |
| **Natural Error Incidence ($\text{NEI}$)** | `18.19%` ($582 / 3,200$) | `[16.89%, 19.55%]` | **`[16.84%, 19.50%]`** | **NO** ($\le 0.05\%$) |
| **Natural Recovery Rate ($\text{NRR}$)** | `30.93%` ($180 / 582$) | `[27.31%, 34.80%]` | **`[27.19%, 34.82%]`** | **NO** ($\le 0.12\%$) |

---

## 2. Publication Precision Selection

Although the clustering effect is minimal, the **`Problem-Blocked Bootstrap 95% CI [27.19%, 34.82%]`** is officially adopted as the primary uncertainty interval for manuscript publication.

*Signed by Lead Statistical Methodologist & Causal-Inference Reviewer*
