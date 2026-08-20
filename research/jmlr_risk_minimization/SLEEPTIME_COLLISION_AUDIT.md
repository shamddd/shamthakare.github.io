# COLLISION AUDIT: SLEEP-TIME COMPUTE (Lin et al., arXiv:2504.13171)

**Date**: August 16, 2026  
**Auditor**: Lead Scientific Novelty Auditor  

---

## 1. COMPREHENSIVE EXTRACTION OF PRIOR WORK

* **Reference**: Kevin Lin et al., *"Sleep-time Compute: Beyond Inference Scaling at Test-time"*, arXiv:2504.13171 (2025).
* **Research Question**: Can offline compute ("sleep-time") spent generating synthetic self-play trajectories and fine-tuning models improve per-query inference efficiency across multiple downstream queries?
* **Cost Model**: Explicitly parameterizes offline compute $C_{	ext{offline}}$ vs online test-time search cost $C_{	ext{online}}$ amortized over $Q$ queries.
* **Query Horizon**: Analyzes query volume $Q$ where offline trajectory generation amortizes online test-time search.
* **Learned Parameter Updates**: YES (SFT/RLVR on sleep-time generated trajectories).
* **Distribution Shift**: Analyzes performance under benchmark domain shifts.
* **Competence Conditioning**: Evaluates sleep-time gains relative to base model accuracy.

---

## 2. OVERLAP CLASSIFICATION & COLLISION VERDICT

$$\boxed{{\textbf{{COLLISION VERDICT: DIRECT / STRONG OVERLAP}}}}$$

### Direct Overlap Boundaries:
1. **Multi-Query Amortization**: Lin et al. already established the exact framework for amortizing up-front offline compute ($C_{	ext{offline}}$) over downstream serving volume $Q$.
2. **Post-Training vs Test-Time Search**: Lin et al. already proved that fine-tuning on offline trajectories reduces the required test-time search samples $N$ per query.
3. **Competence Conditioning**: Lin et al. demonstrated that harder prompts benefit more from offline sleep-time compute.

*Conclusion*: Attempting to claim the basic deterministic query-amortization equation $C_{	ext{train}} + Q \cdot C_{	ext{infer}}$ as a novel contribution is **TOTALLY DESTROYED** by Lin et al. (2025).
