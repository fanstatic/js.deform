from deform import Form
from deform import ValidationFailure

from js.deform import includeme


def test_includeme(config):

    original_form_render = Form.render
    original_validationfailure_render = ValidationFailure.render

    includeme(config)

    assert Form.render != original_form_render
    assert ValidationFailure.render != original_validationfailure_render
