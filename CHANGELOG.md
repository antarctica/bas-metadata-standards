# UK Polar Data Centre (UK-PDC) Metadata Records - Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* Local media type definition for ArcGIS hosted raster tiles
* Local media type definition for Garmin FPL files
* Local media type definition for GPX files
* MAGIC products local licence v1
* MAGIC Administrative metadata profile v1
* MAGIC Discovery metadata profile v2

## [0.9.0] 2025-12-06

### Changed

* Moving resources site pages within resources directory to prepare for documentation site migration
* Refactoring Terraform resources into a module for static sites
* Migrating documentation site to use a basic Flask based static site generator

## [0.8.1] 2025-03-14

### Changed

* All rights reserved local licence v1 (minor revision)

## [0.8.0] 2025-03-13

### Added

* Local licences
* Operations mapping local licence v1
* All rights reserved local licence v1

## [0.7.0] 2025-02-22

### Added

* Local media type definitions for ArcGIS hosted OGC API Features services

## [0.6.0] 2024-11-08

### Changed [BREAKING!]

* Jekyll static site replaced with GitBook rewrite

### Removed [BREAKING!]

* Outdated example ISO 19115 records

### Added

* Standalone `metadata-resources.data.bas.ac.uk` website setup for related resources (XML stylesheets, etc.)
* Local media type definitions for zipped Shapefiles/GeoPackages and georeferenced PDFs

### Changed

* Project copyright dates updated
* Static site content significantly streamlined and updated
* Managing XML stylesheets as a resource within this project
* Replacing and upgrading Terraform configuration
* Project README rewritten

### Removed

* Old contributing policy

## [0.5.0] 2022-09-20

### Added

* SpatioTemporal Asset Catalogue (STAC) as a new candidate standard
  [#206](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/-/issues/206)
* IEC 61174 (RTZ) as a new standard
  [#192](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/-/issues/192)

### Changed

* Scripts to allow example ISO 19115 records to be updated from configuration files
  [#201](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/-/issues/201)

## [0.4.0] 2022-02-14 [BREAKING!]

### Changed [BREAKING!]

* Re-licencing project under the MIT licence

### Added

* Tools menu (BAS Metadata Library)

### Changed

* Updating project README
* Updating project website (profiles and standards)

## [0.3.0] 2021-06-09

### Changed [BREAKING!]

* Flask application replaced with Jekyll static site
* Sample ISO 19915 record replaced with real world example record

### Removed [BREAKING!]

* Candidate records for DataCite and Schema.org, until these can be introduced properly as supported standards
* GEMINI ISO 19115 profile due to its incompatibility with ISO 19115-2
* Vocabulary information from website, including GCMD keyword term listings
* Link to internal wiki from website

### Changed

* switching copyright holder to UKRI

### Removed

* Synk support

## [0.2.0] 2019-09-02

### Added

* Documentation on vocabularies used
* Documentation for the UK Discovery profile
* Link to project wiki in the project website
* INSPIRE compatible sample record with altered schemaLocation
* Per-standard/profile information pages with links to sample records where relevant
* Updating to BAS metadata generator library 0.2.2
* Fake artefacts for sample records to refer to

### Changed

* Replacing candidate record with new UK PDC Discovery profile
* References to candidate records changed to sample records
* Refactoring about page content into other pages (notably summary of standards moved to home page)
* CD no longer deletes items in S3 buckets it doesn't own, as other projects now publish to them as well

### Removed

* References to DataCite and Schema.org until these are implemented properly

## [0.1.1] 2019-07-22

### Added

* BAS Style Kit styling
* Missing documentation on using Flask Freeze
* Snyk project URL

### Fixed

* Case sensitivity on ISO to HTML stylesheet file (`printTextLines.xsl`)

### Changed

* End user documentation moved from README to static site

## [0.1.0] 2019-07-19

### Added

* Candidate metadata record for ISO 19115, ISO 19139, EU Inspire and UK Gemini
* Candidate metadata record for DataCite metadata standard
* Candidate metadata record for Schema.org
* XML stylesheets applied to ISO 19115 for comparing records against best practices and for viewing by humans
