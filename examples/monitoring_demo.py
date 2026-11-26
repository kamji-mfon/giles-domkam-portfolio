"""Synthetic monitoring example; no network, equipment, or control commands."""

import json
import math


def evaluate(sample, now, max_age):
    """Classify one reading; invalid or stale data must not look healthy."""
    if not isinstance(sample, dict):
        return "invalid"
    timestamp, value = sample.get("timestamp"), sample.get("value")
    numbers = (timestamp, value, now, max_age)
    if any(isinstance(n, bool) or not isinstance(n, (int, float)) for n in numbers):
        return "invalid"
    try:
        finite = all(math.isfinite(n) for n in numbers)
    except OverflowError:
        return "invalid"
    if not finite or max_age < 0:
        return "invalid"
    if timestamp > now:
        return "invalid"
    if now - timestamp > max_age:
        return "stale"
    return "available"


def main():
    # Synthetic seconds on a shared clock; the threshold is illustrative only.
    now, max_age = 100, 10
    samples = {
        "fresh": {"timestamp": 95, "value": 12},
        "stale": {"timestamp": 80, "value": 12},
        "future": {"timestamp": 101, "value": 12},
        "invalid": {"timestamp": 95, "value": float("nan")},
    }
    print(json.dumps({name: evaluate(sample, now, max_age) for name, sample in samples.items()}, indent=2))


if __name__ == "__main__":
    main()
