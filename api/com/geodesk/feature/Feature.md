---
layout: default
title:  Feature
nav_order: 0
parent: com.geodesk.feature
grand_parent: API Reference
---

<h1><span>Interface</span> Feature</h1>

<div class="classh">
    <div class="class root">
        <span class="package">java.lang.</span>Object
    </div>
    <div class="classh">
        <div class="class leaf">
            <span class="package">com.geodesk.feature.</span>Feature
        </div>
    </div>
</div>

```java
public class FeatureLibrary
extends Object
implements Features<Feature>
```

A Geographic Object Library containing features.

## Constructor Summary

## Method Summary

## Constructor Details

## Method Details

<h3 id="features(java.lang.String)"><code>features</code></h3>

`public Features<?> features(String query)`

Returns a view of this collection that only contains features matching the given query.

| Params:  | `query` - a query in GOQL format    |
| Returns: | a feature collection    |

*Specified by `features` in interface `Features<Feature>`*

