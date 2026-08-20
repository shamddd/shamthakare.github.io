# Author Response & Rebuttal Document

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Target Venues**: JMLR (Preserved), IEEE TDSC, IEEE TPDS, IEEE TCC.

---

## Response to Reviewer 1 (Novelty & Prior Art)

* **R1 Concern (JMLR Submission)**: Re-confirmed preservation of JMLR manuscript.
  - **Author Response**: We confirm that the JMLR submitted manuscript (*Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study*) remains 100% preserved and untouched, with zero dual-submission or competing submission actions. Post-submission future work has been cleanly separated.
* **R1 Concern (`secure-cloud-infrastructure-platform`)**: Clarify distinction between static AST graph checking and dynamic eBPF runtime monitoring.
  - **Author Response**: We have added an explicit subsection in Section 3 ("System Boundary") clarifying that static AST invariant checking serves as a pre-admission deployment control gate, complementing rather than replacing dynamic kernel-level eBPF instrumentation.

---

## Response to Reviewer 2 (Methodology & Statistics)

* **R2 Concern (`enclaveshield`)**: Add standard deviation error bars to latency distribution CDF plots.
  - **Author Response**: We have updated `scripts/generate_figures.py` to plot shaded 95% confidence intervals and explicit standard deviation bars on all page access latency CDF curves ($N=5$ seeds).
* **R2 Concern (`quorumshift`)**: Clarify joint-consensus epoch transition invariants.
  - **Author Response**: We added formal proof sketches in Section 4.2 demonstrating that quorum configuration changes follow Raft Joint Consensus transitions ($C_{\text{old,new}}$), guaranteeing that read and write quorums intersect at all times during network partition recovery ($S_{\text{stale}} = 0$).

---

## Response to Reviewer 3 (Reproducibility & Systems)

* **R3 Praise**: Confirmed full pass across all unit test suites and CLI artifact reproduction commands.
  - **Author Response**: We thank Reviewer 3 for evaluating the reproducibility package. All lockfiles (`uv.lock`) and script entrypoints have been pinned and verified.
