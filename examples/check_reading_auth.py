"""Run from the repository root using python3 examples/check_reading_auth.py."""

from reading_auth import Verifier, sign

KEY_A, KEY_B = b"synthetic-key-a", b"synthetic-key-b"
r1 = {"device": "edge-a", "seq": 1, "signal": "motor_current_a", "ts": 100, "value": 12.5}
v = Verifier({"edge-a": KEY_A, "edge-b": KEY_B})

assert v.accept(r1, sign(KEY_A, r1)) == "ok"
assert v.accept(r1, sign(KEY_A, r1)) == "replay"                       # same reading again
old = {**r1, "seq": 0}
assert v.accept(old, sign(KEY_A, old)) == "replay"                     # older counter
r2 = {**r1, "seq": 2}
assert v.accept({**r2, "value": 99.0}, sign(KEY_A, r2)) == "bad-tag"    # value changed in transit
assert v.accept(r2, sign(KEY_B, r2)) == "bad-tag"                      # wrong device key
tag = sign(KEY_A, r2)
assert v.accept(r2, tag[:-1] + ("1" if tag[-1] == "0" else "0")) == "bad-tag"  # one digit altered
assert v.last_seq["edge-a"] == 1
r3 = {**r1, "seq": 3}
assert v.accept(r3, sign(KEY_A, r3)) == "ok"                           # gaps in seq are allowed
forged = {**r1, "seq": 10**6}
assert v.accept(forged, "0" * 64) == "bad-tag"
assert v.last_seq["edge-a"] == 3                                       # forged seq did not advance

other = {**r1, "device": "edge-c"}
assert v.accept(other, sign(KEY_A, other)) == "unknown-device"
for bad_reading in (None, [], {**r1, "seq": True}, {**r1, "seq": "4"}, {**r1, "device": ["edge-a"]},
                    {**r1, "seq": 4, "value": float("nan")}):
    assert v.accept(bad_reading, "0" * 64) == "malformed", bad_reading
assert v.accept(r1, None) == "malformed"
print("Synthetic reading-authentication checks passed")
