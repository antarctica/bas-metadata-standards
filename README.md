# BAS Metadata Standards

[This website](https://metadata-standards.data.bas.ac.uk) documents the metadata standards used by the
[British Antarctic Survey](https://www.bas.ac.uk) (BAS), and the [UK Polar Data Centre](https://www.bas.ac.uk/pdc)
(PDC), for producing discovery level metadata.

Decisions on which standards to use, and how to use them consistently, are managed and discussed through this project's
[Issue Tracker](#issue-tracking) [Internal].

The remainder of this README relates to managing the website for this project.

## Usage

**Note:** You will need a [Local Development Environment](#local-development-environment) to perform these tasks.

### Adding a new standard

1. create a new page for the standard in `/site/_standard/`
1. in the front matter for this page, add the page to the standards drop down menu [1]
1. link to the new standard from the site index (`/site/index.md`)

[1]

```markdown
---
title: Foo Standard
menus:
  standards:
    weight: 5
---
```

Where the weight option, and the weight option of existing standards pages, should be set to create an alphabetical list.

### Adding a new profile

1. create a new page for the profile in `/site/_profile/`
1. in the front matter for this page, add the page to the profiles drop down menu [1]
1. link to the new profile from the site index (`/site/index.md`)

[1]

```markdown
---
title: Foo Profile
menus:
  profiles:
    weight: 5
---
```

Where the weight option, and the weight option of existing profiles pages, should be set to create an alphabetical list.

## Implementation

This website uses [Jekyll](https://jekyllrb.com) as a framework to produce a static website hosted using AWS S3 and
Cloudfront. The [BAS Style Kit Jekyll Theme](https://style-kit.web.bas.ac.uk/start/introduction/#jekyll) is used to
provide common styling and page templates.

## Setup

### Terraform

Terraform resources are defined in [`provisioning/terraform/`](/provisioning/terraform/).

[Terraform](https://terraform.io) is used for configuring two static sites (testing/production) using AWS S3,
CloudFront and the Amazon Certificate Manager (for HTTPS).


Access to the [BAS AWS account](https://gitlab.data.bas.ac.uk/WSF/bas-aws) is required to provision these resources.
Docker and Docker Compose are recommended for running Terraform.

```shell
$ cd provisioning/terraform
$ docker-compose run terraform

$ terraform init
$ terraform validate
$ terraform fmt

$ terraform apply

$ exit
$ docker-compose down
```

#### Terraform remote state

State information for this project is stored remotely using a
[Backend](https://www.terraform.io/docs/backends/index.html).

Specifically the [AWS S3](https://www.terraform.io/docs/backends/types/s3.html) backend as part of the
[BAS Terraform Remote State](https://gitlab.data.bas.ac.uk/WSF/terraform-remote-state) project.

Remote state storage will be automatically initialised when running `terraform init`. Any changes to remote state will
be automatically saved to the remote backend, there is no need to push or pull changes.

##### Remote state authentication

Permission to read and/or write remote state information for this project is restricted to authorised users. Contact
the [BAS Web & Applications Team](mailto:servicedesk@bas.ac.uk) to request access.

See the [BAS Terraform Remote State](https://gitlab.data.bas.ac.uk/WSF/terraform-remote-state) project for how these
permissions to remote state are enforced.

## Development

### Local development environment

To create a local development environment:

1. checkout project [1]
2. from within project, pull or build Docker image for the static site [2]

[1]

```shell
# If you have access to gitlab.data.bas.ac.uk
$ git clone https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards.git
# Otherwise you can checkout a read only copy
https://github.com/antarctica/bas-metadata-standards.git
```

[2]

```shell
# If you have access to gitlab.data.bas.ac.uk
$ docker login docker-registry.data.bas.ac.uk
$ docker compose pull
# If you don't have access
$ docker compose build
```

### Build Jekyll site locally

To test changes from a local development environment using the Jekyll development server:

```shell
$ docker compose up
```

Then visit http://localhost:9000.

Jekyll will automatically regenerate the static site as source files are changed.

To stop the development server:

```shell
# quit the running container using [ctrl] + c
$ docker compose down
```

## Deployment

### Continuous Deployment

A Continuous Deployment process using GitLab's CI/CD platform is configured in `.gitlab-ci.yml`. This will:

* build the Jekyll site
* publish this build to the relevant AWS S3 bucket (testing or production)

Commits to the `main` branch will be published to the testing site:
[metadata-standards-testing.data.bas.ac.uk](https://metadata-standards-testing.data.bas.ac.uk).

Tagged commits will be published to the production site:
[metadata-standards.data.bas.ac.uk](https://metadata-standards.data.bas.ac.uk).

## Release procedure

### At release

1. create a `release` branch
2. close release in `CHANGELOG.md`
3. push changes, merge the `release` branch into `main` and tag with version

The project will be built and published automatically through [Continuous Deployment](#continuous-deployment).

## Issue tracking

This project uses issue tracking, both for managing this website, and discussions on how metadata standards should be
used. See the [issue tracker](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/issues)
[Internal] for more information.

**Note**: Read & write access to this issue tracker is restricted. Contact the project maintainer to request access.

## License

Copyright (c) 2018-2022 UK Research and Innovation (UKRI), British Antarctic Survey (BAS).

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
