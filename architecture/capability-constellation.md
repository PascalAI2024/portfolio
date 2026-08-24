# Capability Constellation

The projects differ in medium, but repeat four design commitments: measurable
claims, legible state, bounded authority, and explicit current status.

```mermaid
flowchart TB
    S[Selected public work] --> A[Bounded authority]
    S --> B[Measured claims]
    S --> C[Legible product state]
    S --> D[Explicit status]
    A --> Z[ZiggyZag]
    A --> V[VibeGotchi]
    B --> F[fplbench]
    B --> M[Maple CUDA]
    B --> Q[Qwen Quant Bench]
    C --> J[JarvisNano]
    C --> P[PicoArmy]
    D --> E[Evidence ledger]
    Z --> E
    V --> E
    F --> E
    M --> E
    Q --> E
    J --> E
    P --> E
```

This is a conceptual map, not a dependency graph. It does not imply that the
projects share code, customers, infrastructure, or production services. Follow
the [case-study index](../case-studies/README.md) for project-level evidence.
