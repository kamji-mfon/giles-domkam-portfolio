# Industrial monitoring — risks and timing

[← CPS case study](../projects/cps-monitoring.md)

This is an initial cross-property risk analysis, not a certified hazard analysis. Proposed controls are design requirements unless explicitly marked as demonstrated. No numerical risk budget has been allocated because severity, exposure, and system requirements have not been established.

| Scenario | Connected concerns | Expected response or proposed control | Evidence and remaining gap |
|---|---|---|
| Old reading appears current | Safety, reliability, timing | Mark stale and prevent it being presented as current | Public synthetic classifier marks data stale; actual clock accuracy and end-to-end latency not measured |
| Missing, non-finite, or future-dated input | Reliability, timing, safety | Reject the reading and surface invalid state | Public synthetic checks cover examples; no real sensor mapping tested |
| Unauthorized device access | Security, safety, reliability | Authorization, least privilege, network segmentation, and read-only access | Design requirements; actual network and access controls not demonstrated |
| False or manipulated observations | Security, safety, human decision | Verify source and data integrity; show uncertainty; use independent procedures | Not implemented in public example; operator and physical controls require review |
| Collector or host stops | Reliability, resilience, timing | Detect missing data and communicate loss of visibility | Synthetic stale behavior only; detection latency and recovery bounds unmeasured |
| Sensitive operational data exposed | Privacy, security, business | Minimize data, restrict access, and review public artifacts | Public example uses invented values; actual deployment controls not assessed |

## Timing and failure semantics

The public example compares synthetic timestamps against an illustrative maximum age. It does not establish a real-time timing class, clock synchronization accuracy, worst-case execution time, detection latency, or recovery bound. Future timestamps are classified invalid, but that is not a defense against clock spoofing.

For an actual system, identify the clock source, allowable age per decision, timestamp provenance, loss and spoofing threats, detection behavior, backup/holdover, and a safe operating procedure. Those requirements and measurements remain open. No GNSS, PTP, or NTP implementation is claimed.

The example's failure state is **invalid or stale information**, not a machine safe state. The physical safe state, its owner, and any fail-safe or fail-operational decision depend on the actual equipment and must be established separately.
