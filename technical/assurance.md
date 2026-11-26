# Evidence and assurance record

[← Portfolio](../README.md) · [CPS case study](../projects/cps-monitoring.md)

Evidence types matter: a self-test is not an independent audit, simulation is not field validation, and a test of one path does not establish the behavior of an entire system.

| Claim | Evidence available | Limit |
|---|---|---|
| The public example distinguishes fresh, stale, and invalid synthetic readings | Run `python3 examples/check_monitoring_demo.py` | Illustrative implementation only; no hardware, clock security, or control path |
| A synthetic observation contract refuses missing, invalid, expired, and out-of-scope requests | Run `python3 examples/check_observation_contract.py` | Separate illustration; not evidence that private equipment access is gated |
| Synthetic historian records are separated by data quality | Run `python3 examples/check_historian_quality.py` | Separate illustration; not proof of real plant data or calibrated timing |
| A synthetic approval example can deny an action and reject a replay | Run `python3 examples/check_approval_demo.py` | Separate illustration, not Jarvis's implementation or a security certification |
| A synthetic statics example closes vertical equilibrium for a symmetric load | Run `python3 examples/equilibrium_demo.py` | Illustrative calculation only, not a design, code check, or validation of the private engine |
| An industrial protocol simulator was exercised locally | Local self-check printed `sim selftest: all assertions passed` on 2026-11-26 | Its assertions are non-fatal, so the success line alone is not a reliable pass; private working tree; simulator, not real equipment |
| A file-based availability calculation rejects non-increasing timestamps and invalid thresholds | Local availability self-check reported all checks passed on 2026-11-26 | Private working tree; synthetic values; no production freshness or availability guarantee |
| A selected approval workflow can defer, deny, and confirm an action | Local Jarvis confirmation test file reported `11 passed` on 2026-11-26 | Private working tree with local changes; uses test actions and local test server; not proof for every integration |
| The structural validation harness matched its selected expectations | Local harness reported `24 pass, 0 fail, 0 skipped` on 2026-11-26 | Mixed hand/equation and cited reference cases; private working tree; does not validate all modules or establish a professional seal |

The private repositories and inputs are not published. These observed results are first-party reports, not publicly reproducible evidence. The public classifier and checks are reproducible from this repository. See the [engineering assurance case](engineering-assurance.md) for selected sign-off, provenance, and citation checks. No values above should be read as a benchmark, system-wide coverage percentage, or independent certification.

## Open assurance work

- Confirm authorization, source provenance, and the relevant physical system before testing actual equipment.
- Establish device identity, data mapping, units, safety ownership, deployment boundaries, and operator requirements.
- Measure timing and resource behavior on the actual hardware and network before making operational claims.
- Record versioned evidence, review changes, and validate the specific intended use before relying on results.
