# STATIC PROJECT FINAL RECORD & REFINED SCOPE

**Date**: August 16, 2026  

---

## 1. REFINED COLLISION CLASSIFICATION

1. **Sleep-time Compute (Lin et al., 2025, arXiv:2504.13171)**:
   > **Classification**: **`STRONG CONCEPTUAL OVERLAP`** on amortizing offline compute over multiple future queries. It does not necessarily cover parameter-updating adaptation such as SFT/LoRA/RLVR.
2. **Snell et al. (ICLR 2025, arXiv:2408.03314)**:
   > **Classification**: **`STRONG OVERLAP`** on difficulty/competence-conditioned test-time compute; **`PARTIAL OVERLAP`** on one-time learned adaptation vs repeated search.
3. **Roberts et al. (2026, arXiv:2604.01411)**:
   > **Classification**: **`STRONG OVERLAP`** on joint training-inference FLOP optimization and overtraining to reduce inference cost.
4. **Lower-Envelope Concavity**:
   > Downgraded $J^*(Q) = \min_a (F_a + c_a Q)$ from theoretical contribution to a **`STANDARD STRUCTURAL LEMMA`** (standard property of lower envelopes of affine functions).

---

## 2. REFINED NO-GO STATEMENT FOR STATIC FORMULATION

> *"The current deterministic, known-horizon, stationary-cost adaptation-versus-search formulation does not establish sufficient novelty for a JMLR submission."*
