# -*- coding: utf-8 -*-

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from pkg_resources import resource_filename


deform_dir = resource_filename(
    "deform",
    "static")
library = Library(
    "deform",
    deform_dir)
deform_js = Resource(
    library,
    "scripts/deform.js",
    depends=[jquery])
