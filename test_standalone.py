# -*- coding: utf-8 -*-
""" Basic unit tests that don't require installing all of kotti
"""
from __future__ import absolute_import

import unittest
from fanstatic import NeededResources, Resource, Group

class Tests(unittest.TestCase):
    def iter_resources(self):
        import js.deform
        for name, resource in js.deform.__dict__.items():
            if isinstance(resource, (Resource, Group)):
                yield name, resource

    def assert_needable(self, resource):
        needed = NeededResources()
        needed.need(resource)

    def test_resources_can_be_needed(self):
        for name, resource in self.iter_resources():
            self.assert_needable(resource)
