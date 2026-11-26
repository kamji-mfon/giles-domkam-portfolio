# Njoya Engineering — Computational Design

[← Portfolio](../README.md)

## The problem

An engineering result needs context: the inputs, method, units, code edition, and review state all matter. A calculation workflow should make that context visible to the person responsible for the engineering decision.

## My work

I built structural calculation software in Python, including analysis and code-checking workflows. The platform records calculation context and is designed around code references, checks, and human review. It also includes work across other engineering disciplines, with different levels of implementation and validation.

```text
Inputs and method
       ↓
Calculation and code reference
       ↓
Units, provenance, and selected checks
       ↓
Reviewable result and audit record
       ↓
Human engineering review
```

## Skills demonstrated

Structural and computational engineering · Python · frame analysis · engineering code references · verification · auditability

## Validation and boundaries

The work distinguishes checks against hand calculations from comparisons with independent published examples. Validation is specific to the calculation and use case; a tested example does not validate every module. Structural work is implemented, while other disciplines and integrations have differing levels of completeness.

The platform assists engineering review. A licensed professional must independently verify and seal work when required. No licensed standards text, client information, or calculation engine is included in this public case study.

## Runnable synthetic illustration

`python3 examples/equilibrium_demo.py` illustrates equilibrium for a fictional symmetric point load. This newly written example is not an extracted calculation engine, code compliance check, design, or independently validated model.

For the observed local validation run and its limits, see the [assurance record](../technical/assurance.md).

The [engineering assurance case](../technical/engineering-assurance.md) describes selected local sign-off, audit, and citation checks and their limits.

**Project status:** private working platform; selected public description.
