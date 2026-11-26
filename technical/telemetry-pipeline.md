# Telemetry pipeline — architecture and test evidence

[← CPS case study](../projects/cps-monitoring.md) · [Assurance](assurance.md)

## System under study

The private engineering work includes a telemetry branch for moving machine observations from an edge process to an ingest service and a human-facing status view. Its software uses a local outbox, per-device access tokens, input validation, duplicate handling, and deterministic status rules. This description is sanitized; device configuration, source code, site data, and credentials are not published.

```text
Physical equipment → reading interface → edge outbox
                                         ↓
                    authenticated upload → validated storage
                                         ↓
                         deterministic status → human review
```

The branch is software under test. This record does not establish a physical deployment, a production security assessment, a safety function, or a closed control loop. Status information must not replace independent equipment safety controls.

## Evidence observed locally

On 2026-11-26, an isolated copy of a private telemetry branch was tested with synthetic inputs. The local test run reported **11 passed, 1 skipped**. The skipped test required an unavailable Modbus library, so that run does not establish a Modbus round trip. The run included an HTTP test using a local loopback server; it did not contact plant equipment. It reported a test-client deprecation warning.

The selected tests exercise outage/replay behavior, duplicate handling, token roles, malformed and future-dated readings, stale or incomplete status, and an in-process alert timing assertion. They are first-party observations; the branch and its tests are not published here, so a visitor cannot reproduce those private results from this repository. They do not establish lossless delivery under every failure, real-machine accuracy, guaranteed latency, or operational safety.

The branch contains an in-process test with a **1 second test threshold** from a synthetic sample timestamp to an observed alert. That is a test assertion, not a measured field latency, a worst-case execution time, or a timing guarantee. Clock accuracy, communication delays, resource use, network outages, and equipment behavior require separate measurement in the intended environment.

## Publicly reproducible illustration

`python3 examples/check_telemetry_lab.py` runs a newly written offline lab. It shows an invented outage and replay, duplicate detection, conflicting values, and rejected rows retained for review. It uses an in-memory database and an in-memory queue. Device identity is supplied as a string; there is no authentication, encryption, network, persistent recovery, sensor, or actuator. It is not an extraction or verification of the private branch.

## Next evidence needed

Before operational claims, establish source identity and authorization, real sensor mappings and units, clock provenance, loss and replay behavior, field timing requirements, resource headroom, and independent review. Test against authorized equipment and calibrated references where appropriate; report failed and inconclusive cases alongside passes.
