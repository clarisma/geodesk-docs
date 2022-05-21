# GeoDesk

<img src="https://docs.geodesk.com/logo2.png">

GeoDesk is a fast and storage-efficient geospatial database for OpenStreetMap data.

## Why GeoDesk?

- **Small storage footprint** &mdash; GeoDesk's GOL files are only 20% to 50% larger than the original OSM data in PBF format &mdash; that's less than a tenth of the storage consumed by a traditional SQL-based database.

- **Fast queries** &mdash; typically 50 times faster than SQL. 

- **Fast to get started** &mdash; Converting `.osm.pbf` data to a GOL is 20 times faster than an import into an SQL database. Alternatively, download pre-made data tiles for the just the regions you need and automatically assemble them into a GOL.

- **Intuitive API** &mdash; No need for object-relational mapping, GeoDesk queries return `Node`, `Way` and `Relation` objects.
 
- **Proper handling of relations** &mdash; Traditional geospatial databases deal with geometric shapes and require workarounds to support this unique and powerful aspect of OSM data.

- **Seamless integration with the Java Topolgy Suite (JTS)** for advanced geometric operations, such as buffer, union, simplify, convex and concave hulls, Voronoi diagrams, and much more.

- **Modest hardware requirements** &mdash; If it can run a 64-bit JVM, it'll run GeoDesk.
 
## Get started

Include this dependency in your project's `pom.xml`:

```xml
<dependency>
    <groupId>com.geodesk</groupId>
    <artifactId>geodesk</artifactId>
    <version>0.1.0</version>
</dependency>
```

