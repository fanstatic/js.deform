# -*- coding: utf-8 -*-

from fanstatic import Group
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

deform_form_css = Resource(
    library,
    "css/form.css")
deform_beautify_css = Resource(
    library,
    "css/beautify.css")

deform_css = Group([deform_form_css, deform_beautify_css, ])

deform = Group([deform_css, deform_js, ])
