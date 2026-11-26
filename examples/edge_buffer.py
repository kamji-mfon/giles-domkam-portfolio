"""Synthetic edge-box buffer shared by sensor threads and an uploader thread.

While the uplink is down the buffer fills. Policy: keep the newest readings and
count every dropped one, so the gap is visible downstream instead of silent.
The capacity is a tuning value; a real edge box's memory budget is not set.
"""

import threading
from collections import deque


class Buffer:
    def __init__(self, capacity):
        if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 1:
            raise ValueError("capacity must be a positive integer")
        self._items = deque()
        self._capacity = capacity
        self._lock = threading.Lock()
        self.dropped = 0

    def put(self, item):
        with self._lock:
            if len(self._items) == self._capacity:
                self._items.popleft()
                self.dropped += 1
            self._items.append(item)

    def drain(self, limit):
        """Remove and return up to `limit` oldest readings for upload."""
        with self._lock:
            return [self._items.popleft() for _ in range(min(limit, len(self._items)))]

    def __len__(self):
        with self._lock:
            return len(self._items)


if __name__ == "__main__":
    buffer = Buffer(capacity=3)
    for n in range(5):
        buffer.put(n)
    print(buffer.drain(10), "dropped:", buffer.dropped)  # [2, 3, 4] dropped: 2
