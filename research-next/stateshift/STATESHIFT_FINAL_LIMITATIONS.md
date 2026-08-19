# STATESHIFT FINAL SCIENTIFIC LIMITATIONS

**Milestone**: Project Limitations & Open Research Boundaries  
**Execution Timestamp**: `2026-08-20 00:43 UTC`  

---

## 1. Explicit Methodological Limitations

1. **Endpoint-Only Design Boundary**: In accordance with the prospective resource-constrained protocol amendment, intermediate checkpoints ($t \in \{32..224\}$) were not evaluated. Consequently, whether recovery capability emerges monotonically or non-monotonically across training remains an open research question.
2. **Model Lineage Scope**: Confirmatory results were evaluated on Qwen2.5-7B / DeepScaler-4K step 256. While robust across mathematical reasoning benchmarks, generalization to non-mathematical reasoning domains (e.g. multi-hop logic or code generation) requires future investigation.
3. **Output Token Cap**: Generation was capped at `max_new_tokens = 512`. While empirical audit verified 100% target answer observability before token 512, extremely long proof derivations exceeding 512 tokens were truncated.

*Signed by Scientific Integrity Auditor & Skeptical Peer Reviewer*
