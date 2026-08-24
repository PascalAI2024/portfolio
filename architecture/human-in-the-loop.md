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

The exact implementation varies by project. In
[ZiggyZag](../case-studies/ziggyzag.md), the native host owns approval before an
agent mutation reaches the terminal. In
[fplbench](../case-studies/fplbench.md), the human boundary is the frozen
pre-deadline artifact and the refusal to rewrite it after the outcome. In
[VibeGotchi](../case-studies/vibegotchi.md), it is the visible read-only GitHub
permission model. The diagram intentionally omits private execution details.
