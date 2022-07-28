"""Sphinx configuration."""
project = "PyLogFormats"
author = "Matt Limb"
copyright = "2022, Matt Limb"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
