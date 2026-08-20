# DECISIVE KILL EXPERIMENT: INTERVENTION FRONTIERS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. OBJECTIVE & EXPERIMENTAL DESIGN

The goal of the kill experiment is to test whether parameter-efficient RLVR ($A_3$) can produce non-zero accuracy on tasks where the base model has zero support under $10,000$ samples ($A_1$).

### Model Checkpoint:
* `SmolLM2-360M-Instruct`

### Task Set:
* **Synthetic 5-Step Modular Composition Task (ModComp-5)**: Requires computing $f(x) = (((x \cdot a_1 + b_1) \pmod{p} \cdot a_2 + b_2) \pmod{p} \dots)$ for 5 sequential steps.
* Constructed such that base policy `SmolLM2-360M` has **Pass@10,000 = 0** ($0 / 10,000$ correct rollouts).

### Intervention Conditions Evaluated:
1. **$A_1$ (Reweighting Null)**: $N = 10,000$ rollouts from base model ($T=0.7$, $p=0.95$), verifier filtered.
2. **$A_3$ (Prefix-RLVR)**: 16 learned prefix tokens trained via GRPO for 100 steps ($\sim 0.05\%$ parameters updated).
3. **$A_5$ (Full RLVR)**: Standard GRPO updating 100% of parameters for 100 steps.

---

## 2. EXPLICIT FALSIFICATION CRITERIA (KILL RULES)

The hypothesis $H_1$ is **KILLED** if any of the following occur:

* **Kill Condition K1 (Null Dominance)**: $A_1$ (Best-of-$10,000$) achieves non-zero accuracy ($> 5\%$) on ModComp-5, proving the task was within the pre-existing reweighting support of the base model.
* **Kill Condition K2 (Prefix Failure)**: $A_3$ (Prefix-RLVR) fails to achieve $> 5\%$ accuracy after 100 GRPO steps, proving minimal parameter interventions cannot cross the support expansion boundary.
* **Kill Condition K3 (Full RL Dominance)**: $A_5$ (Full RLVR) achieves $> 30\%$ accuracy while $A_3$ achieves $0\%$, proving full parameter updates are mandatory for support expansion.

If $K1$, $K2$, or $K3$ triggers, the Intervention Frontier hypothesis is falsified and the project is halted immediately.

---

## 3. PRE-REGISTERED SUCCESS CRITERION

$$\text{Success} \iff \text{Acc}(A_1, N=10,000) = 0\% \quad \text{AND} \quad \text{Acc}(A_3, \text{Prefix-RLVR}) \ge 15\%$$

This outcome proves that a minimal parameter-efficient intervention ($A_3$) induces true support expansion where massive inference-time search ($A_1$) completely fails.
