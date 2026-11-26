# Jarvis — Local-First AI Operations

[← Portfolio](../README.md)

## The problem

An operations assistant needs access to useful context while giving its operator control over consequential actions.

## My work

I built Jarvis as a local-first assistant with a voice command center and services for task routing, knowledge search, procurement, and engineering status. Its tool registry distinguishes reading, preparation, and actions that require confirmation.

```text
Voice or text request
        ↓
Route to a registered tool
        ↓
Read information or prepare a result
        ↓
Request confirmation for a gated action
```

## Skills demonstrated

Python · AI tool integration · voice interfaces · service design · local data management · approval workflows

## Boundaries

Jarvis is designed for a single operator. This page is a high-level description, not a claim that every possible action or integration has been independently audited. Private memory, communications, credentials, and operating data are not part of this portfolio.

For the observed local confirmation checks and their limits, see the [assurance record](../technical/assurance.md).

## Runnable synthetic illustration

`python3 examples/approval_demo.py` and `python3 examples/check_approval_demo.py` demonstrate a single-use decision using only an in-memory action. This is a new illustrative example, not Jarvis's implementation or evidence that every action path is gated.

**Project status:** private working system; selected public description.
