"""
Unit tests for spectral representation diagnostics and statistical evaluation in PRELUDE v1.
"""

import numpy as np
from ..diagnostics.representation import compute_matrix_spectral_metrics
from ..analysis.statistical_tests import evaluate_incremental_predictive_gain


def test_spectral_matrix_metrics():
    # 1. Identity matrix (Uniform spectrum -> maximal effective rank)
    d = 20
    X_ident = np.eye(d)
    m_ident = compute_matrix_spectral_metrics(X_ident)
    assert m_ident["effective_rank"] > 10.0
    assert m_ident["stable_rank"] > 5.0
    
    # 2. Rank-1 matrix (Completely collapsed spectrum -> minimal effective rank)
    v = np.ones((50, 1))
    u = np.ones((1, d))
    X_rank1 = v @ u
    m_rank1 = compute_matrix_spectral_metrics(X_rank1)
    assert m_rank1["effective_rank"] < 1.5
    assert m_rank1["stable_rank"] < 1.5


def test_incremental_statistical_evaluation():
    np.random.seed(42)
    N = 30
    
    # 3 model families
    families = ["SmolLM2"] * 10 + ["Pythia"] * 10 + ["Qwen"] * 10
    
    # Base features
    X_base = np.random.randn(N, 2)
    # Internal diagnostic features
    X_internal = np.random.randn(N, 2)
    
    # True target with signal from both
    y_true = 0.5 * X_base[:, 0] + 0.8 * X_internal[:, 0] + np.random.randn(N) * 0.1
    
    results = evaluate_incremental_predictive_gain(X_base, X_internal, y_true, families)
    
    assert "delta_r2" in results
    assert "kendall_tau_combined" in results
    assert "clustered_permutation_p_value" in results
    assert results["num_samples"] == N


if __name__ == "__main__":
    test_spectral_matrix_metrics()
    test_incremental_statistical_evaluation()
    print("[+] All diagnostic and statistical unit tests PASSED.")
