import os
import tempfile
import hashlib
import pytest

def verify_checkpoint_file(filepath, expected_sha256):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Checkpoint file not found: {filepath}")
    
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
            
    actual_sha256 = hasher.hexdigest()
    if actual_sha256 != expected_sha256:
        raise ValueError(f"Checkpoint SHA-256 mismatch: expected {expected_sha256}, got {actual_sha256}")
    return True

def test_checkpoint_hash_matches_file():
    """Verify that checkpoint verification calculates actual SHA-256 over weight binary files."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"dummy model weights tensor data binary")
        tmp_path = tmp.name
        
    try:
        actual_sha = hashlib.sha256(open(tmp_path, "rb").read()).hexdigest()
        assert verify_checkpoint_file(tmp_path, actual_sha) is True
        
        with pytest.raises(ValueError):
            verify_checkpoint_file(tmp_path, "0000000000000000000000000000000000000000000000000000000000000000")
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
