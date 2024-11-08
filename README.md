# BAS Metadata Standards

Management, documentation, and resources for, standards used by the [British Antarctic Survey](https://www.bas.ac.uk) 
(BAS), and the [UK Polar Data Centre](https://www.bas.ac.uk/pdc) (PDC), for producing metadata records.

## Overview

**Note:** This project is focused on needs within the British Antarctic Survey. It has been open-sourced in case it is
of interest to others. Some resources, indicated with a '🛡' or '🔒' symbol, can only be accessed by BAS staff or
project members respectively. Contact the [Project Maintainer](#project-maintainer) to request access.

This project aims to promote alignment and best practice across BAS for producing consistent, high quality metadata.

It consists project consists of:

- an [Issue Tracker 🛡️](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/-/issues),
  used to discuss and agree the use of metadata standards, profiles and the development of any associated resources
- a [Documentation Website](https://metadata-standards.data.bas.ac.uk), providing high level information about these
  standards, profiles and resources
- hosting for associated resources which aid in the implementation of standards and profiles, such as JSON schemas, 
  XML stylesheets, sample files, etc

### Scope

This project is primarily focused on discover level metadata to aid users in finding and evaluating BAS information 
holdings. Metadata for other use-cases may be managed by this project as well on a case by case basis.

## Resources

### Local media types

**Note:** See the [Documentation Website](https://metadata-standards.data.bas.ac.uk/resources/media-types) for why 
these media types exist.

Local media types (MIME types) should be defined in [`resources/media-types/`](/resources/media-types/) in the form:
`{media type name}/{media subtype name}/index.html`, e.g. `resources/media-types/application/foo/index.html`.

**Note:** If registering a media type outside of the established IANA top-level types (application, text, etc.), prefix 
it with `x-`. E.g. `resources/media-types/x-foo/bar/index.html`.

Each `index.html` file should:

- resemble a text file by wrapping content in a `<pre>` element
- include a common preamble [1]
- define the local media type using a template based on those used in the 
  [IANA media types registry](https://www.iana.org/assignments/media-types/media-types.xhtml)

**Note:** IANA registrations are known to be inconsistent over time. Our local registrations can similarly vary based
on need (for example the `x-service` series are more minimal).

Once added, media types should be listed in the 
[Documentation Website](https://metadata-standards.data.bas.ac.uk/resources/media-types).

[1] Common preamble for local media types:

```
This file represents a local media-type registration for use within the British Antarctic Survey (BAS).

It is not an official IANA media type as defined by: https://www.iana.org/assignments/media-types/media-types.xhtml

For more information see: https://metadata-standards.data.bas.ac.uk/resources/media-types#local-media-types

A pseudo media-type template follows.

----
```

### XML stylesheets

Any XML stylesheets should be defined in [`resources/xml-stylesheets/`](/resources/xml-stylesheets/) within a directory.

**Note:** Browsers don't support loading stylesheets across origins. Therefore stylesheets will likely need to be
copied to the origin the XML document will be served from, or reversed proxied to appear as though it is.

## Implementation

### Documentation website

The [Documentation Website](https://metadata-standards.data.bas.ac.uk) uses [GitBook](https://www.gitbook.com), 
managed under the MAGIC account.

[GitBook Site 🔒](https://app.gitbook.com/o/-MbhSFJ1AEZxhIfX9tgr/sites/site_lZkoI).

The site configured with a custom URL, via a DNS record managed by [Terraform](#terraform), and styled to align with 
the [BAS Style Kit](https://style-kit.web.bas.ac.uk) to the extent possible.

### Resources hosting

Resources can be remotely hosted via S3. Separate buckets are provided for testing and production:

- Testing: [metadata-resources-testing.data.bas.ac.uk](https://metadata-resources-testing.data.bas.ac.uk)
- Production: [metadata-resources.data.bas.ac.uk](https://metadata-resources.data.bas.ac.uk)

All items within these buckets are accessible publicly. All AWS resources are managed by [Terraform](#terraform).

## Setup

### Terraform

[Terraform](https://terraform.io) resources are defined in [`provisioning/terraform/`](/provisioning/terraform/).

Access to the [BAS AWS account 🛡️](https://gitlab.data.bas.ac.uk/WSF/bas-aws) is required to provision these resources.
Docker and Docker Compose are recommended but not required for running Terraform.

```shell
$ cd provisioning/terraform
$ docker compose run terraform

$ terraform init
$ terraform ...
```

#### Terraform remote state

State information for this project is stored remotely using a
[Backend](https://www.terraform.io/docs/backends/index.html).

Specifically the [AWS S3](https://www.terraform.io/docs/backends/types/s3.html) backend as part of the
[BAS Terraform Remote State 🛡️](https://gitlab.data.bas.ac.uk/WSF/terraform-remote-state) project.

Remote state storage will be automatically initialised when running `terraform init`. Any changes to remote state will
be automatically saved to the remote backend, there is no need to push or pull changes.

##### Remote state authentication

Permission to read and/or write remote state information for this project is restricted to authorised users. Contact
the [BAS Web & Applications Team](mailto:servicedesk@bas.ac.uk) to request access.

See the [BAS Terraform Remote State 🛡️](https://gitlab.data.bas.ac.uk/WSF/terraform-remote-state) project for how these
permissions to remote state are enforced.

## Deployment

[Resources](#resources) managed directly by this project (i.e. within [`/resources`](#resources)) are synced to S3 
using [Continuous Deployment](#continuous-deployment). External resources will need to provision an IAM user with 
suitable permissions to contribute content.

### Continuous Deployment

A Continuous Deployment process using GitLab's CI/CD platform is configured in [`.gitlab-ci.yml`](/.gitlab-ci.yml). 

## Project maintainer

British Antarctic Survey ([BAS](https://www.bas.ac.uk)) Mapping and Geographic Information Centre
([MAGIC](https://www.bas.ac.uk/teams/magic)). Contact [magic@bas.ac.uk](mailto:magic@bas.ac.uk).

The project lead is [@felnne](https://www.bas.ac.uk/profile/felnne).

## License

Copyright (c) 2018-2024 UK Research and Innovation (UKRI), British Antarctic Survey (BAS).

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
