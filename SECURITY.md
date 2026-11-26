# Security and disclosure

This repository contains synthetic examples and documentation. It does not connect to plant equipment and is not intended as a production security or safety system.

## Threat model for the illustrated monitoring workflow

The design analysis considers unauthorized observation, false or replayed readings, compromised devices or hosts, clock manipulation, loss of connectivity, disclosure of operational data, and misleading status presented to a person. Its boundaries and open controls are documented in [CPS architecture](technical/cps-architecture.md) and [risks and timing](technical/cps-risks-timing.md).

The public examples do not implement production authentication, network encryption, physical protection, clock security, or machinery controls. They must not be used to operate equipment.

## Reporting

Contact [the repository owner](https://github.com/kamji-mfon) through a private channel listed on the profile before disclosing sensitive information. Do not include credentials, personal data, or confidential plant details in a public issue.
