# ENVIRONMENT STATE REGISTRY SPECIFICATION (`STATE_REGISTRY.json`)

**Date**: August 16, 2026  

---

## 1. ENVIRONMENT-ONLY PRE-FREEZING PROTOCOL

`STATE_REGISTRY.json` is generated and SHA-256 hashed **BEFORE ANY TRAINING BEGINS**. Zero fields depend on model outputs.

### Schema Fields per State Entry:
* `state_id`: Unique string ID (e.g., `OOD_D_graph042_node07`).
* `graph_id`: Topology identifier.
* `distribution`: One of `[train, iid_test, ood_b, ood_d, ood_m, ood_c]`.
* `recovery_or_control`: Categorical `recovery` ($S_R$) or `control` ($S_C$).
* `depth`: Integer trajectory depth $t$.
* `branching_factor`: Integer outgoing action count $|\mathcal{A}(s)|$.
* `distance_to_goal`: Integer shortest path length $d(v_t, g)$.
* `observation_length`: Character length of environment observation text.
* `optimal_action`: Ground-truth optimal action $a^* \in \mathcal{A}(s)$.
* `recovery_depth`: Depth of required recovery steps.
* `matching_pair_id`: ID of paired control state $s_C \in S_C$.
