"""Run with python3 examples/check_monitoring_demo.py."""

from monitoring_demo import evaluate

assert evaluate({"timestamp": 90, "value": 1}, 100, 10) == "available"
assert evaluate({"timestamp": 89, "value": 1}, 100, 10) == "stale"
assert evaluate({"timestamp": 101, "value": 1}, 100, 10) == "invalid"
assert evaluate({"timestamp": 95, "value": float("nan")}, 100, 10) == "invalid"
assert evaluate({"timestamp": 95}, 100, 10) == "invalid"
assert evaluate({"timestamp": True, "value": 1}, 100, 10) == "invalid"
assert evaluate({"timestamp": 95, "value": 10**1000}, 100, 10) == "invalid"
assert evaluate({"timestamp": 95, "value": 1}, 100, -1) == "invalid"
assert evaluate([95, 1], 100, 10) == "invalid"
print("Synthetic monitoring checks passed")
