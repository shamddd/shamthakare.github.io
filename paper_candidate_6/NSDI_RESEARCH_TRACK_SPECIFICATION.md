# Paper Candidate #6 — Research Contribution Specification for NSDI Research Track

**Canonical Title**: *Trust but Verify the Predictor: Uncertainty-Gated Adaptive Consensus under Nonstationary Distribution Shift*  
**Author**: Sham Satish Thakare (Independent Researcher)  
**Target Venue**: USENIX NSDI Fall '27 Research Track  
**Repository**: `quorumshift` / `paper_candidate_6`

---

## 1. Canonical Systems Problem

Adaptive consensus controllers can improve write tail latency under familiar network conditions. However, deployment-time trust decisions cannot be based on input feature novelty alone. A networked system must decide whether an adaptive consensus action is **reliable**, not merely whether its current feature vector looks familiar.

---

## 2. Primary Research Question

Under temporally nonstationary workload and network conditions, can a reliability signal derived from predictive uncertainty distinguish harmful adaptive-consensus decisions from benign distribution shift better than input-distance OOD gating, while preserving the latency benefits of adaptation when the controller remains reliable?

---

## 3. Original Networked Systems Contribution

The contribution is **NOT**:
* Generic OOD detection
* Generic prediction fallback
* Generic uncertainty estimation
* A new Raft safety proof

The contribution **IS** a consensus-control trust architecture and evaluation methodology that:
1. Separates **input feature novelty** from **decision unreliability** using a Q1--Q4 operating taxonomy;
2. Integrates a predictive-reliability gate directly into the adaptive Raft control path so the system retains adaptive quorum behavior in OOD-but-reliable states (Q3) and falls back to static majority in ID-looking-but-harmful states (Q4);
3. Evaluates the resulting robustness--performance trade-off using multi-dimensional simulator sweeps, seed-level statistical inference ($N=20$), topology scaling ($N \in \{3, 5, 7\}$ nodes), and a real 5-node containerized execution testbed.

---

## 4. Networked Systems Control Path Integration

```
System Telemetry (RTT, jitter, loss, write skew)
                      │
                      ▼
        Adaptive Quorum Predictor
                      │
                      ▼
     Predictive Reliability Estimator (U_t = Var(L - L_hat))
                      │
                      ▼
                 Trust Gate (U_t > tau_trust)
                ╱            ╲
               ╱              ╲
      [Reliable]              [Unreliable]
          │                        │
          ▼                        ▼
Adaptive Quorum Policy      Conservative Static Raft (R=5)
```

The trust gate is an active component of the runtime consensus control path that changes which quorum policy is executed under nonstationary network conditions.

---

## 5. Main Evidence Summary

* **Q3 (OOD-but-reliable)**: Naive OOD distance gate ($T_2$) suffers $50.0\%$ false fallback rate in simulation ($100.0\%$ in testbed). Calibrated uncertainty gate ($T_3$) achieves **$0.0\%$ false fallback rate**, preserving $-2.00\,\text{ms}$ adaptive latency speedups ($p = 9.54 \times 10^{-7}$) and improving testbed throughput from $58.5$ to $64.2\,\text{ops/s}$ ($+9.7\%$ speedup).
* **Q4 (ID-looking-but-harmful)**: Naive OOD distance gate ($T_2$) suffers $100.0\%$ missed failure rate and $+80.99 \pm 1.01\,\text{ms}$ $p99$ tail regret. Uncertainty gate ($T_3$) achieves **$0.0\%$ missed failure rate** and **$+0.00\,\text{ms}$ tail regret** ($t(19) = 167.06, d = 37.35, p = 1.47 \times 10^{-31}$).
* **Raft Safety Invariants**: $100\%$ linearizability and zero stale reads ($S_{\text{stale}}=0$) structurally preserved by Raft joint consensus configuration transitions.

---

## 6. Bounded Scientific Claims

The manuscript strictly obeys the following boundaries:
* Does **NOT** claim that input OOD detection is generally useless.
* Does **NOT** claim that uncertainty gating eliminates all possible distribution shifts.
* Does **NOT** claim that Raft consensus safety depends on the ML gate (safety is guaranteed by Raft majority intersection).
* Does **NOT** claim that zero observed regret is a formal worst-case guarantee.
* Does **NOT** claim that the 5-node testbed is a multi-datacenter production deployment.
