---
layout: default
title:  Editing
parent: GeoDesk for Python
has_toc: false
nav_order: 11
---

> .module geodesk
> .class Changes

# Editing API

The **Editing API** prepares batches of changes for updating a local GOL or upload to the global OpenStreetMap database.

<blockquote class="important" markdown="1">

Automated bulk edits and imports uploaded to OpenStreetMap must follow the [Automated Edits Code of Conduct](https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct).

</blockquote>

> .method Changes()
 
Creates a unit of changes (equivalent to an [OpenStreetMap changeset](https://wiki.openstreetmap.org/wiki/Changeset)).

```python
changes = Changes()
```

> .method create(*args*)

Creates a new feature. 

The arguments of this method are flexible and can be comprised of the following:

- A Shapely [`Geometry`](https://shapely.readthedocs.io/en/stable/geometry.htm): a [`Point`](https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html) creates a **node**, a [`LineString`](https://shapely.readthedocs.io/en/stable/reference/shapely.LineString.html), [`LinearRing`](https://shapely.readthedocs.io/en/stable/reference/shapely.LinearRing.html) or simple [`Polygon`](https://shapely.readthedocs.io/en/stable/reference/shapely.Polygon.html) creates a **way**; all other `Geometry` subtypes create a **relation**

- A `Coordinate` or longitude/latitude tuple (for a node)

- `lon` / `lat` arguments
 
- A list of nodes or coordinates (for a way)

- A list of features or `(*feature*, *string`) tuples (as the members of a relation)
  
- A Python `dict`, tuples or keyword arguments representing the tags of the feature

**Tag values** can be strings, numbers, `True`/`False` (converted to `"yes"`/`"no"`) or a list/tuple (becomes a single string with the values separated by semicolons)

For example, to create a node for a bookstore at a given longitude and latitude:

```python
node = changes.create(8.21, 49.35, 
    { "shop": "books", "name": "The Book Nook"})
# or
pt = shapely.Point(8.21, 49.35)
node = changes.create(pt, ("shop", "books"), ("name", "The Book Nook"))
# or
c = latlon(49.35, 8.21)
node = changes.create(c, shop="books", name="The Book Nook")
```

To create a way that represents a street:

```python
ls = shapely.LineString([[2.92, 45.4], [2.95, 45.21], [3.12, 45.3]])
way = changes.create(ls, 
    highway="primary", name="Main Street", 
    maxspeed=50, oneway=True)
# or
coords = lonlat((2.92, 45.4), (2.95, 45.21), (3.12, 45.3))
way = changes.create(coords, 
    { "highway": "primary", "name": "Main Street",
        "maxspeed": 50, "oneway": "yes" })
```

To create a route relation:

```python
relation = changes.create([way1, (way2, "forward"), 
    (way3, "backward"), ...], 
    type="route", route="bus", ref="51A" 
    name="Forest Hill to Back Bay")
```

If the list consists solely of nodes, `create()` always constructs a way. To obtain a relation, ensure that at least one item in the list is a tuple with a role (the role can simply be an empty string):

```python
way = changes.create([node1, node2, node2], ...)

relation = changes.create([(node1,""), node2, node2], ...)
```

- If a `LineString` or `LinearRing` has more than 2,000 vertexes (the maximum node count for a way), `create()` constructs a relation with `type=multilinestring` with multiple ways.

- Likewise, if a simple `Polygon` exceeds 2,000 vertexes, it is created as a relation (`type=multipolygon`), with its shell split across multiple member ways.

<blockquote class="note" markdown="1">

All polygon relations are `type=multipolygon`, even if they represent a single polygon.

</blockquote>

The `create()` method returns a `ChangedFeature`, which can be further modified and used to construct other features.

> .method modify(*feature*, *args*)

Modifies an existing feature. The optional arguments work the same as `create()`, except for the following:

- Passing a Shapely `Geometry` is not allowed (To modify a feature's geometry, manipulate its `lon`/`lat`, `nodes` or `members`)

- Tags passed as dictionaries or tuples add the given tags (or replace only the specific keys); to replace *all* tags of a feature, pass the new tags via the `tags` keyword arguments.

- To delete a tag, set it to `None` or an empty string.

Example:

```python
changes.modify(way, maxspeed=30)
changes.modify(node, lon=-4.72, lat=49.3)
changes.modify(relation, members=[way1, way2, ...], { "route": "bicycle"})
```

A shorter form is the subscript operator:

```python
changes[street].name="Draper Street"
hotel = changes[hotel]
```

The `modify()` method returns a `ChangedFeature`. Multiple calls for the same feature return the same object.


> .method delete(*feature*)

Deletes a feature. 

Before deleting a feature, you must remove it from all ways and relations to which it belongs:

```python
for parent in feature.parents:
    changes[parent].members.remove(feature)
changes.delete(feature)
```

> .method validate(url="https://overpass-api.de")

Checks the changes for conflicts via an Overpass query, and also assigns version numbers to the `ChangedFeature` objects. Any changes with possible conflicts are noted in `Changes.issues`.  


 
> .method save(*filename*)
 
Writes the change instructions to an `.osc` file (the file extension can be omitted from *filename*)

## Resolving Conflicts

> .property issues

A `list` of all merge conflicts, in the form of a three-value tuple:

- `"error"` or `"warning"`

- the `ChangedFeature` to which the issue applies

- a detailed message

 Any `error` issue will prevent the changes from being submitted to the OpenStreetMap server).


> .class ChangedFeature
 
## ChangedFeature Objects

A `ChangedFeature` represents a feature tracked by a `Changes` object. It is created by [`create()`](Changes_create), [`modify()`](Changes_modify), [`delete()`](Changes_delete) or via lookup (`[]`].   

> .property id
 
The feature’s numeric OSM identifier. *Read-only*

- The `id` of a newly-created feature is `0`, until the `Changes` object is validated or saved, at which point it is set to a negative number.

> .property is_node

`True` if this feature is a node, otherwise `False`. *Read-only*

> .property is_way

`True` if this feature is a way (linear or area), otherwise `False`. *Read-only*

> .property is_relation

`True` if this feature is a relation (area or non-area), otherwise `False`. *Read-only*

> .property is_deleted

`True` if this feature has been deleted, otherwise `False`. *Read-only*

> .property tags

The feature’s tags (as a `dict` of key/value pairs). Setting this attribute to a new `dict` (or list of tuples) replaces all tags.  
 
> .property original
 
The original [`Feature`](Feature#Feature), or `None` for a newly created feature. *Read-only*

> .property nodes
 
The nodes of a way (as a `list` of `ChangedFeature` objects), or `None` for a node or relation.

> .property members
 
The members of a relation (as a `list` of `ChangedFeature` objects), or `None` for a node or way.


## Modifying the nodes of a way

Once a way has been created or modified (or added to the set of changes via `changes[way]`), its `nodes` can be manipulated like a regular Python `list`:

```python
way.nodes.append(node)
way.nodes.extend([node1, node2, node3])
way.nodes.insert(3, node)
way.remove(node)
way.nodes.reverse()   # flips the order of the nodes 
```

Note that unlike `remove()` of a regular list (which removes only the *first* occurrence of an item), `nodes.remove()` removes *all* instances of the given node. 

Nodes can be `Feature`, `ChangedFeature` or `Coordinate` objects, or simple coordinate tuples. Once added to `nodes`, they become `ChangedFeature` objects.  

The tags and locations of nodes can be changed directly:

```python
way.nodes[2].traffic_calming = "bump"   
    # turns the node into speed bump 
way.nodes[5].lat -= .0005 
    # moves the node south
```

Assigning a `Coordinate` or longitude/latitude tuple to a node changes its location, which affects the geometry of all ways to which this node belongs. To replace the node in the given way, without changing the original node, assign a `Feature` or `ChangedFeature` object instead:

```python
way.nodes[12] = (8.17, 51.9)    
    # changes the node's location
way.nodes[12] = changes.create(8.17, 51.9)
    # replaces the node with a new one
```

## Modifying the members of a relation

Similar to `nodes`, the `members` of a relation can be manipulated like a regular Python `list`. In addition, the `role` attribute of a member can be set:

```python
relation.members.append(way)
relation.members[5].role = "side_stream"
```

## Examples

### Replacing misspelled tags

This script renames a misspelled `highway` key in a given region:

```python
from geodesk import Features, Changes
misspelled_key = "hihgway"  
correct_key = "highway"

world = Features("world.gol")
region = ...    

fixed = Changes()
for feature in world(region)(f"[{misspelled_key}]"):
    tags = fixed[feature].tags
    tags[correct_key] = tags[misspelled_key]
    del tags[misspelled_key]
fixed.validate()    
fixed.save(f"{region.name}-fixes")
```

