import json
import os
import sys
import hashlib
from transformers import AutoTokenizer

def verify_canary_independently():
    root_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026")
    canary_file = os.path.join(root_dir, "09_genuine_execution_v1/NEURAL_CANARY_RAW.jsonl")
    
    assert os.path.exists(canary_file), "NEURAL_CANARY_RAW.jsonl missing!"
    
    records = []
    with open(canary_file, "r") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
                
    assert len(records) == 2, f"Expected 2 canary records, found {len(records)}"
    
    for r in records:
        assert r["record_type"] == "forensic_neural_canary"
        assert r["parameter_count"] > 1_000_000_000, "Parameter count too low!"
        assert "Qwen2ForCausalLM" in r["model_class"], f"Invalid model class {r['model_class']}"
        assert r["generation_duration_sec"] > 0.05, "Generation runtime implausibly fast!"
        
        # Token round trip check
        tok = AutoTokenizer.from_pretrained(r["model_id"], revision=r["model_revision"])
        decoded_text = tok.decode(r["generated_token_ids"], skip_special_tokens=True)
        assert decoded_text == r["generated_text"], f"Decode mismatch for {r['model_id']}!"
        
        # Check token IDs are within BPE vocabulary bounds
        vocab_size = tok.vocab_size
        assert all(0 <= t < vocab_size for t in r["generated_token_ids"]), "Token ID out of BPE vocab range!"

    print("[+] INDEPENDENT CANARY VERIFIER: ALL CHECKS PASSED 100%.")

if __name__ == "__main__":
    verify_canary_independently()
