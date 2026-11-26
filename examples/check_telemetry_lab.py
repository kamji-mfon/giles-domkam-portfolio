"""Run with python3 examples/check_telemetry_lab.py."""

from telemetry_lab import TelemetryLab

lab = TelemetryLab()
lab.queue_sample("device-a", "speed", 10, 42)
assert lab.deliver("device-a", 10, online=False)["accepted"] == 0
assert len(lab.queue) == 1
assert lab.deliver("device-a", 10) == {"accepted": 1, "duplicates": 0, "rejected": 0}
assert not lab.queue
lab.queue_sample("device-a", "speed", 10, 42)
assert lab.deliver("device-a", 10)["duplicates"] == 1
lab.queue_sample("device-a", "speed", 10, 43)
lab.queue_sample("device-b", "speed", 10, 1)
lab.queue_sample("device-a", "speed", 11, 1)
lab.queue_sample("device-a", "speed", 10, float("nan"))
lab.queue_sample("device-a", "speed", -(2**64), 1)
lab.queue_sample("device-a", " ", 10, 1)
lab.queue_sample("device-a", "speed", 9, "42")
lab.queue_sample("device-a", "speed", 8, 10**1000)
assert lab.deliver("device-a", 10)["rejected"] == 8
assert len(lab.queue) == 8
assert lab.db.execute("SELECT COUNT(*) FROM samples").fetchone()[0] == 1
print("Synthetic telemetry lab checks passed")
