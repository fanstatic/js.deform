How to use?
===========

JS
--

You can import ``deform_js`` from ``js.deform`` and ``need``
it where you want these resources to be included on a page::

  >>> from js.deform import deform_js
  >>> deform_js.need()

CSS
---

You can import ``deform_css`` from ``js.deform`` and ``need``
it where you want these resources to be included on a page::

  >>> from js.deform import deform_css
  >>> deform_css.need()

This will include Deform's default ``form.css`` as well as the
``beautify.css``.  If you only want one or the other, you can
``need`` them like so::

  >>> from js.deform import deform_form_css
  >>> deform_form_css.need()

  >>> from js.deform import deform_beautify_css
  >>> deform_beautify_css.need()


All
---

You can import ``deform`` from ``js.deform`` and ``need``
it where you want these resources to be included on a page::

  >>> from js.deform import deform
  >>> deform.need()

This automatically includes all of Deform's CSS and JS and is
the equivalent to needing both ``deform_js`` and ``deform_css``
as described above.

Auto-needing Resources
----------------------

You can avoid needing to manually import and ``need()`` each
Fanstatic dependency of your ``Deform`` form by use of the ``auto_need``
function provided in this package.

  >>> import js.deform
  >>> import colander
  >>> import deform

  >>> schema = colander.Schema()
  >>> form = deform.Form(schema)
  >>> js.deform.auto_need(form)

By doing the above, any widget requirements - including those of `Deform`
itself - will be included for Fanstatic.

So, you may have a form that requires a ``deform.widget.RichTextWidget``
for one of its fields.  This type of widget requires resources relating to
`TinyMCE`.  ``js.deform.auto_need`` will use ``js.tinymce`` for this
requirement.

This is all best illustrated in the following example.

Initialise Fanstatic so we can see resources being included:

  >>> import fanstatic
  >>> dummy = fanstatic.init_needed()
  >>> len(fanstatic.get_needed().resources())
  0

Create a demonstration schema and form:

  >>> schema = colander.Schema()
  >>> node = colander.SchemaNode(colander.String(),
  ...                            widget=deform.widget.RichTextWidget())
  >>> schema.add(node)
  >>> form = deform.Form(schema)

Check the form's resource requirements:

  >>> form.get_widget_requirements()
  [('deform', None), ('tinymce', None)]

Ask ``auto_need`` to include the resources for us:

  >>> js.deform.auto_need(form)
  >>> needed = fanstatic.get_needed()

So we can now see the resources that have been included:

  >>> from js.jquery import jquery
  >>> jquery in needed.resources()
  True
  >>> from js.tinymce import tinymce
  >>> tinymce in needed.resources()
  True
  >>> from js.deform import deform_js
  >>> deform_js in needed.resources()
  True

The above resources will automatically be included on your page once
Fanstatic is configured accordingly.


Patching deform to automatically need the resources for a widget
----------------------------------------------------------------

If you don't want to have to call ``auto_need(form)`` for every form
instance in your application, you can patch deform (e.g. on application
startup) to automagically ``need()`` everything for you where required.
If you use Pyramid adding ``js.deform`` to your ``pyramid.includes``
is enough.

Let's reinit fanstatic...

  >>> dummy = fanstatic.init_needed()
  >>> len(fanstatic.get_needed().resources())
  0

...and patch ``deform`` this time:

  >>> from js.deform import includeme
  >>> includeme()

Note that you only have too do this once, e.g on application startup.

Now do the same as above, but without calling auto_need.  Note that
the ``need()`` calls are not issued before rendering the form.

  >>> schema = colander.Schema()
  >>> node = colander.SchemaNode(colander.String(),
  ...                            widget=deform.widget.RichTextWidget())
  >>> schema.add(node)
  >>> form = deform.Form(schema)
  >>> needed = fanstatic.get_needed()
  >>> len(needed.resources())
  0
  >>> html = form.render()
  >>> needed = fanstatic.get_needed()

Again all resources have been included for us:

  >>> jquery in needed.resources()
  True
  >>> tinymce in needed.resources()
  True
  >>> deform_js in needed.resources()
  True
