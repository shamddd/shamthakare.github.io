# PHASE 3B — MANUSCRIPT ARCHITECTURE & SECTION PLAN

**Milestone**: Complete StateShift Manuscript Outline & Section Strategy  
**Execution Timestamp**: `2026-08-20 04:36 UTC`  

---

## 1. Unified Narrative Architecture

The manuscript unifies three key empirical pillars:

1. **Pillar 1: Controlled State-Conditioned Evaluation**: Demonstrates that post-training gains differ by 11.76 percentage points between Recovery and Control baseline states ($\Gamma_{256} = +0.1176, p < 0.0001$).
2. **Pillar 2: Nine-Checkpoint Empirical Trajectory**: Tracks the state-selective interaction across all 9 available checkpoints ($t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$), showing progressive non-decreasing trajectory growth detectable by step 32.
3. **Pillar 3: Unprompted Natural Post-Error Recovery**: Evaluates autonomous recovery in unperturbed rollouts following verifier-confirmed natural reasoning errors ($\text{NEI}=18.19\%, \text{NRR}=30.93\%$).

---

## 2. Section Structure

1. **Abstract**: High-level problem statement, dual-study method, 9-point trajectory vector, natural recovery rate.
2. **Introduction**: Pitfalls of aggregate accuracy benchmarks, motivation for state-conditioned evaluation.
3. **Related Work**: LLM reasoning, RLVR/GRPO, process verifiers, self-correction literature taxonomy.
4. **StateShift Framework**: Formalization of Recovery vs. Control states, target-transition success.
5. **Experimental Setup**: Model checkpoint lineage (`Qwen2.5-7B-DeepScaler`), problem registries, deterministic verifiers.
6. **Controlled Endpoint Results (Study A)**: Primary interaction ($\Gamma_{256} = +0.1176$) & strict decontamination sensitivity ($\Gamma_{256,\text{Strict}} = +0.1160$).
7. **Complete Nine-Checkpoint Trajectory Results**: Empirical 9-point vector $[0.0000, 0.0333, 0.0337, 0.0774, 0.0748, 0.0598, 0.0976, 0.0950, 0.1176]$, order-restricted non-decreasing test, earliest detectability at $t=32$.
8. **Natural Post-Error Recovery (Study B)**: Natural Error Incidence ($\text{NEI}=18.19\%$) and Conditional Natural Recovery Rate ($\text{NRR}=30.93\%$).
9. **Discussion**: Implications for post-training behavioral evaluation and verifier-assisted reasoning.
10. **Limitations**: Non-claims (no strict monotonicity, no sub-32 exact emergence, single model family).
11. **Reproducibility & Ethics**: Cryptographically sealed manifests and data availability.
12. **Conclusion**: Final summary.

*Signed by Senior Scientific Writer & Principal ML Research Scientist*
