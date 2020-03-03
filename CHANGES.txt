CHANGES
=======

2.0.3 - 2016-11-20
------------------

- Depend on deform 2.0.3.

2.0a2-3 2015-01-31
------------------

- Add mapping for ``select2``.

------------------
2.0a2-1 2014-05-13
------------------

- Use the typeahead bundled with deform instead of ``js.typeahead`` as the
  latter fails on Python 2.6.

2.0a2 2014-05-13
----------------

- Depend on deform 2.0a2 (Bootstrap 3).
  THIS IS NOT BACKWARD COMPATIBLE AND WILL BREAK WITH OLDER DEFORMS!

0.9.8 - 2013-11-19
------------------

- Resolve ``modernizr`` dependency with js.modernizr; this was introduced
  in deform-0.9.6.

0.9.7 - 2013-03-14
------------------

- Add ``deform_basic`` to the available resource groupings. Using this
  includes just the basic CSS and JavaScript, without the 'beautify' CSS.
  [davidjb]

0.9.6 - 2013-02-23
------------------

- No changes.

0.9.5-6
-------

- Fix a bug that caused requirements not to be loaded on ValidationFailure
  (thanks icemac!).

0.9.5-5
-------

- Include ``js.jquery_form`` dependency in setup.py (thanks icemac!).

0.9.5-4
-------

- Make all items in resource_mapping a list, so that third party
  packages (e.g. kotti_tinymce) can append resources.

0.9.5-3
-------

- Add an includme for easy using in Pyramid projects.

- Change patching to only patch deform.form.Form instead of individual
  widgets.

0.9.5-2
-------

- Add ``auto_need`` method for automatically including Fanstatic resources
  for a given Deform form instance.

- Add ``patch_deform`` function for automagically including Fanstatic
  resources.  This feature will vanish when deform gets a FormRender
  event which we can subscribe to.

0.9.5-1
-------

- Make the CSS resources available separately as well as combined with
  the JS resource.

0.9.5
-----

- Initial release.
