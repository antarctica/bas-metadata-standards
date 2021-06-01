---
title: UK PDC Discovery
menus:
  profiles:
    weight: 2
---

The *UK PDC Discovery* profile builds upon builds upon the [EU INSPIRE](/profiles/inspire) profile for the
[ISO 19115](/standards/iso-19115) standard.

It defines rules and requirements needed to ensure:

* metadata is useful for discovery through catalogues and portals, such as [data.bas.ac.uk](https://data.bas.ac.uk)
* metadata meets the minimum requirements of other standards, such as DataCite, to allow for effective cross-walks

This metadata profile should be used for all BAS and UK PDC discovery metadata.
{:.bsk-alert.bsk-alert-solid.bsk-alert-info}

Note this profile is still experimental and under development
{:.bsk-alert.bsk-alert-outline.bsk-alert-experimental}

## Example record

* [Raw XML](/static/example-records/ad7d345a-0650-4f44-b7eb-c48e1999086b.xml)
* [XML to HTML stylesheet](/static/example-records/ad7d345a-0650-4f44-b7eb-c48e1999086b-html.xml)
* [ISO rubric stylesheet](/static/example-records/ad7d345a-0650-4f44-b7eb-c48e1999086b-rubric.xml)

## Requirements

1. [Responsible parties - individual or organisational name](#rule-01)
1. [Responsible parties - Individual/Organisational name anchor reference](#rule-02)
1. [Responsible parties - Individual/Organisational name anchor title](#rule-03)
1. [Online resource function](#rule-04)
1. [File identifier](#rule-05)
1. [Character set (metadata)](#rule-06)
1. [Hierarchy level](#rule-07)
1. [Maintenance (metadata)](#rule-08)
1. [Metadata standard (name)](#rule-09)
1. [Metadata standard (version)](#rule-10)
1. [Maintenance (resource)](#rule-11)
1. [Edition](#rule-12)
1. [Lineage statement](#rule-13)
1. [Dates](#rule-14)
1. [Identifier anchor reference](#rule-15)
1. [Identifier anchor title](#rule-16)

### Summary of obligations

| ISO 19115 Element                                                     | INSPIRE Obligation | UK-PDC Discovery Obligation |
| --------------------------------------------------------------------- | ------------------ | --------------------------- |
| Responsible parties - individual or organisational name               | (O) Optional       | (M) Mandatory               |
| Responsible parties - Individual/Organisational name anchor reference | (O) Optional       | (M) Mandatory               |
| Responsible parties - Individual/Organisational name anchor title     | (O) Optional       | (M) Mandatory               |
| Online resource function code                                         | (O) Optional       | (M) Mandatory               |
| File identifier                                                       | (O) Optional       | (M) Mandatory               |
| Character set                                                         | (O) Optional       | (M) Mandatory               |
| Hierarchy level (scope)                                               | (M) Mandatory      | (M) Mandatory               |
| Hierarchy level (name)                                                | (M) Mandatory      | (M) Mandatory               |
| Maintenance (metadata)                                                | (M) Mandatory      | (M) Mandatory               |
| Metadata standard (name)                                              | (M) Mandatory      | (M) Mandatory               |
| Metadata standard (version)                                           | (M) Mandatory      | (M) Mandatory               |
| Maintenance (resource)                                                | (M) Mandatory      | (M) Mandatory               |
| Edition                                                               | (M) Mandatory      | (M) Mandatory               |
| Lineage statement                                                     | (M) Mandatory      | (M) Mandatory               |
| Dates                                                                 | (M) Mandatory      | (M) Mandatory               |
| Identifier anchor reference                                           | (O) Optional       | (M) Mandatory               |
| Identifier anchor title                                               | (O) Optional       | (M) Mandatory               |
{: .bsk-table }

### Responsible parties - individual or organisational name
{: #rule-01 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_ResponsibleParty.html"><code>gmd:CI_ResponsibleParty</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_individualName-1.html"><code>gmd:individualName</code></a>,
        <br />
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_ResponsibleParty.html"><code>gmd:CI_ResponsibleParty</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_organisationName-1.html"><code>gmd:organisationalName</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..2</dd>
</dl>

All responsible parties **MUST** have one or both of these name elements:

* [`gmd:individualName`](http://www.datypic.com/sc/niem21/e-gmd_individualName-1.html)
* [`gmd:organisationalName`](http://www.datypic.com/sc/niem21/e-gmd_organisationName-1.html)

---

### Responsible parties - Individual/Organisational name anchor reference
{: #rule-02 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_ResponsibleParty.html"><code>gmd:CI_ResponsibleParty</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_individualName-1.html"><code>gmd:individualName</code></a>/
            <a href="http://www.datypic.com/sc/niem20/e-gmx_Anchor.html"><code>gmx:Anchor</code></a>[@
            <a href="http://www.datypic.com/sc/niem20/a-niem-xlink_href.html"><code>xlink:href</code></a>],
        <br />
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_ResponsibleParty.html"><code>gmd:CI_ResponsibleParty</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_organisationName-1.html"><code>gmd:organisationalName</code></a>/
        <a href="http://www.datypic.com/sc/niem20/e-gmx_Anchor.html"><code>gmx:Anchor</code></a>[@
        <a href="http://www.datypic.com/sc/niem20/a-niem-xlink_href.html"><code>xlink:href</code></a>]
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All responsible party individual or organisational names **MUST** be an
[`gmx:Anchor`](http://www.datypic.com/sc/niem20/e-gmx_Anchor.html) element, which **SHOULD** contain a
[`xlink:href`](http://www.datypic.com/sc/niem20/a-niem-xlink_href.html) attribute for a suitable remote resource.

---

### Responsible parties - Individual/Organisational name anchor title
{: #rule-03 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_ResponsibleParty.html"><code>gmd:CI_ResponsibleParty</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_individualName-1.html"><code>gmd:individualName</code></a>/
            <a href="http://www.datypic.com/sc/niem20/e-gmx_Anchor.html"><code>gmx:Anchor</code></a>[@
            <a href="http://www.datypic.com/sc/niem20/a-niem-xlink_title.html"><code>xlink:title</code></a>],
        <br />
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_ResponsibleParty.html"><code>gmd:CI_ResponsibleParty</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_organisationName-1.html"><code>gmd:organisationalName</code></a>/
        <a href="http://www.datypic.com/sc/niem20/e-gmx_Anchor.html"><code>gmx:Anchor</code></a>[@
        <a href="http://www.datypic.com/sc/niem20/a-niem-xlink_title.html"><code>xlink:title</code></a>]
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All responsible party individual or organisational names **MUST** be an
[`gmx:Anchor`](http://www.datypic.com/sc/niem20/e-gmx_Anchor.html) element, which **MUST** contain a
[`xlink:title`](http://www.datypic.com/sc/niem20/a-niem-xlink_title.html) attribute. The value of this `xlink:title`
element **MUST** be one of:

| Value   | Meaning                                                                            | Notes                                    |
| ------- | ---------------------------------------------------------------------------------- | ---------------------------------------- |
| `orcid` | [Open Researcher and Contributor Identifier (ORCID) identifier](https://orcid.org) | Recommended identifier for individuals   |
| `ror`   | [Research Organization Registry (ROR) identifier](https://ror.org/)                | Recommended identifier for organisations |
| `isni`  | [International Standard Name Identifier (ISNI)](http://www.isni.org)               | Legacy identifier for organisations      |
{: .bsk-table }

---

### Online resource function
{: #rule-04 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        ../<a href="http://www.datypic.com/sc/niem21/e-gmd_CI_OnlineResource.html"><code>gmd:CI_OnlineResource</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_function-1.html"><code>gmd:function</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_CI_OnLineFunctionCode.html"><code>gmd:CI_OnLineFunctionCode</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All online resources **MUST** have an online function code element.

---

### File identifier
{: #rule-05 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_fileIdentifier-1.html"><code>gmd:fileIdentifier</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a file identifier, the value of which **MUST** be a UUID (version 4).

---

### Character set (metadata)
{: #rule-06 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_characterSet-1.html"><code>gmd:characterSet</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a (metadata) character set, the value of which **MUST** be one of:

* `utf8`

---

### Hierarchy level
{: #rule-07 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_hierarchyLevel-1.html"><code>gmd:hierarchyLevel</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_ScopeCode.html"><code>gmd:MD_ScopeCode</code></a>
        <br />
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_hierarchyLevelName-1.html"><code>gmd:hierarchyLevelName</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a hierarchy level name and scope code, the value of which **MUST** be one of:

* `dataset`

---

### Maintenance (metadata)
{: #rule-08 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_metadataMaintenance-1.html"><code>gmd:metadataMaintenance</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_MaintenanceInformation.html"><code>gmd:MD_MaintenanceInformation</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a (metadata) maintenance element, which **MUST** include these elements:

* [`gmd:maintenanceAndUpdateFrequency`](http://www.datypic.com/sc/niem21/e-gmd_maintenanceAndUpdateFrequency-1.html)
* [`gmd:MD_MaintenanceFrequencyCode`](http://www.datypic.com/sc/niem21/e-gmd_MD_MaintenanceFrequencyCode.html)
* [`gmd:maintenanceNote`](http://www.datypic.com/sc/niem21/e-gmd_maintenanceNote-1.html)
* [`gmd:MD_ProgressCode`](http://www.datypic.com/sc/niem21/e-gmd_MD_ProgressCode.html)

---

### Metadata standard (name)
{: #rule-09 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_metadataStandardName-1.html"><code>gmd:metadataStandardName</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a (metadata) standard name element, the value of which **MUST** be:

> ISO 19115-2 Geographic Information - Metadata - Part 2: Extensions for Imagery and Gridded Data

---

### Metadata standard (version)
{: #rule-10 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_metadataStandardVersion-1.html"><code>gmd:metadataStandardVersion</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a metadata standard version element, the value of which **MUST** be:

> ISO 19115-2:2009(E)

---

### Maintenance (resource)
{: #rule-11 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identificationInfo-1.html"><code>gmd:identificationInfo</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_DataIdentification.html"><code>gmd:MD_DataIdentification</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_resourceMaintenance-1.html"><code>gmd:resourceMaintenance</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_MaintenanceInformation.html"><code>gmd:MD_MaintenanceInformation</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a (resource) maintenance element, which **MUST** include these elements:

* [`gmd:maintenanceAndUpdateFrequency`](http://www.datypic.com/sc/niem21/e-gmd_maintenanceAndUpdateFrequency-1.html)
* [`gmd:MD_MaintenanceFrequencyCode`](http://www.datypic.com/sc/niem21/e-gmd_MD_MaintenanceFrequencyCode.html)
* [`gmd:maintenanceNote`](http://www.datypic.com/sc/niem21/e-gmd_maintenanceNote-1.html)
* [`gmd:MD_ProgressCode`](http://www.datypic.com/sc/niem21/e-gmd_MD_ProgressCode.html)

---

### Edition
{: #rule-12 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identificationInfo-1.html"><code>gmd:identificationInfo</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_DataIdentification.html"><code>gmd:MD_DataIdentification</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_citation-1.html"><code>gmd:citation</code></a>/
        <a href="http://www.datypic.com/sc/niem21/e-gmd_edition-1.html"><code>gmd:edition</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have an edition (version).

---

### Lineage statement
{: #rule-13 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_dataQualityInfo-1.html"><code>gmd:dataQualityInfo</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_DQ_DataQuality.html"><code>gmd:DQ_DataQuality</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_lineage-1.html"><code>gmd:lineage</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_LI_Lineage.html"><code>gmd:LI_Lineage</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_statement-1.html"><code>gmd:statement</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All records **MUST** have a lineage statement.

---

### Dates
{: #rule-14 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identificationInfo-1.html"><code>gmd:identificationInfo</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_DataIdentification.html"><code>gmd:MD_DataIdentification</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_citation-1.html"><code>gmd:citation</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_date-1.html"><code>gmd:date</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_CI_Date.html"><code>gmd:CI_Date</code></a>
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..*</dd>
</dl>

All records **MUST** have a date elements with at least these `dateType` code values:

* `creation`
* `released`

### Identifier anchor reference
{: #rule-15 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identificationInfo-1.html"><code>gmd:identificationInfo</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_DataIdentification.html"><code>gmd:MD_DataIdentification</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_citation-1.html"><code>gmd:citation</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identifier-1.html"><code>gmd:identifier</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_Identifier.html"><code>gmd:MD_Identifier</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_code-1.html"><code>gmd:code</code></a>[@
            <a href="http://www.datypic.com/sc/niem20/a-niem-xlink_href.html"><code>xlink:href</code></a>]
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All record identifier codes **MUST** be a [gmx:Anchor](http://www.datypic.com/sc/niem20/e-gmx_Anchor.html) element,
which **SHOULD** contain a [xlink:href](http://www.datypic.com/sc/niem20/a-niem-xlink_href.html) attribute for a
suitable remote resource..

---

### Identifier anchor title
{: #rule-16 }

<dl class="bsk-dl-lg">
    <dt>ISO element</dt>
    <dd>
        /<a href="https://schemas.isotc211.org/19115/-2/gmi/1.0/gmi/#element_MI_Metadata"><code>gmi:MI_Metadata</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identificationInfo-1.html"><code>gmd:identificationInfo</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_DataIdentification.html"><code>gmd:MD_DataIdentification</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_citation-1.html"><code>gmd:citation</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_identifier-1.html"><code>gmd:identifier</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_MD_Identifier.html"><code>gmd:MD_Identifier</code></a>/
            <a href="http://www.datypic.com/sc/niem21/e-gmd_code-1.html"><code>gmd:code</code></a>[@
            <a href="http://www.datypic.com/sc/niem20/a-niem-xlink_href.html"><code>xlink:title</code></a>]
    </dd>
    <dt><em>UK-PDC Discovery</em> obligation</dt>
    <dd>(M) Mandatory</dd>
    <dt><em>UK-PDC Discovery</em> occurrence</dt>
    <dd>1..1</dd>
</dl>

All record identifier codes **MUST** be a [gmx:Anchor](http://www.datypic.com/sc/niem20/e-gmx_Anchor.html) element,
which **MUST** contain a [xlink:title](http://www.datypic.com/sc/niem20/a-niem-xlink:title.html) attribute.

At least one record identifiers **MUST** have a `xlink:title` value of `self`.

The value of this `xlink:title` element **MUST** be one of:

| Value         | Meaning                                                                    | Obligation | Notes |
| ------------- | -------------------------------------------------------------------------- | ---------- | ----- |
| `self`        | Link to this record in its original data catalogue (i.e. `data.bas.ac.uk`) | Mandatory  | -     |
| `doi`         | Digital Object Identifier (DOI)                                            | Optional   | -     |
| `award`       | Reference to an award or grant related to the record                       | Optional   | -     |
| `publication` | Reference to a publication related to the record                           | Optional   | -     |
{: .bsk-table }

## Validation

Not currently supported.
