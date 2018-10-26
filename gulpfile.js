'use strict';
/*eslint-env node */

var fs   = require ('fs'),
    path = require('path');

var gulp         = require('gulp'),
    pug          = require('gulp-pug'),
    xml          = require('xml2json'),
    pump         = require('pump'),
    data         = require('gulp-data'),
    inject       = require('gulp-inject-string'),
    rename       = require('gulp-rename'),
    request      = require('request');

const config = {
  'sources': {
    'source': path.join('.', 'src'),
    'data': path.join('.', 'data'),
    'html': path.join('.', 'src', 'html')
  },
  'destinations': {
    'root': path.join('.'),
    'public': path.join('.', 'public')
  }
};

// Task definitions
//
// Tasks build from specific to general. It's likely you will want to run the more generic tasks.

gulp.task('build--styled-record-iso-rubric', buildStyledRecordIsoRubric);
gulp.task('build--styled-record-iso-html',  buildStyledRecordIsoHtml);
gulp.task('build--record-example',  buildRecordExample);

gulp.task('test--load-record', loadRecordTest);

gulp.task('build', gulp.parallel(
  'build--styled-record-iso-rubric',
  'build--styled-record-iso-html',
  'build--record-example'
));

gulp.task('watch', watchBuild);

// Tasks

function buildStyledRecordIsoRubric(done) {
  pump(
    [
      gulp.src([
        path.join(config.sources.data, 'iso-pdc-resolved-example-rubric.xml')
      ]),
      inject.after('<?xml version="1.0" encoding="UTF-8"?>', '\n<?xml-stylesheet href="../assets/xml-stylesheets/iso-rubric/isoRubricHTML.xsl" type="text/xsl" media="screen"?>'),
      gulp.dest(path.join(config.destinations.public))
    ],
    done
  );
}

function buildStyledRecordIsoHtml(done) {
  pump(
    [
      gulp.src([
        path.join(config.sources.data, 'iso-19115', '*.xml')
      ]),
      inject.after('<?xml version="1.0" encoding="UTF-8"?>', '\n<?xml-stylesheet href="../assets/xml-stylesheets/iso-html/xml-to-html-ISO.xsl" type="text/xsl" media="screen"?>'),
      rename({suffix: "-html"}),
      gulp.dest(path.join(config.destinations.public))
    ],
    done
  );
}

function buildStyledRecordIsoRubric(done) {
  pump(
    [
      gulp.src([
        path.join(config.sources.data, 'iso-19115', '*.xml')
      ]),
      inject.after('<?xml version="1.0" encoding="UTF-8"?>', '\n<?xml-stylesheet href="../assets/xml-stylesheets/iso-rubric/isoRubricHTML.xsl" type="text/xsl" media="screen"?>'),
        // Lookup values are hard-coded - in the future this would be based be dynamic based on available records
        return prepareRecordData();
      }),
      rename({suffix: "-rubric"}),
      pug(),
      gulp.dest(path.join(config.destinations.public))
    ],
    done
  );
}

function loadRecordTest(done) {
  var recordRaw = fs.readFileSync(path.join(config.sources.data, 'iso-19115', 'uk-pdc-discovery-metadata-record-gemini.xml'));
  var record = xml.toJson(recordRaw);

  console.log(record);

  done();
}

function watchBuild(done) {
  gulp.watch(
    [
      path.join(config.sources.data, 'iso-19115', '*.xml')
    ],
    gulp.parallel('build')
  );
  done();
}

// Processing functions

async function prepareRecordData() {
  var record = await getRecord();
  var doi_citation = await getDoiCitation();

  return {
    'metadata_record': record,
    'metadata_citation': doi_citation
  };
}

function getRecord() {
  // Load record data from XML (hard-coded source for now)
  var recordPath = path.join(config.sources.data, 'iso-pdc-resolved-example.xml');
  
  return new Promise(function(resolve, reject) {
    // Read XML and convert into JSON object, then convert that into a JS object
    var record = fs.readFileSync(recordPath);
    record = xml.toJson(record);
    record = JSON.parse(record);

    resolve(record);
  });
}

function getDoiCitation() {
  // Load DOI citation from CrossRef (hard-coded for now)
  var options = {
    url: 'https://doi.org/10.5285/3cf26ab6-7f47-4868-a87d-c62a2eefea1f',
    headers: {
      'accept': 'text/x-bibliography; style=apa'
    }
  };

  return new Promise(function(resolve, reject) {
    request.get(options, function(err, resp, body) {
      if (err) {
        console.error(err);
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
};
