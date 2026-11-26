# Evidence roadmap

Dated targets set by the owner on 2026-11-26. These are targets, not commitments or a claim that a pilot is approved. A target date moves if its precondition is not met; it is never met by a simulation.

| Stage | Owner | Target | Success criterion | Status |
|---|---|---|---|---|
| Public synthetic examples | Giles Domkam | Done | Nine documented checks run in CI on every push, with branch coverage, resource measurement and a secret scan | Available; see [checks](technical/review-process.md) |
| Risk budget ratings | Giles Domkam rates; site owner approves | Before sensor install | Every scenario in the [draft risk budget](technical/cps-risks-timing.md#draft-qualitative-risk-budget-for-approval-not-approved) has an owner-proposed severity and tolerance and site-owner approval | Owner ratings proposed 2026-11-26; site-owner approval pending |
| Site preconditions | Site owner | Before sensor install | Written permission to install, machine anchoring confirmed, emergency stop and guarding confirmed | Questions sent; no answer recorded |
| Read-only sensor install | Site owner (physical install); Giles Domkam (software) | Mid-December 2026 | Clamp-on current sensor and pulley speed sensor feed an edge box; nothing connects to machine control; first readings received | Not started |
| First read-only data | Giles Domkam | 2027-01-15 | 14 days of read-only data received; gaps, stale periods and time-uncertain readings counted against the 60 s freshness rule; results published as a first-party observation with limits | Not started |
| Timing on intended hardware | Giles Domkam | After first data; date pending | Measured sensor-to-display latency and clock offset on the installed edge box, with method and uncertainty | Not started |
| Independent review | Named software/security reviewer (published only with their consent) | 2027-02-28 | Reviewer inspects claims, evidence, method and limits after install; findings published with consent | Not started |
| Private simulator evidence | Giles Domkam | Not scheduled | A repaired simulator and evidence gate that fail on failed assertions | Blocked: an ingest module is missing from all history and will not be reconstructed; see [status](technical/observation-evidence.md#simulator-status) |

A completed simulation does not satisfy physical validation. Machine safety functions, including overload protection and emergency stopping, stay with the site and are outside this monitor.
