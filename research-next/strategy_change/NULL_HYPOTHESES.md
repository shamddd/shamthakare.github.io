# MANDATORY NULL HYPOTHESES

1. **Null 1 (Prefix Strategy Selection Null)**: Full RLVR gain is entirely explained by initial prefix strategy selection ($P_{\text{RL}}(z|x)$ reweighting).
2. **Null 2 (Length Inflation Null)**: Performance differences arise solely from increased sequence generation length.
3. **Null 3 (Base Sampling Support Null)**: RL gains arise entirely from sampling support already present in base model Pass@$K$ ($K=1024$).
4. **Null 4 (Style Artefact Null)**: Trajectory divergence reflects formatting/stylistic changes, not algorithmic transitions.
5. **Null 5 (Forced-Prefix Collapse Null)**: Performance differences disappear when forced to share identical strategy prefixes.
