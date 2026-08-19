# PHASE 2 — AIJ MANUSCRIPT ARCHITECTURE

**Target Journal**: *Artificial Intelligence* (AIJ)  
**Formatting Standard**: Elsevier `elsarticle.cls` Single-Column Format  

---

## 1. Section Hierarchy

1. **Title & Abstract**: Canonical title, 200-word locked abstract, keywords, Highlights.
2. **1. Introduction**: Limitations of aggregate accuracy, state-conditioned reasoning paradigm, summary of main contributions.
3. **2. Background and Related Work**:
   * 2.1 Reinforcement Learning from Verifier Feedback (RLVR/GRPO)
   * 2.2 Process Supervision and Step-Level Verifiers
   * 2.3 Categorical Self-Correction Literature Taxonomy
4. **3. The StateShift Framework**:
   * 3.1 Problem Formalization and State Definitions
   * 3.2 Target-Transition Success Estimand ($\Gamma_t$)
   * 3.3 Matched Recovery vs. Control Pair Construction
5. **4. Experimental Methodology**:
   * 4.1 Model Lineage (`Qwen2.5-7B` / `DeepScaler-4k`)
   * 4.2 Problem Registries and Contamination Filtering
   * 4.3 Deterministic Verification and Execution Engine
6. **5. Controlled State-Conditioned Evaluation (Study A)**:
   * 5.1 Primary Endpoint Interaction ($\Gamma_{256} = +0.1176$)
   * 5.2 Strict Decontamination Sensitivity ($N=388, \Gamma_{256,\text{Strict}} = +0.1160$)
7. **6. Post-Training Trajectory Analysis**:
   * 6.1 Complete Nine-Checkpoint Empirical Trajectory
   * 6.2 Order-Restricted Non-Decreasing Trajectory Analysis
   * 6.3 Earliest Available Checkpoint Detectability ($t=32$)
8. **7. Natural Post-Error Recovery (Study B)**:
   * 7.1 Unperturbed Rollout Protocol and Error Event Rules
   * 7.2 Natural Error Incidence ($\text{NEI} = 18.19\%$)
   * 7.3 Conditional Natural Post-Error Recovery Rate ($\text{NRR} = 30.93\%$)
9. **8. Discussion**:
   * 8.1 Behavioral Structure Obscured by Aggregate Accuracy
   * 8.2 Implications for Model Evaluation and Verification
10. **9. Limitations**:
    * 9.1 Non-Claims (No Strict Monotonicity, No Exact Step Emergence)
    * 9.2 Scope Boundaries (Single Lineage, Math Domain)
11. **10. Declarations & Reproducibility**: Competing Interests, Funding, CRediT Roles, Data Availability.
12. **References**: Elsevier style bibliography.

*Signed by Senior Scientific Writer & Technical Editor*
