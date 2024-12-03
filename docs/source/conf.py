# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Henry'
copyright = '2024, Autonomy and Mobility Lab'
author = 'Eelis Peltola'

# release = '1.0'
# version = '1.0.0'

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

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Role for code output highlighting, use with :bash:`my bash command`
rst_prolog = """
.. role:: bash(code)
    :language: bash
    :class: highlight

.. role:: python(code)
    :language: python
    :class: highlight
"""
