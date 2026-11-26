# CPS case study — industrial monitoring

[← Portfolio](../README.md) · [Architecture](../technical/cps-architecture.md) · [Risk and timing](../technical/cps-risks-timing.md) · [Assurance](../technical/assurance.md)

## Problem and scope

Industrial machine data can support human decisions, but a reading may be missing, stale, malformed, or misunderstood. My work includes industrial telemetry processing and machine-protocol simulation. This case study presents a **sanitized, read-only monitoring scenario** inspired by that work.

The physical machine is outside the public example. The public code does not connect to equipment, authenticate users, operate a controller, or issue commands. A human would decide what to do with an observation; machinery safety and emergency stopping remain independent of this monitoring example.

```text
Physical process → sensor / controller → observation boundary
                                         ↓
                         validate and classify reading
                                         ↓
                         present status → human decision

Public example begins at a synthetic reading. It has no actuation path.
```

## Public evidence

Run the independent synthetic example with Python's standard library:

```sh
python3 examples/monitoring_demo.py
python3 examples/check_monitoring_demo.py
```

The example distinguishes available, stale, and invalid readings. The check exercises the threshold boundary, future timestamps, non-finite values, missing data, and invalid configuration. The time values and threshold are synthetic, not operational requirements or measured latency. The example was written for this portfolio and is not an extraction of a private implementation.

[Observation evidence](../technical/observation-evidence.md) adds independently written examples of a scoped authorization contract and synthetic historian data-quality handling.

## What the private work adds

The private projects include a loopback simulator for selected industrial protocol interactions and file-based telemetry processing. The simulator self-check uses non-fatal assertions and its success message alone is not reliable proof. [The assurance record](../technical/assurance.md) explains the observations and limits. No plant data, machine addresses, private implementation, or customer configuration is included here.

## Status and limitations

This is monitoring and simulation, not autonomous control or a safety function. Real-machine connectivity, sensor accuracy, timing bounds, environmental behavior, and deployment security are not established by this public example. No production deployment or external certification is claimed.
