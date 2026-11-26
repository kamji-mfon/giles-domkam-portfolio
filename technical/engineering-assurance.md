# Engineering assurance — selected claims

[← Njoya Engineering](../projects/njoya-engineering.md) · [Evidence and assurance record](assurance.md)

The table records selected first-party test observations from a private working tree on 2026-11-26. They are not reproducible from this public repository or an independent audit. They do not establish that every engineering workflow is covered. No client inputs, licensed standards prose, calculation engine, or real sign-off is published.

| Claim | Selected check | Observed result | Limit |
|---|---|---|---|
| A selected output path rejects missing licensed-engineer sign-off | Structural workbench sign-off gate test | Passed in the focused local run | Synthetic test; not proof of every output path, the identity of a real signer, or a professional seal |
| A selected output path records review and provenance data | Structural workbench audit-row test | Passed in the focused local run | Test artifact in temporary storage; does not independently verify the entire audit chain or a real project |
| Selected unpinned or unlisted references are blocked | Structural citation rejection test | Passed in the focused local run | Tests selected cases; does not prove every standards reference is correct or licensed |
| A selected validation harness matches its expectations | Structural and related calculation validation harness | Previously reported 24 passing cases | Mixed hand/equation and cited-reference cases; not universal validation or experimental proof |

The focused run reported **3 passed**. A separate synthetic equilibrium illustration is runnable with `python3 examples/equilibrium_demo.py`; it is not the private engine or a code-compliance calculation. Licensed professional review remains necessary where applicable.
