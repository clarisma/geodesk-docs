---
id: build
layout: default
title: build
parent: GOL Utility
nav-order: 0
---

<doc-command name="build">

Creates a new feature library from an OpenStreetMap data file.

Usage:

    gol build [<options>] <gol-file> <source-file>

`<gol-file>` is the name of the library to build. If no extension is given, `.gol` will be added.

`<source-file>` is the file that contains the OpenStreetMap data. Currently, only files in [OSM-PBF format](https://wiki.openstreetmap.org/wiki/PBF_Format) are supported. This format is popular due to its compact size and wide tool support.

## Sources of OpenStreetMap Data

A complete copy of the worldwide map data (updated weekly) is available for download on the [OSM website](https://planet.osm.org/). Because of the size of the download (multiple gigabytes) and limited server bandwidth, it is highly recommended to use [torrents](https://wiki.openstreetmap.org/wiki/Planet.osm#BitTorrent).

A better alternative may be using a [mirror](https://wiki.openstreetmap.org/wiki/Planet.osm#Planet.osm_mirrors), or a provider of [processed datasets](https://wiki.openstreetmap.org/wiki/Processed_data_providers).

If you are looking for regional or country-sized subsets, [GeoFabrik](https://download.geofabrik.de/) offers a large selection of datasets (updated daily).

<blockquote class="note" markdown="1">
Need the whole world? [OpenPlanetData.com](https://openplanetdata.com) publishes the full planet as a ready-to-use GOL (about 100 GB; updated daily).
</blockquote>

## Hardware Requirements

Building a library is a resource-intense operation. To build a GOL that contains the worldwide OpenStreetMap dataset, you should have a machine with at least 8 physical cores and 24 GB of RAM, or the build process may take multiple hours.

For smaller datasets, any reasonably modern machine will do fine (a 10-year-old dual-core laptop with 8 GB RAM will build country-size datasets such as Germany, France or Japan in about 20 minutes each). A fast solid-state drive is recommended in any case.

Your drive should have free space equal to at least three times the size of the .osm.pbf file (in addition to that file). So if you wish to download the planet file (currently 60 GB) and turn it into a GOL, you should have 240 GB of disk space available.

The resulting GOL itself will only be 30% to 50% larger than the planet file (The additional storage is needed to accommodate temporary files).


## Options

<doc-option name="areas">

The tags that determine whether a closed OSM way is treated as an area or a linear ring. Rules can be specified for one or more keys. A closed way is treated as an area if it fulfills at least one of these rules (or is explicitly tagged `area=yes`), and is *not* tagged `area=no`.

Key rules have the following format:

<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code><i>key</i> [ <b>(</b> <b>only</b>|<b>except</b> <i>value</i>+ <b>)</b> ]
</code></pre>
</div>
</div>

Multiple key rules and values must be separated by whitespace and/or commas.

Example:


```
--areas "building, barrier (only city_wall, ditch),  man_made (except embankment)
```

The above will cause any closed way tagged `building` (except `building=no`), `barrier=city_wall`, `barrier=ditch` or `man_made` (except `man_made=embankment` or `man_made=no`) to be treated as an area.

</doc-option>
<doc-option name="levels" short="l" value="list">

The zoom levels at which tile-tree nodes should be created. Together with [`max-tiles`](#max-tiles) and [`min-tile-density`](#min-tile-density), this setting shapes the tile structure of a GOL.

- Zoom levels must be between 0 and 12.
- The difference between zoom levels must not exceed 3 (e.g. you can specify `0,3,6,9`, but not `0,4,6,12`).
- The root level (`0`) is always included implicitly.
- Fewer zoom levels result in a flatter tree that may yield better query performance, but cause a higher variance in tile sizes.
- Setting the top zoom level too low may cause the maximum tile size (1 GB uncompressed) to be exceeded. (Very large tiles may also cause the build process to run out of memory.)

</doc-option>
<doc-option name="max-tiles" short="m" value="number" min="1" max="8000000" default="65535">

Value: 1 -- 8,000,000 (default: 65,535)

The maximum number of tiles into which the features of the GOL are organized. The actual number of tiles may be significantly less, based on [`min-tile-density`](#option-min-tile-density). A lower tile count results in a more compact GOL, while a higher tile count improves the performance of certain large-area spatial queries.

A higher setting is also preferred if you intend to host a tile repository, as a more granular tileset reduces the amount of data users will have to download for their regions of interest.

If this number is set too low, a tile may exceed the maximum size of 1 GB (uncompressed). An unreasonably low setting may also cause the build process to fail with an `OutOfMemoryError`.

</doc-option>
<doc-option name="max-strings" value="number" min="256" max="65535" default="16384">

Value: 256 -- 65,535 (default: 16,384)

The maximum number of strings that will be stored in the GOL's Global String Table. A higher value results in a smaller GOL file and increased query performance. (Loading a larger string table consumes more memory and may cause a slight delay when opening a GOL file, but the impact of this is generally negligible.)

The actual number of strings will be less if fewer strings meet the minimum usage threshold ([`--min-string-usage`](#option-min-string-usage))

</doc-option>
<doc-option name="min-string-usage" value="number" min="1" max="100000000" default="300">

### `--min-string-usage` <code><em>&lt;NUMBER&gt;</em></code> {#option-min-string-usage}

Value: 1 -- 100,000,000 (default: 300)

Specifies the minimum number of times a string must be used by features (as a tag key or value, or as a role in a relation) in order to be included in the GOL's Global String Table.

See [`--max-strings`](#option-max-strings).

</doc-option>
<doc-option name="min-tile-density" short="n" value="number" min="1" max="10000000" default="75000">

### `-n`, `--min-tile-density` <code><em>&lt;NUMBER&gt;</em></code> {#option-min-tile-density}

Value: 1 -- 10,000,000 (default: 75,000)

If there are fewer nodes in a tile area than this number, the tile will be omitted, and all features in the tile area will be placed into tiles at lower zoom levels. A lower threshold will result in more tiles, up to the maximum specified by [`--max-tiles`](#option-max-tiles).

</doc-option>

### `-r`, `--rtree-branch-size` <code><em>&lt;NUMBER&gt;</em></code> {#option-rtree-branch-size}

Value: 1 -- 256 (default: 16)

GOLs use R-tree indexes to accelerate spatial queries. This setting specifies the maximum number of features (or child branches) in each branch (a node in the R-tree). A larger number reduces the size of the GOL, a smaller number increases query performance (but set too low, it may have the opposite effect). Square numbers (4, 9, 16, 25, etc.) tend to perform best.


### `-w`, `--waynode-ids` {#option-waynode-ids}

Stores the IDs for all nodes, including untagged nodes that exist solely to define the geometry of ways. By default, the IDs of such nodes are omitted to save storage space. Option `-w` increases the size of a GOL by about 20%, but is needed to allow updates.

{% include gol/option-silent.md %}

### `-u`, `--updatable` {#option-updatable}

Enables incremental updates to the GOL file (using the [`update`](update.md) command). Setting this option enables [`--waynode-ids`](#option-waynode-ids). It also enables [`--id-indexing`](#option-id-indexing) if the `build` command determines that ID indexes are likely to significantly speed up updating.

{% include gol/option-verbose.md %}

## Build Settings

{% comment %}

### `area-tags`  ~~0.2~~ {#area-tags}

The tags that determine whether a closed OSM way is treated as an area or a linear ring. Rules can be specified for one or more keys. A closed way is treated as an area if it fulfills at least one of these rules (or is explicitly tagged `area=yes`), and is *not* tagged `area=no`.

Key rules have the following format:

<div class="language-plaintext highlighter-rouge">
<div class="highlight">
<pre class="highlight"><code><i>key</i> [ <b>(</b> <b>only</b>|<b>except</b> <i>value</i>+ <b>)</b> ]
</code></pre>
</div>
</div>


Multiple key rules and values must be separated by whitespace and/or commas.

Example:


### `id-indexing` ~~0.3~~ {#id-indexing}

Value: `yes` / `no` (defaults to value of [`updatable`](#updatable))

If enabled, instructs the `build` command to retain the external ID indexes used during building, so incremental updates can be processed faster (`updatable` must be enabled).

In case this option is disabled, the [`update`](/gol/update) command can also re-create these indexes if needed.

{% endcomment %}

### `indexed-keys`

To enhance query performance, GOLs organize features into separate indexes based on their tags. The `index-keys` section specifies which keys should be considered for indexing. The ideal keys for indexing are those that create categories of features (similar to *layers* in a traditional GIS database), such as `highway`, `landuse` or `shop`. As the number of indexes is limited (see [`max-key-indexes`](#max-key-indexes)), multiple keys may be consolidated into one index (This is done automatically on a per-type, per-tile basis). Features whose tags have multiple indexed keys (e.g. `tourism` and `amenity` for a hotel that is also a restaurant) are consolidated with features with the same key, or placed into a separate mixed-key index.

Keys that should always be placed into the same index can be specified as *key-pairs* by placing forward slashes between these keys (useful for rare-but-similar categories like `telecom`/`communication`).

Example:

```
indexed-keys:
  amenity
  building
  highway
  natural/geological
  shop
```

### `key-index-min-features`

Value: 0 -- 1,000,000 (default: 300)

If there are fewer features in a key index than this number, these features will be consolidated into another index.

Used with [`indexed-keys`](#indexed-keys) and [`max-key-indexes`](#max-key-indexes).


### `max-key-indexes`

Value: 0 -- 30 (default: 8)

The maximum number of key-based indexes to create, per feature type (*node*, *way*, *area*, *relation*). A higher number boosts the performance of queries that make use of indexed keys (queries that require the presence of a key/tag). However, a higher number of key indexes may reduce the performance of queries not based on indexed keys. Key indexes are very storage-efficient, so specifying a higher number has a minimal impact on file size.

If the number of key indexes is lower than the number of keys and key-pairs in [`indexed-keys`](#indexed-keys), features with less frequent keys will be consolidated in one or more combined indexes. Index consolidation also happens if the number of features in an index is below [`key-index-min-features`](#key-index-min-features)

Specifying `0` disables key indexing.


### `properties`

A section with key-value pairs that are stored as GOL metadata, which are displayed by [`gol info`](/gol/info) and can be read by other applications.

Common properties include:

`generator`   | The program used to create the GOL ("geodesk/gol {{ site.geodesk_version }}")
`copyright`   | Text indicating the copyright holder of the data ("OpenStreetMap contributors")
`license`     | The license under which the data is distributed ("Open Database License 1.0")
`license-url` | Link to the website where the license text can be found ("https://opendatacommons.org/licenses/odbl/1-0/")
`tileset-url` | The default URL from which tiles can be downloaded or updated (e.g. "https://data.geodesk/world")

<blockquote class="important" markdown="1">

If you wish to distribute tilesets based on OpenStreetMap data, you must do so in accordance
with the [Open Database License](https://opendatacommons.org/licenses/odbl/1-0/). You can
use the `build` command to create a GOL from any geodata in OSM-PBF format, so in theory,
GOLs could contain data from non-OSM sources (or very old OSM datasets distributed under a
Creative Commons License) -- but in general, you should not override the defaults for
`copyright`, `license` and `license_url`.

</blockquote>

To set properties from the command line, use <code>--property:<i>property</i>=<i>value</i></code> or <code>-p:<i>property</i>=<i>value</i></code>.

</doc-command>
