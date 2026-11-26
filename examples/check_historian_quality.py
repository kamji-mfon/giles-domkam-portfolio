"""Run from the repository root using python3 examples/check_historian_quality.py."""

from historian_quality import classify_csv

data = "asset,timestamp,value,unit\nA,95,12,rpm\nA,90,10,rpm\nB,95,bad,rpm\nC,96,4,rpm\nC,96,5,rpm\nA,95,12,rpm\n"
assert [r["status"] for r in classify_csv(data, 100, 5)] == [
    "accepted", "stale", "invalid", "conflict", "conflict", "duplicate"
]
assert classify_csv("asset,timestamp,value,unit\nA,101,1,rpm\n", 100, 5)[0]["status"] == "invalid"
assert classify_csv("asset,timestamp,value,unit\nA,95,nan,rpm\n", 100, 5)[0]["status"] == "invalid"
try:
    classify_csv("asset,value\nA,2\n", 100, 5)
except ValueError:
    pass
else:
    raise AssertionError("missing required columns were accepted")
for now, max_age in ((100.0, 5), (100, -1), (100, True)):
    try:
        classify_csv(data, now, max_age)
    except ValueError:
        pass
    else:
        raise AssertionError(f"invalid clock arguments were accepted: {now!r}, {max_age!r}")
print("Synthetic historian quality checks passed")
