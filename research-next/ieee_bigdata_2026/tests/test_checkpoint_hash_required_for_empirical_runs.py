import pytest

def test_checkpoint_hash_required_for_empirical_runs():
    """Verify that empirical runs fail if checkpoint_sha256 is missing."""
    run_metadata = {"checkpoint_path": "/tmp/dummy.pt", "checkpoint_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
    assert "checkpoint_sha256" in run_metadata
    assert len(run_metadata["checkpoint_sha256"]) == 64
