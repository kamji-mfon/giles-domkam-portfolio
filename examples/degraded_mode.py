"""Synthetic degraded-mode state machine for a read-only monitor. Actuates nothing.

Events come from clock_trust: 'current', 'stale', 'time-uncertain', 'rejected'.
Only 'normal' may present a value as current. The machine's own safe state is
outside this monitor and owned by the site.
"""

# Consecutive current readings needed before trusting the feed again; a tuning knob.
RECOVERY_READINGS = 3

TRANSITIONS = {
    ("normal", "current"): "normal",
    ("normal", "time-uncertain"): "degraded",
    ("normal", "rejected"): "degraded",
    ("normal", "stale"): "no-visibility",
    ("degraded", "current"): "recovering",
    ("degraded", "time-uncertain"): "degraded",
    ("degraded", "rejected"): "degraded",
    ("degraded", "stale"): "no-visibility",
    ("recovering", "current"): "recovering",
    ("recovering", "time-uncertain"): "degraded",
    ("recovering", "rejected"): "degraded",
    ("recovering", "stale"): "no-visibility",
    ("no-visibility", "current"): "recovering",
    ("no-visibility", "time-uncertain"): "degraded",
    ("no-visibility", "rejected"): "no-visibility",
    ("no-visibility", "stale"): "no-visibility",
}

DISPLAY = {
    "normal": "value shown as current",
    "recovering": "value shown, labelled not yet trusted",
    "degraded": "value withheld: time or data untrustworthy",
    "no-visibility": "NO CURRENT DATA (> 60 s): check the machine in person",
}

START = ("no-visibility", 0)


def step(state, event):
    """Return the next (mode, streak). Unknown modes or events raise KeyError."""
    mode, streak = state
    nxt = TRANSITIONS[(mode, event)]
    if nxt != "recovering":
        return nxt, 0
    streak = streak + 1 if mode == "recovering" else 1
    return ("normal", 0) if streak >= RECOVERY_READINGS else ("recovering", streak)


if __name__ == "__main__":
    state = START
    for event in ("current", "current", "current", "time-uncertain", "stale"):
        state = step(state, event)
        print(f"{event:15} -> {state[0]:14} {DISPLAY[state[0]]}")
