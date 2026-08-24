# Qwen Quant Bench — Useful Results Include Corrections

**Publication status:** published<br>
**Project status:** completed public research record<br>
**Domains:** LLM inference, quantization, speculative decoding, benchmark design<br>
**Evidence reviewed:** 24 August 2026<br>
**Public proof:** [source, recipes, raw results, and corrections](https://github.com/PascalAI2024/qwen38-27b-quant-bench)

## The brief

Determine what actually makes a dense 27B Qwen3.8 model useful on a 16 GB GPU:
more aggressive quantization, selective tensor protection, or a different
speculative-decoding strategy.

## The constraints

At very low bit widths, perplexity can hide meaningful distribution drift.
Published importance matrices do not cover the model's MTP head. Benchmark
results also change when a draft model pushes target layers out of limited
VRAM, making a large-card test answer the wrong question.

## The decisive move

The study split quality and serving into different controlled questions:

- quantify quality against the same Q8_0 reference with KL divergence and
  top-one agreement;
- preserve the uncovered MTP block explicitly rather than accepting a
  plausibly sized but invalid GGUF;
- test speculative methods on the constrained 16 GB machine where the tradeoff
  matters;
- restart servers and use distinct prompts after detecting shared n-gram state
  contaminating an earlier result.

## The evidence

The repository publishes quantization recipes, hardware and runtime versions,
raw CSV and JSON results, harness scripts, limitations, and a corrections log.
It records the invalid-file failure mode, the measurement contaminated by
shared n-gram state, and abandoned recipes that failed the size objective.

The study explicitly limits its interpretation: one text corpus for quality,
Q8_0 rather than BF16 as the reference, small per-cell serving samples, and
single hardware samples for several comparisons.

## The learning

A negative result can be more reusable than a winning bar chart. Here, the
important engineering output is the set of failure checks—anchored tensor
matching, header validation, unfiltered stderr, clean server state, and
hardware-matched comparisons—that make the next benchmark harder to fool.

## The boundary

The research does not claim general instruction, coding, or vision quality from
one text corpus. It does not publish model weights or provider credentials, and
it does not merge measurements from materially different serving paths.
