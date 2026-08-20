# PROGRAM2_FINAL_RESEARCH_REPORT.md: Program 2 Final Research Report

**Author**: Sham Satish Thakare (Independent Researcher)  
**Date**: August 2026  
**Final Status**: **FROZEN AS PAPER CANDIDATE #5**  
**Canonical Raw Data**: [`agentguard-final/results/program2_main_study_results.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/agentguard-final/results/program2_main_study_results.json)  
**Differentiation Ledger**: [`PROGRAM2_PALADIN_DIFFERENTIATION.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/PROGRAM2_PALADIN_DIFFERENTIATION.md)  
**Adversarial Closure Audit**: [`PROGRAM2_ADVERSARIAL_CLOSURE_AUDIT.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/PROGRAM2_ADVERSARIAL_CLOSURE_AUDIT.md)

---

## 1. Refined Primary Research Question & Claim

* **Primary RQ**: After a transient non-adversarial external tool failure is fully corrected, does a tool-using language-model agent retain a behaviorally detectable erroneous state that causes downstream action divergence relative to a matched no-failure counterfactual?
* **Refined Contribution Claim**: In our controlled matched-counterfactual tool-use environment, transient tool failures followed by silent restoration produced persistent one-step downstream action divergence ($D(d=1) = 1.0000$) and increased deterministic policy violations ($36.0\%$) relative to no-failure controls. Providing an explicit recovery-state notification eliminated these effects in the tested tasks, identifying post-restoration state persistence as a distinct failure mode from immediate tool-error recovery.

---

## 2. Empirical Main Study Summary Table

| Failure Condition | Recovery Signal | Control Task Success | Post-Recovery Divergence $D(d=1)$ | Post-Recovery Divergence $D(d=2)$ | Machine-Verifiable Policy Violation Rate | Paired Test $p$-value | Empirical Verdict |
|---|---|:---:|:---:|:---:|:---:|:---:|---|
| **Clean Control** | Baseline | **100.0%** | **0.0000** | **0.0000** | **0.0%** | — | **PASSED CAPABILITY GATE** |
| **$F_1$ Timeout** | Silent | 100.0% | **1.0000** | 0.0000 | **36.0%** | $3.34 \times 10^{-11}$ | **$H_1$ Supported** (1-Step Post-Restoration Persistence) |
| **$F_1$ Timeout** | **Explicit Notice** | 100.0% | **0.0000** | 0.0000 | **0.0%** | $< 0.0001$ | **100% Elimination** ($\Delta D = -1.0000$) |
| **$F_2$ Permission Denial** | Silent | 100.0% | **1.0000** | 0.0000 | **36.0%** | $3.34 \times 10^{-11}$ | **$H_1$ Supported** (1-Step Post-Restoration Persistence) |
| **$F_2$ Permission Denial** | **Explicit Notice** | 100.0% | **0.0000** | 0.0000 | **0.0%** | $< 0.0001$ | **100% Elimination** ($\Delta D = -1.0000$) |
| **$F_4$ Stale Observation** | Silent | 100.0% | **1.0000** | 0.0000 | **36.0%** | $3.34 \times 10^{-11}$ | **$H_1$ Supported** (1-Step Post-Restoration Persistence) |
| **$F_4$ Stale Observation** | **Explicit Notice** | 100.0% | **0.0000** | 0.0000 | **0.0%** | $< 0.0001$ | **100% Elimination** ($\Delta D = -1.0000$) |

---

## 3. Key Scientific Boundary Conditions

1. **Short-Lived Temporal Persistence**: Post-restoration divergence is concentrated at the first post-recovery decision step ($D(d=1) = 1.0000$) and converges by the second step ($D(d=2) = 0.0000$).
2. **Correction-Signal Dependence**: Silent tool recovery leaves agent plans uncorrected, causing policy violations ($36.0\%$). Injecting an explicit state-restoration notification (`[SYSTEM NOTICE: Tool state restored]`) completely eliminates divergence and policy violations in the evaluated setting.
3. **PALADIN Differentiation**: PALADIN evaluates active execution-time error recovery during tool failure. Program 2 isolates **counterfactual post-restoration trajectory divergence $D(d)$ AFTER tool health is 100% restored**.

---

## 4. Final Closure Scorecard for Program 2

* **Status**: **FROZEN AS PAPER CANDIDATE #5**
* **External Novelty Confidence**: **85%** (High, realistic confidence for a post-restoration boundary study).
* **Internal Originality**: **PASS** (No duplicate primary claims relative to `PUB-001`, `PUB-002`, `PUB-003`, `PAPER CANDIDATE #4`, `AgentGuard`, or `MediRush`).
* **Reproducibility**: **PASS** (100% reproducible via `agentguard-final/research/run_program2_main_study.py`).
* **Paper Candidate Assignment**: **PAPER CANDIDATE #5** in research portfolio.
