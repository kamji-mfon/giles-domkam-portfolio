"""Run from the repository root using python3 examples/check_observation_contract.py."""

from observation_contract import permitted

record = {"start": 10, "end": 20, "scope": ["192.0.2.0/24"]}
assert permitted(record, "192.0.2.7", 10)
assert permitted(record, "192.0.2.7", 20)
assert not permitted(None, "192.0.2.7", 15)
assert not permitted(record, "192.0.2.7", 21)
assert not permitted(record, "192.0.2.7", 9)
assert not permitted(record, "198.51.100.7", 15)
assert not permitted({"start": 10, "scope": ["192.0.2.0/24"]}, "192.0.2.7", 15)
assert not permitted({**record, "scope": ["bad-network"]}, "192.0.2.7", 15)
assert not permitted(record, "bad-address", 15)
assert not permitted({**record, "scope": []}, "192.0.2.7", 15)
assert not permitted(record, None, 15)
print("Synthetic observation authorization checks passed")
