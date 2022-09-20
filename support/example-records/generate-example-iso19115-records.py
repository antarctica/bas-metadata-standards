import json

from pathlib import Path

from bas_metadata_library.standards.iso_19115_2 import MetadataRecordConfigV2, MetadataRecord
from lxml.etree import ElementTree, fromstring, ProcessingInstruction, tostring


source_configs_path: Path = Path('configs')
generated_records_path: Path = Path('output')

for source_config_path in source_configs_path.glob('*.json'):
  print(f"Loading record configuration from: {source_config_path.resolve()}")
  configuration = MetadataRecordConfigV2()
  configuration.load(file=source_config_path.resolve())
  record = MetadataRecord(configuration=configuration)

  try:
    record.validate()
  except RecordValidationError as e:
      print('Record invalid, skipping')
      print(e)
      continue
  _id = configuration.config['file_identifier']
  print(f"Record '{_id}' is valid")

  document = record.generate_xml_document()
  record_path = generated_records_path.joinpath(f"{_id}.xml")
  record_path.parent.mkdir(exist_ok=True)
  with open(record_path, mode='w') as record_file:
    record_file.write(document.decode())
  print(f"Record written as: {record_path.resolve()}")

  record_html_element = ElementTree(fromstring(document))
  record_html_element_root = record_html_element.getroot()
  record_html_element_root.addprevious(
    ProcessingInstruction(
      "xml-stylesheet", 'type="text/xsl" href="/static/xml-stylesheets/iso-html/xml-to-html-ISO.xsl"'
    )
  )
  document_html = tostring(record_html_element, pretty_print=True, xml_declaration=True, encoding="utf-8")
  record_html_path = generated_records_path.joinpath(f"{_id}-html.xml")
  record_html_path.parent.mkdir(exist_ok=True)
  with open(record_html_path, mode='w') as record_html_file:
    record_html_file.write(document_html.decode())
  print(f"Record written as: {record_html_path.resolve()}")

  record_rubric_element = ElementTree(fromstring(document))
  record_rubric_element_root = record_rubric_element.getroot()
  record_rubric_element_root.addprevious(
    ProcessingInstruction(
      "xml-stylesheet", 'type="text/xsl" href="/static/xml-stylesheets/iso-rubric/isoRubricHTML.xsl"'
    )
  )
  document_rubric = tostring(record_rubric_element, pretty_print=True, xml_declaration=True, encoding="utf-8")
  record_rubric_path = generated_records_path.joinpath(f"{_id}-rubric.xml")
  record_rubric_path.parent.mkdir(exist_ok=True)
  with open(record_rubric_path, mode='w') as record_rubric_file:
    record_rubric_file.write(document_rubric.decode())
  print(f"Record written as: {record_rubric_path.resolve()}")
