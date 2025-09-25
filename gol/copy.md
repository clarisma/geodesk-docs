---
layout: default
title: copy
parent: GOL Tool
nav-order: 2
---

# `gol copy` ~~2.2~~

Copies tiles between Libraries and Bundles.

Usage:

    gol copy <source> <target> [<options>]

`<source>` and `<target>` must be of the same type (GOLs or GOBs).

- To copy tiles from a GOB into a GOL, use [`gol load`](load.md). 

- To store tiles from a GOL as a GOB, use [`gol save`](save.md)

If an area is specified (using [`--bbox`](#option-bbox) or [`--area`]((#option-area)), only the tiles touching that area are copied.

If the source and target GOL contain different versions, the target's version is set to the newer version, and all tiles from the older GOL are marked as stale.


## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

