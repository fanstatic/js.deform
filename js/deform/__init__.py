# -*- coding: utf-8 -*-

from deform import Form, ValidationFailure
from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from js.jquery_form import jquery_form
from js.jquery_maskedinput import jquery_maskedinput
from js.jquery_maskmoney import jquery_maskmoney
from js.jquery_sortable import jquery_sortable
from js.jquery_timepicker_addon import timepicker
from js.jqueryui import ui_autocomplete
from js.jqueryui import ui_datepicker
from js.jqueryui import ui_sortable
from js.modernizr import modernizr
from js.select2 import select2
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
    depends=[jquery, ])

deform_form_css = Resource(
    library,
    "css/form.css")
deform_beautify_css = Resource(
    library,
    "css/beautify.css")

deform_css = Group([deform_form_css, deform_beautify_css, ])

deform_basic = Group([deform_form_css, deform_js, ])
deform = Group([deform_css, deform_js, ])

modernizr = Resource(
    library,
    'scripts/modernizr.custom.input-types-and-atts.js')

typeahead_js = Resource(
    library,
    'scripts/typeahead.min.js',
    depends=[jquery, ])
typeahead_css = Resource(
    library,
    'css/typeahead.css')
typeahead = Group([typeahead_js, typeahead_css])

fileupload = Resource(
    library,
    'scripts/file_upload.js')

pickadate_js_legacy = Resource(
    library,
    'pickadate/legacy.js')
pickadate_js_base = Resource(
    library,
    'pickadate/picker.js',
    depends=[pickadate_js_legacy, ])
pickadate_js_date = Resource(
    library,
    'pickadate/picker.date.js',
    depends=[pickadate_js_base, ])
pickadate_js_time = Resource(
    library,
    'pickadate/picker.time.js',
    depends=[pickadate_js_base, ])
pickadate_js = Group([
    pickadate_js_date,
    pickadate_js_time, ])
pickadate_css_base = Resource(
    library,
    'pickadate/themes/default.css')
pickadate_css_date = Resource(
    library,
    'pickadate/themes/default.date.css',
    depends=[pickadate_css_base, ])
pickadate_css_time = Resource(
    library,
    'pickadate/themes/default.time.css',
    depends=[pickadate_css_base, ])
pickadate_css = Group([
    pickadate_css_date,
    pickadate_css_time, ])

pickadate = Group([pickadate_js, pickadate_css, ])

resource_mapping = {
    'datetimepicker': [timepicker, ],
    'deform': [deform_js, ],
    'fileupload': [fileupload, ],
    'jquery': [jquery, ],
    'jquery.form': [jquery_form, ],
    'jquery.maskMoney': [jquery_maskmoney, ],
    'jquery.maskedinput': [jquery_maskedinput, ],
    'jqueryui': [ui_autocomplete, ui_datepicker, ui_sortable, ],
    'modernizr': [modernizr, ],
    'pickadate': [pickadate, ],
    'select2': [select2, ],
    'sortable': [jquery_sortable, ],
    'tinymce': [tinymce, ],
    'typeahead': [typeahead, ],
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
        resources = resource_mapping[library]
        if not isinstance(resources, list):  # pragma: no cover (bw compat only)
            resources = [resources]
        for resource in resources:
            resource.need()


def includeme(config=None):

    _marker = object()

    def form_render(self, appstruct=_marker, **kw):

        if appstruct is not _marker:  # pragma: no cover  (copied from deform)
            kw['appstruct'] = appstruct

        html = super(Form, self).render(**kw)
        auto_need(self)

        return html

    def validationfailure_render(self):

        auto_need(self.field)

        return self.field.widget.serialize(self.field, self.cstruct)

    def patch_deform():

        Form.render = form_render
        ValidationFailure.render = validationfailure_render

    patch_deform()
