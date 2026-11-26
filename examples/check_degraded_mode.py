"""Run from the repository root using python3 examples/check_degraded_mode.py."""

from degraded_mode import DISPLAY, RECOVERY_READINGS, START, TRANSITIONS, step

MODES = set(DISPLAY)
EVENTS = {"current", "stale", "time-uncertain", "rejected"}

# The table is total: every mode handles every event and lands on a known mode.
assert set(TRANSITIONS) == {(m, e) for m in MODES for e in EVENTS}
assert set(TRANSITIONS.values()) <= MODES

# Start without visibility; recovery needs RECOVERY_READINGS consecutive current readings.
state = START
for _ in range(RECOVERY_READINGS - 1):
    state = step(state, "current")
    assert state[0] == "recovering"
state = step(state, "current")
assert state == ("normal", 0)

# Any loss of trust leaves normal; stale always means no visibility.
for event, expected in (("time-uncertain", "degraded"), ("rejected", "degraded"), ("stale", "no-visibility")):
    assert step(("normal", 0), event) == (expected, 0)
for mode in MODES:
    assert step((mode, 0), "stale") == ("no-visibility", 0)

# A bad reading mid-recovery resets the streak.
state = step(("degraded", 0), "current")
state = step(state, "rejected")
assert state == ("degraded", 0)
state = step(state, "current")
assert state == ("recovering", 1)

# A rejected reading never restores visibility.
assert step(("no-visibility", 0), "rejected") == ("no-visibility", 0)

for bad in ((("normal", 0), "unknown"), (("halted", 0), "current")):
    try:
        step(*bad)
    except KeyError:
        pass
    else:
        raise AssertionError(f"accepted {bad}")
print("Synthetic degraded-mode checks passed")
