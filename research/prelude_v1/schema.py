"""
Schema definitions for PRELUDE v1.
Strict typing and validation for diagnostic feature sets, run manifests, and telemetry records.
"""

from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field


class BaseDiagnostics(BaseModel):
    """Observable baseline feature set z_base(M, D)."""
    model_name: str
    model_family: str
    model_scale_params: int
    checkpoint_step: Optional[int] = None
    pretraining_tokens: Optional[int] = None
    
    # Task behavioral metrics at t = 0
    task_name: str
    task_difficulty_tier: str  # 'easy', 'hard', 'full'
    base_pass_at_1: float
    base_pass_at_k: float  # e.g., pass@8 or pass@16
    prompt_nll_loss: float
    mean_token_entropy: float
    sampled_success_coverage: float  # p_hat_K = (1 / nK) sum_i sum_j I[r(x_i, y_ij) == 1]
    group_reward_variance: float
    
    # Optional SFT generalization proxy (if evaluated)
    sft_heldout_loss: Optional[float] = None
    
    # Early RL pilot benchmark (10-step GRPO linear extrapolation)
    early_pilot_delta_hat: Optional[float] = None


class InternalDiagnostics(BaseModel):
    """Internal model-state representation and gradient diagnostic feature set z_internal(M, D)."""
    model_name: str
    task_name: str
    
    # Representation geometry
    residual_effective_rank: float  # erank(Sigma) = exp(-sum p_i ln p_i)
    residual_stable_rank: float     # srank(Sigma) = ||Sigma||_F^2 / ||Sigma||_2^2
    top_singular_value_ratio: float  # sigma_1 / sum(sigma_i)
    condition_number_subspace: float # sigma_1 / sigma_k
    
    # Reward probe linear separability
    reward_probe_auroc: float
    reward_probe_r2: float
    
    # Gradient saliency & variance
    microbatch_gradient_norm: float
    gradient_noise_scale: float     # Var(grad) / ||E[grad]||^2
    layernorm_to_output_grad_ratio: float


class RLVRGroundTruthResult(BaseModel):
    """Observed empirical result from full standardized RLVR run."""
    model_name: str
    model_family: str
    model_scale_params: int
    checkpoint_step: Optional[int] = None
    task_name: str
    seed: int
    
    # Pre-RL baseline accuracy
    pre_rl_accuracy: float
    
    # Post-RL observed accuracy
    post_rl_accuracy: float
    
    # True marginal gain
    marginal_rlvr_gain: float  # Delta_RLVR = post_rl_accuracy - pre_rl_accuracy
    
    # Binary intervention decision label
    is_worth_intervention: bool  # 1[Delta_RLVR > epsilon]
    
    # Training dynamics
    total_rl_steps: int
    final_policy_entropy: float
    mean_reward_final_window: float
    wall_clock_seconds: float


class TelemetryMeasurement(BaseModel):
    """Hardware profiling measurement for Step-0 compute calibration."""
    device_name: str
    device_type: str  # 'cuda', 'mps', 'cpu'
    model_name: str
    model_scale_params: int
    group_size: int
    max_gen_length: int
    batch_size: int
    
    prompt_tokens_per_sec: float
    generation_tokens_per_sec: float
    backward_latency_sec: float
    step_wall_clock_sec: float
    peak_memory_mb: float
    gpu_utilization_pct: Optional[float] = None


class RunManifest(BaseModel):
    """Immutable provenance record attached to every experiment."""
    experiment_id: str
    git_commit_hash: str
    timestamp_utc: str
    python_version: str
    torch_version: str
    transformers_version: str
    hardware_info: Dict[str, Any]
    config_digest_sha256: str
    is_locked: bool = True
