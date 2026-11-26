# Industrial monitoring — architecture and boundaries

[← CPS case study](../projects/cps-monitoring.md)

This is a design analysis of a sanitized monitoring scenario. The only publicly executable component is the synthetic classifier; the other components describe the intended context, not a verified deployed system.

## Boundaries and composition

| Crossing | Information | Required property to establish | Current public evidence |
|---|---|---|---|
| Physical process → sensor/controller | Machine condition | Sensor suitability, calibration, and physical protection | Not demonstrated |
| Controller → collector | Readings via an authorized observation interface | Read-only access, identity, network isolation, and meaningful data mapping | Private loopback simulator was exercised; no real-device evidence is public |
| Collector → classifier | Timestamped values | Valid input, known units, freshness, and rejection of malformed records | Public synthetic classifier checks a subset: timestamp, numeric value, and freshness |
| Classifier → person | Status and context | Clear limits, data age, and no misleading healthy state | Synthetic statuses are shown by the public example; an operator interface is not included |
| Person → machinery | Independent human/plant procedure | Authorized action and separate machinery safety controls | Outside scope; no actuation path in the example |

## Aspects and facets

| Aspect | Conceptualization: question | Realization / assurance: public evidence and gap |
|---|---|---|
| Functional | What decision does monitoring support? | Synthetic freshness classification; no equipment control |
| Business | Who owns the data and deployment decision? | Ownership, costs, and customer context are not published |
| Human | Can an operator recognize uncertainty? | `stale` and `invalid` are distinct; no human-factors study |
| Trustworthiness | What happens when data or access fails? | [Risk analysis](cps-risks-timing.md) distinguishes proposed controls from evidence |
| Timing | How old can a reading be? | Example threshold is synthetic; operational limit and latency are unmeasured |
| Data | What is a reading and what does it mean? | Timestamp and numeric value in the example; units and real sensor mapping remain to be established |
| Boundaries | Where do physical, device, and operator responsibilities meet? | Crossing table above; no live plant access |
| Composition | How do components fail together? | Design analysis only; integration with real equipment not demonstrated |
| Lifecycle | How is the system changed, rolled back, or retired? | Requirements identified below; implementation not demonstrated |

These facets are modes of analysis, not a sequential delivery claim. Assurance remains open until relevant evidence is supplied for the actual deployment.

## Lifecycle and trade-off

For a real deployment, changes would need authorization, versioned configuration, rollback, and a documented retirement path. Those controls have not been demonstrated by the public example.

**Design choice:** observe and inform a person rather than write control commands from this public monitor. This reduces the example's control authority, but cannot eliminate physical risk: a misleading observation could still influence a human decision. A real deployment would need independent safety controls and a review of that human decision path.
