from datetime import datetime, timezone, date


iso19115_v1_gemini_v2_3_uk_pdc_discovery_sample = {
    'file_identifier': '84340f7c-e4f1-4a01-9309-93f8d115c571',
    'language': 'eng',
    'character_set': 'utf8',
    'hierarchy_level': 'dataset',
    'contacts': [
        {
            'organisation': {
                'name': 'UK Polar Data Centre',
                'href': 'http://isni.org/isni/0000000405983800',
                'title': 'isni'
            },
            'phone': '+44 (0)1223 221400',
            'address': {
                'delivery_point': 'British Antarctic Survey, High Cross, Madingley Road',
                'city': 'Cambridge',
                'administrative_area': 'Cambridgeshire',
                'postal_code': 'CB3 0ET',
                'country': 'United Kingdom'
            },
            'email': 'polardatacentre@bas.ac.uk',
            'online_resource': {
                'href': 'https://www.bas.ac.uk/team/business-teams/information-services/uk-polar-data-centre/',
                'function': 'information'
            },
            'role': ['pointOfContact']
        }
    ],
    'date_stamp': datetime(2019, 8, 17, 14, 51, 30, tzinfo=timezone.utc),
    'maintenance': {
        'maintenance_frequency': 'asNeeded',
        'progress': 'completed'
    },
    'metadata_standard': {
        'name': 'ISO 19115 (UK GEMINI)',
        'version': '1.0 (2.3)'
    },
    'reference_system_info': {
        'code': {
            'value': 'urn:ogc:def:crs:EPSG::4326',
            'href': 'http://www.opengis.net/def/crs/EPSG/0/4326'
        },
        'version': '6.18.3',
        'authority': {
            'title': {
                'value': 'European Petroleum Survey Group (EPSG) Geodetic Parameter Registry'
            },
            'dates': [{
                'date': date(2008, 11, 12),
                'date_type': 'publication'
            }],
            'contact': {
                'organisation': {
                    'name': 'European Petroleum Survey Group'
                },
                'email': 'EPSGadministrator@iogp.org',
                'online_resource': {
                    'href': 'https://www.epsg-registry.org/',
                    'function': 'information'
                },
                'role': ['publisher']
            }
        }
    },
    'resource': {
        'title': {
            'value': 'Atmospheric Ozone measurements at Halley Clean Air Sector Laboratory (CASLab) 2011-2012 '
                     '- BAS Metadata Standards sample record (UK PDC discovery metadata)'
        },
        'abstract': 'This abstract, and the record to which it belongs, is fictitious. This record is a demonstration '
                    'of typical UK Polar Data Centre discovery level metadata. It is part of the BAS Metadata '
                    'Standards project (https://metadata-standards.data.bas.ac.uk), which documents the metadata '
                    'standards used by the British Antarctic Survey (BAS) and UK Polar Data Centre (UK PDC), and how '
                    'these are to be implemented correctly and consistently. This sample record demonstrates the UK '
                    'Polar Data Centre\'s discovery metadata profile, which is implemented on top of the ISO '
                    '19115 / 19139 standards and EU INSPIRE / UK GEMINI profiles. See the BAS Data Catalogue to '
                    'discover real dataset\'s from the British Antarctic Survey and UK Polar Data Centre '
                    '(https://www.data.bas.ac.uk).',
        'dates': [
            {
                'date': date(2012, 1, 1),
                'date_type': 'creation'
            },
            {
                'date': date(2012, 2, 20),
                'date_type': 'revision'
            },
            {
                'date': datetime(2012, 2, 24, 14, 40, 44, tzinfo=timezone.utc),
                'date_type': 'publication'
            },
            {
                'date': datetime(2012, 2, 24, 14, 40, 44, tzinfo=timezone.utc),
                'date_type': 'released'
            }
        ],
        'edition': '2',
        'identifiers': [
            {
                'identifier': 'https://metadata-standards.data.bas.ac.uk/standards/iso-19115/uk-pdc-discovery',
                'href': 'https://metadata-standards.data.bas.ac.uk/standards/iso-19115/uk-pdc-discovery',
                'title': 'self'
            },
            {
                'identifier': 'https://handle.test.datacite.org/10.5285/84340f7c-e4f1-4a01-9309-93f8d115c571',
                'href': 'https://handle.test.datacite.org/10.5285/84340f7c-e4f1-4a01-9309-93f8d115c571',
                'title': 'doi'
            },
            {
                'identifier': 'bas0100032',
                'href': 'https://gtr.ukri.org/projects?ref=bas0100032',
                'title': 'award'
            }
        ],
        'contacts': [
            {
                'individual': {
                    'name': 'Watson, Constance',
                    'href': 'https://sandbox.orcid.org/0000-0001-8373-6934',
                    'title': 'orcid'
                },
                'organisation': {
                    'name': 'British Antarctic Survey'
                },
                'email': 'conwat@bas.ac.uk',
                'online_resource': {
                    'href': 'https://www.bas.ac.uk/profile/conwat',
                    'title': 'BAS staff profile',
                    'description': 'Staff profile for Constance Watson in the British Antarctic Survey public website.',
                    'function': 'information'
                },
                'role': ['author']
            },
            {
                'organisation': {
                    'name': 'UK Polar Data Centre',
                    'href': 'http://isni.org/isni/0000000405983800',
                    'title': 'isni'
                },
                'phone': '+44 (0)1223 221400',
                'address': {
                    'delivery_point': 'British Antarctic Survey, High Cross, Madingley Road',
                    'city': 'Cambridge',
                    'administrative_area': 'Cambridgeshire',
                    'postal_code': 'CB3 0ET',
                    'country': 'United Kingdom'
                },
                'email': 'polardatacentre@bas.ac.uk',
                'online_resource': {
                    'href': 'https://www.bas.ac.uk/team/business-teams/information-services/uk-polar-data-centre/',
                    'function': 'information'
                },
                'role': [
                    'pointOfContact',
                    'custodian',
                    'publisher',
                    'distributor'
                ]
            }
        ],
        'maintenance': {
            'maintenance_frequency': 'asNeeded',
            'progress': 'completed'
        },
        'keywords': [
            {
                'terms': [
                    {
                        'term': 'Atmospheric conditions',
                        'href': 'https://www.eionet.europa.eu/gemet/en/inspire-theme/ac'
                    },
                    {
                        'term': 'Environmental monitoring facilities',
                        'href': 'https://www.eionet.europa.eu/gemet/en/inspire-theme/ef'
                    }
                ],
                'type': 'theme',
                'thesaurus': {
                    'title': {
                        'value': 'General Multilingual Environmental Thesaurus - INSPIRE themes',
                        'href': 'http://www.eionet.europa.eu/gemet/inspire_themes'
                    },
                    'dates': [
                        {
                            'date': date(2018, 8, 16),
                            'date_type': 'publication'
                        }
                    ],
                    'edition': '4.1.2',
                    'contact': {
                        'organisation': {
                            'name': 'European Environment Information and Observation Network (EIONET), '
                                    'European Environment Agency (EEA)'
                        },
                        "email": "helpdesk@eionet.europa.eu",
                        'online_resource': {
                            'href': 'https://www.eionet.europa.eu/gemet/en/themes/',
                            'title': 'General Multilingual Environmental Thesaurus (GEMET) themes',
                            'function': 'information'
                        },
                        'role': ['publisher']
                    },
                }
            },
            {
                'terms': [
                    {
                        'term': 'EARTH SCIENCE > ATMOSPHERE > AIR QUALITY > TROPOSPHERIC OZONE',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/426aee98-764c-4c21-ab65-1e9d4bd6b0d0'
                    },
                    {
                        'term': ' EARTH SCIENCE > ATMOSPHERE > ATMOSPHERIC CHEMISTRY > OXYGEN COMPOUNDS > OZONE',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/dd316647-9043-40c3-9329-f22f9215fefa'
                    }
                ],
                'type': 'theme',
                'thesaurus': {
                    'title': {
                        'value': 'Global Change Master Directory (GCMD) Science Keywords',
                        'href': 'https://earthdata.nasa.gov/about/gcmd/global-change-master-directory-gcmd-keywords'
                    },
                    'dates': [
                        {
                            'date': date(2018, 3, 15),
                            'date_type': 'publication'
                        }
                    ],
                    'edition': '8.6',
                    'contact': {
                        'organisation': {
                            'name': 'Global Change Data Center, Science and Exploration Directorate, Goddard Space '
                                    'Flight Center (GSFC) National Aeronautics and Space Administration (NASA)'
                        },
                        'address': {
                            'city': 'Greenbelt',
                            'administrative_area': 'MD',
                            'country': 'United States of America'
                        },
                        'online_resource': {
                            'href': 'https://earthdata.nasa.gov/about/gcmd/'
                                    'global-change-master-directory-gcmd-keywords',
                            'title': 'Global Change Master Directory (GCMD) Keywords',
                            'description': 'The information provided on this page seeks to define how the GCMD '
                                           'Keywords are structured, used and accessed. It also provides information '
                                           'on how users can participate in the further development of the keywords.',
                            'function': 'information'
                        },
                        'role': ['publisher']
                    },
                }
            }
        ],
        'constraints': {
            'access': [
                {
                    'restriction_code': 'otherRestrictions',
                    'inspire_limitations_on_public_access': 'noLimitations'
                }
            ],
            'usage': [
                {
                    'restriction_code': 'otherRestrictions',
                    'copyright_licence': {
                        'code': 'OGL-UK-3.0',
                        'href': 'http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/',
                        'statement': 'This information is licensed under the Open Government Licence v3.0. To view this'
                                     ' licence, visit http://www.nationalarchives.gov.uk/doc/open-government-licence/'
                    }
                },
                {
                    'restriction_code': 'otherRestrictions',
                    'required_citation': {
                        'statement': 'Cite this information as: "Watson, C. (2012). Atmospheric Ozone measurements at '
                                     'Halley Clean Air Sector Laboratory (CASLab) 2011-2012 - BAS Metadata Standards '
                                     'sample record (UK PDC discovery metadata). UK Polar Data Centre. '
                                     'https://doi.org/10.5285/84340F7C-E4F1-4A01-9309-93F8D115C571"'
                    }
                }
            ]
        },
        'supplemental_information': 'It is recommended that careful attention be paid to the contents of any data, and '
                                    'that the author be contacted with any questions regarding appropriate use. If you '
                                    'find any errors or omissions, please report them to polardatacentre@bas.ac.uk.',
        'spatial_representation_type': 'textTable',
        'spatial_resolution': None,
        'language': 'eng',
        'topics': [
            'environment',
            'climatologyMeteorologyAtmosphere'
        ],
        'extent': {
            'geographic': {
                'bounding_box': {
                    'west_longitude': -26.65,
                    'east_longitude': -26.65,
                    'south_latitude': -75.58,
                    'north_latitude': -75.58
                }
            },
            'vertical': {
                'minimum': 25,
                'maximum': 35,
                'identifier': 'ogp-crs-5714',
                'code': 'urn:ogc:def:crs:EPSG::5714',
                'name': 'MSL height',
                'remarks': 'Not specific to any location or epoch.',
                'scope': 'Hydrography.',
                'domain_of_validity': {
                    'href': 'urn:ogc:def:area:EPSG::1262'
                },
                'vertical_cs': {
                    'href': 'urn:ogc:def:cs:EPSG::6498'
                },
                'vertical_datum': {
                    'href': 'urn:ogc:def:datum:EPSG::5100'
                }
            },
            'temporal': {
                'period': {
                    'start': datetime(2011, 6, 21, 0, 0, 0),
                    'end': datetime(2012, 6, 20, 23, 59, 30)
                }
            }
        },
        'formats': [
            {
                'format': 'Comma Separated Values (CSV)',
                'href': 'https://www.iana.org/assignments/media-types/text/csv'
            }
        ],
        'transfer_options': [
            {
                'size': {
                    'unit': 'MB',
                    'magnitude': 26.4
                },
                'online_resource': {
                    'href': 'https://metadata-standards.data.bas.ac.uk/sample-record-artefacts/'
                            'caslab-ozone-2011-2012.csv',
                    'title': 'Download Data',
                    'description': 'Download measurement data',
                    'function': 'download'
                }
            }
        ],
        'measures': [
            {
                'code': 'Conformity_001',
                'code_space': 'INSPIRE',
                'pass': True,
                'title': {
                    'value': 'Commission Regulation (EU) No 1089/2010 of 23 November 2010 implementing Directive '
                             '2007/2/EC of the European Parliament and of the Council as regards interoperability of '
                             'spatial data sets and services',
                    'href': 'http://data.europa.eu/eli/reg/2010/1089'
                },
                'dates': [
                    {
                        'date': date(2010, 12, 8),
                        'date_type': 'publication'
                    }
                ],
                'explanation': 'See the referenced specification'
            }
        ],
        'lineage': 'This lineage statement, and data referenced in this record, are fictitious. This lineage statement '
                   'has been included as a demonstration of a typical UK Polar Data Centre discovery level metadata '
                   'record. Ozone measurements where recorded using an Ozone measuring instrument every 30 seconds, '
                   'with a 60 second moving average. The standard deviation for a one hour data sample (at low '
                   'atmospheric variability) is estimated at 0.2 ppbv. Standard quality assurance procedures where '
                   'then applied to the raw data resulting in: 360 missing measurements (due to maintenance or '
                   'malfunction); 40 measurements discarded as erroneous (due to malfunction); 1,204 measurements '
                   'discarded as being anomalous. The ozone measuring instrument was calibrated using standard '
                   'calibration procedures and verified against known true values prior to use.'
    }
}
