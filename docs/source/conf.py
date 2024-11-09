# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Flashing Lights Unofficial Modding'
copyright = 'Maintained by SillyMonkey982 - All assets are copyrighted by the respected owners of Flashing Lights Game.'
author = 'SillyMonkey982'

release = ''
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'

# -- Options for EPUB output
epub_show_urls = 'footnote'
