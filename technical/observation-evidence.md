# Industrial observation — reproducible examples

[← CPS case study](../projects/cps-monitoring.md) · [Assurance record](assurance.md)

These examples are independently written for the portfolio using invented data and documentation-only IP address ranges. They do not connect to equipment or contain the private system's implementation. They are examples of design choices and failure handling, not a deployed security control.

## Authorization contract

The example requires an explicit scope and validity interval. It refuses absent, malformed, expired, not-yet-valid, and out-of-scope requests. A passing check does not establish identity, verify a real authorization record, or prove that any private machine-access path is gated.

```sh
python3 examples/observation_contract.py
python3 examples/check_observation_contract.py
```

## Historian quality

The example consumes invented CSV rows with explicit fields and labels readings as accepted, invalid, stale, duplicate, or conflicting. Conflicting readings sharing an asset and timestamp are not accepted as good data. A missing schema is an error, not a guessed mapping.

```sh
python3 examples/historian_quality.py
python3 examples/check_historian_quality.py
```

The freshness window and clock values are invented for the illustration. These checks do not validate a real plant export, establish clock trust, prove a sensor's accuracy, or provide a machinery safety function. A real deployment needs a verified schema, units, data provenance, access controls, operational thresholds, and appropriate human review.

## Simulator status

The private work includes a loopback protocol simulator. Its self-check uses non-fatal assertions, and the larger fault-scenario soak and evidence gate are not currently reproducible: the reconstructed evidence pipeline has missing dependencies and incompatible interfaces. No public fault-scenario pass or physical equipment result is claimed. A simulator case study should be added only after the actual harness and its evidence gate are repaired and rerun.
