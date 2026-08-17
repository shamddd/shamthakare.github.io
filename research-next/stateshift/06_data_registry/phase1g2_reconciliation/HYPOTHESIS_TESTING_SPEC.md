# HYPOTHESIS TESTING PROTOCOL DECISION

**Selected Protocol**: **OPTION A — DESCRIPTIVE PRIMARY ESTIMATE + 95% BOOTSTRAP CONFIDENCE INTERVAL ONLY**  

---

## Protocol Specification

1. **Primary Reporting**: Report point estimate $\hat{\Gamma}_T$ along with 95% Problem-Blocked Bootstrap Confidence Interval $[\Gamma_{T,0.025}, \Gamma_{T,0.975}]$.
2. **Scientific Rationale**: StateShift evaluates trajectory interaction mechanics across a post-training series. Option A avoids arbitrary binary thresholding while providing rigorous, non-parametric uncertainty bounds.
3. **No Multiple Testing**: Checkpoint-wise curves $\Gamma_t$ across intermediate steps $t \in \{32, 64, \dots, 224\}$ are presented descriptively to contextualize the primary scalar endpoint $\Gamma_T$.

---
