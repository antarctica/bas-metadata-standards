---
layout: "layout.html:main"
title: "Media Types | Resources"
---

# Media Types

{% include 'toc.html' %}

[Media types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types) (also known as MIME types) indicate the 
format of a given file or resource artefact, such as application/pdf for a PDF, or image/png for a PNG image.

Media types for common formats are standardised via the 
[IANA media types](https://www.iana.org/assignments/media-types/media-types.xhtml) registry.

Media types are shown:

- in metadata record distribution options, describing the formats a resource can be downloaded as
- in data access systems, when resource artefacts (files) are downloaded

> [!NOTE]
> Typically, these media types will match, however Metadata records MAY use a local media type where additional context 
> can be usefully provided.

## Local media types

A set of local media types are registered for use within BAS to provide additional context, or where no suitable IANA 
media type is available. Wherever possible, local types are based on a broader or closest matching IANA registered type.

> [!NOTE]
> For example the [`application/pdf+geo`](https://metadata-resources-testing.data.bas.ac.uk/media-types/application/pdf+geo) 
> local media type is based on the IANA [`application/pdf`](https://www.iana.org/assignments/media-types/application/pdf) type.

> [!WARNING]
> These local types are intended for use within metadata records included in the BAS Data Catalogue. They may be used by others for other purposes if useful, but may be changed or removed at any time.

| Type                                                                                                                             | Name                        |
|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| [`application/pdf+geo`](https://metadata-resources-testing.data.bas.ac.uk/media-types/application/pdf+geo)                       | Geo-referenced PDF document |
| [`application/geopackage+sqlite3+zip`](https://metadata-resources.data.bas.ac.uk/media-types/application/geopackage+sqlite3+zip) | Zipped GeoPackage           |
| [`application/vnd.shp+zip`](https://metadata-resources.data.bas.ac.uk/media-types/application/vnd.shp+zip)                       | Zipped Shapefile            |

## Local media types (services)

A set of additional [Local Media Types](https://metadata-standards.data.bas.ac.uk/resources/media-types#local-media-types) 
are defined to represent services within distribution options.

> [!WARNING]
> This approach is known bad practice but cannot be fixed until services (and service bindings) can be used within the 
> BAS metadata ecosystem.

| Type                                                                                                                                 | Name                                 |
|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| [`x-service/arcgis+service+feature`](https://metadata-resources.data.bas.ac.uk/media-types/x-service/arcgis+service+feature)         | Esri ArcGIS Feature Service          |
| [`x-service/ogc+api+feature`](https://metadata-resources.data.bas.ac.uk/media-types/x-service/ogc+api+feature/)                      | OGC API Features Service             |
| [`x-service/arcgis+service+tile+vector`](https://metadata-resources.data.bas.ac.uk/media-types/x-service/arcgis+service+tile+vector) | Esri ArcGIS Vector Tile Service      |
| [`x-service/arcgis+layer+feature`](https://metadata-resources.data.bas.ac.uk/media-types/x-service/arcgis+layer+feature)             | Esri ArcGIS Hosted Feature Layer     |
| [`x-service/arcgis+layer+feature+ogc`](https://metadata-resources.data.bas.ac.uk/media-types/x-service/arcgis+layer+feature+ogc/)    | Esri ArcGIS Hosted OGC Feature Layer |
| [`x-service/arcgis+layer+tile+vector`](https://metadata-resources.data.bas.ac.uk/media-types/x-service/arcgis+layer+tile+vector)     | Esri ArcGIS Hosted Vector Tile Layer |
