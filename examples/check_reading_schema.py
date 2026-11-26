"""Run from the repository root using python3 examples/check_reading_schema.py."""

from reading_schema import compatible, parse_version, validate

base = {"device": "edge-1", "signal": "motor_current_a", "ts": 100, "value": 12.5}

# Compatibility rule: same major, record minor no newer than reader.
assert compatible("1.1", "1.0") and compatible("1.1", "1.1")
assert not compatible("1.0", "1.1")      # old reader, newer optional fields
assert not compatible("1.1", "2.0")      # breaking change
assert not compatible("2.0", "1.0")
assert parse_version("10.2") == (10, 2)
for bad in ("1", "1.", ".1", "a.b", "1.1.1", None, 1.1):
    try:
        parse_version(bad)
    except ValueError:
        pass
    else:
        raise AssertionError(f"parsed {bad!r}")

assert validate({**base, "schema": "1.0"}) == []
assert validate({**base, "schema": "1.1", "unit": "A"}) == []
assert validate({**base, "schema": "1.1"}) == []                  # unit is optional
assert validate({**base, "schema": "1.0", "unit": "A"}) == ["unknown field unit"]
assert validate({**base, "schema": "1.1", "unit": "A"}, reader="1.0") == ["schema 1.1 not readable by 1.0"]
assert validate({**base, "schema": "2.0"}) == ["schema 2.0 not readable by 1.1"]
assert validate({**base}) == ["bad schema version None"]
assert validate([1]) == ["record is not an object"]
assert validate({"schema": "1.0", "device": "edge-1"}) == ["missing signal", "missing ts", "missing value"]
assert validate({**base, "schema": "1.0", "ts": 1.5}) == ["bad ts"]
assert validate({**base, "schema": "1.0", "ts": True}) == ["bad ts"]
assert validate({**base, "schema": "1.0", "value": float("nan")}) == ["bad value"]
assert validate({**base, "schema": "1.0", "device": ""}) == ["bad device"]
assert validate({**base, "schema": "1.1", "unit": 5}) == ["bad unit"]
print("Synthetic reading-schema checks passed")
