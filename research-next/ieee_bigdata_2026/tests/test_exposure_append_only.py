import pytest
import sys
import os
import json

pkg_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research-next/ieee_bigdata_2026")
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from recovery_eval.exposure.event_ledger import EventLedger

def test_exposure_append_only(tmp_path):
    f = tmp_path / "ledger.json"
    el = EventLedger(str(f))
    el.record_transition("item1", "GSM8K", "hash1", "CONFIRMATORY_RESERVED", "Locking for evaluation")
    el.save()
    
    assert len(el.events) == 1
    assert el.get_current_status("item1") == "CONFIRMATORY_RESERVED"

def test_exposure_illegal_downgrade(tmp_path):
    f = tmp_path / "ledger.json"
    el = EventLedger(str(f))
    el.record_transition("item1", "GSM8K", "hash1", "DEVELOPMENT_EXPOSED", "Dev use")
    
    with pytest.raises(ValueError, match="Illegal status downgrade"):
        el.record_transition("item1", "GSM8K", "hash1", "UNSEEN", "Attempt downgrade")

def test_exposure_hash_chain(tmp_path):
    f = tmp_path / "ledger.json"
    el = EventLedger(str(f))
    el.record_transition("item1", "GSM8K", "hash1", "CONFIRMATORY_RESERVED", "Lock 1")
    el.record_transition("item2", "GSM8K", "hash2", "DEVELOPMENT_EXPOSED", "Lock 2")
    el.save()
    
    # Tamper with file
    with open(f, "r") as fp:
        data = json.load(fp)
    data[0]["reason"] = "Tampered reason"
    with open(f, "w") as fp:
        json.dump(data, fp)
        
    with pytest.raises(ValueError, match="payload tampered"):
        EventLedger(str(f))

def test_excluded_terminal(tmp_path):
    f = tmp_path / "ledger.json"
    el = EventLedger(str(f))
    el.record_transition("item1", "GSM8K", "hash1", "EXCLUDED", "Defective format")
    
    with pytest.raises(ValueError, match="terminal status"):
        el.record_transition("item1", "GSM8K", "hash1", "UNSEEN", "Reactivate")
