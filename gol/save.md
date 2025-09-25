---
layout: default
title: save
parent: GOL Tool
nav-order: 9
---

# `save` ~~2.1~~

Saves tiles from a Geo-Object Library to a Geo-Object Bundle.

Usage:

    gol save <gol-file> <gob-file> [<options>]

If no area is defined (via [`--area`](#option-area) or [`--bbox`](#option-bbox)), all tiles are saved.

By default, the IDs of untagged nodes that don't belong to relations (i.e. nodes that merely define the geometry of ways) are not saved, resulting in a smaller GOB. To include these IDs, use option [`--waynode-ids`](#option-waynode-ids).


## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

### `-w`, `--waynode-ids` {#waynode-ids}

Saves the IDs of *all* nodes, including those that are untagged and don't belong to relations. 