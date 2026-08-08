# Public-Safe System Shapes

This folder holds high-level Mermaid and SVG diagrams that explain decisions,
data ownership, and user-facing flows. They intentionally exclude live hosts,
credentials, vendor contracts, internal network layout, and operational
runbooks.

Each diagram needs a short Markdown explanation so its meaning survives outside
the rendered image.

## Gallery

| Diagram | What it makes legible | What it intentionally does not show |
| --- | --- | --- |
| [Capability constellation](capability-constellation.md) | How the selected work shares a set of design principles | Infrastructure, credentials, client data, or live production topology |
| [Human-in-the-loop boundary](human-in-the-loop.md) | The recurring relationship between people, product surfaces, and bounded systems | Prompts, model settings, execution paths, or operational controls |

The diagrams are narrative maps, not implementation blueprints. Pair them with
the [case studies](../case-studies/README.md) and [public boundaries](../PUBLIC_BOUNDARIES.md).
