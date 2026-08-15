# STAGE 7.2 CONFIRMATORY PREREGISTRATION (FINAL LOCK)

**Date**: August 16, 2026  
**Status**: `FIVE-SEED CONFIRMATORY DESIGN SEALED; EXECUTION PENDING AUTHORIZATION`  

---

## 1. PRIMARY DIRECTIONAL TEST ($N=5$ FRESH SEEDS)

* **Fresh Confirmatory Seeds**: $\omega \in \{43, 44, 45, 46, 47\}$ ($N=5$). Seed 42 is quarantined as pilot reference.
* **Exact One-Sided Sign Test**:
  - $H_0: \mathbb{P}(\Delta_{\text{late, } \omega} > 0) \le 0.5$
  - $H_1: \mathbb{P}(\Delta_{\text{late, } \omega} > 0) > 0.5$
  - Rejection Rule: Rejects $H_0$ if and only if **all 5 fresh seed effects are positive** ($\Delta_{\text{late, } \omega} > 0$ for all $\omega \in \{43, 44, 45, 46, 47\}$), yielding exact $P = 0.03125 < 0.05$.

---

## 2. DUAL MECHANISTIC INTERSECTION-UNION REQUIREMENT

A positive mechanistic claim requires **BOTH** component hypotheses to hold simultaneously across all 5 fresh seeds:

1. **Component A (Value Advantage)**: $\Delta_{\text{late, } \omega} > 0$ for $5/5$ fresh seeds.
2. **Component B (Behavioral Recovery Action Advantage)**: $\text{RAI}_{\omega} > 0$ for $5/5$ fresh seeds, where:
   $$\text{RAI}_{\omega} = \left[\mathbb{P}_{\text{FULL}}(a_{\text{rec}} | S_R) - \mathbb{P}_{\text{PREFIX}}(a_{\text{rec}} | S_R)\right] - \left[\mathbb{P}_{\text{FULL}}(a_{\text{rec}} | S_C) - \mathbb{P}_{\text{PREFIX}}(a_{\text{rec}} | S_C)\right]$$

If either component fails, the mechanistic claim is rejected.
