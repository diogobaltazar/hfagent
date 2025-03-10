# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'hfagent'
copyright = '2025, diogo'
author = 'diogo'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'm2r2',
]

templates_path = ['_templates']
exclude_patterns = []

source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# filepath: /home/dipm/docs/sphinx/source/conf.py
from docutils import nodes
from docutils.parsers.rst import roles

def agent_definition_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.inline(rawtext, text, **options)
    node['classes'].append('agent-definition')
    return [node], []

roles.register_local_role('agent-definition', agent_definition_role)

# filepath: /home/dipm/docs/sphinx/source/conf.py
def setup(app):
    app.add_css_file('custom.css')