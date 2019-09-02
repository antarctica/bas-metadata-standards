# UK Polar Data Centre (UK-PDC) Metadata Records - Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
