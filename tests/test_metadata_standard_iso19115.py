from http import HTTPStatus

# noinspection PyPackageRequirements
# Exempting Bandit security issue (Using Element to parse untrusted XML data is known to be vulnerable to XML attacks)
#
# We don't currently allow untrusted/user-provided XML so this is not a risk
from lxml.etree import fromstring  # nosec

from tests.test_base import BaseTestCase


class UKPDCDiscoveryMetadataRecordTestCase(BaseTestCase):
    def test_raw_record(self):
        response = self.client.get(
            '/records/standards/iso-19115/uk-pdc-discovery/',
            base_url='http://localhost:9000'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.mimetype, 'text/xml')

        document = fromstring(response.data)
        self.assertIsNotNone(document)

    def test_iso_html_record(self):
        response = self.client.get(
            '/records/standards/iso-19115/uk-pdc-discovery/iso-html/',
            base_url='http://localhost:9000'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.mimetype, 'text/xml')

        document = fromstring(response.data)
        self.assertIsNotNone(document)

    def test_iso_rubric_record(self):
        response = self.client.get(
            '/records/standards/iso-19115/uk-pdc-discovery/iso-rubric/',
            base_url='http://localhost:9000'
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.mimetype, 'text/xml')

        document = fromstring(response.data)
        self.assertIsNotNone(document)
