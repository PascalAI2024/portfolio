# ZiggyZag — A Terminal That Keeps the Human in Charge

**Status:** draft
**Domains:** native desktop, systems programming, local AI, developer tools
**Public proof:** [public repository](https://github.com/PascalAI2024/ZiggyZag)

## The brief

Build a readable shell and native terminal host that can add local AI help
without turning the terminal into an opaque automation surface.

## Constraints

Terminal correctness, cross-platform native behaviour, readable architecture,
and explicit approval for mutations all matter. The work also needed to remain
small enough to understand and build from source.

## The decisive move

The product separates shell, desktop host, and AI sidecar into distinct
processes. The AI sidecar can suggest actions, but the host requires human
approval before a mutation reaches the terminal.

## The system shape

The shell owns command interpretation; the desktop owns the window and terminal
surface; the sidecar handles local AI interaction. Events and approval intent
move between them without collapsing their responsibilities into one process.

## Public proof

The public repository documents native Windows and macOS paths, a Zig-only
build, terminal conformance coverage, approval-gated writes, and the project's
explicit alpha status.

## Outcome or learning

ZiggyZag makes the case that agent assistance becomes more credible when the
approval boundary is part of the product shape, not a convention users must
remember.

## The boundary

This study does not expose local command history, user files, provider settings,
or unpublished release plans. Platform claims remain limited to the documented
alpha status.
