# Synthetic telemetry interface — version 1

[← Telemetry pipeline](telemetry-pipeline.md)

This is the contract for `examples/telemetry_lab.py` only. It is a public educational example, not the interface of any private product and not a network API. The version identifies this documented example; incompatible changes should use a new version or explicitly revise this one.

## Input and trust boundary

An invented sample is a tuple: `device`, `signal`, `ts`, `value`. The example receives an `allowed_device` string from its caller. That string is a policy input, **not authenticated identity**. The example checks device equality, a nonblank signal, a signed 64-bit integer timestamp no later than the supplied synthetic `now`, and a finite numeric value. It has no units, calibrated sensor, transport security, access control, or clock verification.

## Processing and outcomes

| Condition | Example outcome |
|---|---|
| Offline | Leave the invented reading in the in-memory queue |
| Valid new observation | Store in an in-memory database and remove from the queue |
| Same device, signal, timestamp and value | Count as duplicate and remove from the queue |
| Same device, signal and timestamp but different value | Retain as rejected for review; do not overwrite the stored value |
| Wrong device, future timestamp, invalid value or blank signal | Retain as rejected for review |

An example run is `python3 examples/check_telemetry_lab.py`. The queue and database do not survive restart; the example does not guarantee recovery, model concurrency, or represent a production historian. The data model deliberately omits plant configuration, credentials, client data, and proprietary calculation rules.

## Versioned record schema

`examples/reading_schema.py` adds a dictionary form of the same reading with a `schema` field of the form `MAJOR.MINOR`. Version `1.0` requires `device`, `signal`, `ts` (integer) and `value` (finite number). Version `1.1` adds an optional `unit` string. The compatibility rule: a reader accepts a record only when the major versions match and the record's minor is no newer than the reader's; a minor may only add optional fields, and any removal, rename or type change needs a new major. Unknown fields are rejected rather than ignored, so a reader never silently drops data it does not understand. `python3 examples/check_reading_schema.py` checks the rule, including rejection of a `2.0` record and of a `1.1` record by a `1.0` reader. This is a synthetic example, not the schema of a deployed system.
