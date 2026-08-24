# VibeGotchi — Turning Contribution Data Into a Product

**Publication status:** published<br>
**Project status:** live public application<br>
**Domains:** product engineering, GitHub integration, privacy-aware UX, web<br>
**Evidence reviewed:** 24 August 2026<br>
**Public proof:** [source](https://github.com/PascalAI2024/VibeGotchi) ·
[live application](https://vibegotchi.pages.dev) ·
[GitHub Pages demo](https://pascalai2024.github.io/VibeGotchi/)

## The brief

Turn GitHub activity into something more memorable than another contribution
chart: a virtual pet whose level, mood, evolution, technology badges, and
achievements remain understandable to the person using it.

## The constraints

The product needs enough GitHub data to feel personal without asking for broad
repository access. Its scoring must remain legible, demoable without login, and
safe for users whose contribution graph includes private work.

## The decisive move

VibeGotchi separates three modes:

- public username lookup for visible public activity;
- read-only OAuth using `read:user`;
- optional GitHub App access limited to selected repositories with read-only
  metadata and contents permissions.

Demo profiles expose the complete product loop without requiring an account.
The score breakdown shows why a pet reached its current stage rather than
asking the user to trust an opaque engagement number.

## The evidence

The public application provides demo states, a live dashboard, achievements,
technology badges, and a downloadable share card. The repository documents the
scoring model, architecture, deployment paths, OAuth boundary, and security
posture. GitHub Actions build and deploy the static demo.

## The learning

Data products become easier to trust when the user can see the boundary and the
reasoning. Privacy copy, permission design, and score explanation are part of
the product—not compliance text added after the interaction is finished.

## The boundary

The application does not request classic OAuth `repo` scope or write access.
Private repository names and source are not part of public scoring. Current
behavior is limited to the data and permissions documented in the public
repository.
