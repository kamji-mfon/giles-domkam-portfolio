"""Run from the repository root using python3 examples/check_edge_buffer.py."""

import threading

from edge_buffer import Buffer

# Drop-oldest policy, single thread.
b = Buffer(3)
for n in range(5):
    b.put(n)
assert b.drain(2) == [2, 3] and b.dropped == 2 and len(b) == 1
assert b.drain(10) == [4] and b.drain(10) == []

for bad in (0, -1, True, 2.5, None):
    try:
        Buffer(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"accepted capacity {bad!r}")

# Two sensor threads and an uploader at once: nothing lost without being counted,
# and each sensor's readings stay in order.
PER_SENSOR = 20_000
b = Buffer(100)
uploaded = []
done = threading.Event()


def sensor(name):
    for seq in range(PER_SENSOR):
        b.put((name, seq))


def uploader():
    while not done.is_set():
        uploaded.extend(b.drain(25))
    uploaded.extend(b.drain(10**9))


sensors = [threading.Thread(target=sensor, args=(name,)) for name in ("current", "speed")]
up = threading.Thread(target=uploader)
up.start()
for t in sensors:
    t.start()
for t in sensors:
    t.join()
done.set()
up.join()

assert len(uploaded) + b.dropped == 2 * PER_SENSOR, (len(uploaded), b.dropped)
assert len(b) == 0
for name in ("current", "speed"):
    seqs = [seq for who, seq in uploaded if who == name]
    assert seqs == sorted(seqs) and len(set(seqs)) == len(seqs)
# Not asserted: a share per sensor. One busy sensor can evict all of another's
# readings from a shared buffer; see the trade-offs in cps-architecture.md.
print("Synthetic edge-buffer checks passed")
