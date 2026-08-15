# STRUCTURAL OOD GENERATION PROTOCOL

**Date**: August 16, 2026  

---

## 1. THREE-TIER DISTRIBUTION GENERATION

1. **$D_{\text{train}}$**: Graph topologies with branching factor $b=3$, dead-end depth $d=2$.
2. **$D_{\text{IID\_test}}$**: Unseen random seeds from identical generator ($b=3, d=2$).
3. **$D_{\text{structural\_OOD}}$**: topographically altered graphs with $b=5$, dead-end depth $d=4$, misleading transition motifs, and sequential multi-recovery paths. Action semantics remain invariant.
