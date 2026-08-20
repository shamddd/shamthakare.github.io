# STATE-MATCHED CONTROLLED POLICY COMPARISON PROTOCOL

**Date**: August 16, 2026  

---

## 1. STATE-MATCHED PROTOCOL

To compare policies $\pi_{\text{BASE}}$, $\pi_{\text{PREFIX}}$, and $\pi_{\text{FULL-RLVR}}$:
1. Fix externally controlled environment state $s \in S_R \cup S_C$.
2. Supply identical action set $\mathcal{A}(s)$, observation $o(s)$, history $h(s)$, and verifier.
3. Sample $M=100$ continuation trajectories per policy to estimate value $V^\pi(s) = \mathbb{E}_{\tau \sim \pi}[R(\tau)|s]$.
