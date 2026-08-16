"""
Dataset loader and benchmark split management for PRELUDE v1.
Handles GSM8K, SVAMP, and difficulty tier partitioning with deterministic caching.
"""

from typing import List, Dict, Any, Optional
import json
import hashlib
from datasets import load_dataset
from ..config import TaskSpec


def compute_dataset_hash(examples: List[Dict[str, Any]]) -> str:
    """Computes SHA-256 digest of prompt-answer text to verify immutability."""
    raw_str = "".join([f"{ex['question']}||{ex['answer']}" for ex in examples])
    return hashlib.sha256(raw_str.encode("utf-8")).hexdigest()


def load_reasoning_task(spec: TaskSpec, cache_dir: Optional[str] = None) -> Dict[str, Any]:
    """
    Loads and standardizes reasoning benchmark dataset.
    Returns:
        Dict with 'train' (if needed), 'test' examples, and metadata hash.
    """
    if spec.name.startswith("gsm8k"):
        ds = load_dataset("openai/gsm8k", "main", cache_dir=cache_dir)
        test_data = list(ds["test"])
        train_data = list(ds["train"])
        
        # Difficulty tier partitioning based on reasoning step count
        if spec.difficulty_tier == "easy":
            # 1-2 calculation steps
            filtered = [ex for ex in test_data if ex["answer"].count("\n") <= 3]
            test_data = filtered[:spec.sample_limit]
        elif spec.difficulty_tier == "hard":
            # 4+ calculation steps
            filtered = [ex for ex in test_data if ex["answer"].count("\n") >= 5]
            test_data = filtered[:spec.sample_limit]
        else:
            test_data = test_data[:spec.sample_limit]
            
        return {
            "name": spec.name,
            "tier": spec.difficulty_tier,
            "train": train_data,
            "test": test_data,
            "test_hash": compute_dataset_hash(test_data),
            "num_test": len(test_data)
        }
        
    elif spec.name == "svamp":
        ds = load_dataset("Chillee/SVAMP", cache_dir=cache_dir)
        test_data = []
        for item in ds["test"]:
            test_data.append({
                "question": f"{item['Body']} {item['Question']}",
                "answer": f"#### {item['Answer']}"
            })
        test_data = test_data[:spec.sample_limit]
        return {
            "name": "svamp",
            "tier": "shift",
            "train": [],
            "test": test_data,
            "test_hash": compute_dataset_hash(test_data),
            "num_test": len(test_data)
        }
    else:
        raise ValueError(f"Unknown task name: {spec.name}")
