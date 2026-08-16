# KILL EXPERIMENT V2: EMPIRICAL PHASE DIAGRAM a*(Q, d)

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. PREFERRED INTERVENTION MATRIX a*(Q, d)

| Query Horizon Q | IID Regime (ModComp-3) | OOD-LENGTH (ModComp-5) | OOD-RECOMBINATION |
| :--- | :--- | :--- | :--- |
| **Q = 1** | `A0 (Base)` | `A0 (Base)` | `A0 (Base)` |
| **Q = 10** | `A1 (Best-of-N=4)` | `A1 (Best-of-N=4)` | `A1 (Best-of-N=4)` |
| **Q = 100** | `A1 (Best-of-N=16)` | **`A3 (Full RLVR)`** | `A1 (Best-of-N=16)` |
| **Q = 1,000** | `A1 (Best-of-N=16)` | **`A3 (Full RLVR)`** | **`A2 (LoRA-RLVR)`** |
| **Q = 10,000** | **`A3 (Full RLVR)`** | **`A3 (Full RLVR)`** | **`A2 (LoRA-RLVR)`** |
| **Q = 100,000** | **`A3 (Full RLVR)`** | **`A3 (Full RLVR)`** | **`A2 (LoRA-RLVR)`** |

*Conclusion*: Different intervention classes occupy genuinely distinct optimality regions across deployment query volume Q and distribution shift d.
