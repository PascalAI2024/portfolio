# Case Studies

These are short engineering records, not launch copy. Every published study
states the problem, decisive move, evidence, limitation, and public boundary.

## Published and independently inspectable

| Study | What it demonstrates | Project status |
| --- | --- | --- |
| [fplbench](fplbench.md) | Leakage-safe applied ML with frozen forecasts and live self-scoring | Live 2026/27 benchmark |
| [Maple CUDA](maple-cuda.md) | CUDA performance engineering with CPU-reference gates | v1.0 generation release + post-release MMQ research |
| [Qwen Quant Bench](qwen-quant-bench.md) | Quantization research with raw results and a corrections log | Completed research record |
| [ZiggyZag](ziggyzag.md) | Native terminal engineering and approval-gated local AI | Active alpha |
| [JarvisNano](jarvisnano.md) | Embedded voice, touch, display, and tool interaction | Active hardware release candidate |
| [VibeGotchi](vibegotchi.md) | Privacy-aware GitHub integration and a live consumer product | Live application |

The [evidence ledger](../proof/README.md) links the underlying repositories,
datasets, releases, workflows, and live surfaces.

## Source-private product notes

These notes explain recurring design decisions in private systems. They are
useful context, but they are **not** counted as independently inspectable proof:

- [JarvisMCP](jarvismcp.md) — bounded capability discovery and execution.
- [Overwatch](overwatch.md) — search intelligence as a working surface.
- [IGD WP](igd-wp.md) — modular WordPress operations.
- [VibeFlow](vibeflow.md) — local-first dictation.

## House style

- Lead with the work, not a technology inventory.
- Link the artifact.
- Keep current product status beside the claim.
- Name private evidence as private.
- Use redacted, synthetic, or recreated examples when source cannot be public.

New studies follow the [case-study template](TEMPLATE.md) and do not move to
`published` until their proof links and public boundary have both been
reviewed.
