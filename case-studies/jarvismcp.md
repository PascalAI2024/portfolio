# JarvisMCP — A Smaller Interface for Broader Work

**Publication status:** public-safe narrative
**Project status:** source-private production infrastructure
**Domains:** agent systems, developer infrastructure, sandboxed execution
**Evidence posture:** authenticated service; not counted as inspectable public proof

## The brief

Give coding agents access to a broad company capability surface without
presenting an unmanageable wall of individual tools.

## Constraints

The interface had to stay small, preserve discoverability, and keep arbitrary
agent-authored code away from upstream credentials.

## The decisive move

The gateway presents a compact discovery-and-execution interface instead of a
tool per integration. Capability lookup happens before execution, while the
execution environment is separated from credential-holding services.

## The system shape

Client requests enter a shared gateway, which resolves the relevant capability
and runs bounded work through a sandboxed execution layer. Trusted services
remain outside that execution boundary.

## Evidence posture

The production service is authenticated and its source is private. This note
describes a reviewed public boundary, not an invitation to infer implementation
details or production status from an endpoint.

## Outcome or learning

The design establishes a useful product principle: reduce the visible surface
without reducing the underlying capability. A smaller interface can make an
agent system easier to use, audit, and evolve.

## The boundary

This story omits authentication material, service addresses, operational
runbooks, provider configuration, and implementation details that would weaken
the security boundary.
