# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Open Metadata Exchange"
version = "0.0.1"
copyright = "2024, ISKME and contributors"
author = "ISKME and contributors"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

autoapi_dirs = ["../src"]
exclude_patterns = [
    ".*/*",
    ".DS_Store",
    "docs/_build",
    "fe/src/*/README.md",
    "LICENSE.rst",
    "src/iindex.rst",
    "src/Open_Metadata_Exchange.egg-info/*",
    "Thumbs.db",
]
extensions = [
    "autoapi.extension",
    "myst_parser",
    "sphinxcontrib.mermaid",
]
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_fence_as_directive = [
    "include",
    "mermaid",
]
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
suppress_warnings = ["epub.unknown_project_files"]
templates_path = ["_templates"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]
html_theme = "alabaster"
