import metadata_record_configs

from flask import Flask, Response

from bas_metadata_library.standards.iso_19115_v1 import MetadataRecordConfig as ISO19115MetadataRecordConfig, \
    MetadataRecord as ISO19115MetadataRecord


def create_app():
    app = Flask(__name__)

    @app.route('/standards/iso-19115/<configuration>')
    def standard_iso_19115(configuration: str):
        if configuration == 'uk-pdc-candidate':
            configuration_object = metadata_record_configs.iso19115_v1_gemini_v2_3_uk_pdc_candidate
        else:
            return KeyError('Invalid configuration, valid options: [uk-pdc-candidate]')

        configuration = ISO19115MetadataRecordConfig(**configuration_object)
        record = ISO19115MetadataRecord(configuration)

        return Response(record.generate_xml_document(), mimetype='text/xml')

    return app
