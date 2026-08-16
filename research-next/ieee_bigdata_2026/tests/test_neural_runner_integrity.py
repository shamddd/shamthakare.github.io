import pytest
import sys
import os
import ast

pkg_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026")
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

def test_no_synthetic_probability_in_runner():
    runner_file = os.path.join(pkg_dir, "recovery_eval/execution/neural_runner.py")
    with open(runner_file, "r") as f:
        code = f.read()
        
    assert "np.random.rand()" not in code
    assert "p_success" not in code
    assert "ord(" not in code
    assert "model.generate" in code

def test_empirical_tokens_round_trip(tmp_path):
    from recovery_eval.execution.neural_runner import EmpiricalNeuralRolloutRecord
    import torch
    
    class DummyTokenizer:
        def decode(self, token_ids, skip_special_tokens=True):
            return "Decoded math answer."
            
    tok = DummyTokenizer()
    input_tensor = torch.tensor([[1, 2, 3]])
    output_tensor = torch.tensor([[1, 2, 3, 100, 101, 102]])
    
    rec = EmpiricalNeuralRolloutRecord(
        experiment_id="test", rollout_id="r1", problem_id="p1", state_id="s1",
        recovery_or_control="CONTROL", policy_id="m1", model_id="m1", model_revision="r",
        model_class="Qwen2ForCausalLM", parameter_count=1500000000, weight_manifest_sha256="h",
        tokenizer_revision="r", device="mps:0", dtype="torch.float16",
        canonical_semantic_state_hash="h1", serialized_input_sha256="h2",
        input_ids_tensor=input_tensor, output_ids_tensor=output_tensor, tokenizer=tok,
        generation_seed=401, temperature=0.7, top_p=0.9, max_new_tokens=32,
        start_ns=1000000, end_ns=500000000, verifier_input="q", verifier_raw_output={},
        primitive_success=True, git_commit="e68dde7"
    )
    
    assert rec.generated_token_ids == [100, 101, 102]
    assert rec.generated_text == "Decoded math answer."
