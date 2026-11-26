# Industrial monitoring — risks and timing

[← CPS case study](../projects/cps-monitoring.md)

This is an initial cross-property risk analysis, not a certified hazard analysis. Proposed controls are design requirements unless explicitly marked as demonstrated. No numerical risk budget has been allocated because severity, exposure, and system requirements have not been established.

| Scenario | Connected concerns | Expected response or proposed control | Control owner (role) | Evidence and remaining gap | Residual risk |
|---|---|---|---|---|---|
| Old reading appears current | Safety, reliability, timing | Mark stale and prevent it being presented as current | Software maintainer | Public synthetic classifier marks data stale; actual clock accuracy and end-to-end latency not measured | NOT ESTABLISHED |
| Missing, non-finite, or future-dated input | Reliability, timing, safety | Reject the reading and surface invalid state | Software maintainer | Public synthetic checks cover examples; no real sensor mapping tested | NOT ESTABLISHED |
| Unauthorized device access | Security, safety, reliability | Authorization, least privilege, network segmentation, and read-only access | Site owner and network administrator | Design requirements; actual network and access controls not demonstrated | NOT ESTABLISHED |
| False or manipulated observations | Security, safety, human decision | Verify source and data integrity; show uncertainty; use independent procedures | Site owner, operator | Not implemented in public example; operator and physical controls require review | NOT ESTABLISHED |
| Collector or host stops | Reliability, resilience, timing | Detect missing data and communicate loss of visibility | Software maintainer, operator | Synthetic stale behavior only; detection latency and recovery bounds unmeasured | NOT ESTABLISHED |
| Sensitive operational data exposed | Privacy, security, business | Minimize data, restrict access, and review public artifacts | Data owner (site owner) | Public example uses invented values; actual deployment controls not assessed | NOT ESTABLISHED |

Roles are the parties who would own each control in a real deployment; no named person or organization has accepted them. Residual risk cannot be rated until severity, exposure, and tolerances are set for an actual system.

## Proposed consequence-led allocation

For a future field deployment, prioritize resources first around physical harm from incorrect human decisions, then unauthorized or manipulated observations, then recoverability and data confidentiality, subject to the actual hazard analysis. This is an illustrative ordering, not an approved allocation or a quantified risk budget. The operator, site owner, and responsible engineer must determine consequences, tolerances, control owners, and residual-risk acceptance for the particular system.

## Timing and failure semantics

### Proposed timing class

**Class: non-real-time, staleness-bounded monitoring (proposed design classification, not a measured result).** Justification: the monitor has no actuation path and no control deadline; its output informs a person who acts on human timescales through separate plant procedures. Missing a delivery deadline therefore degrades information quality (a reading becomes stale) rather than causing a control failure. The correctness requirement is that an old or untrustworthy reading is never presented as current, not that a reading arrives within a hard deadline. This classification would change if the system ever drove an interlock, alarm with a required response time, or actuator; that would require a new hazard analysis and a hard or firm real-time design.

Not applicable to this classification, and not tested: interrupt service routines, DMA, hardware watchdogs on a controller, deterministic scheduling, and worst-case execution time analysis. The public examples are single-threaded Python with no concurrency.

### Time-source threat model

| Threat | Effect on the monitor | Proposed detection | Proposed response | Status |
|---|---|---|---|---|
| Edge clock not synchronized after power loss (no RTC) | Readings carry wrong timestamps; fresh data may look stale or old data current | Compare edge time with ingest receipt time; flag sync state | Mark readings time-uncertain; do not show as current | Clock source of a real edge device NOT ESTABLISHED |
| Clock steps backward | Duplicate or out-of-order timestamps | Reject non-increasing timestamps per signal | Hold readings for review | Synthetic future-timestamp rejection only; backward-step handling not public |
| Clock runs fast (future-dated readings) | Reading appears fresher than it is | Reject timestamps later than receiver time | Classify invalid | Demonstrated on synthetic input by `check_monitoring_demo.py` and `check_telemetry_lab.py` |
| Malicious or misconfigured time server | Coordinated wrong time across devices | Cross-check independent sources; alert on large offsets | Stop relying on time-sensitive outputs; operator alert | Design proposal; no NTP/PTP/GNSS implementation claimed |
| Ingest host clock wrong | Freshness decisions wrong for every device | Monitor host sync state | Alert maintainer; mark status uncertain | Not demonstrated |

Allowable reading age per decision, clock accuracy, and holdover duration are open requirements for an actual site and are not set here.

### Synthetic example behavior

The public example compares synthetic timestamps against an illustrative maximum age. It does not establish a real-time timing class, clock synchronization accuracy, worst-case execution time, detection latency, or recovery bound. Future timestamps are classified invalid, but that is not a defense against clock spoofing.

For an actual system, identify the clock source, allowable age per decision, timestamp provenance, loss and spoofing threats, detection behavior, backup/holdover, and a safe operating procedure. Those requirements and measurements remain open. No GNSS, PTP, or NTP implementation is claimed.

Possible threats include clock loss, backward steps, misconfiguration, and a malicious or incorrect time source. A proposed response is to detect implausible time or lost synchronization, mark data uncertain, alert the operator, and use an approved holdover or stop relying on time-sensitive outputs. This is a design proposal, not an implemented detection-to-failover guarantee.

The example's failure state is **invalid or stale information**, not a machine safe state. The physical safe state, its owner, and any fail-safe or fail-operational decision depend on the actual equipment and must be established separately.
