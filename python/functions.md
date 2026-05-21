---
layout: default
title:  Geometric Functions
parent: GeoDesk for Python
description: Mercator-aware geometric functions
nav_order: 11
---


# Geometric Functions

GeoDesk provides several Mercator-aware replacements for common Shapely [measurement](https://shapely.readthedocs.io/en/2.0.2/measurement.html) and [constructive](https://shapely.readthedocs.io/en/2.0.2/constructive.html) functions.

The functions described below are easier to use and are often faster than their Shapely equivalents, as they avoid the need for constructing temporary `Geometry` objects and converting measurements into the Cartesian units expected by Shapely.

In addition to Shapely [`Geometry`](Geometry) objects, these functions accept [`Feature`](Feature), as well as [`Box`](Box) and [`Coordinate`](Coordinate) (where meaningful).

The following units may be used:

### Length

- `meters` (`m`)
- `feet` (`ft`)
- `yards` (`yd`)
- `kilometers` (`km`)
- `miles` (`mi`)

### Area

- `square_meters` (`m2`)
- `square_feet` (`ft2`)
- `square_yards` (`yd2`)
- `square_kilometers` (`km2`)
- `square_miles` (`mi2`)
- `hectares` (`ha`)
- `acres` (`ac`)

Length units such as `m` or `ft` are also accepted and treated as their area equivalent.


## Measurement

<h3 id="area" class="api"><span class="prefix">geodesk.</span><span class="name">area</span><span class="paren">(</span><i>geom</i>, units=<span class="default">'square_meters'</span><span class="paren">)</span></h3><div class="api" markdown="1">

Computes the area of a `Geometry`, `Box` or `Feature`.

</div><h3 id="length" class="api"><span class="prefix">geodesk.</span><span class="name">length</span><span class="paren">(</span><i>geom</i>, units=<span class="default">'meters'</span><span class="paren">)</span></h3><div class="api" markdown="1">

Computes the length of a (multi)linestring or polygon perimeter.

`geom` can be a `Geometry` or `Feature`

</div><h3 id="distance" class="api"><span class="prefix">geodesk.</span><span class="name">distance</span><span class="paren">(</span><i>geom1</i>, <i>geom2</i>, units=<span class="default">'meters'</span><span class="paren">)</span></h3><div class="api" markdown="1">

Computes the distance between two `Geometry`, `Feature` or `Coordinate` objects.

</div>
## Constructive operations

<h3 id="buffer" class="api"><span class="prefix">geodesk.</span><span class="name">buffer</span><span class="paren">(</span><i>geom</i>, distance, units=<span class="default">'meters'</span><span class="paren">)</span></h3><div class="api" markdown="1">

Computes the buffer (a polygonal `Geometry`) of a `Geometry`, `Feature`, `Box` or `Coordinate`.

`distance` may be negative. A negative buffer may produce an empty geometry.

As an alternative to `distance` and `units`, the buffer distance may also be given as a unit-keyword argument:

```python
buf = buffer(geom, feet=20)
```

</div><h3 id="simplify" class="api"><span class="prefix">geodesk.</span><span class="name">simplify</span><span class="paren">(</span><i>geom</i>, tolerance, units=<span class="default">'meters'</span>, preserve_topology=<span class="default">True</span><span class="paren">)</span></h3><div class="api" markdown="1">

Returns a simplified `Geometry` of an input `Geometry` or `Feature` using the Douglas-Peucker algorithm.

`tolerance`: The maximum allowed geometry displacement. The higher this value, the smaller the number of vertices in the resulting geometry.

`preserve_topology`: By default (`True`), the operation will avoid creating invalid geometries (checking for collapses, ring-intersections, etc), but this is computationally more expensive.

As an alternative to `tolerance` and `units`, the maximum displacement may also be given as a unit-keyword argument:

```python
generalized = simplify(geom, feet=5)
```

</div>



Adapted from [Shapely Documentation](https://shapely.readthedocs.io/) --- &copy; 2011 -- 2023 Sean Gillies and Shapely contributors. Licensed under [CC-BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/)
{:.text-small}


