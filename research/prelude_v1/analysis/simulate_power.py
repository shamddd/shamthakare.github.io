"""
Monte Carlo Hierarchical Power Simulation for PRELUDE v1.
Simulates realistic intra-family, checkpoint, and task correlations to compute statistical power
as a function of incremental effect size (small, moderate, large) for Leave-One-Model-Family-Out validation.
"""

from typing import Dict, List, Tuple
import numpy as np
from scipy import stats
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score


def run_power_simulation(num_simulations: int = 500, random_seed: int = 42) -> Dict[str, Dict[str, float]]:
    """
    Simulates statistical power for BHI vs BH comparison under hierarchical observation tree:
        Family (3) -> Model (2/family) -> Checkpoint (2/model) -> Task (2/ckpt) -> Seed (1) = 24 runs
        (and N=48 confirmatory design)
    """
    np.random.seed(random_seed)
    
    # Structure definition: 3 families, 2 models per family, 2 checkpoints per model, 2 tasks = 24 observations
    families = ["SmolLM2", "Pythia", "Qwen2.5"]
    
    effect_sizes = {
        "small": {"delta_beta": 0.15, "true_delta_r2_target": 0.03},
        "moderate": {"delta_beta": 0.40, "true_delta_r2_target": 0.10},
        "large": {"delta_beta": 0.75, "true_delta_r2_target": 0.20}
    }
    
    power_results = {}
    
    for effect_name, effect_cfg in effect_sizes.items():
        delta_beta = effect_cfg["delta_beta"]
        rejections_mae_paired = 0
        rejections_perm = 0
        
        delta_r2_list = []
        delta_mae_list = []
        
        for sim in range(num_simulations):
            # Generate hierarchical random effects
            # 1. Family-level variance
            u_family = {fam: np.random.normal(0, 0.4) for fam in families}
            
            # 2. Checkpoint-level variance within family
            u_ckpt = {}
            obs_family = []
            obs_base_features = []
            obs_headroom_features = []
            obs_internal_features = []
            obs_targets = []
            
            for fam in families:
                for model_idx in range(2):
                    for ckpt_idx in range(2):
                        ckpt_id = f"{fam}_m{model_idx}_c{ckpt_idx}"
                        u_ckpt[ckpt_id] = u_family[fam] + np.random.normal(0, 0.3)
                        
                        # Generate features
                        # Base features B (Pass@1, Pass@k, NLL, scale)
                        b1 = np.random.uniform(0.1, 0.7)
                        b2 = b1 + np.random.uniform(0.05, 0.2)
                        
                        # Headroom features H (ceiling distance, step age, difficulty)
                        h1 = 1.0 - b1
                        h2 = np.random.uniform(0.2, 0.8)
                        
                        # Internal features I (residual rank, probe AUROC)
                        # Has some alignment with H/B plus unique signal
                        i1 = 0.5 * h1 + np.random.normal(0, 0.2)
                        i2 = 0.4 * b2 + np.random.normal(0, 0.2)
                        
                        for task_idx in range(2):
                            task_diff = 0.2 if task_idx == 0 else 0.6
                            
                            # True ground truth gain Delta_RLVR
                            # Signal comes from B, H, and incremental internal signal I
                            base_signal = 0.3 * b2 - 0.2 * b1
                            headroom_signal = 0.4 * h1 - 0.3 * task_diff
                            internal_signal = delta_beta * i1
                            
                            noise = np.random.normal(0, 0.15)
                            
                            y_delta = (u_ckpt[ckpt_id] * 0.2 + 
                                       base_signal + 
                                       headroom_signal + 
                                       internal_signal + 
                                       noise)
                            
                            obs_family.append(fam)
                            obs_base_features.append([b1, b2])
                            obs_headroom_features.append([h1, h2, task_diff])
                            obs_internal_features.append([i1, i2])
                            obs_targets.append(y_delta)
                            
            X_B = np.array(obs_base_features)
            X_BH = np.hstack([X_B, np.array(obs_headroom_features)])
            X_BHI = np.hstack([X_BH, np.array(obs_internal_features)])
            y_arr = np.array(obs_targets)
            
            # Leave-One-Model-Family-Out CV
            preds_BH = np.zeros_like(y_arr)
            preds_BHI = np.zeros_like(y_arr)
            
            for held_out in families:
                tr_mask = np.array([f != held_out for f in obs_family])
                te_mask = np.array([f == held_out for f in obs_family])
                
                m_BH = Ridge(alpha=1.0).fit(X_BH[tr_mask], y_arr[tr_mask])
                m_BHI = Ridge(alpha=1.0).fit(X_BHI[tr_mask], y_arr[tr_mask])
                
                preds_BH[te_mask] = m_BH.predict(X_BH[te_mask])
                preds_BHI[te_mask] = m_BHI.predict(X_BHI[te_mask])
                
            errors_BH = np.abs(y_arr - preds_BH)
            errors_BHI = np.abs(y_arr - preds_BHI)
            
            mae_BH = np.mean(errors_BH)
            mae_BHI = np.mean(errors_BHI)
            
            delta_mae = mae_BH - mae_BHI  # Positive means BHI reduces error
            r2_BH = r2_score(y_arr, preds_BH)
            r2_BHI = r2_score(y_arr, preds_BHI)
            delta_r2 = r2_BHI - r2_BH
            
            delta_r2_list.append(delta_r2)
            delta_mae_list.append(delta_mae)
            
            # Paired Wilcoxon signed-rank test on absolute errors across cluster means
            fam_errors_BH = [np.mean(errors_BH[np.array(obs_family) == f]) for f in families]
            fam_errors_BHI = [np.mean(errors_BHI[np.array(obs_family) == f]) for f in families]
            
            # Paired t-test across cluster means
            t_stat, p_val = stats.ttest_rel(fam_errors_BH, fam_errors_BHI)
            if p_val < 0.05 and mae_BHI < mae_BH:
                rejections_mae_paired += 1
                
        power_mae = rejections_mae_paired / num_simulations
        
        power_results[effect_name] = {
            "empirical_power": float(power_mae),
            "mean_delta_r2": float(np.mean(delta_r2_list)),
            "mean_delta_mae": float(np.mean(delta_mae_list)),
            "sample_size_N": len(y_arr),
            "effective_clusters_K": len(families)
        }
        
    return power_results


if __name__ == "__main__":
    res = run_power_simulation()
    print("[+] Monte Carlo Hierarchical Power Simulation Results:")
    for k, v in res.items():
        print(f"  Effect Size [{k.upper()}]: Power = {v['empirical_power']:.3f} | Mean Delta_R2 = {v['mean_delta_r2']:.3f} | Mean Delta_MAE = {v['mean_delta_mae']:.4f}")
