class AbstractPolicy:
    def act(self, state):
        raise NotImplementedError

    def evaluate_v(self, state, n_rollouts=100):
        raise NotImplementedError

class MockBasePolicy(AbstractPolicy):
    def act(self, state):
        return state["legal_actions"][0]

    def evaluate_v(self, state, n_rollouts=100):
        # Base policy gets 0.4 on recovery, 0.7 on control
        return 0.4 if state["is_recovery"] else 0.7

class MockPrefixRLPolicy(AbstractPolicy):
    def __init__(self, prefix_h=None):
        self.prefix_h = prefix_h

    def act(self, state):
        return state["legal_actions"][0]

    def evaluate_v(self, state, n_rollouts=100):
        # PrefixRL gets 0.5 on recovery, 0.8 on control
        return 0.5 if state["is_recovery"] else 0.8

class MockFullRLVRPolicy(AbstractPolicy):
    def act(self, state):
        return state["optimal_action"]

    def evaluate_v(self, state, n_rollouts=100, case="A"):
        if case == "A": # Delta_late > 0
            return 0.9 if state["is_recovery"] else 0.9
        elif case == "B": # Delta_late == 0 (Global improvement null)
            return 0.7 if state["is_recovery"] else 1.0
        elif case == "C": # Delta_late < 0
            return 0.45 if state["is_recovery"] else 0.95
        return 0.9
