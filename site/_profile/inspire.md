---
title: EU INSPIRE
menus:
  site_navigation_primary:
    identifier: profiles
    title: Profiles
    weight: 1
  profiles:
    weight: 1
---

The European Union Infrastructure for spatial information in Europe
[(EU INSPIRE)](https://inspire.ec.europa.eu/about-inspire/563) profile builds upon the [ISO 19115](/standards/iso-19115)
standard.

BAS currently implements INSPIRE because it is the basis for the GEMINI profile, which is recommended by the UK
Government. The GEMINI profile itself is not used however because it is not compatible with ISO 19115-2:2009.
{:.bsk-alert.bsk-alert-highlight.bsk-alert-info}

## Vocabularies

The INSPIRE profile defines a number of code lists and vocabularies used for controlling terms such as limitations on
public access types and topic categories.

Code lists for EU INSPIRE:

* [INSPIRE Spatial Data Themes](http://inspire.ec.europa.eu/theme)
* [INSPIRE Limitation On Public Access](http://inspire.ec.europa.eu/metadata-codelist/LimitationsOnPublicAccess/)

## Guidance

* [Inspire Technical Guidance for ISO 19115 (profile)](https://inspire.ec.europa.eu/documents/inspire-metadata-implementing-rules-technical-guidelines-based-en-iso-19115-and-en-iso-1)
* [Inspire Technical Guidance for ISO 19139 (for datasets) (profile)](https://inspire.ec.europa.eu/id/document/tg/metadata-iso19139)

## Validation

* EU INSPIRE:
  * [validation service](http://inspire.ec.europa.eu/validator/about/)

All records should be compliant with these conformance classes:

* [XML encoding of ISO 19115/19119 metadata](http://inspire.ec.europa.eu/id/ats/metadata/1.3/xml-encoding)
* [INSPIRE Profile based on EN ISO 19115 and EN ISO 19119](http://inspire.ec.europa.eu/id/ats/metadata/1.3/iso-19115-19119)

Relevant records should also be compliant with these conformance classes:

* [Metadata for interoperability](http://inspire.ec.europa.eu/id/ats/data/master/interoperability-metadata)

Note that the *Metadata for interoperability* conformance class requires a version for all data format elements. In
cases where this isn't known, INSPIRE does not support the conventional `gco:nilReason` attribute. Therefore it is
acceptable to fail this conformance class.
{:.bsk-alert.bsk-alert-highlight.bsk-alert-info}

When using the INSPIRE validator, change the schema location attribute (`xsi:schemaLocation`) to use an INSPIRE provided
XSD for the `http://www.isotc211.org/2005/gmd` namespace. This is a
[known limitation](https://github.com/inspire-eu-validation/community/issues/37) of the validator.
{:.bsk-alert.bsk-alert-highlight.bsk-alert-info}

E.g. For a record starting:

```xml
<gmi:MI_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd" ... xsi:schemaLocation="http://www.isotc211.org/2005/gmd https://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/gmd/gmd.xsd ...">
```

Use:

```xml
<gmi:MI_Metadata xmlns:gmd="http://www.isotc211.org/2005/gmd" ... xsi:schemaLocation="http://www.isotc211.org/2005/gmd https://inspire.ec.europa.eu/draft-schemas/inspire-md-schemas-temp/apiso-inspire/apiso-inspire.xsd ...">
```
