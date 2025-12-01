---
layout: default
title: query
parent: GOL Tool
nav-order: 6
has_toc: false
permalink: /gol/query
---

# `gol query`

Outputs all features that match the given query to `stdout`, in a variety of formats. If no query is provided, enters [interactive mode](#interactive-mode), which enables more sophisticated access to the GOL's features.

Usage:

    gol query <gol-file> [<query>] [<options>] 

Any query must be written in [GOQL](../goql), the Geo-Object Query Language. GOQL is similar to [MapCSS](https://wiki.openstreetmap.org/wiki/MapCSS/0.2), which is used by Mapnik and Overpass to select OSM objects.

For example:

    gol query geodata/france \
      na[amenity=fire_station], n[emergency=fire_hydrant] \
      -b 2.2,48.8,2.5,48.9 -f geojson 

retrieves all fire stations (which can be nodes or areas) and hydrants
(which only exist as nodes) from the `france.gol` library (stored in the `geodata`
folder). The features must lie fully or partially inside the specified bounding box (a rectangle that covers metropolitan Paris) and are printed to `stdout` as GeoJSON (*see below*).

## Interactive mode

**Interactive mode** supports complex queries using [GeoDesk for Python](../python). 

<blockquote class="note" markdown="1">
You will need to install Python. On Windows, required Python modules are downloaded automatically; on Linux and macOS, install them manually via `pip install geodesk`.
</blockquote>

For example:

    gol query france

begins interactive mode using `france.gol`.

Let's retrieve the administrative area of Paris:

```python
>>> paris = france("a[boundary=administrative][admin_level=6][name=Paris]").one
```

We can query its tags like this:

```python
>>> paris.population
2165423
>>> paris["name:it"]
'Parigi'
```

Now, we'll get all named main roads in Paris and count them:

```python
>>> streets = france("w[highway=primary][name]")(paris)
>>> streets.count
27525
```

Next, we'll get their unique names, sorted alphabetically:

```python
>>> sorted({s.name for s in streets})
['Allée de Longchamp', "Allée du Bord de l'Eau", 'Avenue Aristide Briand', ... ]
```

Let's compute their combined length (in meters):

```python
>>> round(streets.length)
235472
```

Finally, we'll display them on a map:

```python
>>> streets.map.show()
```

When you're done, press `Ctrl-Z` followed by `Enter` to return to the shell.


## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}

### `-f`, `--format` <code><em>&lt;TYPE&gt;</em></code> {#option-format}

The output format of the results:

`brief` | Prints a per-feature overview (*default*) 
`count` | Prints only the *number* of features. 
`csv` | Comma-separated values
`geojson` / `geojsonl` | GeoJSON ([traditional](https://geojson.org) / [one feature per line](https://stevage.github.io/ndgeojson/))
`list` | Simple list of IDs 
`table` | Simple text-based table
`wkt` | Well-known text (geometries only)
`xml` | [OSM-XML](https://wiki.openstreetmap.org/wiki/OSM_XML)


### `-k`, `--keys` <code><em>&lt;LIST&gt;</em></code> {#option-keys}

A comma-separated list of OSM keys, which determine the feature tags to be
included in the output.

There are several special keys that only apply to the `csv` output option and produce additional columns:

<table>
  <tr>
    <td><code>bbox</code></td>
    <td markdown="span">

The bounding-box coordinates of the feature (West, South, East, North).
For `--format=geojson`, this becomes the [`bbox`](https://datatracker.ietf.org/doc/html/rfc7946#section-5) member of the `Feature` object.
 
  </td>
</tr>
<tr>
  <td><code>geom</code></td>
  <td>

The geometry of the feature (as <a href="https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry">well-known text</a>).<br>
          Only applies to <code>--format=csv</code>. 
      </td>
    </tr>
    <tr>
      <td><code>id</code></td>
      <td>
          The OSM ID of the feature, prefixed by the type letter (e.g. "N1234")
      </td>
    </tr>
    <tr>
      <td><code>lat</code></td>
      <td>
          The WGS-84 latitude of the feature's centroid
      </td>
    </tr>
    <tr>
      <td><code>lon</code></td>
      <td>
          The WGS-84 longitude of the feature's centroid
      </td>
    </tr>
    <tr>
      <td><code>tags</code><br>(or&nbsp;<code>*</code>)</td>
      <td>
          A comma-separated list of key-value pairs, representing the keys of the tags
          that are not already printed in a column of their own. 
       </td>
    </tr>
  </table>

If `--keys` is omitted, all tags are included in the output.

`--keys` is ignored for the `count` and `list` formats.


{% include gol/option-output.md %}

### `-p`, `--precision` <code><em>&lt;NUMBER&gt;</em></code> {#option-precision}

Value: 0 -- 15 (default: 7)

The coordinate precision (digits after the decimal point).

<!--
<div class="language-plaintext highlighter-rouge">
<pre class="highlight"><code>--precision=<em>0-15</em></code></pre></div>
-->

Applies only to `csv`, `geojson`/`geojsonl` and `wkt`.

{% include gol/option-quiet.md %}
{% include gol/option-silent.md %}
{% include gol/option-verbose.md %}