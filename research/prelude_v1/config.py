"""
Immutable experiment configuration system for PRELUDE v1.
Locks standardized RLVR operator settings and defines model anchors and datasets.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any
import hashlib
import json


@dataclass(frozen=True)
class RLVRStandardizedConfig:
    """Standardized GRPO training operator settings. LOCKED across all models."""
    algorithm: str = "GRPO"
    learning_rate: float = 1e-5
    optimizer: str = "AdamW"
    weight_decay: float = 0.01
    beta_kl: float = 0.04
    temperature: float = 0.7
    top_p: float = 0.95
    group_size: int = 8  # G = 8 rollouts per prompt
    max_gen_length: int = 256
    num_optimization_steps: int = 150
    batch_size: int = 4
    gradient_accumulation_steps: int = 2
    precision: str = "bfloat16"  # or float32 / float16 depending on hardware
    evaluation_frequency: int = 25
    checkpoint_frequency: int = 50
    epsilon_decision_threshold: float = 0.05  # Delta > +5% is considered worth intervention


@dataclass(frozen=True)
class ModelAnchor:
    """Specification of a pre-trained foundation model checkpoint."""
    model_id: str
    family: str
    scale_params: int
    checkpoint_alias: str
    trajectory_step: int = -1  # -1 indicates final checkpoint


@dataclass(frozen=True)
class TaskSpec:
    """Specification of a target reasoning dataset."""
    name: str
    split: str
    difficulty_tier: str
    sample_limit: int = 1000
    verifier_type: str = "math_exact"


# Standard Model Anchors for MVSE & Scaled Evaluation
STANDARD_MODELS: List[ModelAnchor] = [
    # Family 1: SmolLM2
    ModelAnchor(model_id="HuggingFaceTB/SmolLM2-360M", family="SmolLM2", scale_params=360_000_000, checkpoint_alias="smollm2_360m"),
    ModelAnchor(model_id="HuggingFaceTB/SmolLM2-1.7B", family="SmolLM2", scale_params=1_700_000_000, checkpoint_alias="smollm2_1.7b"),
    
    # Family 2: Pythia (Includes trajectory checkpoints)
    ModelAnchor(model_id="EleutherAI/pythia-410m", family="Pythia", scale_params=410_000_000, checkpoint_alias="pythia_410m_final"),
    ModelAnchor(model_id="EleutherAI/pythia-410m-step10000", family="Pythia", scale_params=410_000_000, checkpoint_alias="pythia_410m_10k", trajectory_step=10_000),
    ModelAnchor(model_id="EleutherAI/pythia-410m-step50000", family="Pythia", scale_params=410_000_000, checkpoint_alias="pythia_410m_50k", trajectory_step=50_000),
    ModelAnchor(model_id="EleutherAI/pythia-1.4b", family="Pythia", scale_params=1_400_000_000, checkpoint_alias="pythia_1.4b_final"),
    
    # Family 3: Qwen 2.5
    ModelAnchor(model_id="Qwen/Qwen2.5-0.5B", family="Qwen2.5", scale_params=490_000_000, checkpoint_alias="qwen2.5_0.5b"),
    ModelAnchor(model_id="Qwen/Qwen2.5-1.5B", family="Qwen2.5", scale_params=1_540_000_000, checkpoint_alias="qwen2.5_1.5b"),
]

# Standard Task Specifications
STANDARD_TASKS: List[TaskSpec] = [
    TaskSpec(name="gsm8k", split="test", difficulty_tier="full", sample_limit=1000),
    TaskSpec(name="gsm8k_easy", split="test", difficulty_tier="easy", sample_limit=500),
    TaskSpec(name="gsm8k_hard", split="test", difficulty_tier="hard", sample_limit=500),
    TaskSpec(name="svamp", split="test", difficulty_tier="shift", sample_limit=500),
]


def get_config_hash(obj: Any) -> str:
    """Returns SHA-256 digest of serialized configuration."""
    if hasattr(obj, "__dict__"):
        d = obj.__dict__
    else:
        d = dict(obj)
    serialized = json.dumps(d, sort_keys=True, default=str)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
