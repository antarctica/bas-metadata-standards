# UK Polar Data Centre (UK PDC) Metadata Records

Discovery metadata standards used in BAS and the UK PDC - 
[metadata-standards.data.bas.ac.uk](https://metadata-standards.data.bas.ac.uk)

## Implementation

A [Flask](http://flask.palletsprojects.com) application is used for generating metadata records for each
[Metadata standard](#metadata-standards) and applying [XML stylesheets](#xml-stylesheets).

See the [development](#development) section for more information.

## Setup

```shell
$ git clone https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards.git
$ cd metadata-schemas
```

#### Local development - Docker Compose

If you have access to the [BAS GitLab instance](https://gitlab.data.bas.ac.uk), you can pull the application Docker 
image from the BAS Docker Registry. Otherwise you will need to build the Docker image locally.

```shell
# If you have access to gitlab.data.bas.ac.uk
$ docker login docker-registry.data.bas.ac.uk
$ docker-compose pull
# If you don't have access
$ docker-compose build
```

Copy `.env.example` to `.env` and edit the file to set at least any required (uncommented) options.

To run the application using the Flask development server (which reloads automatically if source files are changed):

```shell
$ docker-compose up
```

To run other commands against the Flask application (such as [Integration tests](#integration-tests)):

```shell
# in a separate terminal to `docker-compose up`
$ docker-compose run app flask [command]
# E.g.
$ docker-compose run app flask test
# List all available commands
$ docker-compose run app flask
```

## Development

Candidate records in this project are generated with a bundled Flask application. Records for each metadata standard 
are implemented using different libraries:

| Standard/Profile                                               | Type                 | Implemented With                                                       | Notes               |
| -------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------- | ------------------- |
| [ISO 19115](https://www.iso.org/standard/26020.html)           | Standard (abstract)  | *N/A*                                                                  | -                   |
| [ISO 19139](https://www.iso.org/standard/32557.html)           | Standard (concrete)  | [bas-metadata-library](https://pypi.org/project/bas-metadata-library/) | -                   |
| [EU Inspire](https://inspire.ec.europa.eu/about-inspire/563)   | Profile              | [bas-metadata-library](https://pypi.org/project/bas-metadata-library/) | -                   |
| [UK Gemini](https://www.agi.org.uk/gemini/)                    | Profile              | [bas-metadata-library](https://pypi.org/project/bas-metadata-library/) | -                   |
| [DataCite Metadata Standard](https://schema.datacite.org/meta) | Standard (concrete)  | *None*                                                                 | Not yet implemented |
| [Schema.org](https://schema.org)                               | Standard (concrete)  | *None*                                                                 | Not yet implemented |
 
These records are generated dynamically with the option to apply XML stylesheets where relevant.

For ease of distribution a static versions of these dynamically generated records are captured using 
[Frozen Flask](https://github.com/Frozen-Flask/Frozen-Flask). See the [Generating static site](#generating-static-site)
section for more information.
 
### Adding a new standard

To add a new standard:

1. update the inbuilt Flask application in `app.py` with a route for generating candidate records for the new standard
2. add relevant [Integration tests](#integration-tests) with methods to test candidate records are generated correctly

### Generating static site

A custom CLI command, `freeze`, is available for *freezing* the Flask application to a series of static files, written
to a `build/` (Git ignored).

Flask Freeze is configured in the `freeze_routes()` method in `app.py`.

There are some limitations with Flask Freeze:

* all routes need to use a trailing slash [1]
* routes producing non-HTML content needs to be manually corrected [2]
* methods with multiple routes will trigger a `MissingURLGeneratorWarning` warning [3]

[1]

I.e. `@app.route('/legal/privacy')` should be written as `@app.route('/legal/privacy/')`.

Without the route will be saved as a bare file (`/build/legal/privacy`) rather than as an index file 
(`/build/legal/privacy/index.html`).

[2]

I.e. a route producing XML content will still create an `index.html` file rather than `index.xml`. The generated file 
will need to be manually renamed, see the `freeze` custom CLI command for where examples.

**Note:** As the static site for this project is hosted in AWS, which only allows a single index document`, non-HTML
content is renamed more extensively than just to correct the file extension.

[3]

I.e. a route such as:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/standards/iso-19115/<configuration>/')
@app.route('/standards/iso-19115/<configuration>/<stylesheet>/')
def standard_iso_19115(configuration: str, stylesheet: str = None):
    pass
```

Will generate a warning:

```
/usr/local/lib/python3.7/site-packages/flask_frozen/__init__.py:199: MissingURLGeneratorWarning: Nothing frozen for endpoints standard_iso_19115. Did you forget a URL generator?
  return set(page.url for page in self.freeze_yield())
```

This can be safely ignored, as 
[acknowledged](https://github.com/Frozen-Flask/Frozen-Flask/issues/2#issuecomment-1378960) by Flask Freeze project.

### Code Style

PEP-8 style and formatting guidelines must be used for this project, with the exception of the 80 character line limit.

[Flake8](http://flake8.pycqa.org/) is used to ensure compliance, and is ran on each commit through 
[Continuous Integration](#continuous-integration).

To check compliance locally:

```shell
$ docker-compose run app flake8 . --ignore=E501
```

### Dependencies

Python dependencies should be defined using Pip through the `requirements.txt` file. The Docker image is configured to
install these dependencies into the application image for consistency across different environments. Dependencies should
be periodically reviewed and updated as new versions are released.

To add a new dependency:

```shell
$ docker-compose run app ash
$ pip install [dependency]==
# this will display a list of available versions, add the latest to `requirements.txt`
$ exit
$ docker-compose down
$ docker-compose build
```

If you have access to the BAS GitLab instance, push the rebuilt Docker image to the BAS Docker Registry:

```shell
$ docker login docker-registry.data.bas.ac.uk
$ docker-compose push
```

### Dependency vulnerability scanning

To ensure the security of this API, all dependencies are checked against 
[Snyk](https://app.snyk.io/org/antarctica/project/-/history) for vulnerabilities. 

**Warning:** Snyk relies on known vulnerabilities and can't check for issues that are not in it's database. As with all 
security tools, Snyk is an aid for spotting common mistakes, not a guarantee of secure code.

Some vulnerabilities have been ignored in this project, see `.snyk` for definitions and the 
[Dependency exceptions](#dependency-vulnerability-exceptions) section for more information.

Through [Continuous Integration](#continuous-integration), on each commit current dependencies are tested and a snapshot
uploaded to Snyk. This snapshot is then monitored for vulnerabilities.

#### Dependency vulnerability exceptions

This project contains known vulnerabilities that have been ignored for a specific reason.

* [Py-Yaml `yaml.load()` function allows Arbitrary Code Execution](https://snyk.io/vuln/SNYK-PYTHON-PYYAML-42159)
    * currently no known or planned resolution
    * indirect dependency, required through the `bandit` package
    * severity is rated *high*
    * risk judged to be *low* as we don't use the Yaml module in this application
    * ignored for 1 year for re-review

### Static security scanning

To ensure the security of this API, source code is checked against [Bandit](https://github.com/PyCQA/bandit) for issues 
such as not sanitising user inputs or using weak cryptography. 

**Warning:** Bandit is a static analysis tool and can't check for issues that are only be detectable when running the 
application. As with all security tools, Bandit is an aid for spotting common mistakes, not a guarantee of secure code.

Through [Continuous Integration](#continuous-integration), each commit is tested.

To check locally:

```shell
$ docker-compose run app bandit -r .
```

### Debugging

To debug using PyCharm:

* *Run* -> *Edit Configurations*
* *Add New Configuration* -> *Python*

In *Configuration* tab:

* Script path: `[absolute path to project]/manage.py`
* Python interpreter: *Project interpreter* (*app* service in project Docker Compose)
* Working directory: `[absolute path to project]`
* Path mappings: `[absolute path to project]=/usr/src/app`

## Testing

### Integration tests

This project uses integration tests to ensure features work as expected and to guard against regressions and 
vulnerabilities.

The Python [UnitTest](https://docs.python.org/3/library/unittest.html) library is used for running tests using Flask's 
test framework. Test cases are defined in files within `tests/` and are automatically loaded when using the 
`test` Flask CLI command.

Tests are automatically ran on each commit through [Continuous Integration](#continuous-integration).

To run tests manually:

```shell
$ docker-compose run -e FLASK_ENV=testing app flask test --test-runner text
```

To run tests using PyCharm:

* *Run* -> *Edit Configurations*
* *Add New Configuration* -> *Python Tests* -> *Unittests*

In *Configuration* tab:

* Script path: `[absolute path to project]/tests`
* Python interpreter: *Project interpreter* (*app* service in project Docker Compose)
* Working directory: `[absolute path to project]`
* Path mappings: `[absolute path to project]=/usr/src/app`

**Note:** This configuration can be also be used to debug tests (by choosing *debug* instead of *run*).

#### JUnit support

To run integration tests to produce a JUnit compatible file, test-results.xml:

```
$ docker-compose run -e FLASK_ENV=testing app flask test --test-runner junit
```

### Continuous Integration

All commits will trigger a Continuous Integration process using GitLab's CI/CD platform, configured in `.gitlab-ci.yml`.

This process will run the application [Integration tests](#integration-tests).

Pip dependencies are also [checked and monitored for vulnerabilities](#dependency-vulnerability-scanning).

## Deployment

### Continuous Deployment

A Continuous Deployment process using GitLab's CI/CD platform is configured in `.gitlab-ci.yml`. This will:

* build the frozen version of the Flask application
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

## Feedback

The maintainer of this project is the BAS Web & Applications Team, they can be contacted at: 
[servicedesk@bas.ac.uk](mailto:servicedesk@bas.ac.uk).

## Issue tracking

This project uses issue tracking, see the 
[issue tracker](https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/issues) for more 
information.

**Note**: Read & write access to this issue tracker is restricted. Contact the project maintainer to request access.

## License

© Natural Environment Research Council (NERC), 2018-2019, British Antarctic Survey.

You may use and re-use this software and associated documentation files free of charge in any format or medium, under
the terms of the Open Government Licence v3.0.

You may obtain a copy of the Open Government Licence at http://www.nationalarchives.gov.uk/doc/open-government-licence/
