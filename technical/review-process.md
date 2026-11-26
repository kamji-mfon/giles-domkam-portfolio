# Public evidence and review process

[← Portfolio](../README.md)

## Scope of the public examples

The examples are self-contained illustrations written for this portfolio. They accept synthetic inputs, use the Python standard library, and do not connect to equipment or external services. They are not a substitute for the private implementations described in the case studies.

## Reproduce the public checks

From the repository root:

```sh
python3 examples/check_monitoring_demo.py
python3 examples/check_observation_contract.py
python3 examples/check_historian_quality.py
python3 examples/check_telemetry_lab.py
python3 examples/check_approval_demo.py
python3 examples/equilibrium_demo.py
python3 examples/check_clock_trust.py
python3 examples/check_degraded_mode.py
python3 examples/check_reading_schema.py
python3 examples/check_resource_use.py
```

Checks use plain `assert` and exit nonzero on failure; do not run them with `python3 -O`, which removes assertions.

## Automated checks in CI

The [workflow](../.github/workflows/portfolio-checks.yml) runs on every push and pull request:

| Check | Tool | What it shows | What it does not show |
|---|---|---|---|
| Synthetic examples | Python standard library | The nine example checks pass | Behavior of any private system |
| Resource use | `check_resource_use.py`; `os.wait4` CPU time and the child's own `VmHWM` per run | Wall time, CPU time and peak RSS of each check on the CI runner, written to the job summary; fails above 5 s wall or 100 MiB RSS | Resource use of any edge device or private system |
| Branch coverage | `coverage` 7.10.7, `--branch`, fails under 85% | Which lines and branches of `examples/` the checks execute (local run on 2026-11-26 with the nine checks: 89% combined statement and branch coverage; misses were `__main__` demonstration blocks) | That the assertions are sufficient or the examples correct |
| Secret scan | `gitleaks` 8.30.1 (MIT), checksum-verified, full git history | No match for gitleaks' default rules (local run on 2026-11-26: 4 commits, no leaks found) | Absence of every secret, client name, or private detail; pattern scanners miss context-dependent disclosures, so a human review of each change is still required |

## Private evidence boundary

The [assurance record](assurance.md) distinguishes these public checks from first-party observations of private tests. A private test result is a reported observation and cannot be independently reproduced from this repository.

## Changes and disclosure

Before adding material, review ownership and rights, use synthetic or approved data, inspect source and generated files, and run a secret scan. Report security concerns as described in [SECURITY.md](../SECURITY.md); do not post credentials or confidential data in a public issue.

All rights are reserved; see [LICENSE](../LICENSE). You may view the repository and run the examples locally to evaluate the work. No open-source or commercial reuse license is granted; contact the owner for permissions.
