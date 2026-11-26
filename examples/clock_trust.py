"""Synthetic clock-trust example. Classifies invented readings; connects to nothing.

Times are seconds on one invented timeline. `ts` is the edge timestamp, `receipt`
is when the ingest host received the reading, `now` is the ingest host's clock.
"""

from math import isfinite
from numbers import Real

# Owner requirement for the overload-watch decision: older readings are shown as stale.
MAX_AGE_S = 60


def _bad_time(x):
    return isinstance(x, bool) or not isinstance(x, Real) or not isfinite(x)


class ClockGuard:
    """Per-signal trust state. `max_offset_s` is a calibration knob, not a site value."""

    def __init__(self, max_offset_s, max_age_s=MAX_AGE_S):
        if _bad_time(max_offset_s) or max_offset_s < 0 or _bad_time(max_age_s) or max_age_s <= 0:
            raise ValueError("offset and age limits must be finite; age must be positive")
        self.max_offset_s = max_offset_s
        self.max_age_s = max_age_s
        self.last_trusted = {}

    def observe(self, signal, ts, receipt, now):
        """Return 'current', 'stale', 'time-uncertain' or 'rejected'.

        Only current or stale readings advance the per-signal timestamp, so one
        future-dated reading cannot lock out later correct ones.
        """
        if not isinstance(signal, str) or not signal or any(_bad_time(x) for x in (ts, receipt, now)):
            return "rejected"
        previous = self.last_trusted.get(signal)
        if previous is not None and ts <= previous:
            return "rejected"  # backward step or repeated timestamp
        if abs(ts - receipt) > self.max_offset_s or receipt > now:
            return "time-uncertain"  # edge and ingest clocks disagree; never shown as current
        self.last_trusted[signal] = ts
        return "stale" if now - ts > self.max_age_s else "current"

    def age_status(self, signal, now):
        """Tick check with no new reading: has the last trusted reading aged out?"""
        last = self.last_trusted.get(signal)
        if last is None or _bad_time(now) or now - last > self.max_age_s:
            return "stale"
        return "current"


if __name__ == "__main__":
    guard = ClockGuard(max_offset_s=2)
    print(guard.observe("motor_current_a", 100, 100.4, 101))   # current
    print(guard.observe("motor_current_a", 99, 101.0, 102))    # rejected: backward step
    print(guard.observe("motor_current_a", 150, 103.0, 104))   # time-uncertain: offset
    print(guard.age_status("motor_current_a", 170))            # stale: 70 s since last trusted
