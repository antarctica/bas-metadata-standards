'use strict';
/*eslint-env node */

var fs   = require ('fs'),
    path = require('path');

var gulp         = require('gulp'),
    xml          = require('xml2json'),
    pump         = require('pump'),
    inject       = require('gulp-inject-string'),
    rename       = require('gulp-rename');

const config = {
  'sources': {
    'source': path.join('.', 'src'),
    'data': path.join('.', 'data')
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

gulp.task('test--load-record', loadRecordTest);

gulp.task('build', gulp.parallel(
  'build--styled-record-iso-rubric',
  'build--styled-record-iso-html'
));

gulp.task('watch', watchBuild);

// Tasks

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
      rename({suffix: "-rubric"}),
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
