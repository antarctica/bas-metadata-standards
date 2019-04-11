'use strict';
/*eslint-env node */

var path = require('path');

var gulp         = require('gulp'),
    pump         = require('pump'),
    inject       = require('gulp-inject-string'),
    rename       = require('gulp-rename')

const config = {
  'sources': {
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

function watchBuild(done) {
  gulp.watch(
    path.join(config.sources.data, 'iso-19115', '*.xml'),
    gulp.parallel('build')
  );
  done();
}

