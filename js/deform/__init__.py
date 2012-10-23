# -*- coding: utf-8 -*-

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from fanstatic.wsgi import resolve
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

#Deform widget dependencies
deform_jqueryui_css = Resource(
    library,
    "css/ui-lightness/jquery-ui-1.8.11.custom.css")
deform_jqueryui_js = Resource(
    library,
    "scripts/jquery-ui-1.8.11.custom.min.js",
    depends=[jquery])
deform_jqueryui = Group([deform_jqueryui_css, deform_jqueryui_js])

deform_jquery_time_picker_addon_css = Resource(
    library,
    "css/jquery-ui-timepicker-addon.css")
deform_jquery_time_picker_addon_js = Resource(
    library,
    "scripts/jquery-ui-timepicker-addon.js",
    depends=[deform_jqueryui])
deform_jquery_time_picker_addon = Group([deform_jquery_time_picker_addon_css,
                                         deform_jquery_time_picker_addon_js])

deform_jquery_form = Resource(
    library,
    "scripts/jquery.form-3.09.js",
    depends=[jquery])

deform_jquery_maskmoney = Resource(
    library,
    "scripts/jquery.maskMoney-1.4.1.js",
    depends=[jquery])

deform_jquery_maskedinput = Resource(
    library,
    "scripts/jquery.maskedinput-1.2.2.min.js",
    depends=[jquery])

deform_tinymce = Resource(
    library,
    "tinymce/jscripts/tiny_mce/tiny_mce.js",
    depends=[jquery])

resource_mapping = {
    'datetimepicker': ['js.jquery_timepicker_addon.timepicker',
                       deform_jquery_time_picker_addon],
    'deform': [deform],
    'jquery': ['js.jquery.jquery'],
    'jquery.form': ['js.jquery_form.jquery_form',
                    deform_jquery_form],
    'jquery.maskMoney': ['js.jquery_maskmoney.jquery_maskmoney',
                         deform_jquery_maskmoney],
    'jquery.maskedinput': ['js.jquery_maskedinput.jquery_maskedinput',
                           deform_jquery_maskedinput],
    'jqueryui': ['js.jqueryui.jqueryui',
                 deform_jqueryui],
    'tinymce': ['js.tinymce.tinymce',
                deform_tinymce]
}

def try_resolve(name):
    """Attempt to load the given object referred to by ``name``.

    This function automatically returns ``name`` if this object is anything
    but a string.
    """
    if type(name) != str:
        return name

    obj = None
    try:
        obj = resolve(name)
    except:
        pass
    return obj

def auto_need(form):
    """Automatically ``need()`` the relevant Fanstatic resources for a form.

    This function automatically utilises libraries in the ``js.*`` namespace
    if they're available (such as ``js.jquery``, ``js.tinymce`` and so
    forth) to allow Fanstatic to better manage these resources (caching,
    minifications) and avoid duplication across the rest of your
    application.

    If you don't have a certain library installed, then this function
    will fall back to using that which is automatically provided as a
    static resource within `Deform`.
    """
    requirements = form.get_widget_requirements()
    for library, version in requirements:
        potentials = resource_mapping[library]
        found = None
        for lib in potentials:
            found = try_resolve(lib)
            if found:
                break
        if found:
            found.need()
        else:
            raise ImportError("Can't locate a library for %s" % library)


