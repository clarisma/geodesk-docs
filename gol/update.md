---
layout: default
title: update
parent: GOL Tool
nav-order: 10
---

# `update`

Updates a Geo-Object Library by applying changes from `.osc` files or a replication server.

{% include gol/lab.html %}

Usage:

    gol update <gol-file> [ <osc-file>+ | <url> ] [<options>]

If no files or URL is specified, `update` will download changes from the replication server from which this GOL was last successfully updated.

In order to be updatable, a GOL must have been built or loaded with option `--waynode-ids` (`-w).

*Since 2.5*

## Options

### `-C`, `--connections` <code><em>&lt;NUMBER&gt;</em></code> {#option-connections}

Value: 1 -- 256 (default: 2)

The maximum number of simultaneous connections to use when downloading changes.

### `-r`, `--revision` <code><em>&lt;NUMBER&gt;</em></code> {#option-revision}

The latest revision for which changes will be downloaded. If omitted, all available changes will be downloaded.

{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

