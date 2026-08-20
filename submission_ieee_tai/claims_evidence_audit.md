# Claims to Evidence Audit Ledger (IEEE TAI Submission)

## Frozen Research Project: QuorumShift (AdaptiveReplica)
- **Git Commit SHA**: `e41a976`
- **Benchmark Seeds**: $N=5$ random seeds
- **Fault Injection Mode**: 50ms asymmetric network link latency degradation & packet loss

---

## Claims Ledger

| Claim ID | Claim Description | Experiment / Metric | Raw Result / Source | Table/Figure in Paper | Supported? | Correction Needed? |
|---|---|---|---|---|---|---|
| **C1** | Write p99 tail-latency reduction | Dynamic vs static quorum latency benchmark | $13.50\text{ms}$ vs $120.48\text{ms}$ ($R=5$) | Table I | YES | None (exact match) |
| **C2** | Percentage latency reduction | Relative decrease calculation | $(120.48 - 13.50) / 120.48 = 88.8\%$ | Abstract / Sec VI | YES | None (exact match) |
| **C3** | System availability under asymmetric fault | Availability under 50ms partition | $99.97\%$ vs $99.10\%$ ($R=5$) | Table I | YES | None (exact match) |
| **C4** | Strong consistency / zero stale reads | Read freshness audit ($N=10,000$ operations) | $S_{\text{stale}} = 0$ | Table I / Theorem 1 | YES | None (exact match) |
| **C5** | Joint-consensus safety invariant | Formal proof & state machine validation | $\mathcal{Q}_A \cap \mathcal{Q}_B \neq \emptyset$ | Section V | YES | None (exact match) |

---

### Integrity Statement
No empirical numbers were altered, inflated, or fabricated for aesthetics or formatting. All reported values originate from direct execution of the `quorumshift` benchmark suite.
