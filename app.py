import os

from pathlib import Path

from flask import Flask, Response, render_template, url_for
from flask_frozen import Freezer
# noinspection PyPackageRequirements
# Exempting Bandit security issue (Using Element to parse untrusted XML data is known to be vulnerable to XML attacks)
#
# We don't currently allow untrusted/user-provided XML so this is not a risk
from lxml.etree import PI  # nosec
from bas_metadata_library.standards.iso_19115_v1 import MetadataRecordConfig as ISO19115MetadataRecordConfig, \
    MetadataRecord as ISO19115MetadataRecord

import metadata_record_configs

freezer = Freezer()


def create_app():
    app = Flask(__name__)
    freezer.init_app(app)

    app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

    @app.route('/')
    def index():
        return render_template('index.j2')

    @app.route('/standards/iso-19115/<configuration>/')
    @app.route('/standards/iso-19115/<configuration>/<stylesheet>/')
    def standard_iso_19115(configuration: str, stylesheet: str = None):
        if configuration == 'uk-pdc-candidate':
            configuration_object = metadata_record_configs.iso19115_v1_gemini_v2_3_uk_pdc_candidate
        else:
            return KeyError('Invalid configuration, valid options: [uk-pdc-candidate]')

        configuration = ISO19115MetadataRecordConfig(**configuration_object)

        record = ISO19115MetadataRecord(configuration)
        if stylesheet is not None:
            if stylesheet == 'iso-html':
                record.record.addprevious(PI(
                    'xml-stylesheet',
                    'type="text/xsl" href="/static/xml-stylesheets/iso-html/xml-to-html-ISO.xsl"'
                ))
            elif stylesheet == 'iso-rubric':
                record.record.addprevious(PI(
                    'xml-stylesheet',
                    'type="text/xsl" href="/static/xml-stylesheets/iso-rubric/isoRubricHTML.xsl"'
                ))

        return Response(record.generate_xml_document(), mimetype='text/xml', content_type='text/xml; charset=utf-8')

    @freezer.register_generator
    def freeze_standard_iso_19115():
        return [
            url_for('index'),
            url_for('standard_iso_19115', configuration='uk-pdc-candidate'),
            url_for('standard_iso_19115', configuration='uk-pdc-candidate', stylesheet='iso-html'),
            url_for('standard_iso_19115', configuration='uk-pdc-candidate', stylesheet='iso-rubric')
        ]

    @app.cli.command('freeze')
    def freeze_app():
        """Build static version of application"""
        freezer.freeze()
        # Rename records as XML as Frozen Flask saves everything as 'index.html'
        os.rename(
            Path('./build/standards/iso-19115/uk-pdc-candidate/index.html'),
            Path('./build/standards/iso-19115/uk-pdc-candidate/uk-pdc-iso-19115-candidate.xml')
        )
        os.rename(
            Path('./build/standards/iso-19115/uk-pdc-candidate/iso-html/index.html'),
            Path('./build/standards/iso-19115/uk-pdc-candidate/iso-html/uk-pdc-iso-19115-candidate-html.xml')
        )
        os.rename(
            Path('./build/standards/iso-19115/uk-pdc-candidate/iso-rubric/index.html'),
            Path('./build/standards/iso-19115/uk-pdc-candidate/iso-rubric/uk-pdc-iso-19115-candidate-rubric.xml')
        )

    return app
