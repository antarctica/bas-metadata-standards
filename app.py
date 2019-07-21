import os

import metadata_record_configs

from pathlib import Path

from flask import Flask, Response, render_template, url_for
from jinja2 import PrefixLoader, PackageLoader, FileSystemLoader
from flask_frozen import Freezer
# noinspection PyPackageRequirements
# Exempting Bandit security issue (Using Element to parse untrusted XML data is known to be vulnerable to XML attacks)
#
# We don't currently allow untrusted/user-provided XML so this is not a risk
from lxml.etree import PI  # nosec
from bas_metadata_library.standards.iso_19115_v1 import MetadataRecordConfig as ISO19115MetadataRecordConfig, \
    MetadataRecord as ISO19115MetadataRecord
from bas_style_kit_jinja_templates import BskTemplates


freezer = Freezer()


def create_app():
    app = Flask(__name__)

    freezer.init_app(app)
    app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

    app.jinja_loader = PrefixLoader({
        'app': FileSystemLoader('templates'),
        'bas_style_kit': PackageLoader('bas_style_kit_jinja_templates'),
    })
    app.config['bsk_templates'] = BskTemplates()
    app.config['bsk_templates'].site_title = 'BAS Metadata Standards'
    app.config['bsk_templates'].site_description = 'Discovery metadata standards used in BAS and the UK PDC'
    app.config['bsk_templates'].bsk_site_nav_brand_text = 'BAS Metadata Standards'
    app.config['bsk_templates'].bsk_site_development_phase = 'alpha'
    app.config['bsk_templates'].bsk_site_feedback_href = 'mailto:polardatacentre@bas.ac.uk'
    app.config['bsk_templates'].bsk_site_footer_policies_cookies_href = '/legal/cookies'
    app.config['bsk_templates'].bsk_site_footer_policies_copyright_href = '/legal/copyright'
    app.config['bsk_templates'].bsk_site_footer_policies_privacy_href = '/legal/privacy'
    app.config['bsk_templates'].bsk_site_nav_primary.append({'value': 'About', 'href': '/about'})

    @app.route('/')
    def index():
        return render_template('app/index.j2')

    @app.route('/about/')
    def about():
        return render_template('app/about.j2')

    @app.route('/legal/cookies/')
    def legal_cookies():
        return render_template('app/legal-cookies.j2')

    @app.route('/legal/copyright/')
    def legal_copyright():
        return render_template('app/legal-copyright.j2')

    @app.route('/legal/privacy/')
    def legal_privacy():
        return render_template('app/legal-privacy.j2')

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
    def freeze_routes():
        return [
            url_for('index'),
            url_for('about'),
            url_for('legal_cookies'),
            url_for('legal_copyright'),
            url_for('legal_privacy'),
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
