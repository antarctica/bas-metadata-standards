# BAS Metadata Standards

Management, documentation, and resources for, metadata standards used by the 
[British Antarctic Survey](https://www.bas.ac.uk) and [UK Polar Data Centre](https://www.bas.ac.uk/data/uk-pdc/).

## Overview

This project aims to promote alignment and best practice across teams within BAS for producing consistent and 
high-quality metadata.

It consists of:

- an [Issue Tracker 🛡️](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/-/issues),
  used to discuss and agree the use of metadata standards, profiles and the development of any associated resources
- a [Documentation Website](https://metadata-standards.data.bas.ac.uk), providing high-level information about these
  standards, profiles and resources
- a [Resources Website](https://metadata-resources.data.bas.ac.uk) for supporting resources to implement standards and 
  profiles, including JSON schemas, XML stylesheets, sample files, etc.

> [!NOTE]
> This project is focused on needs within the British Antarctic Survey. It has been open-sourced in case parts are of
> interest to others. Some resources, indicated with a '🛡' or '🔒' symbol, can only be accessed by BAS staff or
> project members respectively. Contact the [Project Maintainer](#project-maintainer) to request access.

## Resources

### Local licences

> [!NOTE]
> See the [Documentation Website](https://metadata-standards.data.bas.ac.uk/resources/licences) for existing licences
> and why they exist.

To add new licences:

- define the licence in `resources/licences/` in the form: `{licence}/index.html`
- wrap content in a `<pre>` element to resemble a text file
- reference the licence in `site/src/pages/resources/licences.md`

### Local media types

> [!NOTE]
> See the [Documentation Website](https://metadata-standards.data.bas.ac.uk/resources/media-types) for existing 
> media types and why they exist.

To add new media types:

- define the media type in `resources/media-types/` in the form: `{media-type}/{media-subtype}index.html`
- reference the licence in `site/src/pages/resources/media-types.md`

> [!NOTE]
> If registering a media type outside the established IANA top-level types (application, text, etc.), prefix it with 
> `x-`. E.g. `resources/media-types/x-service/foo/index.html`.

Each `index.html` file should:

- wrap content in a `<pre>` element to resemble a text file
- include a common preamble [1]
- define the local media type using a template based on those used in the 
  [IANA media types registry](https://www.iana.org/assignments/media-types/media-types.xhtml)

> [!NOTE]
> IANA registrations are known to be inconsistent over time. Our local registrations can similarly vary based on need 
> (for example the `x-service` series are more minimal).

[1] Common preamble for local media types:

```
This file represents a local media-type registration for use within the British Antarctic Survey (BAS).

It is not an official IANA media type as defined by: https://www.iana.org/assignments/media-types/media-types.xhtml

For more information see: https://metadata-standards.data.bas.ac.uk/resources/media-types#local-media-types

A pseudo media-type template follows.

----
```

### XML stylesheets

Any XML stylesheets should be defined in `resources/xml-stylesheets/` within a directory.

> [!NOTE]
> Browsers don't support loading stylesheets across origins. Therefore stylesheets will likely need to be copied to the 
> origin the XML document will be served from, or reversed proxied to appear as though it is.

## Implementation

### Documentation website

The [Documentation Website](https://metadata-standards.data.bas.ac.uk) uses a [Flask](https://flask.palletsprojects.com) 
based static site generator, with content written in Markdown.

Content stored in `site/src/pages/` is built to `site/build` by the `site/src/build.py` script which uses:

- [Frozen-Flask](https://frozen-flask.readthedocs.io/en/latest/) to capture a Flask site as static HTML
- [Flask file routes](https://github.com/hyperflask/flask-file-routes) within this app to render Markdown files as HTML
- [pytailwindcss](https://github.com/timonweb/pytailwindcss) to generate Tailwind CSS styles
- a simple method to copy other static assets (favicons, etc.)

To build a preview the documentation site locally:

```
% cd site/
% uv run python src/build.py
% uv run python -m http.server 9000 --directory build
```

To debug the underlying Flask app locally:

```
% uv run flask --app src/app.py run --port 9000
```

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

[Resources](#resources) and the [Documentation Website](#documentation-website) are synced to S3 using 
[Continuous Deployment](#continuous-deployment). Related external projects can contribute their own resources by 
provisioning an IAM user with suitable S3 permissions.

### Continuous Deployment

A Continuous Deployment process using GitLab's CI/CD platform is configured in [`.gitlab-ci.yml`](/.gitlab-ci.yml). 

## Project maintainer

Mapping and Geographic Information Centre ([MAGIC](https://www.bas.ac.uk/teams/magic)), British Antarctic Survey
([BAS](https://www.bas.ac.uk)).

Project lead: [@felnne](https://www.bas.ac.uk/profile/felnne).

## Data protection

A Data Protection Impact Assessment (DPIA) does not apply to this project.

## License

Copyright (c) 2018-2025 UK Research and Innovation (UKRI), British Antarctic Survey (BAS).

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
