import metadata_record_configs

from flask import Flask, Response, render_template
# noinspection PyPackageRequirements
from lxml.etree import PI

from bas_metadata_library.standards.iso_19115_v1 import MetadataRecordConfig as ISO19115MetadataRecordConfig, \
    MetadataRecord as ISO19115MetadataRecord


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.j2')

    @app.route('/standards/iso-19115/<configuration>')
    @app.route('/standards/iso-19115/<configuration>/<stylesheet>')
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

        return Response(record.generate_xml_document(), mimetype='text/xml')

    return app
