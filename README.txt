js.deform
=========

Introduction
------------

This library packages `deform`_ for `fanstatic`_.

.. _`fanstatic`: http://fanstatic.org
.. _`deform`: http://docs.pylonsproject.org/projects/deform/

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.deform``) are published to some URL.

Included resources
------------------

``js.deform`` is different from most ``js.`` packages in that it doesn't
include any resources itself.  It references the resources from ``deform``
instead.  The only resources that are made available from ``js.deform``
are ``deform.js``, ``form.css`` and ``beautify.css`` [#nb]_.  All other resources
that are part of the ``deform`` distribution are available separately:

  - jQuery (http://pypi.python.org/pypi/js.jquery)
  - jQuery Form (http://pypi.python.org/pypi/js.jquery_form)
  - jquery.maskedinput (http://pypi.python.org/pypi/js.jquery_maskedinput)
  - jquery-maskmoney (http://pypi.python.org/pypi/js.jquery_maskmoney)
  - TinyMCE (http://pypi.python.org/pypi/js.tinymce)

.. [#nb]
    For the ``deform2`` branch of deform, currently there are a number
    of other resources from ``deform`` which are referenced:

    - jquery-sortable.js
    - typeahead.js (and css)
    - customized modernizr.js
    - pickadate javascript and css
    - select2.js (and css)
