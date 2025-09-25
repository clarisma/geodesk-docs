---
layout: default
title: GOL Tool
has_children: true
has_toc: false
nav_order: 5
permalink: /gol
---

# The GOL Tool

The `gol` ("Geo-Object Librarian") command-line utility allows you to build, manage, and query [Geo-Object Libraries](/libraries) and Bundles.

Most commands follow this form:

    gol <command> <gol-file> [<arguments>] [<options>]

<img class="figure" src="/img/gol-diagram2.png" width=400>

## Commands

<table>
<tr>
<td markdown="1">
[`build`](/gol/build)
</td>
<td markdown="1">
Create a Geo-Object Library from OpenStreetMap data.
</td>
</tr>

<tr>
<td markdown="1">
[`check`](/gol/check)
</td>
<td markdown="1">
Verifies a Library's integrity.
</td>
</tr>

<!--
<tr>
<td markdown="1">
[`copy`](/gol/copy)
</td>
<td markdown="1">
Copy tiles between Libraries or Bundles.
</td>
</tr>
-->

<tr>
<td markdown="1">
[`help`](/gol/help)
</td>
<td markdown="1">
Display documentation.
</td>
</tr>

<tr>
<td markdown="1">
[`info`](/gol/info)
</td>
<td markdown="1">
Provide basic file statistics.
</td>
</tr>

<tr>
<td markdown="1">
[`load`](/gol/load)
</td>
<td markdown="1">
Import tiles from a Bundle into a Library.
</td>
</tr>

<tr>
<td markdown="1">
[`map`](/gol/map)
</td>
<td markdown="1">
Display features on a map.
</td>
</tr>

<tr>
<td markdown="1">
[`query`](/gol/query)
</td>
<td markdown="1">
Retrieve features.
</td>
</tr>

<!--
<tr>
<td markdown="1">
[`remove`](/gol/remove) ~~0.2~~
</td>
<td markdown="1">
Removes tiles in a specific area.
</td>
</tr>

<tr>
<td markdown="1">
[`retain`](/gol/retain) ~~0.2~~
</td>
<td markdown="1">
Removes tiles *outside* a specific area.
</td>
</tr>
-->

<tr>
<td markdown="1">
[`save`](/gol/save)
</td>
<td markdown="1">
Writes tiles from a Library to a Bundle.
</td>
</tr>

<!--
<tr>
<td markdown="1">
[`update`](/gol/update) ~~0.3~~
</td>
<td markdown="1">
Updates the library.
</td>
</tr>
-->

</table>

<blockquote class="note" markdown="1">
On Windows, progress bars may appear ragged. To fix this, switch the shell's font to Cascadia Mono (in `Properties`) or another font with broad Unicode support (such as [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) or [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro)).
</blockquote>


## Common Options

The following options are supported across most commands:

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}
{% include gol/option-output.md %}
{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}
{% include gol/option-wait.md %}

