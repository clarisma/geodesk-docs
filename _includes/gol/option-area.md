### `-a`, `--area` <code><em>&lt;COORDS&gt;</em></code> | <code><em>&lt;FILE&gt;</em></code> {#option-area}

Defines the (multi)polygon area to which the command should be applied. The following coordinate formats are supported:

- GeoJSON

- WKT

- Raw coordinates in the form `lon_0, lat_0, ... , lon_n, lat_n`. To specify multiple polygons, or a polygon with one or more "holes," place each ring in parentheses. Rings do not need to be closed.

You can specify coordinate values directly, or via a file.


