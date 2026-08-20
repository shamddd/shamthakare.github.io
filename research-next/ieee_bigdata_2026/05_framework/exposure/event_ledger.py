import json
import hashlib
import os
import time

ALLOWED_STATUSES = {
    "UNSEEN", "CONFIRMATORY_RESERVED", "DEVELOPMENT_EXPOSED",
    "PILOT_EXPOSED", "SIMULATION_EXPOSED", "EXCLUDED"
}

ALLOWED_TRANSITIONS = {
    "UNSEEN": {"CONFIRMATORY_RESERVED", "DEVELOPMENT_EXPOSED", "PILOT_EXPOSED", "SIMULATION_EXPOSED", "EXCLUDED"},
    "CONFIRMATORY_RESERVED": {"DEVELOPMENT_EXPOSED", "PILOT_EXPOSED", "SIMULATION_EXPOSED", "EXCLUDED"},
    "DEVELOPMENT_EXPOSED": {"PILOT_EXPOSED", "SIMULATION_EXPOSED", "EXCLUDED"},
    "PILOT_EXPOSED": {"SIMULATION_EXPOSED", "EXCLUDED"},
    "SIMULATION_EXPOSED": {"EXCLUDED"},
    "EXCLUDED": set()  # Terminal state
}

class EventLedger:
    def __init__(self, ledger_file):
        self.ledger_file = ledger_file
        self.events = []
        if os.path.exists(ledger_file):
            with open(ledger_file, "r") as f:
                self.events = json.load(f)
            self._verify_chain()

    def _verify_chain(self):
        prev_hash = "GENESIS"
        for i, ev in enumerate(self.events):
            if ev["previous_event_hash"] != prev_hash:
                raise ValueError(f"Hash chain broken at event index {i}")
            # Re-compute event hash
            payload = {k: v for k, v in ev.items() if k != "event_hash"}
            calc_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
            if calc_hash != ev["event_hash"]:
                raise ValueError(f"Event payload tampered at index {i}")
            prev_hash = ev["event_hash"]

    def get_current_status(self, item_id):
        status = None
        for ev in self.events:
            if ev["item_id"] == item_id:
                status = ev["new_status"]
        return status or "UNSEEN"

    def record_transition(self, item_id, dataset, item_hash, new_status, reason, git_commit="bc7c62a", actor="governance_agent"):
        if new_status not in ALLOWED_STATUSES:
            raise ValueError(f"Invalid status: {new_status}")
            
        curr_status = self.get_current_status(item_id)
        if curr_status == new_status:
            return  # No-op
            
        if curr_status == "EXCLUDED":
            raise ValueError(f"Item {item_id} is EXCLUDED (terminal status) and cannot transition to {new_status}")
            
        if new_status not in ALLOWED_TRANSITIONS.get(curr_status, set()):
            raise ValueError(f"Illegal status downgrade/transition for {item_id}: {curr_status} -> {new_status}")

        prev_hash = self.events[-1]["event_hash"] if self.events else "GENESIS"
        event_id = f"ev_{len(self.events) + 1:06d}"
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        payload = {
            "event_id": event_id,
            "item_id": item_id,
            "dataset": dataset,
            "item_hash": item_hash,
            "previous_status": curr_status,
            "new_status": new_status,
            "timestamp_utc": timestamp,
            "reason": reason,
            "git_commit": git_commit,
            "actor": actor,
            "previous_event_hash": prev_hash
        }
        event_hash = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
        payload["event_hash"] = event_hash
        self.events.append(payload)

    def save(self):
        with open(self.ledger_file, "w") as f:
            json.dump(self.events, f, indent=2)
