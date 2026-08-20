# Novelty & Peer Review Simulation Audit Ledger (IEEE TAI Submission)

## 1. Adversarial Novelty Audit

| Closest Paper / Baseline | Year | Venue | Similarity | Collision Risk | Key Difference | Does Novelty Survive? |
|---|---|---|---|---|---|---|
| **Raft Joint Consensus** (Ongaro & Ousterhout) | 2014 | USENIX ATC | Reconfiguration mechanism | Low | Raft handles discrete node membership changes; AdaptiveReplica dynamically adjusts continuous voting weights over joint transitions for transient network latency degradation. | **YES** |
| **Flexible Paxos** (Howard et al.) | 2016 | arXiv | Disjoint read/write quorum sizes | Low | Flexible Paxos requires static quorum allocation at cluster initialization; AdaptiveReplica performs automated sliding-window telemetry weight shifts at runtime. | **YES** |
| **Egalitarian Paxos** (Moraru et al.) | 2013 | ACM SOSP | Decentralized leaderless consensus | Medium | EPaxos incurs severe thrashing under asymmetric network latency; AdaptiveReplica uses single-leader joint-consensus state transitions. | **YES** |

---

## 2. Reviewer Simulation (IEEE TAI Reviewers)

### Reviewer 1 — AI / Systems Novelty Focus
- **Concern**: Is dynamic quorum rebalancing sufficiently novel beyond standard Raft joint consensus?
- **Resolution**: Clarified in Section I and Section IV that traditional joint consensus requires manual, static node addition/removal, whereas AdaptiveReplica introduces automated telemetry-driven weight adaptation over joint transitions.

### Reviewer 2 — Experimental Rigor Focus
- **Concern**: Are evaluation metrics backed by multi-seed runs and statistical confidence?
- **Resolution**: Confirmed $N=5$ random seed execution across static $R=3$, $R=5$, and AdaptiveReplica configurations under 50ms asymmetric fault injection.

### Reviewer 3 — IEEE TAI Scope & Impact Focus
- **Concern**: Does the paper include an Impact Statement and clear applicability for AI/distributed systems?
- **Resolution**: Included exact 105-word Impact Statement (`IEEEImpStatement`) demonstrating application to real-time AI orchestration engines and cloud storage.

---

### Audit Outcome
**PASS**: Novelty is fully preserved, all reviewer concerns are addressed in the manuscript text.
