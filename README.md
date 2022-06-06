<img src="https://docs.geodesk.com/logo2.png#gh-light-mode-only" width="30%">

GeoDesk is a fast and storage-efficient geospatial database for OpenStreetMap data.

## Why GeoDesk?

- **Small storage footprint** &mdash; GeoDesk's GOL files are only 20% to 50% larger than the original OSM data in PBF format &mdash; that's less than a tenth of the storage consumed by a traditional SQL-based database.

- **Fast queries** &mdash; typically 50 times faster than SQL. 

- **Fast to get started** &mdash; Converting `.osm.pbf` data to a GOL is 20 times faster than an import into an SQL database. Alternatively, download pre-made data tiles for just the regions you need and automatically assemble them into a GOL.

- **Intuitive API** &mdash; No need for object-relational mapping; GeoDesk queries return `Node`, `Way` and `Relation` objects.
 
- **Proper handling of relations** &mdash; Traditional geospatial databases deal with geometric shapes and require workarounds to support this unique and powerful aspect of OSM data.

- **Seamless integration with the Java Topolgy Suite (JTS)** for advanced geometric operations, such as buffer, union, simplify, convex and concave hulls, Voronoi diagrams, and much more.

- **Modest hardware requirements** &mdash; If it can run a 64-bit JVM, it'll run GeoDesk.
 
## Get started

## Maven

Include this dependency in your project's `pom.xml`:

```xml
<dependency>
    <groupId>com.geodesk</groupId>
    <artifactId>geodesk</artifactId>
    <version>0.1.0</version>
</dependency>
```

## Example Application

```java
import com.geodesk.feature.*;
import com.geodesk.util.*;

public class PubsExample
{
    public public static void main(String[] args)
    {
        FeatureLibrary library = new FeatureLibrary(     // 1    
            "example.gol",                               // 2
            "https://data.geodesk.com/switzerland");     // 3
        
        for(Feature pub: library                         // 4
            .select("na[amenity=pub]")                   // 5
            .in(Box.ofWSEN(8.53,47.36,8.55,47.38)))      // 6
        {
            System.out.println(pub.stringValue("name")); // 7
        }
        
        library.close();                                 // 8
    }
}
```

What's going on here?

1. We're opening a feature library ...

2. ... with the file name `example.gol` (If it doesn't exist, a blank one is created)

3. ... and a URL from which data tiles will be downloaded

4. We iterate through all the features ...

5. ... that are pubs ([query language](https://docs.geodesk.com/goql))

6. ... in downtown Zurich (bounding box with West/South/East/North coordinates)

7. We print the name of each pub

8. We close the library.

That's it, you've created your first GeoDesk application! 