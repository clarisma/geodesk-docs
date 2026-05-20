---
layout: default
title: map
parent: GOL Tool
nav-order: 6
has_toc: false
permalink: /gol/map
---

# `gol map`

Displays query results on a Leaflet map in a web browser.

Usage:

    gol map <gol-file> <query> [<options>] 

The query must be written in [GOQL](../goql), the Geo-Object Query Language. GOQL is similar to [MapCSS](https://wiki.openstreetmap.org/wiki/MapCSS/0.2), which is used by Mapnik and Overpass to select OSM objects.

The basemap and the click/hover behavior of the displayed features can be customized using various options.

For example:

    gol map france na[tourism=museum] -a paris.wkt -t {name} -l {website}

queries `france.gol` and displays all museums in the Paris area (defined in `paris.wkt`). Their names are shown as tooltips. Clicking on a feature will open the museum's website.

Multiple sets of features can be displayed on the same map. In this case, the query for each subset is prefixed by a color:

    gol map berlin red: na[amenity=fire_station] yellow: n[emergency=fire_hydrant]

displays all fire stations in red, and hydrants in yellow. The color can be any predefined Web color, or a custom color in the form `#RRBBGG` (e.g. `#00f0e0` for bright turquoise).

## Options

{% include gol/option-area.md %}
{% include gol/option-bbox.md %}

### `-m`, `--map` <code><em>&lt;URL&gt;</em></code> {#option-map}

The URL of the tileserver which hosts the basemap.

### `-A`, `--attribution` <code><em>&lt;TEXT&gt;</em></code> {#option-attribution}

The attribution text to display at the bottom of the map. Can be plain text or HTML, and must be enclosed in double quotes if it contains spaces, pspecial characters or HTML tags.

### `-t`, `--tooltip` [ <code><em>&lt;TEXT&gt;</em></code> ] {#option-tooltip}

Text to display when user hovers over a feature. `<TEXT>` may be HTML and typically includes template parameters. If `<TEXT>` is omitted, the tooltip displays the feature's tags (Use option `--keys` to control which tags will be included).

### `-p`, `--popup` [ <code><em>&lt;TEXT&gt;</em></code> ] {#option-tooltip}

Text to display in a popup when user clicks on a feature. `<TEXT>` may be HTML and typically includes template parameters. If `<TEXT>` is omitted, the popup displays the feature's tags (Use option `--keys` to control which tags will be included). In that case, you can use `--link` to customize the popup's header link, and `--edit` to display an `EDIT` button.

### `-l`, `--link` [ <code><em>&lt;URL&gt;</em></code> ] {#option-link}

Navigates to the given URL (may be a template) when user clicks on a feature. If `<URL>` is omitted, it defaults to `https://www.openstreetmap.org/{type}/{id}`.

If option `--popup` is specified, this option defines the page that will be opened when the user click's on the popup's header.

If option `--edit` is specified, but not `--popup`, `--link` is ignored.

### `-e`, `--edit` [ <code><em>&lt;URL&gt;</em></code> ] {#option-edit}

Navigates to the given URL (may be a template) when user clicks the `EDIT` button in a feature's popup. If `--popup` is not specified, `--edit` takes the place of `--link`. If `<URL>` is omitted, it defaults to `https://www.openstreetmap.org/edit?{type}={id}`.






