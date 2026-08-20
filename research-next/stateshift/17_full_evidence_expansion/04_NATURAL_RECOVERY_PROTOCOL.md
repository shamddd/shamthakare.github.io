# PHASE 2 STAGE A — NATURAL SELF-CORRECTION EXPERIMENTAL PROTOCOL (`StateShift-NaturalRecovery`)

**Milestone**: Prospective Natural Error & Autonomous Recovery Protocol  
**Study Identifier**: `StateShift-NaturalRecovery`  

---

## 1. Research Question & Rationale

The existing StateShift Recovery condition injects a controlled locally invalid state. It does NOT measure whether the model naturally generates and self-corrects its own errors. `StateShift-NaturalRecovery` tests:

> "When the unmodified model naturally produces an invalid intermediate reasoning step during unprompted generation, does it subsequently recover to a valid final answer without external intervention?"

---

## 2. Experimental Design

* **Sample Population**: $N=200$ complex multi-step reasoning problems.
* **Unmodified Rollouts**: $K=16$ unperturbed rollouts per problem.
* **Sampling Parameters**: $T=0.6, \text{top\_p}=0.95, \text{max\_tokens}=512$.
* **Natural Recovery Outcome**: $\text{NATURAL\_RECOVERY\_SUCCESS} \in \{0, 1\}$.
* **Pilot Compute Requirement**: $3,200$ rollouts $\approx 0.39$ GPU-hours $\approx$ **`$0.63 USD`**.

*Signed by Principal ML Research Scientist & LLM Post-Training Researcher*
