# FORENSIC PROJECT AUDIT: STATESHIFT SCIENTIFIC REBUILD

**Project**: StateShift: Tracking State-Dependent Reasoning Recovery Across Post-Training  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Previous Submission**: *Artificial Intelligence* (Elsevier / AIJ), Manuscript ID: ARTINT-D-26-01491  
**Editorial Status**: Rejected  
**Audit Timestamp**: `2026-08-26 23:10 UTC`  

---

## 1. Forensic Project Claim Traceability Table

| Claim ID | Claim Description | Manuscript Location | Raw Evidence File | Reproduction Code | Verified? | Scientific Problem / Limitation |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **C1** | Base-to-step-256 state-by-checkpoint interaction ($\Gamma_{256} = +0.1176$, 95% CI $[+0.0955, +0.1400]$) | Section 4.1, Table 1, Fig 3 | `artifacts/endpoint/controlled_endpoint_outcomes.csv` | `scripts/reproduce_analysis.py` | **`VERIFIED`** | Evaluated on single model family (`Qwen2.5-7B-deepscaler`) and single math dataset (`MATH-500`). |
| **C2** | Strict decontamination subgroup interaction ($\Gamma_{256,\text{Strict}} = +0.1160$, 95% CI $[+0.0913, +0.1408]$) | Section 4.2, Table 1 | `artifacts/endpoint/strict_decontamination_subset.csv` | `scripts/reproduce_analysis.py` | **`VERIFIED`** | Decontamination filtering is static; does not account for algorithmic overlap in post-training pre-filtering. |
| **C3** | 9-checkpoint empirical trajectory vector $\mathbf{\Gamma} = [0, .0333, .0337, .0774, .0748, .0598, .0976, .0950, .1176]$ | Section 5.1, Figure 2 | `artifacts/trajectory/nine_checkpoint_trajectory.csv` | `scripts/reproduce_analysis.py` | **`VERIFIED`** | Intermediate steps $t \in \{32..224\}$ evaluated at low sample size ($K=2$), creating local sampling noise dips ($96\to 128$). |
| **C4** | Interaction detectable at earliest available checkpoint $t=32$ ($\Gamma_{32} = +0.0333$, multiplicity-adj 95% CI $[+0.0011, +0.0655]$) | Section 5.2, Figure 2 | `artifacts/trajectory/intermediate_checkpoint_cell_means.csv` | `stateshift/statistics/bootstrap.py` | **`VERIFIED`** | Checkpoints $t \in (0, 32)$ do not exist in lineage; exact step emergence is unidentifiable. |
| **C5** | Trajectory consistent with non-decreasing trend under order-restricted analysis (PAVA) | Section 5.3 | `artifacts/trajectory/nine_checkpoint_trajectory.csv` | `stateshift/trajectory/order_restricted.py` | **`VERIFIED`** | Order-restricted fit proves trend consistency but cannot rule out intermediate plateauing or non-monotonicity. |
| **C6** | Natural Error Incidence ($\text{NEI} = 18.19\%$, $582/3200$ rollouts) | Section 6.1, Figure 4 | `artifacts/natural_recovery/natural_error_episodes.csv` | `stateshift/statistics/metrics.py` | **`VERIFIED`** | Endogenous error occurrence is prompt- and problem-dependent; not controlled counterfactually. |
| **C7** | Conditional Natural Post-Error Recovery Rate ($\text{NRR} = 30.93\%$, 95% CI $[27.19\%, 34.82\%]$) | Section 6.2, Figure 4 | `artifacts/natural_recovery/natural_recovery_episodes.csv` | `stateshift/statistics/metrics.py` | **`VERIFIED`** | Natural recovery is subject to survivorship bias; rollouts with errors may differ systematically from non-error rollouts. |
| **C8** | Immutable Model Provenance (Commit SHAs for $t \in \{0..256\}$) | Section 3.2, Table 2 | `artifacts/provenance/checkpoint_provenance.csv` | `tests/test_provenance.py` | **`VERIFIED`** | Single training lineage (`DeepScaler-4K`); zero cross-model or cross-dataset validation. |

---

## 2. Core Scientific Deficiencies of the Rejected Manuscript

1. **Lack of Conceptual Depth & Model Generality**:
   * The paper evaluated a single model lineage (`Qwen2.5-7B-deepscaler`) trained via GRPO on a single math dataset (`MATH-500`).
   * A top-tier journal like AIJ expects general AI findings that generalize across model scales (e.g. 1.5B, 7B, 14B, 32B), model architectures (e.g., Qwen, Llama), and reasoning domains (e.g., GSM8K, MATH, code generation, logic puzzles).

2. **Construct Validity Ambiguity**:
   * The paper operationally defined "state" as an injected string prefix containing a verifier-confirmed invalid step, and "recovery" as target-answer correctness following that prefix.
   * This is a **behavioral state** observation. The manuscript flirted with mechanistic claims ("the model learns to self-correct internal reasoning state") without providing model-internal mechanistic evidence (such as activation probing, attention allocation, or latent state dynamics).

3. **Confounder Control & Sampling Scope**:
   * The intermediate trajectory rollouts at $t \in \{32, 96, 160, 224\}$ were evaluated at low rollout depth ($K=2$), introducing sampling noise.
   * Item difficulty was treated homogeneously rather than controlling for problem-level difficulty strata or regression to the mean.

---

## 3. Forensic Conclusion & Next Steps

All 8 core empirical claims (**C1–C8**) are 100% reproducible from raw artifact data (`artifacts/`). However, the paper in its rejected form suffered from narrow scope (1 model family, 1 dataset), construct ambiguity (behavioral vs. mechanistic state), and lack of strong baseline models or cross-domain generalization.

*Signed by Principal ML Research Scientist & Reproducibility Auditor*
