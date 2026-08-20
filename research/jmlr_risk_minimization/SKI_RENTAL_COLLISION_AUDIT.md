# SKI-RENTAL COLLISION & ONLINE ADAPTATION FORMULATION

**Date**: August 16, 2026  

---

## 1. SKI-RENTAL REDUCTION & COMPETITIVE RATIO

Consider a sequential deployment stream where queries $t = 1, 2, \dots, Q$ arrive online, but total volume $Q$ is unknown in advance.

* **Search (Renting)**: Pays per-query search cost $c_{	ext{search}}$ per query.
* **Adaptation (Buying)**: Pays one-time training cost $F = C_{	ext{train}}$, then pays reduced inference cost $c_{	ext{adapt}} < c_{	ext{search}}$.
* **Per-Query Savings**: $s = c_{	ext{search}} - c_{	ext{adapt}} > 0$.

### Classical Ski-Rental Threshold Policy:
Trigger adaptation at step $	au^* = \left\lceil rac{F}{s} ightceil$.

### Competitive Ratio Theorem:
The deterministic threshold policy $	au^* = \lceil F / s ceil$ achieves a **2-Competitive Ratio** against an offline oracle with perfect knowledge of $Q$:
$$rac{	ext{Cost}(	ext{Online Policy})}{	ext{Cost}(	ext{Offline Oracle})} \le 2.0$$

*Conclusion*: When deployment volume $Q$ is deterministic and static, online adaptation-or-search reduces **EXACTLY** to classical ski-rental (Karlin et al., 1988).
