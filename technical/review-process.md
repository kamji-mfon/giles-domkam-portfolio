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
python3 examples/check_approval_demo.py
python3 examples/equilibrium_demo.py
```

The [assurance record](assurance.md) distinguishes these public checks from first-party observations of private tests. A private test result is a reported observation and cannot be independently reproduced from this repository.

## Changes and disclosure

Before adding material, review ownership and rights, use synthetic or approved data, inspect source and generated files, and run a secret scan. Review security concerns through [the repository's GitHub owner](https://github.com/kamji-mfon); do not post credentials or confidential data in a public issue.

No license is included. The absence of a license does not grant an open-source or commercial reuse license; contact the owner for permissions.
