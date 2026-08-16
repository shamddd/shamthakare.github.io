# EXPERIMENTAL UNIT ACCOUNTING

**Date**: August 16, 2026  

---

## 1. CANONICAL HIERARCHICAL ACCOUNTING

* **Problem Level**: 20 distinct GSM8K evaluation problems.
* **Matched Pair Level**: 20 matched pairs ($1 S_R + 1 S_C$ per problem).
* **State Level**: 40 total evaluation states ($20 S_R, 20 S_C$).
* **Policy Arm Level**: 2 released checkpoint-interface policy configurations (`BaseModelAdapter` vs `InstructModelAdapter`).
* **Replicate Level**: 5 stochastic rollouts per state per policy arm ($T=0.7, p=0.9$).

$$\boxed{\text{TOTAL PRIMITIVE GENERATIONS} = 20 \text{ problems} \times 2 \text{ states/problem} \times 2 \text{ policies} \times 5 \text{ rollouts} = 400 \text{ primitive rollouts}}$$
