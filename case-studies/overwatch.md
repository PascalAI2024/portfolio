# Overwatch — Search Intelligence as One Working Surface

I built Overwatch to connect search and analytics data with the decisions
needed to maintain a website. It brings site context, proposed work and
review into one self-hosted application.

The images show actual released interface components running locally with
fictional demo data and execution disabled, captured September 5, 2026.
The production source is private.

## See the exact change before approving it

The queue keeps the proposal list beside its evidence and proposed changes.
Selecting an item reveals the affected content and a before-and-after view,
so the operator can review a specific edit rather than accept a vague summary.

![Overwatch queue detail with the exact proposed SEO title and description changes](../assets/overwatch/overwatch-queue-detail.jpg)

The same queue adapts to a narrow screen, keeping the proposed changes and
decision controls together.

<img src="../assets/overwatch/overwatch-queue-mobile-420.jpg" alt="Actual Overwatch queue on mobile with fictional demo metadata and disabled execution" width="420" />

## Review work across sites

Mission Control brings pending decisions and site context into a shared
workspace. The example includes a proposed metadata revision, a keyword
tracking suggestion and a question requiring a decision.

![Actual Overwatch Mission Control route with fictional proposals and execution disabled](../assets/overwatch/overwatch-mission-desktop.jpg)

## Engineering approach

The application combines search, analytics and business-profile signals around
a site workspace. Background work gathers the data; the review interface keeps
the affected site, evidence and proposed edit together. That separation makes
an AI-assisted recommendation concrete enough for an operator to assess.

[Capture provenance](../assets/overwatch/README.md) explains the local fixture
setup and the distinction between this UI demonstration and backend execution.
