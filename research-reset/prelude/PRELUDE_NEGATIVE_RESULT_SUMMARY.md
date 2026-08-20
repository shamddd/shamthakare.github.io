# PRELUDE NEGATIVE RESULT SUMMARY

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Status**: PERMANENTLY TERMINATED (NO CONFIRMATORY SCALING / NO CONFERENCE SUBMISSION)  

---

## 1. SCIENTIFIC EXECUTIVE SUMMARY

Project PRELUDE evaluated whether frozen internal model-state diagnostics ($I$: reward-probe separability, effective rank, stable rank, gradient norms, gradient noise scale, LayerNorm gradient ratios) provide incremental out-of-family predictive value for marginal compute-normalized RLVR gain:
$$\Delta_{\mathrm{RLVR}}(M, D, C) = U(\mathcal{T}_{\mathrm{RLVR}}(M, D, C), D_{\text{test}}) - U(M, D_{\text{test}})$$
beyond strong behavioral baselines ($B$: Pass@1, Pass@8, Pass@64, prompt NLL, held-out loss) and headroom/training-history predictors ($H$: pretraining step age, base error rate $1-\text{Pass@1}$, failure rate $1-\text{Pass@64}$, empirical competence proximity).

In a pre-registered 18-run pilot across 3 model families (SmolLM2-360M, Pythia-410M, Qwen2.5-0.5B), 6 checkpoints, 2 task conditions, and 3 seed replications under strict Leave-One-Model-Family-Out Cross-Validation (LOMFO-CV):
* Baseline $M_1$ ($BH$) achieved held-out MAE = `0.0090`.
* Full model $M_5$ ($BH + I$) achieved held-out MAE = `0.0101`.
* Primary incremental gain $\Delta\text{MAE} = \text{MAE}_{M1} - \text{MAE}_{M5} = -0.0011$.
* Residual correlation between internal features and baseline prediction error $r = \Delta_{\text{RLVR}} - \hat{\Delta}_{\text{BH}}$ was near zero or slightly negative ($\rho \in [-0.042, -0.014]$).

---

## 2. PRECISE SCIENTIFIC BOUND

> **Scope Bound**: Within the tested models, tasks, GRPO protocol and diagnostic set, we detected no incremental predictive value for the evaluated frozen internal model-state features beyond the tested behavioral and headroom baselines.

---

## 3. IMMUTABLE PRESERVATION & GOVERNANCE RECORD

* All 18 run manifests, raw generation traces, design matrices, pre-registration documents, and forensic audit logs are preserved immutably in `research-reset/prelude/NEGATIVE_RESULT_PACKAGE/`.
* Dissemination is restricted to repository preservation and an internal technical note. No conference submissions or public uploads will be made.
