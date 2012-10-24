# -*- coding: utf-8 -*-

import deform.widget
from js.deform import deform_js
from js.jquery_maskedinput import jquery_maskedinput
from js.jquery_maskmoney import jquery_maskmoney
from js.jquery_timepicker_addon import timepicker_addon_js
from js.jqueryui import ui_autocomplete
from js.jqueryui import ui_datepicker
from js.jqueryui import ui_sortable
from js.tinymce import tinymce

autocomplete_input_widget_serialize = deform.widget.AutocompleteInputWidget.serialize
checked_input_widget_serialize = deform.widget.CheckedInputWidget.serialize
date_input_widget_serialize = deform.widget.DateInputWidget.serialize
date_time_input_widget_serialize = deform.widget.DateTimeInputWidget.serialize
mapping_widget_serialize = deform.widget.MappingWidget.serialize
money_input_widget_serialize = deform.widget.MoneyInputWidget.serialize
richt_text_widget_serialize = deform.widget.RichTextWidget.serialize
sequence_widget_serialize = deform.widget.SequenceWidget.serialize
text_input_widget_serialize = deform.widget.TextInputWidget.serialize


# TextInputWidget sometimes needs jquery_maskedinput
def patched_text_input_widget_serialize(self, field, cstruct, **kw):
    if self.mask is not None:
        jquery_maskedinput.need()
    return text_input_widget_serialize(self, field, cstruct, **kw)


# MoneyInputWidget needs jquery_maskmoney
def patched_money_input_widget_serialize(self, field, cstruct, **kw):
    jquery_maskmoney.need()
    return money_input_widget_serialize(self, field, cstruct, **kw)


# MappingWidget needs deform.js
def patched_mapping_widget_serialize(self, field, cstruct, **kw):
    deform_js.need()
    return mapping_widget_serialize(self, field, cstruct, **kw)


# CheckedInputWidget sometimes needs jquery_maskedinput
def patched_checked_input_widget_serialize(self, field, cstruct, **kw):
    if self.mask is not None:
        jquery_maskedinput.need()
    return checked_input_widget_serialize(self, field, cstruct, **kw)


# AutocompleteInputWidget needs jqueryui
def patched_autocomplete_input_widget_serialize(self, field, cstruct, **kw):
    ui_autocomplete.need()
    return autocomplete_input_widget_serialize(self, field, cstruct, **kw)


# DateInputWidget needs jqueryui
def patched_date_input_widget_serialize(self, field, cstruct, **kw):
    ui_datepicker.need()
    return date_input_widget_serialize(self, field, cstruct, **kw)


# DateTimeInputWidget needs jqueryui, datetimepicker
def patched_date_time_input_widget_serialize(self, field, cstruct, **kw):
    timepicker_addon_js.need()
    return date_time_input_widget_serialize(self, field, cstruct, **kw)


# RichTextWidget needs tinymce
def patched_richt_text_widget_serialize(self, field, cstruct, **kw):
    tinymce.need()
    return richt_text_widget_serialize(self, field, cstruct, **kw)


# SequenceWidget needs deform, jqueryui
def patched_sequence_widget_serialize(self, field, cstruct, **kw):
    ui_sortable.need()
    return sequence_widget_serialize(self, field, cstruct, **kw)


def patch_deform():
    deform.widget.AutocompleteInputWidget.serialize = patched_autocomplete_input_widget_serialize
    deform.widget.CheckedInputWidget.serialize = patched_checked_input_widget_serialize
    deform.widget.DateInputWidget.serialize = patched_date_input_widget_serialize
    deform.widget.DateTimeInputWidget.serialize = patched_date_time_input_widget_serialize
    deform.widget.MappingWidget.serialize = patched_mapping_widget_serialize
    deform.widget.MoneyInputWidget.serialize = patched_money_input_widget_serialize
    deform.widget.RichTextWidget.serialize = patched_richt_text_widget_serialize
    deform.widget.SequenceWidget.serialize = patched_sequence_widget_serialize
    deform.widget.TextInputWidget.serialize = patched_text_input_widget_serialize
