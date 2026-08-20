import numpy as np

def compute_estimands(v_base_sr, v_prefix_sr, v_full_sr, v_base_sc, v_prefix_sc, v_full_sc):
    # Primary Estimand: Delta_late = mean_SR(V_FULL - V_PREFIX) - mean_SC(V_FULL - V_PREFIX)
    full_minus_prefix_sr = np.mean(v_full_sr - v_prefix_sr)
    full_minus_prefix_sc = np.mean(v_full_sc - v_prefix_sc)
    delta_late = full_minus_prefix_sr - full_minus_prefix_sc

    # Supporting Estimands: Gamma_FULL and Gamma_PREFIX
    gamma_full = np.mean(v_full_sr - v_base_sr) - np.mean(v_full_sc - v_base_sc)
    gamma_prefix = np.mean(v_prefix_sr - v_base_sr) - np.mean(v_prefix_sc - v_base_sc)

    return {
        "delta_late": float(delta_late),
        "gamma_full": float(gamma_full),
        "gamma_prefix": float(gamma_prefix),
        "sens_002": bool(delta_late > 0.02),
        "sens_005": bool(delta_late > 0.05),
        "sens_010": bool(delta_late > 0.10)
    }

def match_control(recovery_states, control_candidates):
    matched_pairs = []
    unmatched_states = []

    for s_r in recovery_states:
        match = None
        for s_c in control_candidates:
            if (s_c["depth"] == s_r["depth"] and
                s_c["branching_factor"] == s_r["branching_factor"] and
                abs(s_c["observation_length"] - s_r["observation_length"]) <= 20):
                match = s_c
                break
        if match:
            matched_pairs.append({"recovery_id": s_r["state_id"], "control_id": match["state_id"]})
        else:
            unmatched_states.append(s_r["state_id"])

    return matched_pairs, unmatched_states
