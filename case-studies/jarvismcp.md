# JarvisMCP — A Smaller Interface for Broader Work

**Status:** draft
**Domains:** agent systems, developer infrastructure, sandboxed execution
**Public proof:** [production endpoint](https://mcp.igddev.com/mcp)

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

## Public proof

The public project record describes the two-tool interface, a shared SDK with
bundled and manifest-driven services, and the separation between sandboxed code
and trusted processes.

## Outcome or learning

The design establishes a useful product principle: reduce the visible surface
without reducing the underlying capability. A smaller interface can make an
agent system easier to use, audit, and evolve.

## The boundary

This story omits authentication material, service addresses, operational
runbooks, provider configuration, and implementation details that would weaken
the security boundary.
