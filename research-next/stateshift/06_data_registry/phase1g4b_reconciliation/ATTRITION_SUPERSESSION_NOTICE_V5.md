# ATTRITION LEDGER SUPERSESSION NOTICE (V5)

**Superseded Ledger**: Phase 1G.4a Ledger V4 ($468 \text{ registered} + 1 \text{ no-transition} + 2 \text{ no-mutation} = 471$)  
**Authoritative Active Ledger**: Phase 1G.4b Ledger V5 ($465 \text{ registered} + 1 \text{ no-transition} + 5 \text{ no-mutation} = 471$)  

---

## Formal Supersession Rationale

In Phase 1G.4b, `OP_TERM_SWAP` was removed from the admissible perturbation engine because swapping equality sides ($A=B \iff B=A$) is logically equivalent and does not produce a mathematically invalid assertion. Additionally, text corruption in `math500_498` was eliminated.

Registry V4 contains **exactly 465 registered problem pairs**. The active authoritative ledger is hereby frozen as:
$$\mathbf{465 \text{ FINAL\_REGISTERED} + 1 \text{ NO\_VERIFIABLE\_TRANSITION} + 5 \text{ NO\_EFFECT\_MUTATION} = 471 \text{ TOTAL PRIMARY POOL}}$$

All future manuscript and protocol references shall cite **$N = 465$** for the primary state registry.

---
