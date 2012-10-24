# -*- coding: utf-8 -*-

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from js.jquery_form import jquery_form
from js.jquery_maskedinput import jquery_maskedinput
from js.jquery_maskmoney import jquery_maskmoney
from js.jquery_timepicker_addon import timepicker
from js.jqueryui import jqueryui
from js.tinymce import tinymce
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

resource_mapping = {
    'datetimepicker': timepicker,
    'deform': deform,
    'jquery': jquery,
    'jquery.form': jquery_form,
    'jquery.maskMoney': jquery_maskmoney,
    'jquery.maskedinput': jquery_maskedinput,
    'jqueryui': jqueryui,
    'tinymce': tinymce,
}


def auto_need(form):
    """Automatically ``need()`` the relevant Fanstatic resources for a form.

    This function automatically utilises libraries in the ``js.*`` namespace
    (such as ``js.jquery``, ``js.tinymce`` and so forth) to allow Fanstatic
    to better manage these resources (caching, minifications) and avoid
    duplication across the rest of your application.
    """

    requirements = form.get_widget_requirements()

    for library, version in requirements:
        resource_mapping[library].need()


from deform_patches import patch_deform
