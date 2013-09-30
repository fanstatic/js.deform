# -*- coding: utf-8 -*-

from deform import Form, ValidationFailure
from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery
from js.jquery_form import jquery_form
from js.jquery_maskedinput import jquery_maskedinput
from js.jquery_maskmoney import jquery_maskmoney
# This is stale (4.0.2), use tinymce from deform (4.0.6) for now
#from js.tinymce import tinymce
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
    depends=[jquery, jquery_form])

# XXX: I'm pretty sure these are no longer used/required
#deform_form_css = Resource(
#    library,
#    "css/form.css")
#deform_beautify_css = Resource(
#    library,
#    "css/beautify.css")

#deform_css = Group([deform_form_css, deform_beautify_css, ])
#deform_basic = Group([deform_form_css, deform_js, ])
#deform = Group([deform_css, deform_js, ])

tinymce = Resource(
    library, "tinymce/tinymce.min.js")

sortable_js = Resource(
    library, "scripts/jquery-sortable.js")

# XXX: There is a js.typeahead package, but it does not install on
# py2.6 (and it is currently one version of typeahead behind)
typeahead_js = Resource(
    library, "scripts/typeahead.min.js")
typeahead_css = Resource(
    library, "css/typeahead.css")

modernizr_js = Resource(
    library, "scripts/modernizr.custom.input-types-and-atts.js")

# XXX: Not sure these dependencies are right...
pickadate_base_css = Resource(
    library, "pickadate/themes/default.css")
pickadate_date_css = Resource(
    library, "pickadate/themes/default.date.css",
    depends=[pickadate_base_css])
pickadate_time_css = Resource(
    library, "pickadate/themes/default.time.css",
    depends=[pickadate_base_css])
pickadate_legacy_js = Resource(
    library, "pickadate/legacy.js")
pickadate_picker_js = Resource(
    library, "pickadate/picker.js")
pickadate_picker_date_js = Resource(
    library, "pickadate/picker.date.js",
    depends=[pickadate_picker_js])
pickadate_picker_time_js = Resource(
    library, "pickadate/picker.time.js",
    depends=[pickadate_picker_js])

pickadate_css = Group([
    pickadate_date_css,
    pickadate_time_css,
    ])
pickadate_js = Group([
    pickadate_legacy_js,
    pickadate_picker_date_js,
    pickadate_picker_time_js,
    ])

# XXX: use js.select2?
select2_css = Resource(library, "select2/select2.css")
select2_js = Resource(library, "select2/select2.js")

# XXX: 'jquery' is no longer listed in deform.widget.default_resources
resource_mapping = {
    'deform': [deform_js, ],
    'jquery': [jquery, ],
    'jquery.form': [jquery_form, ],
    'jquery.maskMoney': [jquery_maskmoney, ],
    'jquery.maskedinput': [jquery_maskedinput, ],
    'tinymce': [tinymce, ],

    'sortable': [sortable_js, ],
    'typeahead': [typeahead_js, typeahead_css, ],
    'modernizr': [modernizr_js, ],
    'pickadate': [pickadate_css, pickadate_js],
    'select2': [select2_css, select2_js, ],
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
