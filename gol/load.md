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

    gol load [<gol-file>] <gob-file> [<options>]

If *gol-file* is omitted, the name of the GOL is assumed to be the base name of *gob-file* (with extension `.gol`). If the GOL does not exist, it is created.

*gob-file* can be a local file, or a URL (*since 2.2*). for local files, the `.gob` extension may be omitted.

If no area is defined (via [`--area`](#option-area) or [`--bbox`](#option-bbox)), all tiles that aren't already present in the Library are imported from the Bundle.

The Library and the Bundle must have the same tileset ID.

By default, the IDs of untagged nodes that don't belong to relations (i.e. nodes that merely define the geometry of ways) are omitted from the GOL, reducing its size. To include these IDs, use option [`--waynode-ids`](#option-waynode-ids).

*Since 2.1*

Example:

```bash 
gol load japan
```

loads all tiles from `japan.gob` into `japan.gol` (creating the GOL if it doesn't yet exist).

```bash
gol load paris https://download.openplanetdata.com/osm/planet/gob/v2/planet-latest.osm.gob \
    -a 2.383,48.807,2.248,48.825,2.235,48.858,2.298,48.903,2.407,48.905,2.426,48.840,2.383,48.807 \
    -C 8
```

loads the region of metropolitan Paris into `paris.gol` from the given URL, using 8 concurrent connections.

<blockquote class="note" markdown="1">
[Open Planet Data](https://openplanetdata.com) publishes a world-wide Geo-Object Bundle (about 50 GB, updated daily).
</blockquote>

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}

### `-C`, `--connections` {#option-connections}

Value: 1 -- 256 (default: 4)

The maximum number of simultaneous connections to use when downloading tiles from a URL.

{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

### `-w`, `--waynode-ids` {#option-waynode-ids}

Includes the IDs of *all* nodes, including those that are untagged and don't belong to relations. 

This option is only considered for newly-created GOLs. 