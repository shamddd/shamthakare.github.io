import json

class SyntheticGraphMDP:
    def __init__(self, distribution="train", generator_seed=42):
        self.distribution = distribution
        self.generator_seed = generator_seed
        self._build_graph()

    def _build_graph(self):
        # Configure factored distributions
        if self.distribution == "train":
            self.branching_factor = 3
            self.recovery_depth = 2
            self.motif_type = "standard"
        elif self.distribution == "iid_test":
            self.branching_factor = 3
            self.recovery_depth = 2
            self.motif_type = "standard"
        elif self.distribution == "ood_b":
            self.branching_factor = 6
            self.recovery_depth = 2
            self.motif_type = "standard"
        elif self.distribution == "ood_d":
            self.branching_factor = 3
            self.recovery_depth = 5
            self.motif_type = "standard"
        elif self.distribution == "ood_m":
            self.branching_factor = 3
            self.recovery_depth = 2
            self.motif_type = "cycle_trap"
        elif self.distribution == "ood_c":
            self.branching_factor = 6
            self.recovery_depth = 5
            self.motif_type = "cycle_trap"
        else:
            raise ValueError(f"Unknown distribution: {self.distribution}")

    def get_state(self, node_id):
        is_rec = (node_id % 2 == 1)
        depth = node_id // 2
        return {
            "state_id": f"{self.distribution}_g{self.generator_seed}_n{node_id}",
            "graph_id": f"graph_{self.generator_seed}",
            "distribution": self.distribution,
            "node_id": node_id,
            "depth": depth,
            "branching_factor": self.branching_factor,
            "distance_to_goal": max(1, 10 - depth),
            "observation_length": 100 + node_id * 5,
            "legal_actions": [f"a_{i}" for i in range(self.branching_factor)] + ["a_backtrack"],
            "optimal_action": "a_backtrack" if is_rec else "a_0",
            "recovery_depth": self.recovery_depth if is_rec else 0,
            "is_recovery": is_rec
        }

    def is_recovery_critical(self, state):
        # Environment-only criteria (zero model outputs used)
        return state["is_recovery"] and (state["recovery_depth"] > 0)
