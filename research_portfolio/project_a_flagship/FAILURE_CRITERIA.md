# FAILURE CRITERIA & PILOT GATE PROTOCOL — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Pilot Gate Classification Framework

Before committing full multi-seed compute resources, a pilot experiment (100 training steps on `CausalTool-Env` and InterCode-Bash) will be executed. The pilot outcome will be classified under one of 5 strict categories:

```
====================================================================================================
PILOT DECISION TREE
====================================================================================================
Category A: Strong Empirical Support
   ├── Action: Proceed to full 3-seed benchmark execution and paper drafting.
Category B: Weak / Ambiguous Signal
   ├── Action: Run diagnostic trace audit; test if learning rate or group size requires re-scaling.
Category C: Negative Finding, Scientifically Clean
   ├── Action: Freeze method; pivot to publishable negative diagnostic on agent credit assignment.
Category D: Implementation / Environment Invalidity
   ├── Action: Quarantine code; fix environment harness bugs and re-run pilot.
Category E: Direct Prior-Art Collision
   ├── Action: Immediately terminate project.
====================================================================================================
```

---

## 2. Definitive Failure & Rejection Thresholds

The project hypothesis is declared **FALSIFIED** if any of the following conditions occur:

1. **Criterion F1 (Statistical Ineffectiveness)**:
   - C3A held-out Pass@1 does not exceed standard GRPO by at least $+2.0\%$ ($p \ge 0.05$) after 1,000 steps.
2. **Criterion F2 (Negative Control Equivalence)**:
   - The permuted-credit control ($\text{C3A}_{\text{perm}}$) achieves test accuracy within $\pm 1.0\%$ of true C3A, demonstrating that credit timing is causally irrelevant.
3. **Criterion F3 (Gradient Variance Explosion)**:
   - The empirical policy gradient trace variance under C3A is higher than standard GRPO ($V_{\text{C3A}} > V_{\text{GRPO}}$).
4. **Criterion F4 (Compute-Matched Domination)**:
   - Compute-matched GRPO ($G=8$) achieves higher accuracy and equal sample efficiency compared to C3A ($G=4$ + ablation).

---

## 3. Policy on Negative Results

In the event of falsification under Criteria F1 or F2, the project will **NOT** be discarded or modified post-hoc with ad-hoc tuning. Instead, following the precedent established in `ear_grpo_reasoning`, the result will be written as a high-impact diagnostic manuscript:
> *"When Counterfactual Interventions Fail to Disentangle Agent Policy Gradients: Pitfalls of Step-Level Credit in Non-Markovian Tool Environments"*
and targeted at *Transactions on Machine Learning Research (TMLR)* or *IEEE TAI*.
