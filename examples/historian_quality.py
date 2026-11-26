"""Classify synthetic historian rows; no network, plant data, or physical control."""

import csv
import io
import json
import math
from collections import Counter

REQUIRED = {"asset", "timestamp", "value", "unit"}


def classify_csv(text, now, max_age):
    """Separate good, invalid, stale, duplicate, and conflicting observations."""
    if not isinstance(now, int) or isinstance(now, bool) or not isinstance(max_age, int) or isinstance(max_age, bool) or max_age < 0:
        raise ValueError("now and max_age must be integer seconds; max_age must be non-negative")
    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
        raise ValueError("missing required columns")
    rows = []
    for row in reader:
        try:
            asset, unit = row["asset"].strip(), row["unit"].strip()
            stamp, value = int(row["timestamp"]), float(row["value"])
            if not asset or not unit or not math.isfinite(value) or stamp > now:
                raise ValueError("invalid reading")
        except (ValueError, TypeError, KeyError, AttributeError):
            rows.append({"status": "invalid"})
            continue
        rows.append({"asset": asset, "timestamp": stamp, "value": value, "unit": unit})
    return _mark_quality(rows, now, max_age)


def _mark_quality(rows, now, max_age):
    groups = {}
    for row in rows:
        if "status" not in row:
            groups.setdefault((row["asset"], row["timestamp"]), set()).add((row["value"], row["unit"]))
    seen = set()
    for row in rows:
        if "status" in row:
            continue
        key = row["asset"], row["timestamp"]
        if len(groups[key]) > 1:
            row["status"] = "conflict"
        elif key in seen:
            row["status"] = "duplicate"
        elif now - row["timestamp"] > max_age:
            row["status"] = "stale"
        else:
            row["status"] = "accepted"
        seen.add(key)
    return rows


if __name__ == "__main__":
    data = "asset,timestamp,value,unit\nA,95,12,rpm\nA,90,10,rpm\nB,95,bad,rpm\nC,96,4,rpm\nC,96,5,rpm\n"
    print(json.dumps(dict(Counter(row["status"] for row in classify_csv(data, 100, 5))), sort_keys=True))
