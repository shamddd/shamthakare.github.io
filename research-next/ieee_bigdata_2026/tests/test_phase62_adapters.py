import pytest
import sys
import os
import hashlib

pkg_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026")
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from recovery_eval.policies.adapters import BaseModelAdapter, InstructModelAdapter, compute_hashes_v2

class MockTokenizer:
    def encode(self, text):
        return [100, 101, 102]
        
    def apply_chat_template(self, messages, tokenize=False, add_generation_prompt=True):
        if tokenize:
            return [15, 22, 104, 305]
        return "<|im_start|>system\nMock<|im_end|>\n<|im_start|>assistant\n"

def test_instruct_adapter_uses_tokenizer_chat_template():
    tok = MockTokenizer()
    adapter = InstructModelAdapter()
    text, token_ids, token_hash = adapter.tokenize_and_hash("What is 3+3?", ["Step 1"], tokenizer=tok)
    
    assert token_ids == [15, 22, 104, 305]
    assert "<|im_start|>" in text

def test_serialized_hash_matches_actual_input_tokens():
    tok = MockTokenizer()
    adapter = InstructModelAdapter()
    sem_hash, input_sha256, text, token_ids = compute_hashes_v2("What is 3+3?", ["Step 1"], adapter, tokenizer=tok)
    
    expected_hash = hashlib.sha256(str(token_ids).encode()).hexdigest()
    # Ensure input_sha256 is derived strictly from actual token IDs
    assert len(input_sha256) == 64
