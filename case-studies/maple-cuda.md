# Maple CUDA — Performance Work That Still Has to Be Correct

**Publication status:** published<br>
**Project status:** public research artifact; v1.0 generation release plus post-release MMQ evidence<br>
**Domains:** CUDA, inference systems, benchmarking, reproducibility<br>
**Evidence reviewed:** 24 August 2026<br>
**Public proof:** [source](https://github.com/PascalAI2024/maple-preview-windows-cuda) ·
[v1.0.0 release](https://github.com/PascalAI2024/maple-preview-windows-cuda/releases/tag/v1.0.0) ·
[benchmark dataset](https://huggingface.co/datasets/x0me/maple-preview-cuda-benchmarks)

## The brief

Make the 20B-A1B Maple-Preview ternary model usable on Windows and consumer
CUDA hardware, then determine whether the memory advantage survives a fair
throughput and correctness comparison.

## The constraints

Mainline llama.cpp did not support the model architecture or its TQ2_0 tensor
type. The available fork could load the model, but the ternary CUDA path was
dramatically slower than a mature Q4_K reference. A fast result without a CPU
correctness reference would merely be a more energetic bug.

## The decisive move

The work separated batch-one generation from prompt processing and optimized
the actual bottleneck in each path:

- expose the dormant MMVQ path for routed experts;
- vectorize the ternary dot product;
- add TQ2_0 to the backend correctness matrix;
- specialize dequantization;
- wire and validate the MMQ prompt-processing path.

Every optimization was measured in controlled configurations, and a regressing
experiment remains documented as reverted rather than disappearing from the
story.

## The evidence

- Original controlled series: **52 → 377 tokens/s** generation, a 7.2× change,
  exceeding the recorded Q4_K reference while using 7.3 GB instead of 12.3 GB.
- Fresh warm A/B/B/A reproduction: **1,457 → 10,674 tokens/s** for prompt
  processing, a 7.33× change.
- Correctness: **31/31 `MUL_MAT` plus 72/72 `MUL_MAT_ID`** cases against the
  CPU reference.
- The fused path was checked on Turing, Ampere, Ada, and Blackwell hardware.
- Raw logs, hashes, harnesses, and cross-architecture artifacts are published;
  model weights are not.

The repository keeps the original matched comparison and the later
reproduction separate because they were not run in the same environment.

## The learning

Performance engineering is strongest when the evidence can explain both why a
path was slow and why the faster path is still the same computation. The
correctness gate made the throughput claim worth publishing.

## The boundary

The results are hardware- and revision-specific. The public record does not
claim universal speedups across every GPU or runtime. No model weights,
credentials, rented-machine state, or private provider data are included.
