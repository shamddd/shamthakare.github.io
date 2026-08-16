# UPDATED TOP 3 CANDIDATES AUDIT REPORT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. RE-AUDIT SUMMARY TABLE

| Candidate Name | Primary Question | Collision Audit Result | Viability Status |
| :--- | :--- | :--- | :--- |
| **Candidate #1 (Primary)** | Amortized Intervention Frontiers ($Q^*$) | Audited against PERL, sGPO, FLOP-Efficient Training. **Distinct on query amortization $Q^*$.** | **`VIABLE & READY`** |
| **Candidate #2 (Downgraded)** | Heavy-Tailed Verification Latency Allocation | Collides directly with `arXiv:2604.14853` (*Adaptive Test-Time Compute Allocation via Constrained Optimization*). | **`UNVIABLE (HIGH COLLISION)`** |
| **Candidate #3 (Downgraded)** | Multi-Agent VCG Context Allocation | Collides with *Economy of Minds* (2025) and *Test-Time Compute Games* (2025). | **`UNVIABLE (HIGH COLLISION)`** |

---

## 2. DETAILED CANDIDATE #1 PROFILE (ONLY VIABLE FLAGSHIP)

* **Precise Question**: How does deployment query volume $Q$ and compositional OOD shift alter the break-even horizon $Q^*(a, b)$ and compute-optimal intervention choice $a^*(Q, d)$ among greedy base generation ($A_0$), Best-of-$N$ search ($A_1$), LoRA-RLVR ($A_2$), and Full RLVR ($A_3$)?
* **Closest Three Papers**:
  1. *Parameter-Efficient RL (PERL)* (Zhang et al., ICLR 2026; `arXiv:2403.10704`)
  2. *sGPO: Trading Inference FLOPs for Training Efficiency* (Park et al., 2025/2026)
  3. *Scaling LLM Test-Time Compute Without Verification is Suboptimal* (Wang et al., 2025/2026)
* **Remaining Scientific Distinction**: Formulates the query-amortized deployment cost model $C_{\text{total}}(a, Q) = C_{\text{train}}(a) + Q \cdot C_{\text{inference}}(a)$ and derives $Q^*(\epsilon)$ under power-law inference scaling $e(N) \propto N^{-\beta}$.
* **Falsifiable Hypothesis**: $H_1$: On Compositional OOD tasks, $Q^*_{\text{OOD}}(A_1, A_3) < \frac{1}{5} \cdot Q^*_{\text{IID}}(A_1, A_3)$, proving that OOD distribution shift shifts the amortization threshold to dramatically smaller deployment query volumes.
* **Smallest Decisive Kill Experiment**: $1.7 \text{ GPU-Hours}$ on `SmolLM2-360M` testing $A_0 \to A_3$ on ModComp-3 and ModComp-5.
* **Theory Opportunity**: Analytical derivation of $Q^*(\epsilon)$ under power-law inference scaling.
* **Kakade Alignment**: **High (8/10)** (Aligns with fundamental research on scaling limits, learning dynamics, and optimal compute allocation).
* **Independence Score**: **8/10** (Substantively distinct theoretical framing based on deployment horizon amortization).
