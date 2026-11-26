"""Run from the repository root using python3 examples/check_clock_trust.py."""

from clock_trust import MAX_AGE_S, ClockGuard

assert MAX_AGE_S == 60

g = ClockGuard(max_offset_s=2)
assert g.age_status("a", 0) == "stale"                      # nothing trusted yet
assert g.observe("a", 100, 101, 101) == "current"
assert g.observe("a", 100, 102, 102) == "rejected"          # repeated timestamp
assert g.observe("a", 90, 103, 103) == "rejected"           # backward step
assert g.observe("a", 200, 104, 104) == "time-uncertain"    # edge clock far ahead
assert g.observe("a", 105, 105, 105) == "current"           # uncertain reading did not lock out
assert g.observe("a", 106, 109, 109) == "time-uncertain"    # offset 3 s > 2 s
assert g.observe("a", 107, 108, 107) == "time-uncertain"    # receipt after host now
assert g.observe("b", 40, 41, 101) == "stale"               # 61 s old on arrival
assert g.observe("b", 41, 42, 101) == "current"             # exactly 60 s is still current
assert g.age_status("a", 165) == "current"
assert g.age_status("a", 166) == "stale"

for bad in (None, True, float("nan"), float("inf"), "1"):
    assert g.observe("c", bad, 1, 1) == "rejected"
    assert g.observe("c", 1, bad, 1) == "rejected"
    assert g.observe("c", 1, 1, bad) == "rejected"
assert g.observe("", 1, 1, 1) == "rejected"
assert g.observe(None, 1, 1, 1) == "rejected"
assert g.age_status("a", float("nan")) == "stale"
assert "c" not in g.last_trusted

for args in ((-1,), (float("nan"),), (True,), (2, 0), (2, float("inf"))):
    try:
        ClockGuard(*args)
    except ValueError:
        pass
    else:
        raise AssertionError(f"accepted bad limits {args}")
print("Synthetic clock-trust checks passed")
