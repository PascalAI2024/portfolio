# IGD Games — a browser-game lab you can play

**[Open IGD Games](https://games.igddev.com)** · Public demos, private source

## The work

A collection of small browser games built around different player decisions:
wire a machine, direct an ant colony, solve a folklore puzzle, or plan a tactical
encounter. The hub gives these experiments one place to discover and play.

Three useful starting points:

- **Gizmo Works:** connect parts into working gadgets and solve a circuit-puzzle
  campaign.
- **SubTerra Lite:** paint pheromone routes and keep an ant colony supplied.
- **Papardes Zieds:** an eighteen-round puzzle journey through six settings from
  Latvian folklore.

## The engineering decision

Each game builds independently and runs inside the shared hub. That keeps a
small HTML5 puzzle alongside larger Phaser and PixiJS games without requiring
every experiment to use the same engine. A shared catalogue describes the
controls, supported play surfaces and current stage of each build.

## Evidence and limits

The [live hub](https://games.igddev.com) is the public artifact. Visitors can
inspect the presentation and try the games themselves. The collection includes
early prototypes and launch candidates; inclusion here is not a claim that a
game has passed an external storefront's review or reached a finished commercial
release. Test records and the source repository remain private.

[Back to the portfolio](../README.md)
