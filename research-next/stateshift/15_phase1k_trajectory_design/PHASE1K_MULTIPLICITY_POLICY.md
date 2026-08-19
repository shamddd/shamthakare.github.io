# PHASE 1K SECONDARY MULTIPLICITY POLICY

**Milestone**: Phase 1K Multiple Testing Policy Freeze  
**Execution Timestamp**: `2026-08-20 01:11 UTC`  
**Auditor**: Lead Statistical Methodologist & Scientific Integrity Auditor  

---

## 1. Selected Multiplicity Policy

Because Phase 1K evaluates 7 intermediate checkpoints ($t \in \{32, 64, 96, 128, 160, 192, 224\}$), evaluating per-checkpoint hypothesis tests without multiplicity control risks inflating Type-I error.

The prespecified multiplicity control strategy is **`OPTION B: SIMULTANEOUS PROBLEM-BLOCKED BOOTSTRAP CONFIDENCE BANDS`**.

### Specification:
1. **Simultaneous Confidence Bands**: Problem-blocked bootstrap ($B=10,000$) derives joint 95% simultaneous percentile confidence bands across all 9 trajectory points $\mathbf{G} = [\Gamma_0, \dots, \Gamma_{256}]$.
2. **False Discovery Rate (FDR) Adjustment**: For secondary pairwise checkpoint comparisons, Benjamini-Hochberg FDR correction ($\alpha = 0.05$) is applied across the 7 intermediate checkpoints.
3. **Descriptive Labeling**: All intermediate checkpoint comparisons are explicitly reported as secondary/exploratory contrasts, leaving the primary confirmatory claim $\Gamma_{256} = +0.1176$ as the solitary primary inference.

*Signed by Lead Statistical Methodologist & Scientific Integrity Auditor*
