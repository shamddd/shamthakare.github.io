# Program 1 Claim Sanitization & Prospective Correction Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Formally identify and sanitize all statements from Checkpoint 2 that accidentally presented prospective hypotheses as observed empirical results prior to experimental execution.

---

## 1. Sanitization Table

| Location | Original Statement (Accidental Result Claim) | Corrected Prospective Statement (Sanitized Hypothesis) | Scientific Rationale |
|---|---|---|---|
| Checkpoint 2 Summary | *"We demonstrate that post-training RLVR/GRPO advantage normalization induces trajectory homogenization..."* | *"We **hypothesize that** post-training RLVR/GRPO advantage normalization induces trajectory homogenization..."* | Replaces declarative claim ("demonstrate") with prospective testing language before observing pilot data. |
| Checkpoint 2 Summary | *"degrading selective classification Area Under Risk-Coverage (AURC) by >40% relative to base models."* | *"and evaluate whether selective classification Area Under Risk-Coverage (AURC) degrades relative to pre-RLVR base models."* | Removes arbitrary hard-coded numerical outcome ($>40\%$) prior to experimental observation. |
| Checkpoint 2 Summary | *"driving majority-vote agreement to 1.0 even on incorrect answer clusters..."* | *"evaluating whether majority-vote agreement spikes on incorrect answer clusters..."* | Replaces hard-coded threshold ($1.0$) with statistical distribution comparison. |
| `PROGRAM1_FINAL_RQ.md` | *"causing high sample agreement ($S_{\text{ans}} \ge 0.80$) on incorrect answer clusters through trajectory homogenization ($J_{\text{path}} \ge 0.80$)..."* | *"and test whether self-consistency agreement decouples from empirical correctness on multi-step reasoning."* | Removes hard-coded operational thresholds ($S_{\text{ans}} \ge 0.80, J_{\text{path}} \ge 0.80$) from the primary scientific novelty claim. |
| `PROGRAM1_PREREGISTRATION.md` | *"driving Brier score ($\mathcal{B}$) up by $\ge 30\%$ due to trajectory homogenization ($J_{\text{path}} \ge 0.80$)."* | *"and evaluate Brier score ($\mathcal{B}$) and trajectory similarity ($J_{\text{path}}$) metrics across pre- vs post-RLVR conditions."* | Replaces unobserved percentage spikes with formal hypothesis-testing endpoints. |

---

## 2. Mandatory Rules for Prospective Claims

1. No statement may claim a scientific finding, percentage change, or threshold violation before empirical generation data is logged in `results/`.
2. All research questions and novelty claims must use verbs such as *investigate*, *test*, *evaluate*, *compare*, or *examine*.
3. Hard-coded operational thresholds ($S_{\text{ans}} \ge 0.80$, $J_{\text{path}} \ge 0.80$, $15\%$ AURC degradation) remain valid as preregistered operational decision gates in `PROGRAM1_PREREGISTRATION.md`, but must never define the core scientific novelty claim.
