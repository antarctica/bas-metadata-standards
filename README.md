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

© UK Research and Innovation (UKRI), 2018-2021, British Antarctic Survey.

You may use and re-use this software and associated documentation files free of charge in any format or medium, under
the terms of the Open Government Licence v3.0.

You may obtain a copy of the Open Government Licence at http://www.nationalarchives.gov.uk/doc/open-government-licence/
