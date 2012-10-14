# -*- coding: utf-8 -*-

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from pkg_resources import resource_filename


deform_dir = resource_filename(
    "deform",
    "static")
lib_deform = Library(
    "deform",
    deform_dir)
deform_js = Resource(
    lib_deform,
    "scripts/deform.js",
    depends=[jquery])
