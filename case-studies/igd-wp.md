# IGD WP — A Modular Control Plane for WordPress

**Status:** draft  
**Domains:** WordPress, product engineering, agency operations  
**Public proof:** [public repository](https://github.com/PascalAI2024/igd-wp)

## The brief

Give site operators one coherent WordPress administration experience without
forcing every site to carry every capability or depend on a SaaS control layer.

## Constraints

The product needed to remain approachable for site operators, modular for
different deployments, and compatible with the ordinary WordPress environment.

## The decisive move

The plugin treats capabilities as independently enabled modules behind one
consistent administration surface. The default posture favours self-hosted
operation, with optional integrations added only when needed.

## The system shape

Site operators interact with one control centre. Underneath, individual modules
own distinct site capabilities while a documented extension point allows the
platform to grow without rewriting its core wiring.

## Public proof

The public GPL project documents its module model, extension hook, supported
WordPress and PHP baseline, and operator-facing control centre.

## Outcome or learning

The work demonstrates a durable platform pattern: a product can be broad
without becoming monolithic when optionality is explicit in its architecture and
interface.

## The boundary

This study excludes customer site configuration, agency provisioning patterns,
private update infrastructure, connector details, and any client data.
