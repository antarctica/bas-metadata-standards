---
title: BAS Metadata Standards
lead: Metadata standards used in BAS and the UK PDC
layout: "bas-style-kit/bsk--standard"
---

This website documents the metadata standards used by the [British Antarctic Survey](https://www.bas.ac.uk) (BAS), and
the [UK Polar Data Centre](https://www.bas.ac.uk/pdc) (PDC), for producing discovery level metadata.

If you have been asked to provide metadata to the PDC as part of a data deposit, please see the
[Creating quality metadata for research data](https://www.bas.ac.uk/data/uk-pdc/metadata-guidance/){:.bsk-alert-link}
page on the BAS website instead.
{:.bsk-alert.bsk-alert-solid.bsk-alert-info}

If you would like to access BAS / UK PDC discovery metadata, please see the [BAS Data Catalogue](https://data.bas.ac.uk),
(which is being redeveloped).
{:.bsk-alert.bsk-alert-highlight.bsk-alert-info}

This website forms part of a wider metadata standards improvement project within BAS and UK-PDC.

This wider project is a collaboration between:

* the [BAS Archives Service](https://www.bas.ac.uk/team/business-teams/information-services/archives/)
* the [BAS Mapping and Geographic Information Centre](https://bas.ac.uk/teams/magic) (MAGIC)
* the [UK Polar Data Centre](https://www.bas.ac.uk/team/business-teams/information-services/uk-polar-data-centre/) (PDC)

The broad aims of this project are:

* to increase the breadth and depth of metadata, to include resources from across BAS
* to improve our adherence with metadata standards, through guidance and more robust validation
* to improve the consistency of our metadata, though profiles and guidance drawn from collective discussions

In addition to recording this guidance, and general information on our use of standards and profiles, this website
provides a canonical location for long-lived resources, such as validation schemas.

## Metadata standards and profiles

Standards and profiles currently used by BAS and the UK PDC for discovery metadata:

| Standard/Profile                              | Type                          | Based On                   | Encoding  | Description                                                                                           |
| --------------------------------------------- | ----------------------------- | -------------------------- | --------- | ----------------------------------------------------------------------------------------------------- |
| [ISO 19115:2003](/standard/iso-19115-19139)   | Standard (abstract)           | None                       | N/A       | Conceptual model for describing geographic information                                                |
| [ISO 19115-2:2009](/standard/iso-19115-19139) | Standard Extension (abstract) | ISO 19115:2003             | N/A       | Extensions to ISO 19115:2003 conceptual model to describe acquisition and processing related concepts |
| [ISO 19139:2007](/standard/iso-19115-19139)   | Standard (encoding)           | ISO 19115:2003             | XML       | Encodes the conceptual model defined by ISO 19115:2003 using XML                                      |
| [ISO 19139-2:2012](/standard/iso-19115-19139) | Standard Extension (encoding) | ISO 19115-2:2009           | XML       | Encodes the conceptual model defined by ISO 19115-2:2009 using XML                                    |
{: .bsk-table .bsk-table-responsive }

Standards and profiles currently used by BAS and the UK PDC for exchanging route information:

| Standard/Profile                                    | Type                                        | Based On       | Encoding  | Description                                                                                                                  |
| --------------------------------------------------- | ------------------------------------------- | -------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [IEC 61174:2015 (RTZ 1.0)](/standard/iec-61174)     | Standard (abstract &amp; encoding)          | None           | XML       | Conceptual model and encodings for Route Plan Exchange (RTZ) files used in marine navigation and electronic charting systems |
| [IEC PAS 61174:2021 (RTZ 1.2)](/standard/iec-61174) | Standard Revision (abstract &amp; encoding) | IEC 61174:2015 | XML       | Revisions and improvements to IEC 61174:2015 including extensions support                                                    |
{: .bsk-table .bsk-table-responsive }

Other standards and profiles, either previously used by BAS and the UK PDC, or that are under consideration for use:

| Standard/Profile                              | Type                | Based On                                                  | Version        | Encoding  | Description                                                                                             | Status                                       |
| --------------------------------------------- | ------------------- | --------------------------------------------------------- | -------------- | --------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [ISO 19115-1:2014](/standard/iso-19115-19139) | Standard (abstract) | None                                                      | -              | N/A       | Conceptual model for describing geographic information                                                  | **Planned**{:.bsk-label.bsk-label-info}      |
| [ISO 19115-2:2019](/standard/iso-19115-19139) | Standard (abstract) | ISO 19115-1:2014                                          | -              | N/A       | Extensions to ISO 19115-1:2014 conceptual model to describe acquisition and processing related concepts | **Planned**{:.bsk-label.bsk-label-info}      |
| [ISO 19139-1:2019](/standard/iso-19115-19139) | Standard (encoding) | None                                                      | -              | XML       | XML encoding rules for conceptual models used for geographic resources                                  | **Planned**{:.bsk-label.bsk-label-info}      |
| [ISO 19139-3:2016](/standard/iso-19115-19139) | Standard (encoding) | ISO 19115-1:2014, ISO 19115-2:2019 &amp; ISO 19139-1:2019 | -              | XML       | Integrated XML encoding for ISO 19115 and ISO 19139 standards/encodings                                 | **Planned**{:.bsk-label.bsk-label-info}      |
| [EU INSPIRE](/profile/inspire)                | Profile             | ISO 19139-2:2009                                          | 1.3            | XML       | Common standard for a common spatial data infrastructure across Europe                                  | **Suspended**{:.bsk-label.bsk-label-warning} |
| [UK GEMINI](/profile/gemini)                  | Profile             | EU INSPIRE                                                | 2.3            | XML       | UK national implementation of INSPIRE                                                                   | **Abandoned**{:.bsk-label.bsk-label-danger}  |
| [UK MEDIN](/profile/medin)                    | Profile             | UK GEMINI                                                 | 3.1.1          | XML       | Marine specific implementation of GEMINI                                                                | **Abandoned**{:.bsk-label.bsk-label-danger}  |
{: .bsk-table .bsk-table-responsive }
