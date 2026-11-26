# Field evidence plan — proposed, not a completed pilot

[← CPS case study](../projects/cps-monitoring.md)

The private workspace contains draft pilot and safety-planning material. The following is a generic proposed plan, not a claim that a partner approved a pilot or that any equipment test occurred.

## Prerequisites

- Obtain documented owner authorization and identify the equipment, observation scope, operator, and stop authority.
- Agree the data source, units, sampling and timing requirements, retention, and permitted use before collection.
- Identify physical hazards and independent machine safety controls. A monitoring system must not be used as an emergency stop.
- Record sensor, firmware, configuration, clock source, and reference instrument details. If no calibrated reference exists, label accuracy exploratory.

## Proposed evidence

| Question | Test to agree in advance | Evidence to retain |
|---|---|---|
| Are observations attributable and authorized? | Confirm the approved source and reject unauthorized access attempts | Authorization record, test configuration, result |
| Can a reviewer reconcile data? | Compare expected observations, received records, duplicates, gaps, and rejected inputs | Counts, input version, handling of each discrepancy |
| What happens when connectivity fails? | Exercise an agreed outage and recovery; record losses and replay | Test timeline, queue/recovery results, limitations |
| Can time be trusted for this decision? | Record time source and synchronization state; test drift, loss, and implausible timestamps | Clock method, measurements, uncertainty, unresolved risks |
| Does the reading match reality? | Compare with an agreed calibrated reference, if available | Reference identity, method, error and uncertainty |
| Can the result be reviewed? | Reproduce the result from pinned inputs and code; record reviewer decision | Versioned manifest, check results, approval status |

Acceptance limits must be agreed for the actual intended use. No threshold, outcome, hardware certification, or site approval is claimed here.
