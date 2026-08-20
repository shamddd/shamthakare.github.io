import sys
import os
import pytest

pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from recovery_eval.exposure.ledger import ExposureLedger

def test_exposure_ledger_escalation_rule(tmp_path):
    ledger_file = tmp_path / "exposure.json"
    ledger = ExposureLedger(str(ledger_file))
    ledger.register_item("item1", "GSM8K", "hash123", status="UNSEEN")
    ledger.register_item("item1", "GSM8K", "hash123", status="DEVELOPMENT_EXPOSED")
    
    with pytest.raises(ValueError):
        ledger.register_item("item1", "GSM8K", "hash123", status="UNSEEN")

def test_exposure_ledger_invalid_status(tmp_path):
    ledger_file = tmp_path / "exposure.json"
    ledger = ExposureLedger(str(ledger_file))
    with pytest.raises(ValueError):
        ledger.register_item("item1", "GSM8K", "hash123", status="INVALID_STATUS")
