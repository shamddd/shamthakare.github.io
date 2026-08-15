import json
import hashlib
import os

VALID_EXPOSURE_STATUSES = {
    "UNSEEN", "DEVELOPMENT_EXPOSED", "PILOT_EXPOSED",
    "SIMULATION_EXPOSED", "CONFIRMATORY_RESERVED", "EXCLUDED"
}

class ExposureLedger:
    def __init__(self, ledger_path):
        self.ledger_path = ledger_path
        self.entries = {}
        if os.path.exists(ledger_path):
            with open(ledger_path, "r") as f:
                self.entries = json.load(f)

    def register_item(self, item_id, dataset, text_hash, status="UNSEEN", reason="Initial import"):
        if status not in VALID_EXPOSURE_STATUSES:
            raise ValueError(f"Invalid exposure status: {status}")
        
        # State transition rule: status can only escalate exposure
        if item_id in self.entries:
            curr_status = self.entries[item_id]["status"]
            if curr_status == "DEVELOPMENT_EXPOSED" and status == "UNSEEN":
                raise ValueError(f"Cannot revert exposure status of {item_id} from {curr_status} to {status}")

        self.entries[item_id] = {
            "item_id": item_id,
            "dataset": dataset,
            "text_hash": text_hash,
            "status": status,
            "reason": reason
        }

    def save(self):
        with open(self.ledger_path, "w") as f:
            json.dump(self.entries, f, indent=2)
