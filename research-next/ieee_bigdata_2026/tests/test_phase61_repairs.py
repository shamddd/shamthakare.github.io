import pytest
import sys
import os
import json

pkg_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026")
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from recovery_eval.policies.adapters import BaseModelAdapter, InstructModelAdapter, compute_hashes

def test_base_model_adapter_formatting():
    adapter = BaseModelAdapter()
    text = adapter.format_input("What is 2+2?", ["Step 1: 2+2=4"])
    assert "Question: What is 2+2?" in text
    assert "Step 1: 2+2=4" in text
    assert "<|im_start|>" not in text

def test_instruct_model_adapter_formatting():
    adapter = InstructModelAdapter()
    text = adapter.format_input("What is 2+2?", ["Step 1: 2+2=4"])
    assert "<|im_start|>system" in text
    assert "<|im_start|>user" in text
    assert "<|im_start|>assistant" in text
    assert "Step 1: 2+2=4" in text

def test_compute_hashes_uniqueness():
    b_adapter = BaseModelAdapter()
    i_adapter = InstructModelAdapter()
    
    sem_b, in_b, _ = compute_hashes("What is 2+2?", ["Step 1"], b_adapter)
    sem_i, in_i, _ = compute_hashes("What is 2+2?", ["Step 1"], i_adapter)
    
    # Semantic state hash MUST be identical
    assert sem_b == sem_i
    # Formatted model input hash MUST be different (due to template)
    assert in_b != in_i
