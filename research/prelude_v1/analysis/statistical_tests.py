"""
Statistical evaluation and clustered significance testing for PRELUDE v1.
Implements Leave-One-Model-Family-Out Cross-Validation, permutation tests, and incremental predictive gain.
"""

from typing import List, Dict, Any, Tuple
import numpy as np
from scipy import stats
from sklearn.linear_model import Ridge, LogisticRegression
from sklearn.metrics import r2_score, mean_absolute_error, roc_auc_score, accuracy_score


def evaluate_incremental_predictive_gain(X_base: np.ndarray,
                                         X_internal: np.ndarray,
                                         y_true: np.ndarray,
                                         families: List[str],
                                         epsilon: float = 0.05) -> Dict[str, Any]:
    """
    Evaluates Base vs. Internal vs. Combined models under Leave-One-Model-Family-Out (LOMFO-CV).
    Returns incremental Delta_R^2, Delta_MAE, Kendall tau, and sign/decision accuracy.
    """
    unique_families = list(set(families))
    if len(unique_families) < 2:
        raise ValueError("LOMFO-CV requires at least 2 distinct model families.")
        
    X_combined = np.hstack([X_base, X_internal])
    
    preds_base = np.zeros_like(y_true)
    preds_internal = np.zeros_like(y_true)
    preds_combined = np.zeros_like(y_true)
    
    # Leave-One-Family-Out Loop
    for held_out_family in unique_families:
        train_mask = np.array([f != held_out_family for f in families])
        test_mask = np.array([f == held_out_family for f in families])
        
        if not np.any(test_mask) or not np.any(train_mask):
            continue
            
        # 1. Base Model f(z_base)
        m_base = Ridge(alpha=1.0)
        m_base.fit(X_base[train_mask], y_true[train_mask])
        preds_base[test_mask] = m_base.predict(X_base[test_mask])
        
        # 2. Internal Model g(z_internal)
        m_internal = Ridge(alpha=1.0)
        m_internal.fit(X_internal[train_mask], y_true[train_mask])
        preds_internal[test_mask] = m_internal.predict(X_internal[test_mask])
        
        # 3. Combined Model h(z_base, z_internal)
        m_comb = Ridge(alpha=1.0)
        m_comb.fit(X_combined[train_mask], y_true[train_mask])
        preds_combined[test_mask] = m_comb.predict(X_combined[test_mask])
        
    # Metrics
    r2_b = float(r2_score(y_true, preds_base))
    r2_c = float(r2_score(y_true, preds_combined))
    delta_r2 = r2_c - r2_b
    
    mae_b = float(mean_absolute_error(y_true, preds_base))
    mae_c = float(mean_absolute_error(y_true, preds_combined))
    delta_mae = mae_b - mae_c  # Positive means error reduced
    
    tau_b, _ = stats.kendalltau(y_true, preds_base)
    tau_c, _ = stats.kendalltau(y_true, preds_combined)
    
    rho_b, _ = stats.spearmanr(y_true, preds_base)
    rho_c, _ = stats.spearmanr(y_true, preds_combined)
    
    # Binary decision evaluation: 1[Delta > epsilon]
    y_bin_true = (y_true > epsilon).astype(int)
    y_bin_pred_b = (preds_base > epsilon).astype(int)
    y_bin_pred_c = (preds_combined > epsilon).astype(int)
    
    acc_bin_b = float(accuracy_score(y_bin_true, y_bin_pred_b))
    acc_bin_c = float(accuracy_score(y_bin_true, y_bin_pred_c))
    
    # Clustered Permutation Test for Delta R^2
    num_permutations = 1000
    permuted_delta_r2 = []
    
    for _ in range(num_permutations):
        # Permute within families to preserve clustering
        perm_y = np.copy(y_true)
        for fam in unique_families:
            fam_idx = np.where(np.array(families) == fam)[0]
            perm_y[fam_idx] = np.random.permutation(perm_y[fam_idx])
            
        r2_perm_b = r2_score(perm_y, preds_base)
        r2_perm_c = r2_score(perm_y, preds_combined)
        permuted_delta_r2.append(r2_perm_c - r2_perm_b)
        
    p_value = float(np.mean([1.0 if p >= delta_r2 else 0.0 for p in permuted_delta_r2]))
    
    return {
        "r2_base": r2_b,
        "r2_combined": r2_c,
        "delta_r2": delta_r2,
        "mae_base": mae_b,
        "mae_combined": mae_c,
        "delta_mae": delta_mae,
        "kendall_tau_base": float(tau_b) if not np.isnan(tau_b) else 0.0,
        "kendall_tau_combined": float(tau_c) if not np.isnan(tau_c) else 0.0,
        "spearman_rho_base": float(rho_b) if not np.isnan(rho_b) else 0.0,
        "spearman_rho_combined": float(rho_c) if not np.isnan(rho_c) else 0.0,
        "binary_decision_accuracy_base": acc_bin_b,
        "binary_decision_accuracy_combined": acc_bin_c,
        "clustered_permutation_p_value": p_value,
        "num_samples": len(y_true)
    }
