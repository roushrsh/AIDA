import os
project = "AIDA"
author = "AIDA authors"
release = "Author draft"
extensions = ["myst_parser"]
source_suffix = {".md": "markdown"}
master_doc = "index"
exclude_patterns = ["_build"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_theme_options = {"navigation_depth": 3, "collapse_navigation": False, "style_nav_header_background": "#173650"}
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
myst_heading_anchors = 3
