import pytest


@pytest.fixture
def settings():
    return {}


@pytest.fixture
def config(request, settings):
    from pyramid import testing
    config = testing.setUp(settings=settings)
    config.include('pyramid_chameleon')
    config.add_default_renderers()
    request.addfinalizer(testing.tearDown)
    return config


def test_includeme(config):

    from deform import Form
    from deform import ValidationFailure
    from js.deform import includeme

    original_form_render = Form.render
    original_validationfailure_render = ValidationFailure.render

    includeme(config)

    assert Form.render != original_form_render
    assert ValidationFailure.render != original_validationfailure_render
