# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------
project = 'Implied Cost of Capital Training'
copyright = '2026, Your Name'
author = 'Your Name'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'myst_parser',
]

# Add support for Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Set default start page
master_doc = 'index'

# -- MyST Parser configuration for math ---------------------------------------
myst_enable_extensions = [
    "dollarmath",  # Enable $...$ and $$...$$ for inline and block math
    "amsmath",     # Enable advanced math environments
    "deflist",     # Definition lists
    "colon_fence", # Use ::: instead of ``` for directives
]

# -- MathJax configuration ----------------------------------------------------
# Use MathJax 3 (latest version) for better rendering
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
        'processEscapes': True,
        'processEnvironments': True,
    },
    'options': {
        'ignoreHtmlClass': 'tex2jax_ignore',
        'processHtmlClass': 'tex2jax_process',
    },
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}

# -- Options for GitHub Pages ------------------------------------------------
# Create .nojekyll file in the build directory
html_extra_path = []

def setup(app):
    app.add_css_file('custom.css')
