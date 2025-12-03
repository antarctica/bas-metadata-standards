from flask import Flask
from flask_file_routes import FileRoutes
from markdown.extensions.toc import TocExtension
from markdown_gfm_admonition import GfmAdmonitionExtension

app = Flask(__name__)
FileRoutes(app)
app.config['PAGES_MARKDOWN_OPTIONS'] = {'extensions': ["md_in_html", "tables", "fenced_code", TocExtension(toc_depth='2-6'), GfmAdmonitionExtension()]}
