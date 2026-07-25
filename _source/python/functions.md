---
layout: default
title:  Geometric Functions
parent: GeoDesk for Python
description: Mercator-aware geometric functions
nav_order: 11
---
> .module geodesk

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

> .method area(*geom*, units='square_meters')

Computes the area of a `Geometry`, `Box` or `Feature`.

*Since 2.2*

> .method length(*geom*, units='meters')

Computes the length of a (multi)linestring or polygon perimeter.

`geom` can be a `Geometry` or `Feature`

*Since 2.2*

> .method distance(*geom1*, *geom2*, units='meters')

Computes the distance between two `Geometry`, `Feature`, `Box` or `Coordinate` objects.

*Since 2.2*

## Constructive operations

> .method buffer(*geom*, distance, units='meters')
 
Computes the buffer (a polygonal `Geometry`) of a `Geometry`, `Feature`, `Box` or `Coordinate`.

`distance` may be negative. A negative buffer may produce an empty geometry.

Example:

```python
buf = buffer(geom, 20, 'feet')
```

*Since 2.2*

{%comment%}

> .method simplify(*geom*, tolerance, units='meters')
 
Returns a simplified `Geometry` of an input `Geometry` or `Feature` using the Douglas-Peucker algorithm. 

`tolerance`: The maximum allowed geometry displacement. The higher this value, the smaller the number of vertices in the resulting geometry.

As an alternative to `tolerance` and `units`, the maximum displacement may also be given as a unit-keyword argument:

```python
generalized = simplify(geom, feet=5)
```

*Since 2.2*

{%endcomment%}

> .end



Adapted from [Shapely Documentation](https://shapely.readthedocs.io/) --- &copy; 2011 -- 2023 Sean Gillies and Shapely contributors. Licensed under [CC-BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/)
{:.text-small}

 
