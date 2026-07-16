---
layout: default
title:  Box Objects
parent: GeoDesk for Python
nav_order: 3
---

> .module geodesk
> .class Box

# Box Objects

A `Box` represents an axis-aligned bounding box.

> .method Box(*coords*)
 
Constructs a `Box` from the given coordinates.

**WGS-84 (longitude & latitude**

- `minlon`/`minlat`/`maxlon`/`maxlat`
- `west`/`south`/`east`/`north` 
- `w`/`s`/`e`/`n`
 
**Mercator-projected** 

- `minx`/`miny`/`maxx`/`maxy` 
- `left`/`bottom`/`right`/`top`

```python
paris = Box(west=2.2, south=48.8, east=2.5, north=48.9)
```

> .method Box(*geom*)

Constructs the smallest `Box` that fully encloses the given `Geometry`, `Feature`, `Coordinate` or `Box`.

```python
bounds  = Box(feature)    # same as feature.bounds
bounds2 = Box(polygon)    # i.e. the envelope of the Polygon
```

## Properties

> .property minlon

The minimum X coordinate (WGS-84). Alias: `west`, `w` 

> .property minlat

The minimum Y coordinate (WGS-84). Alias: `south`, `s`

> .property maxlon

The maximum X coordinate (WGS-84). Alias: `east`, `e`

> .property maxlat

The maximum Y coordinate (WGS-84). Alias: `north`, `n`

> .property minx

The minimum X coordinate (Mercator-projected). Alias: `left` 

> .property miny

The minimum Y coordinate (Mercator-projected). Alias: `bottom` 

> .property maxx

The maximum X coordinate (Mercator-projected). Alias: `right` 

> .property maxy

The maximum Y coordinate (Mercator-projected). Alias: `top` 

> .property area

The area (in square meters).

*Since 2.2*

> .property centroid

The center [`Coordinate`](#Coordinate).

> .property shape

The box as a [`Polygon`](#Geometry).

## Operators

`in` checks if a `Box` contains the given `Coordinate` (or another `Box`).

```python
>>> Coordinate(50,100) in Box(10,20,300,200)
True
>>> Box(-20,30,100,50) in Box(10,20,300,200)
False
```

`+` expands a `Box` so it contains a given `Coordinate` (or another `Box`).

```python
>>> b = Box(10,20,300,200)
>>> b + Coordinate(400,300)
Box(10, 20, 400, 300)
```

`|` does the same:

```python
>>> Box(10,20,300,200) | Box(50,70,400,500)
Box(10,20,400,500)
```

`&` returns the intersection of two `Box` objects (or an empty box if they don't intersect).

```python
>>> a = Box(10,20,300,200)
>>> b = Box(50,70,400,500)
>>> a & b
Box(50, 70, 300, 200)
```

Since an empty `Box` is *falsy*, you can use `&` to check if two boxes intersect:

```python
if a & b:
    print("The bounding boxes intersect.")
```

## Methods

> .method buffer(*units*=*distance*)

Expands this box in all directions by the given distance. Negative values shrink it (which may result in an empty box).

{%comment%}

> .method buffered(*units*=*distance*)

Same as [`buffer()`](#Box.buffer), but returns a copy, leaving this box unmodified.

{%endcomment%}
