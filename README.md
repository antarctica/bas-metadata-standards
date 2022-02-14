# UK Polar Data Centre (UK PDC) Metadata Records

Discovery metadata standards used in BAS and the UK PDC -
[metadata-standards.data.bas.ac.uk](https://metadata-standards.data.bas.ac.uk)

## Usage

Note: Create a [Local development environment](#local-development-environment) first.

### Adding a new standard

1. create a new page for the standard in `/site/_standard/`
1. in the page front matter, add the page to the standards drop down menu [1]
1. link to the standard from the site index (`/site/index.md`)

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
1. in the page front matter, add the page to the profiles drop down menu [1]
1. link to the profile from the site index (`/site/index.md`)

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


### Generating static site

To run the application using the Jekyll development server:

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

## Development

### Local development environment

To create a local development environment:

1. checkout project [1]
2. from within project, pull or build Docker image for static site [2]

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
$ docker-compose pull
# If you don't have access
$ docker-compose build
```

## Deployment

### Continuous Deployment

A Continuous Deployment process using GitLab's CI/CD platform is configured in `.gitlab-ci.yml`. This will:

* build the Jekyll site
* publish this build to the relevant static website

This process will deploy changes to
[metadata-standards-testing.data.bas.ac.uk](https://metadata-standards-testing.data.bas.ac.uk) for
all commits to the *master* branch.

This process will deploy changes to [metadata-standards.data.bas.ac.uk](https://metadata-standards.data.bas.ac.uk) for
all tagged commits.

## Release procedure

### At release

1. create a `release` branch
2. close release in `CHANGELOG.md`
3. push changes, merge the `release` branch into `master` and tag with version

The project will be built and published to
[metadata-standards.data.bas.ac.uk](https://metadata-standards.data.bas.ac.uk) automatically through
[Continuous Deployment](#continuous-deployment).

## Issue tracking

This project uses issue tracking, see the
[issue tracker](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/issues) for more
information.

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
