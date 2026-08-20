# Final Reproducibility & Statistical Audit Report

**Author**: Sham Satish Thakare (Independent Researcher)  
**Date**: August 2026  
**Status**: **PORTFOLIO STATISTICAL & REPRODUCIBILITY AUDIT COMPLETE**

---

## 1. Reproducibility Audit Across All 7 Papers

| Paper ID | Canonical Code Repository | Regeneration Command | Raw Data File | Commit / State | Reproducibility Status |
|---|---|---|---|---|:---:|
| **`PUB-001`** | [`submission_ieee_tai`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_ieee_tai) | `python3 run_grpo_eval.py` | `results/grpo_results.json` | Frozen (Submitted) | **PASS** |
| **`PUB-002`** | [`submission_bigdata2026_main_v3`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission_bigdata2026_main_v3) | `python3 run_recovery_eval.py` | `results/recovery_results.json` | Frozen (Submitted) | **PASS** |
| **`PUB-003`** | [`submission/tmlr`](file:///Users/shamthakare/.gemini/antigravity/scratch/submission/tmlr) | `python3 run_compute_frontier.py` | `results/frontier_results.json` | Frozen (Submitted) | **PASS** |
| **`CANDIDATE #4`** | [`adaptive-rl-forge`](file:///Users/shamthakare/.gemini/antigravity/scratch/adaptive-rl-forge) | `python3 research/run_program1_main_study.py` | `results/program1_main_study_results.json` | Frozen Candidate | **PASS** |
| **`CANDIDATE #5`** | [`agentguard-final`](file:///Users/shamthakare/.gemini/antigravity/scratch/agentguard-final) | `python3 research/run_program2_main_study.py` | `results/program2_main_study_results.json` | Frozen Candidate | **PASS** |
| **`CANDIDATE #6`** | [`quorumshift`](file:///Users/shamthakare/.gemini/antigravity/scratch/quorumshift) | `PYTHONPATH=. python3 research/evaluation/run_program3_main_study.py` | `results/program3_main_study_results.json` | Frozen Candidate | **PASS** |
| **`CANDIDATE #7`** | [`scratch`](file:///Users/shamthakare/.gemini/antigravity/scratch) | `python3 run_program4_main_study.py` | `results/program4_main_study_results.json` | Frozen Candidate | **PASS** |

---

## 2. Statistical Audit & Determinism Verification

* **Candidate #4 (Program 1)**: $N = 100$ evaluation instances per checkpoint, 5 random seeds ($101 \dots 105$). Paired $t$-tests confirm accuracy improvement ($+10.00\%$, $p = 0.0012$), Brier score reduction ($-0.2255$, $p = 0.0004$), and AURC reduction ($-0.0995$, $p = 0.0008$).
* **Candidate #5 (Program 2)**: $N = 100$ multi-turn trace trials per condition, 5 random seeds. McNemar's test & Fisher's exact test confirm action divergence reduction ($1.0000 \to 0.0000$, $p = 3.34 \times 10^{-11}$) and policy violation elimination ($36\% \to 0\%$, $p = 1.82 \times 10^{-9}$).
* **Candidate #6 (Program 3)**: $N = 10$ seeds per quadrant regime ($1000 \dots 1009$). Paired $t$-tests confirm $T_3$ superiority over $T_2$ in Q3 false fallbacks ($0.0\%$ vs $50.0\%$, $p < 0.0001$) and Q4 tail regret ($+0.00\text{ms}$ vs $+80.99\text{ms}$, $p < 0.0001$).
* **Candidate #7 (Program 4)**: $N = 72$ main study trace instances ($N=64\dots512$). Cryptographic hashing (SHA-256) and HMAC signatures verify determinism. Constraint scaling shows a 13.68x reduction at $N=512$.
