# Human-in-the-Loop Boundary

Across the selected work, automation is framed as assistance inside an
understandable product surface—not as an invisible substitute for the person
responsible for the outcome.

```mermaid
flowchart LR
    H[Person with context] -->|sets intent or approves action| P[Product surface]
    P -->|bounded request| S[Capability or service]
    S -->|result or proposal| P
    P -->|legible feedback| H
```

The exact implementation varies by project. In [JarvisMCP](../case-studies/jarvismcp.md)
and [ZiggyZag](../case-studies/ziggyzag.md), the focus is governed agent or
terminal assistance. In [Overwatch](../case-studies/overwatch.md), it is an
approval-aware decision surface. The diagram intentionally omits the internal
mechanics that make each boundary secure.
