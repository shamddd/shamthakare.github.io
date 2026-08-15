# PREFIX-DECIDABLE VS RECOVERY-REQUIRED TASK FORMALISM

**Date**: August 16, 2026  

---

## 1. TASK TAXONOMY

1. **Class A (Prefix-Decidable Tasks)**:
   Tasks where the optimal solution strategy $z^*$ is fully determined by an initial $k$-token prefix $\tau_{1:k}$.
   $$\mathbb{P}(\text{Success} | \tau_{1:k} = z^*) \ge 1 - \epsilon$$

2. **Class B (Recovery-Required / Mid-Trajectory Intervention Tasks)**:
   Tasks constructed with deliberate local dead-ends, where initial greedy paths lead to failure, requiring state-dependent error recognition, backtracking, or branch switching at $t > k$.
   $$\mathbb{P}(\text{Success} | \tau_{1:k} = \text{greedy}) = 0 \quad \implies \quad \text{Requires } a_t = \text{backtrack at } t > k$$
