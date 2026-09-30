# ADR 0001 — Separate method from implementation

- Date: 2026-09-30
- Status: accepted for blueprint
- Owner: blueprint maintainer

## Context

Customers have different authoring habits, identity requirements and operating budgets. A product-specific checklist cannot establish which product is suitable.

## Alternatives

A single-product installation guide is easy to follow but omits selection and exit criteria. A purely abstract framework cannot demonstrate implementation detail.

## Decision

Keep requirements, lifecycle, governance and acceptance product independent. Place a concrete Docmost stack and a BookStack migration example alongside them, explicitly identifying assumptions.

## Consequences and review

Some operational details must be rewritten for each selected product. The reference remains demonstrable without asserting universal suitability. Revisit when another implementation is added; both must meet the same acceptance contract.
