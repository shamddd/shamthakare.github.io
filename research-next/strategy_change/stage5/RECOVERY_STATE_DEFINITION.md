# RECOVERY-CRITICAL STATE DEFINITION ($S_R$) VS MATCHED CONTROL ($S_C$)

**Date**: August 16, 2026  

---

## 1. FORMAL ENVIRONMENT-DRIVEN RECOVERY STATE CRITERIA

Let $V^*(s)$ be the optimal goal reachability probability from state $s$. Let action regret be $\text{Regret}(s, a) = V^*(s) - V^*(P(s, a))$.

A state $s \in \mathcal{S}$ is defined as **Recovery-Critical ($s \in S_R$)** IF AND ONLY IF:
1. **Reachable Post-Error**: $s$ is reachable after an earlier plausible but suboptimal decision $a_{\text{sub}}$.
2. **Restorable Path**: $\exists a_{\text{rec}} \in \mathcal{A}(s)$ such that $V^*(P(s, a_{\text{rec}})) = 1.0$.
3. **Failure on Continuation**: Continuing the locally preferred greedy branch causes terminal failure ($V^*(P(s, a_{\text{greedy}})) = 0.0$).
4. **Model Independence**: Definition depends strictly on environment transition matrix $P$ and $V^*$, entirely independent of evaluated model outputs.

---

## 2. MATCHED ORDINARY CONTROL STATES ($S_C$)

Matched control states $s \in S_C$ are constructed to match $S_R$ on:
* Trajectory depth $t$.
* Branching factor $|\mathcal{A}(s)|$.
* Distance-to-goal $d(v_t, g)$.
* Tokenized observation length.
