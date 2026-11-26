"""Synthetic versioned reading schema with a compatibility rule. No network API.

Versions are 'MAJOR.MINOR'. A reader accepts a record with the same major and a
minor no newer than its own: minors only add optional fields, majors may break.
"""

from math import isfinite
from numbers import Real

# Required fields per major; optional fields introduced by each minor.
REQUIRED = {1: {"device": str, "signal": str, "ts": int, "value": Real}}
OPTIONAL = {(1, 1): {"unit": str}}

READER_VERSION = "1.1"


def parse_version(text):
    major, sep, minor = text.partition(".") if isinstance(text, str) else ("", "", "")
    if not (sep and major.isdigit() and minor.isdigit()):
        raise ValueError(f"bad schema version {text!r}")
    return int(major), int(minor)


def compatible(reader, record_version):
    r_major, r_minor = parse_version(reader)
    w_major, w_minor = parse_version(record_version)
    return r_major == w_major and w_minor <= r_minor


def _type_ok(value, kind):
    if isinstance(value, bool):
        return False
    if kind is Real:
        return isinstance(value, Real) and isfinite(value)
    return isinstance(value, kind) and (kind is not str or value != "")


def validate(record, reader=READER_VERSION):
    """Return a list of problems; an empty list means the reader may use the record."""
    if not isinstance(record, dict):
        return ["record is not an object"]
    try:
        if not compatible(reader, record.get("schema")):
            return [f"schema {record.get('schema')} not readable by {reader}"]
    except ValueError as exc:
        return [str(exc)]
    major, minor = parse_version(record["schema"])
    fields = dict(REQUIRED[major])
    allowed = set(fields) | {"schema"}
    for (o_major, o_minor), extra in OPTIONAL.items():
        if o_major == major and o_minor <= minor:
            allowed |= set(extra)
            fields.update({k: v for k, v in extra.items() if k in record})
    problems = [f"missing {k}" for k in REQUIRED[major] if k not in record]
    problems += [f"unknown field {k}" for k in record if k not in allowed]
    problems += [f"bad {k}" for k, kind in fields.items() if k in record and not _type_ok(record[k], kind)]
    return problems


if __name__ == "__main__":
    print(validate({"schema": "1.0", "device": "edge-1", "signal": "motor_current_a", "ts": 100, "value": 12.5}))
    print(validate({"schema": "2.0", "device": "edge-1", "signal": "motor_current_a", "ts": 100, "value": 12.5}))
