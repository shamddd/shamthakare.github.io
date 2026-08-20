# KILL EXPERIMENT V2: UTILITY-CONSTRAINED FRONTIER AUDIT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. DISTINCTION BETWEEN CROSSOVER CONCEPTS

1. **Cost Crossover ($Q_{\text{cost}}^*$)**: Query horizon where raw total FLOPs $C_{\text{total}}(a, Q) = C_{\text{total}}(b, Q)$.
2. **Utility-Constrained Crossover ($Q_{\text{utility}}^*(u)$)**: Query horizon where both methods achieve target accuracy threshold $u$.
3. **Frontier Crossover ($Q_{\text{frontier}}^*$)**: Query horizon where the preferred method changes on the utility-cost Pareto frontier.

## 2. MINIMUM COST TO REACH TARGET UTILITY $C_{\min}(Q, u)$

For target utility $u = 0.25$ on OOD-LENGTH (ModComp-5):
* $A_1$ Best-of-32 requires $N=32$ samples ($C_{\text{inf}} = 3.15 \times 10^{12}$ FLOPs/query).
* $A_3$ Full RLVR achieves $u=0.28$ at single-sample cost ($C_{\text{inf}} = 9.216 \times 10^{10}$ FLOPs/query).
* **Frontier Crossover $Q_{\text{frontier}}^*$**: Shifts to `79 Queries` on OOD-LENGTH.
