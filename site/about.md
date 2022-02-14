---
title: About
menus:
  site_navigation_primary:
    identifier: about
    weight: 1
---

## Metadata standards and profiles

Metadata *standards* and *profiles* explain how to describe a resource such that it can be understood, unambiguously,
by others.

### Metadata standards, encodings and extensions

* an *abstract metadata standard*, describes a theoretical information model for a standard
* a *metadata standard encoding* describes how to implement an abstract model using, for example, XML
* there are relatively few standards, usually made by international bodies such as ISO
* a *metadata standard extension*, extends the informational model for a standard, typically to cover additional
  concepts
* these extensions have corresponding extensions to standard encodings

### Metadata profiles

* a *metadata profile*, builds upon a metadata standard, typically to standardise how it is used for a particular topic,
  discipline or within an initiative
* they do this in various ways, such as:
  * written guidance/notes
  * restricting how, or which, elements can be used
  * increasing the obligation for elements (e.g. optional to mandatory)

**Note:** Importantly, a profile cannot decrease the obligation for an element (e.g. mandatory to optional). I.e.
profiles can only make things more restrictive, not more permissive.

## Metadata validation

To ensure compliance, metadata standards and profiles typically provide a way to programmatically check records contain:

* any required elements
* any required/controlled element values
* elements in the correct order
* no unexpected or disallowed elements, element values or element structure

Metadata standards typically use XML schemas and schematrons to determine if a record is valid:

* a *schema* checks the structure of elements in a record
* a *schematron* checks specific elements in a record are used in the right way using a series of rules and patterns

Notably a schematron can use conditional logic, e.g. to ensure an element is included if other elements are not.

## Metadata vocabularies and code lists

Metadata *vocabularies* and *code lists* describe lists of controlled terms such that meaning can be expressed and
understood unambiguously and consistently.

A *vocabulary* can take different forms, from simple lists of values to complex linked graphs.

A *code list* is a concept from the [ISO 19115](/standard/iso-19115) standard. It consists of a *code list*, optional *code space* and *code list value* attributes. The code list, is a URI to a list of terms, of which one is selected as the
code list value.

For example, a code list is used to control the types of date in an ISO 19115 record

* the code list for date types is: `https://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/gmxCodelists.xml#CI_DateTypeCode`
* possible code list values for this code list include `creation` or `publication`.
