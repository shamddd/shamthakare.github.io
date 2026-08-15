# MANUSCRIPT OUTLINE (IEEE BIGDATA 2026)

**Title**: A State-Matched Framework for Evaluating Recovery Behavior in Language-Model Reasoning

1. **Abstract**: Problem statement, state-matching framework, primitive rollout provenance, and benchmark engineering.
2. **Introduction**: Conflation of state difficulty in reasoning evaluation.
3. **Related Work**: Process verification, self-correction benchmarks, trajectory evaluation.
4. **Problem Formulation & Definitions**: Formal definitions of $S_R$, $S_C$, $V_\pi(s)$, and contrast $C_1$.
5. **State-Matched Evaluation Framework**: 7 matching covariates, Mahalanobis matching, exposure governance.
6. **Framework Architecture & Implementation**: `recovery_eval` package design, verifiers, CLI.
7. **Validation & Verification Protocol**: Test suite, negative controls, AST taint analysis.
8. **Illustrative Demonstration**: Framework serialization demonstration using mock fixtures (labeled `record_type = "mock_fixture"`).
9. **Limitations**: Scope boundaries, covariate selection bounds.
10. **Conclusion**: Methodological summary and future research outlook.
