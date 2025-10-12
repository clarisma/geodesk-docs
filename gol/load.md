---
layout: default
title: load
parent: GOL Tool
nav-order: 5
---

# `gol load`

Imports tiles into a Geo-Object Library from a Geo-Object Bundle.

{% include gol/lab.html %}

Usage:

    gol load <gol-file> <gob-file> [<options>]

If no area is defined (via [`--area`](#option-area) or [`--bbox`](#option-bbox)), all tiles that aren't already present in the Library are imported from the Bundle.

The Library and the Bundle must have the same tileset ID.

By default, the IDs of untagged nodes that don't belong to relations (i.e. nodes that merely define the geometry of ways) are omitted from the GOL, reducing its size. To include these IDs, use option [`--waynode-ids`](#option-waynode-ids).

*Since 2.1*

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

### `-w`, `--waynode-ids` {#waynode-ids}

Includes the IDs of *all* nodes, including those that are untagged and don't belong to relations. 

This option is only considered for newly-created GOLs. 