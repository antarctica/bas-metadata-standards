import os

from anytree import Node
from flask_caching import Cache
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import SKOS, RDF

import metadata_record_configs

from pathlib import Path

from flask import Flask, Response, render_template, url_for
# noinspection PyPackageRequirements
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
cache = Cache(config={'CACHE_TYPE': 'simple'})

gcmd_rdf_terms_path = 'vocabularies/gcmd-earth-science.rdf'


def create_app():
    app = Flask(__name__)

    freezer.init_app(app)
    cache.init_app(app)
    app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

    app.jinja_loader = PrefixLoader({
        'app': FileSystemLoader('templates'),
        'bas_style_kit': PackageLoader('bas_style_kit_jinja_templates'),
    })
    app.config['bsk_templates'] = BskTemplates()
    app.config['bsk_templates'].site_styles.append({
        'href': 'https://cdn.web.bas.ac.uk/libs/font-awesome-pro/5.9.0/css/all.min.css'
    })
    app.config['bsk_templates'].site_title = 'BAS Metadata Standards'
    app.config['bsk_templates'].site_description = 'Discovery metadata standards used in BAS and the UK PDC'
    app.config['bsk_templates'].bsk_site_nav_brand_text = 'BAS Metadata Standards'
    app.config['bsk_templates'].bsk_site_development_phase = 'alpha'
    app.config['bsk_templates'].bsk_site_feedback_href = 'mailto:polardatacentre@bas.ac.uk'
    app.config['bsk_templates'].bsk_site_footer_policies_cookies_href = '/legal/cookies'
    app.config['bsk_templates'].bsk_site_footer_policies_copyright_href = '/legal/copyright'
    app.config['bsk_templates'].bsk_site_footer_policies_privacy_href = '/legal/privacy'
    app.config['bsk_templates'].bsk_site_nav_primary.append({'value': 'About', 'href': '/about'})
    app.config['bsk_templates'].bsk_site_nav_primary.append({
        'value': 'Standards',
        'items': [
            {
                'value': 'ISO 19115 (19139)',
                'href': '/standards/iso-19115'
            },
            {
                'value': 'ISO 19115 - EU INSPIRE profile',
                'href': '/standards/iso-19115/profiles/inspire'
            },
            {
                'value': 'ISO 19115 - UK GEMINI profile',
                'href': '/standards/iso-19115/profiles/gemini'
            },
            {
                'value': 'ISO 19115 - UK PDC Discovery profile',
                'href': '/standards/iso-19115/profiles/uk-pdc-discovery'
            }
        ]
    })
    app.config['bsk_templates'].bsk_site_nav_primary.append({
        'value': 'Vocabularies',
        'items': [
            {
                'value': 'ISO 19115',
                'href': '/vocabularies/iso-19115'
            },
            {
                'value': 'INSPIRE',
                'href': '/vocabularies/inspire'
            },
            {
                'value': 'GCMD',
                'href': '/vocabularies/gcmd'
            },
            {
                'value': 'Other',
                'href': '/vocabularies/other'
            }
        ]
    })
    app.config['bsk_templates'].bsk_site_nav_primary.append({
        'value': 'Wiki',
        'href': 'https://gitlab.data.bas.ac.uk/uk-pdc/metadata-infrastructure/metadata-standards/wikis/home'
    })

    @cache.cached(timeout=60, key_prefix='gcmd_metadata')
    def process_gcmd_metadata():
        gcmd_metadata = {
            'name': 'GCMD Earth Science keywords',
            'version': None,
            'revision': None
        }

        scheme = Graph()
        with open(gcmd_rdf_terms_path, "r") as file_input:
            scheme.parse(file_input, format="application/rdf+xml")

            gcmd_ns = Namespace('http://gcmd.gsfc.nasa.gov/kms#')
            scheme.bind("gcmd", gcmd_ns)
            scheme.bind("skos", SKOS)
            scheme.bind("rdf", RDF)

            gcmd_version_predicate = gcmd_ns.keywordVersion
            for t_subject, t_predicate, t_object in scheme.triples((None, gcmd_version_predicate, None)):
                gcmd_metadata['version'] = str(t_object)

            gcmd_revision_predicate = gcmd_ns.schemeVersion
            for t_subject, t_predicate, t_object in scheme.triples((None, gcmd_revision_predicate, None)):
                gcmd_metadata['revision'] = str(t_object)

        return gcmd_metadata

    @cache.cached(timeout=60, key_prefix='gcmd_terms')
    def process_gcmd_terms():
        terms = {}

        scheme = Graph()
        with open(gcmd_rdf_terms_path, "r") as file_input:
            scheme.parse(file_input, format="application/rdf+xml")

            gcmd_ns = Namespace('http://gcmd.gsfc.nasa.gov/kms#')
            scheme.bind("gcmd", gcmd_ns)
            scheme.bind("skos", SKOS)
            scheme.bind("rdf", RDF)

            gcmd_concept_scheme = URIRef(
                'https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/sciencekeywords'
            )
            for t_subject, t_predicate, t_object in scheme.triples((None, SKOS.inScheme, gcmd_concept_scheme)):
                term_id = str(t_subject).replace('https://gcmdservices.gsfc.nasa.gov/kms/concept/', '').replace('/', '')
                terms[term_id] = {
                    'term_id': term_id,
                    'name': None,
                    'aliases': [],
                    'definition': None,
                    'relationships': {
                        'broader': [],
                        'narrower': []
                    },
                    'notes': {
                        'change': []
                    }
                }

            for term_id in terms.keys():
                subject = URIRef(f"https://gcmdservices.gsfc.nasa.gov/kms/concept/{term_id}")
                for t_subject, t_predicate, t_object in scheme.triples((subject, None, None)):
                    if t_predicate == URIRef('http://www.w3.org/2004/02/skos/core#broader'):
                        terms[term_id]['relationships']['broader'].append(
                            str(t_object)
                            .replace('https://gcmdservices.gsfc.nasa.gov/kms/concept/', '')
                            .replace('/', '')
                         )
                    elif t_predicate == URIRef('http://www.w3.org/2004/02/skos/core#narrower'):
                        terms[term_id]['relationships']['narrower'].append(
                            str(t_object)
                            .replace('https://gcmdservices.gsfc.nasa.gov/kms/concept/', '')
                            .replace('/', '')
                         )
                    elif t_predicate == URIRef('http://www.w3.org/2004/02/skos/core#definition'):
                        terms[term_id]['definition'] = str(t_object)
                    elif t_predicate == URIRef('http://www.w3.org/2004/02/skos/core#changeNote'):
                        terms[term_id]['notes']['change'].append(str(t_object))
                    elif t_predicate == URIRef('http://www.w3.org/2004/02/skos/core#prefLabel'):
                        terms[term_id]['name'] = str(t_object)
                    elif t_predicate == URIRef('http://www.w3.org/2004/02/skos/core#altLabel'):
                        terms[term_id]['aliases'].append(str(t_object))

            for term in terms.values():
                if len(term['relationships']['broader']) > 0:
                    for _index, broader_term_id in enumerate(term['relationships']['broader']):
                        if broader_term_id in terms.keys():
                            term['relationships']['broader'][_index] = terms[broader_term_id]
                        else:
                            term['relationships']['broader'].pop(_index)
                if len(term['relationships']['narrower']) > 0:
                    for _index, narrower_term_id in enumerate(term['relationships']['narrower']):
                        if narrower_term_id in terms.keys():
                            term['relationships']['narrower'][_index] = terms[narrower_term_id]
                        else:
                            term['relationships']['narrower'].pop(_index)

        return terms

    @cache.cached(timeout=60, key_prefix='gcmd_term_nodes')
    def process_gcmd_term_nodes():
        terms = process_gcmd_terms()
        term_nodes = {}

        for term in terms.values():
            term_nodes[term['term_id']] = Node(term['name'], aliases=term['aliases'], term_id=term['term_id'])

        for term in terms.values():
            if len(term['relationships']['broader']) == 1:
                if term['relationships']['broader'][0]['term_id'] in term_nodes.keys():
                    term_nodes[term['term_id']].parent = term_nodes[term['relationships']['broader'][0]['term_id']]

        return term_nodes

    def process_ancestors(ancestors):
        ancestor = ancestors[0]
        ancestors.pop(0)

        if len(ancestors) == 0:
            return {
                'ancestor': ancestor
            }

        return {
            'ancestor': ancestor,
            'ancestors': process_ancestors(ancestors)
        }

    @app.route('/')
    def index():
        # noinspection PyUnresolvedReferences
        return render_template('app/index.j2')

    @app.route('/about/')
    def about():
        # noinspection PyUnresolvedReferences
        return render_template('app/about.j2')

    @app.route('/legal/cookies/')
    def legal_cookies():
        # noinspection PyUnresolvedReferences
        return render_template('app/legal-cookies.j2')

    @app.route('/legal/copyright/')
    def legal_copyright():
        # noinspection PyUnresolvedReferences
        return render_template('app/legal-copyright.j2')

    @app.route('/legal/privacy/')
    def legal_privacy():
        # noinspection PyUnresolvedReferences
        return render_template('app/legal-privacy.j2')

    @app.route('/standards/iso-19115/')
    def standard_iso_19115():
        # noinspection PyUnresolvedReferences
        return render_template('app/standards/iso-19115/index.j2')

    @app.route('/standards/iso-19115/profiles/inspire/')
    def standard_iso_19115_profile_inspire():
        # noinspection PyUnresolvedReferences
        return render_template('app/standards/iso-19115/profiles/inspire.j2')

    @app.route('/standards/iso-19115/profiles/gemini/')
    def standard_iso_19115_profile_gemini():
        # noinspection PyUnresolvedReferences
        return render_template('app/standards/iso-19115/profiles/gemini.j2')

    @app.route('/standards/iso-19115/profiles/uk-pdc-discovery/')
    def standard_iso_19115_profile_uk_pdc_discovery():
        # noinspection PyUnresolvedReferences
        return render_template('app/standards/iso-19115/profiles/uk-pdc-discovery.j2')

    @app.route('/records/standards/iso-19115/<configuration>/')
    @app.route('/records/standards/iso-19115/<configuration>/<stylesheet>/')
    @app.route('/records/standards/iso-19115/<configuration>/<stylesheet>/<mode>')
    def records_standard_iso_19115(configuration: str, stylesheet: str = None, mode: str = None):
        if configuration == 'uk-pdc-discovery':
            configuration_object = metadata_record_configs.iso19115_v1_gemini_v2_3_uk_pdc_discovery_sample
        else:
            return KeyError('Invalid configuration, valid options: [uk-pdc-discovery]')

        configuration = ISO19115MetadataRecordConfig(**configuration_object)

        record = ISO19115MetadataRecord(configuration)
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

        if mode == 'inspire-compatible':
            record.record.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation'] = \
                'http://www.isotc211.org/2005/gmd https://inspire.ec.europa.eu/draft-schemas/' \
                'inspire-md-schemas-temp/apiso-inspire/apiso-inspire.xsd'

        return Response(record.generate_xml_document(), mimetype='text/xml', content_type='text/xml; charset=utf-8')

    @app.route('/vocabularies/iso-19115/')
    def vocabulary_iso_19115():
        # noinspection PyUnresolvedReferences
        return render_template('app/vocabularies/iso-19115.j2')

    @app.route('/vocabularies/inspire/')
    def vocabulary_inspire():
        # noinspection PyUnresolvedReferences
        return render_template('app/vocabularies/inspire.j2')

    @app.route('/vocabularies/gcmd/')
    def vocabulary_gcmd():
        vocabularies = {'earth_science': process_gcmd_metadata()}

        # noinspection PyUnresolvedReferences
        return render_template('app/vocabularies/gcmd.j2', vocabularies=vocabularies)

    @app.route('/vocabularies/other/')
    def vocabulary_other():
        # noinspection PyUnresolvedReferences
        return render_template('app/vocabularies/other.j2')

    @app.route('/vocabularies/gcmd/earth-science/terms/<term_id>/')
    def vocabulary_term_gcmd_earth_science(term_id: str):
        terms = process_gcmd_terms()
        term_nodes = process_gcmd_term_nodes()
        vocabulary = process_gcmd_metadata()

        term = terms[term_id]
        term_node = term_nodes[term_id]
        term_ancestors = list(term_node.ancestors)
        term_ancestors.append(term_node)


        term_ancestors_nested = process_ancestors(term_ancestors)

        # noinspection PyUnresolvedReferences
        return render_template(
            'app/vocabulary-terms/gcmd-earth-science.j2',
            term=term,
            term_ancestors=term_ancestors_nested,
            vocabulary=vocabulary
        )

    @freezer.register_generator
    def freeze_routes():
        return [
            url_for('index'),
            url_for('about'),
            url_for('legal_cookies'),
            url_for('legal_copyright'),
            url_for('legal_privacy'),
            url_for('standard_iso_19115'),
            url_for('standard_iso_19115_profile_inspire'),
            url_for('standard_iso_19115_profile_gemini'),
            url_for('standard_iso_19115_profile_uk_pdc_discovery'),
            url_for('records_standard_iso_19115', configuration='uk-pdc-discovery'),
            url_for('records_standard_iso_19115', configuration='uk-pdc-discovery', stylesheet='default',
                    mode='inspire-compatible'),
            url_for('records_standard_iso_19115', configuration='uk-pdc-discovery', stylesheet='iso-html'),
            url_for('records_standard_iso_19115', configuration='uk-pdc-discovery', stylesheet='iso-rubric')
        ]

    @freezer.register_generator
    def vocabulary_term_gcmd_earth_science():
        scheme = Graph()
        with open(gcmd_rdf_terms_path, "r") as file_input:
            scheme.parse(file_input, format="application/rdf+xml")

            gcmd_ns = Namespace('http://gcmd.gsfc.nasa.gov/kms#')
            scheme.bind("gcmd", gcmd_ns)
            scheme.bind("skos", SKOS)
            scheme.bind("rdf", RDF)

            gcmd_concept_scheme = URIRef(
                'https://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/sciencekeywords'
            )
            for t_subject, t_predicate, t_object in scheme.triples((None, SKOS.inScheme, gcmd_concept_scheme)):
                yield {
                    'term_id': str(t_subject)
                    .replace('https://gcmdservices.gsfc.nasa.gov/kms/concept/', '')
                    .replace('/', '')
                }

    @app.cli.command('freeze')
    def freeze_app():
        """Build static version of application"""
        freezer.freeze()
        # Rename records as XML as Frozen Flask saves everything as 'index.html'
        os.rename(
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/index.html'),
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/uk-pdc-iso-19115-discovery.xml')
        )
        os.rename(
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/iso-html/index.html'),
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/iso-html/uk-pdc-iso-19115-discovery-html.xml')
        )
        os.rename(
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/iso-rubric/index.html'),
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/iso-rubric/'
                 'uk-pdc-iso-19115-discovery-rubric.xml')
        )
        os.rename(
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/default/inspire-compatible'),
            Path('./build/records/standards/iso-19115/uk-pdc-discovery/'
                 'uk-pdc-iso-19115-discovery-inspire-compatible.xml')
        )
        os.rmdir('./build/records/standards/iso-19115/uk-pdc-discovery/default')

    return app
