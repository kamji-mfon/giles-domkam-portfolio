"""Synthetic reading authentication: the edge box tags each reading, ingest verifies.

Keys here are invented. Key provisioning, storage and rotation on a real edge box
are not demonstrated. The sequence counter must survive an edge reboot, or every
reading after the reboot is rejected as a replay.
"""

import hashlib
import hmac
import json


def _payload(reading):
    return json.dumps(reading, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def sign(key, reading):
    """HMAC-SHA256 over a canonical JSON encoding of the whole reading."""
    return hmac.new(key, _payload(reading), hashlib.sha256).hexdigest()


class Verifier:
    def __init__(self, keys):
        self.keys = dict(keys)
        self.last_seq = {}

    def accept(self, reading, tag):
        """Return 'ok', 'malformed', 'unknown-device', 'bad-tag' or 'replay'."""
        if not isinstance(reading, dict) or not isinstance(tag, str):
            return "malformed"
        device, seq = reading.get("device"), reading.get("seq")
        if not isinstance(device, str) or isinstance(seq, bool) or not isinstance(seq, int):
            return "malformed"
        key = self.keys.get(device)
        if key is None:
            return "unknown-device"
        try:
            expected = sign(key, reading)
        except (TypeError, ValueError):
            return "malformed"
        if not hmac.compare_digest(expected, tag):
            return "bad-tag"
        # Checked after the tag so an attacker cannot advance the counter.
        if seq <= self.last_seq.get(device, -1):
            return "replay"
        self.last_seq[device] = seq
        return "ok"


if __name__ == "__main__":
    key = b"synthetic-key-not-a-secret"
    reading = {"device": "edge-1", "seq": 1, "signal": "motor_current_a", "ts": 100, "value": 12.5}
    verifier = Verifier({"edge-1": key})
    tag = sign(key, reading)
    print(verifier.accept(reading, tag))                       # ok
    print(verifier.accept(reading, tag))                       # replay
    print(verifier.accept({**reading, "seq": 2, "value": 99}, tag))  # bad-tag
