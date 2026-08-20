# Program 3 Existing System Claims Audit & Infrastructure Reuse

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Repository Audited**: [`quorumshift` / `AdaptiveReplica`](file:///Users/shamthakare/.gemini/antigravity/scratch/quorumshift)

---

## 1. Frozen Pre-Existing Claims (Must NOT be Claimed as New)

| System Component | Pre-Existing Scientific Claim | Reusability Boundary |
|---|---|---|
| `AdaptiveReplica` | Dynamic vote-weight adaptation over Raft joint-consensus state transitions bypasses degraded replicas. | **FROZEN**. Cannot claim dynamic vote-weight adaptation as a new contribution. |
| `quorumshift` Benchmark | Reduces write p99 tail latency from $120.48\text{ms}$ to $13.50\text{ms}$ ($88.8\%$ reduction) under 50ms asymmetric fault injection. | **FROZEN**. Cannot claim p99 latency reduction under static asymmetric fault injection as new. |
| Safety & Availability | Achieves $99.97\%$ availability and guarantees zero stale reads ($S_{\text{stale}}=0$). | **FROZEN**. Cannot claim zero stale reads or Raft safety preservation as an ML contribution (Raft joint consensus structurally enforces $C=100\%$). |
| Health Model | Composite node health score $H(r_i) = \alpha (\tau_{\text{base}}/\tau_i) + \beta (1 - \eta_i)$. | **FROZEN**. Cannot claim sliding-window heartbeat health scoring as a new discovery. |

---

## 2. Protocol Safety Invariant Clarification

> **Crucial Invariant**: In Raft joint-consensus transitions ($C_{\text{old}} \to C_{\text{old,new}} \to C_{\text{new}}$), **linearizability and safety ($C=100\%, S_{\text{stale}}=0$) are structurally guaranteed by Raft's majority intersection requirement, regardless of ML controller output**. An ML controller cannot cause linearizability violations.

What CAN fail under ML controller error / nonstationary distribution shift:
* **Worst-Case Tail Latency (p99 Write Latency Spikes)**: ML controller selects slow/flaky quorums.
* **SLO Regret**: Controller performs worse than static standard Raft ($R=5$ majority).
* **Leader Instability & Reconfiguration Churn**: Oscillating configuration transitions under nonstationary jitter.

---

## 3. Permissible Infrastructure Reuse

* ✅ C++20 Raft consensus engine and storage node RPC harness (`quorumshift`).
* ✅ Fault injection network simulator (asymmetric latency spikes, packet loss, jitter).
* ✅ Joint-consensus configuration state transition routines.

---

## 4. New Scientific Delta for Program 3

Program 3 moves strictly beyond AdaptiveReplica:
* **New Research Question**: **When should a fault-tolerant distributed system refusal-to-trust an online learned adaptation controller under nonstationary distribution shift?**
* **Primary Target**: **Uncertainty-Aware Trust Gate & Conservative Fallback Bounds** to eliminate worst-case SLO tail-latency regret under workload/network nonstationarity.
