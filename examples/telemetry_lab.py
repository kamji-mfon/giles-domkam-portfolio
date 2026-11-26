"""Synthetic offline telemetry lab: no devices, networks, or physical control."""

import math
import sqlite3


class TelemetryLab:
    def __init__(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE samples (device TEXT, signal TEXT, ts INTEGER, value REAL, "
                        "PRIMARY KEY(device, signal, ts))")
        self.queue = []

    def queue_sample(self, device, signal, ts, value):
        self.queue.append((device, signal, ts, value))

    def deliver(self, allowed_device, now, online=True):
        """Deliver only explicitly allowed device data; preserve rejects for review."""
        if not online:
            return {"accepted": 0, "duplicates": 0, "rejected": 0}
        counts = {"accepted": 0, "duplicates": 0, "rejected": 0}
        remaining = []
        with self.db:
            for row in self.queue:
                if not valid(row, allowed_device, now):
                    counts["rejected"] += 1
                    remaining.append(row)
                    continue
                old = self.db.execute(
                    "SELECT value FROM samples WHERE device=? AND signal=? AND ts=?", row[:3]
                ).fetchone()
                if old is not None:
                    if old[0] != row[3]:
                        counts["rejected"] += 1
                        remaining.append(row)
                    else:
                        counts["duplicates"] += 1
                    continue
                self.db.execute("INSERT INTO samples VALUES (?, ?, ?, ?)", row)
                counts["accepted"] += 1
        self.queue = remaining
        return counts


def valid(row, allowed_device, now):
    device, signal, ts, value = row
    if not isinstance(allowed_device, str) or not allowed_device or device != allowed_device:
        return False
    if not isinstance(signal, str) or not signal.strip() or isinstance(ts, bool) or not isinstance(ts, int):
        return False
    if isinstance(now, bool) or not isinstance(now, int) or ts > now or not -(2**63) <= ts < 2**63:
        return False
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


if __name__ == "__main__":
    lab = TelemetryLab()
    lab.queue_sample("synthetic-device", "speed", 10, 42)
    print("Offline:", lab.deliver("synthetic-device", 10, online=False))
    print("Replay:", lab.deliver("synthetic-device", 10))
