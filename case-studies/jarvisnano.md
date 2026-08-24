# JarvisNano — Making an Assistant Feel Physical

**Publication status:** published
**Project status:** active hardware release candidate
**Domains:** embedded systems, interaction design, voice, physical computing
**Public proof:** [source](https://github.com/PascalAI2024/JarvisNano) ·
[architecture](https://github.com/PascalAI2024/JarvisNano/blob/main/docs/ARCHITECTURE.md)

## The brief

Explore a small desktop assistant that joins voice, touch, display, and tools
into a single physical interaction surface.

## Constraints

The target is constrained hardware. Input, audio, display ownership, and tool
use must work together without making the device confusing to operate or unsafe
to configure.

## The decisive move

The work treats the device as one interaction system rather than a collection
of peripherals: touch and speech meet a visual state, while a dedicated display
ownership model keeps the screen understandable.

## The system shape

The physical board supplies touch, audio, and display. Firmware coordinates the
voice loop, visual feedback, and optional tool bridge; a browser surface exists
for first-setup and quality assurance.

## Public proof

The public project record names the current Waveshare hardware target, the
declared voice, touch, display, and tool scope, plus the release-candidate QA
items still in progress.

## Outcome or learning

The project shows that embodied AI is an interaction-design problem as much as
an AI problem: state, interruption, and feedback need to be legible on the
device itself.

## The boundary

This study omits device configuration, access routes, credentials,
and source-level setup procedures. It is described as active release-candidate
work, not a finished consumer product.
