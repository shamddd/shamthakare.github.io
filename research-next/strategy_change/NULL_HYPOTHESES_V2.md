# MANDATORY NULL HYPOTHESES (V2)

1. **Null 1--5**: Retained from V1 (Prefix reweighting, length inflation, base sampling support, style artefact, forced-prefix collapse).
2. **Null 6 (Hidden-State Mismatch Null)**: Policy divergence after text prefix is driven by unobserved hidden state drift rather than true policy change.
3. **Null 7 (Calibration-Only Null)**: RL improves late decision token confidence/calibration without changing action ranking.
4. **Null 8 (Topology Memorization Null)**: RL model memorizes task-specific graph transitions rather than acquiring general recovery mechanics.
5. **Null 9 (Prefix-Length Misspecification Null)**: Prefix-RL appears weaker on Class B simply because $k$ was set too short.
6. **Null 10 (Unseen Topology Collapse Null)**: Late policy advantage $A_{\text{recovery}}(s_k)$ vanishes when evaluated on genuinely unseen graph families.

---

## 2. STRONGEST KILL CRITERION

$$\boxed{\text{If } \pi_{\text{RL}} \text{ continuation from identical externally controlled recovery state } s_k \text{ does NOT significantly outperform } \pi_{\text{base}} \text{ or } \pi_{\text{prefix}} \text{ on unseen graph topologies, TERMINATE THE PROJECT.}}$$
