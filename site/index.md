---
title: BAS Metadata Standards
lead: Metadata standards used in BAS and the UK PDC
---

This website documents the [British Antarctic Survey](https://www.bas.ac.uk) (BAS)'</a> and the
[UK Polar Data Centre](https://www.bas.ac.uk/pdc) (PDC)'s compliance with various metadata standards, profiles and
vocabularies for producing discovery level metadata.

This website is part of the [BAS Metadata Standards](https://github.com/antarctica/bas-metadata-standards) project,
which aims to:

* document the metadata standards and vocabularies used by BAS and the UK PDC
* improve our conformance to these standards and profiles
* provide a location to host local schemas and other long-lived resources related to metadata

If you have been asked to provide metadata to the PDC as part of a data deposit, please see the
[Creating quality metadata for research data](https://www.bas.ac.uk/data/uk-pdc/metadata-guidance/){:.bsk-alert-link}
page in the main BAS website instead.
{:.bsk-alert.bsk-alert-outline.bsk-alert-info}

## Metadata standards and profiles

The standards and profiles currently used by BAS and the UK PDC for discovery metadata are:

| Standard/Profile                              | Type                          | Based On                   | Version (Year) | Format  | Description                                                                                           |
| --------------------------------------------- | ----------------------------- | -------------------------- | -------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| [ISO 19115:2003](/standard/iso-19115)         | Standard (abstract)           | None                       | 1.0 (2003)     | N/A     | Conceptual model for describing geographic information                                                |
| [ISO 19115-2:2009](/standard/iso-19115)       | Standard Extension (abstract) | ISO 19115:2003             | 1.0 (2009)     | N/A     | Extensions to ISO 19115:2003 conceptual model to describe acquisition and processing related concepts |
| [ISO 19139:2007](/standard/iso-19115)         | Standard (encoding)           | ISO 19115:2003             | 1.0 (2007)     | XML     | Encodes the conceptual model defined by ISO 19115:2003 using XML                                      |
| [ISO 19139-2:2012](/standard/iso-19115)       | Standard Extension (encoding) | ISO 19115-2:2009           | 1.0 (2012)     | XML     | Encodes the conceptual model defined by ISO 19115-2:2009 using XML                                    |
| [EU INSPIRE](/profile/inspire)                | Profile                       | ISO 19139-2:2009           | 1.3            | XML     | Common standard for a common spatial data infrastructure across Europe                                |
| [UK PDC Discovery](/profile/uk-pdc-discovery) | Profile                       | ISO 19139-2:2009 (INSPIRE) | 2.0            | XML     | UK PDC specific conventions and requirements                                                          |
{: .bsk-table }

This list previously included the [UK Gemini](https://www.agi.org.uk/gemini/){:.bsk-alert-link} ISO 19115 profile,
however this profile was removed as does not (currently) support ISO 19115-2.
{:.bsk-alert.bsk-alert-highlight.bsk-alert-info}
