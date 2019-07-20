from datetime import datetime, timezone, date


iso19115_v1_gemini_v2_3_uk_pdc_candidate = {
    'file_identifier': 'b1a7d1b5-c419-41e7-9178-b1ffd76d5371',
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
    'date_stamp': datetime(2018, 10, 8, 14, 40, 44, tzinfo=timezone.utc),
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
            'value': 'Analysis of d18O and salinity from sea ice and meltwater pool water samples collected in April '
                     '2016 in the Weddell Sea and Scotia Sea of the Southern Ocean during the marine survey JR15006'
        },
        'abstract': 'The dataset contains oxygen stable isotope and salinity measurements from water samples collected '
                    'from sea ice and meltwater pools in April 2016 in the region of South Georgia, Signy and deep '
                    'within the Weddell Sea pack ice during the marine survey JR15006. <br /> The d18O and salinity '
                    'measurements from sea ice and meltwater sources complement the same analysis from CTD casts and '
                    'underway non-toxic flow water system on the RRS James Clark Ross during the JR15006. Establishing '
                    'd18O and salinity values for saline water and oceanic freshwater components can be used to '
                    'identify sources and changes of freshwater contributions to the ocean.',
        'dates': [
            {
                'date': date(2018, 1, 1),
                'date_precision': 'year',
                'date_type': 'creation'
            },
            {
                'date': date(2018, 1, 1),
                'date_precision': 'year',
                'date_type': 'revision'
            },
            {
                'date': datetime(2018, 10, 8, 14, 40, 44, tzinfo=timezone.utc),
                'date_type': 'publication'
            },
            {
                'date': datetime(2018, 12, 8, 14, 40, 44, tzinfo=timezone.utc),
                'date_type': 'released'
            }
        ],
        'edition': '1',
        'identifiers': [
            {
                'identifier': 'https://data.bas.ac.uk/metadata.php?id=b1a7d1b5-c419-41e7-9178-b1ffd76d5371',
                'href': 'https://data.bas.ac.uk/metadata.php?id=b1a7d1b5-c419-41e7-9178-b1ffd76d5371',
                'title': 'self'
            },
            {
                'identifier': 'https://doi.org/10.5285/3cf26ab6-7f47-4868-a87d-c62a2eefea1f',
                'href': 'https://doi.org/10.5285/3cf26ab6-7f47-4868-a87d-c62a2eefea1f',
                'title': 'doi'
            },
            {
                'identifier': 'NE/I022973/1',
                'href': 'https://gtr.ukri.org/projects?ref=NE%2FI022973%2F1',
                'title': 'award'
            }
        ],
        'contacts': [
            {
                'individual': {
                    'name': 'Meredith, Michael',
                    'href': 'https://orcid.org/0000-0002-7342-7756',
                    'title': 'orcid'
                },
                'organisation': {
                    'name': 'British Antarctic Survey'
                },
                'email': 'mmm@bas.ac.uk',
                'online_resource': {
                    'href': 'https://orcid.org/0000-0002-7342-7756',
                    'title': 'ORCID record',
                    'description': 'ORCID is an open, non-profit, community-driven effort to create and maintain a '
                                   'registry of unique researcher identifiers and a transparent method of linking '
                                   'research activities and outputs to these identifiers.',
                    'function': 'information'
                },
                'role': ['author']
            },
            {
                'individual': {
                    'name': 'Arrowsmith, Carol',
                    'href': 'https://orcid.org/0000-0003-3849-5179',
                    'title': 'orcid'
                },
                'organisation': {
                    'name': 'British Geological Survey'
                },
                'email': 'noreply@bas.ac.uk',
                'online_resource': {
                    'href': 'https://orcid.org/0000-0003-3849-5179',
                    'title': 'ORCID record',
                    'description': 'ORCID is an open, non-profit, community-driven effort to create and maintain a '
                                   'registry of unique researcher identifiers and a transparent method of linking '
                                   'research activities and outputs to these identifiers.',
                    'function': 'information'
                },
                'role': ['author']
            },
            {
                'individual': {
                    'name': 'Leng, Melanie',
                    'href': 'https://orcid.org/0000-0003-1115-5166',
                    'title': 'orcid'
                },
                'organisation': {
                    'name': 'British Geological Survey'
                },
                'email': 'noreply@bas.ac.uk',
                'online_resource': {
                    'href': 'https://orcid.org/0000-0003-1115-5166',
                    'title': 'ORCID record',
                    'description': 'ORCID is an open, non-profit, community-driven effort to create and maintain a '
                                   'registry of unique researcher identifiers and a transparent method of linking '
                                   'research activities and outputs to these identifiers.',
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
            },
            {
                'organisation': {
                    'name': 'Natural Environment Research Council',
                    'href': 'http://isni.org/isni/0000000094781573',
                    'title': 'isni'
                },
                'phone': '+44 (0)1793 411500',
                'address': {
                    'delivery_point': 'Natural Environment Research Council, Polaris House, North Star Avenue',
                    'city': 'Swindon',
                    'administrative_area': 'Hampshire',
                    'postal_code': 'SN2 1EU',
                    'country': 'United Kingdom'
                },
                'email': 'researchgrants@nerc.ukri.org',
                'online_resource': {
                    'href': 'https://nerc.ukri.org',
                    'function': 'information'
                },
                'role': [
                    'funder'
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
                        'term': 'Oceanographic geographical features',
                        'href': 'https://www.eionet.europa.eu/gemet/en/inspire-theme/of'
                    },
                    {
                        'term': 'Sea regions',
                        'href': 'https://www.eionet.europa.eu/gemet/en/inspire-theme/sr'
                    },
                    {
                        'term': 'Land cover',
                        'href': 'https://www.eionet.europa.eu/gemet/en/inspire-theme/lc'
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
                        'term': 'EARTH SCIENCE > Hydrosphere > Snow/Ice > Snow Melt',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/dd6de9e1-61e7-41bf-a2dc-9d2afc690bb3'
                    },
                    {
                        'term': 'EARTH SCIENCE > Hydrosphere > Surface Water',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/5debb283-51e4-435e-b2a2-e8e2a977220d'
                    },
                    {
                        'term': 'EARTH SCIENCE > Oceans > Sea Ice > Isotopes',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/9d99408d-0d8b-4642-a2cb-edee8319fe1d'
                    },
                    {
                        'term': 'EARTH SCIENCE > Oceans > Sea Ice > Pack Ice',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/ea85ea0b-1b7d-464a-9f8c-1f80383ffc51'
                    },
                    {
                        'term': 'EARTH SCIENCE > Oceans > Sea Ice > Salinity',
                        'href': 'https://gcmdservices.gsfc.nasa.gov/kms/concept/04fa9023-ab68-4dd0-a82e-abe685105a53'
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
            },
            {
                'terms': [
                    {
                        'term': 'd18O'
                    },
                    {
                        'term': 'meltwater pool'
                    },
                    {
                        'term': 'salinity'
                    },
                    {
                        'term': 'sea ice'
                    }
                ],
                'type': 'theme'
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
                    'required_citation': 'Bougamont, M. (2018). Ice flow model output for Pine Island Glacier (West '
                                         'Antarctica), from numerical inversions of ice surface velocities observed in '
                                         '1996 and 2014 [Data set]. UK Polar Data Centre, Natural Environment Research '
                                         'Council, UK Research and Innovation. '
                                         'https://doi.org/10.5285/3cf26ab6-7f47-4868-a87d-c62a2eefea1f'
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
            'inlandWaters',
            'oceans'
        ],
        'extent': {
            'geographic': {
                'bounding_box': {
                    'west_longitude': -45.61521,
                    'east_longitude': -27.04976,
                    'south_latitude': -68.1511,
                    'north_latitude': -54.30761
                }
            },
            'vertical': {
                'identifier': 'ogp-crs-5715',
                'code': 'urn:ogc:def:crs:EPSG::5715',
                'name': 'MSL depth',
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
                    'start': date(2016, 3, 31),
                    'end': date(2016, 4, 26)
                }
            }
        },
        'formats': [
            {
                'format': 'Microsoft Excel Workbook',
                'href': 'https://www.iana.org/assignments/media-types/application/'
                        'vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            }
        ],
        'transfer_options': [
            {
                'online_resource': {
                    'href': 'https://www.bodc.ac.uk/data/bodc_database/nodb/data_collection/6618/',
                    'title': 'Get Data',
                    'description': 'Download underlying CTD data',
                    'function': 'download'
                }
            },
            {
                'size': {
                    'unit': 'kB',
                    'magnitude': 30
                },
                'online_resource': {
                    'href': 'https://ramadda.data.bas.ac.uk/repository/entry/show?entryid='
                            '63af1e57-8f20-4fb1-a55c-bd0e703f8a56',
                    'title': 'Get Data',
                    'description': 'Download measurement data',
                    'function': 'download'
                }
            },
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
        'lineage': 'At all sample locations, 2 or more salinity bottles and d18O vials were filled following the usual '
                   'procedure. The d18O vials were rinsed 3 times, filled and dried before being closed with a stopper '
                   'and sealed with the crimper. Oxygen isotope (d18O) measurements were made using the CO2 '
                   'equilibration method with an Isoprime 100 mass spectrometer plus Aquaprep device. 90 samples '
                   '(200μl of water) were loaded into Labco Limited exetainers (3.7ml) and placed in the heated '
                   'sample tray at 40°C. The exetainers were then evacuated to remove atmosphere then flushed '
                   'with CO2 and left to equilibrate for between 12 (first sample) - 37 (last sample) hours. Each '
                   'individual gas sample was then admitted to the cryogenic water trap where any water vapour is '
                   'removed. The dry sample gas was then expanded into the dual inlet where it was measured on the '
                   'transducer before being expanded in the dual inlet bellows. Ionvantage software then balances the '
                   'reference bellows relative to this volume. The sample and reference CO2 gases enter alternatively '
                   'into the Isoprime100 through the dual changeover valve for isotope ratio measurement. In each run '
                   'two laboratory standards (CA-HI and CA-LO) plus up to 2 secondary standards were analysed in '
                   'triplicate. The value of these laboratory standards has been accurately determined by comparison '
                   'with international calibration and reference materials (VSMOW2, SLAP2 and GISP) and so the 18O/16O '
                   'ratios (versus VSMOW2) of the unknown samples can be calculated and are expressed in delta units, '
                   'd18O (parts per mille). Errors are < +/- 0.05 per mil.'
    }
}