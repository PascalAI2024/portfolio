# Evidence Ledger

This ledger records what supports the portfolio's headline claims. It is not a
folder of decorative screenshots.

| Claim | Public artifact | Review state |
| --- | --- | --- |
| fplbench freezes forecasts and self-scores the published model | [source and results](https://github.com/PascalAI2024/fplbench), [workflow](https://github.com/PascalAI2024/fplbench/actions/workflows/fplbench.yml), [dataset](https://huggingface.co/datasets/x0me/fplbench), [board](https://huggingface.co/spaces/x0me/fplbench-board) | Verified 24 Aug 2026; first live gameweek still open at review time |
| Maple CUDA improved measured ternary inference while matching the CPU reference | [v1.0.0 generation release](https://github.com/PascalAI2024/maple-preview-windows-cuda/releases/tag/v1.0.0), [post-release repository evidence](https://github.com/PascalAI2024/maple-preview-windows-cuda), [dataset](https://huggingface.co/datasets/x0me/maple-preview-cuda-benchmarks) | Verified 24 Aug 2026; later MMQ and cross-architecture work postdates v1.0; hardware/revision-specific |
| Qwen benchmark publishes methods, raw results, limits, and corrections | [research repository](https://github.com/PascalAI2024/qwen38-27b-quant-bench) | Verified 24 Aug 2026; limited corpora and hardware samples disclosed |
| ZiggyZag separates shell, native host, and approval-gated agent | [source](https://github.com/PascalAI2024/ZiggyZag), [current Actions](https://github.com/PascalAI2024/ZiggyZag/actions), [releases](https://github.com/PascalAI2024/ZiggyZag/releases) | Architecture and artifacts verified 24 Aug 2026; active alpha, current CI must be read directly |
| JarvisNano targets real ESP32-S3 hardware with voice, touch, display, and diagnostics | [source](https://github.com/PascalAI2024/JarvisNano), [architecture](https://github.com/PascalAI2024/JarvisNano/blob/main/docs/ARCHITECTURE.md) | Verified 24 Aug 2026; active release-candidate work |
| VibeGotchi is a live product with bounded GitHub permissions | [live app](https://vibegotchi.pages.dev), [source](https://github.com/PascalAI2024/VibeGotchi), [security documentation](https://github.com/PascalAI2024/VibeGotchi/blob/main/docs/security.md) | Verified 24 Aug 2026 |

## Proof standard

An artifact belongs here when it is public, attributable, current enough for
the claim, and understandable without private context. Accepted forms include:

- source with a runnable or inspectable path;
- a live public demo;
- immutable releases and artifact hashes;
- raw benchmark output plus the harness that produced it;
- CI or test evidence tied to the relevant revision;
- a public-safe diagram paired with an explicit limitation.

Dynamic counters—downloads, stars, rankings, and live scores—are dated when
quoted and are never treated as permanent outcomes.

## What does not count

- a login screen standing in for product behavior;
- an authenticated endpoint standing in for inspectable source;
- a private repository link;
- a screenshot with no date, context, or artifact behind it;
- memory-derived status presented as current fact.

The [public boundaries](../PUBLIC_BOUNDARIES.md) govern what remains omitted.
