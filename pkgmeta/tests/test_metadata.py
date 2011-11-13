# -*- coding: utf-8 -*-
from pkgmeta.tests import unittest


class TestMetadataComparisons(unittest.TestCase):
    """Test for metadata version comparison functionality."""

    def make_one(self, **kwargs):
        from pkgmeta.metadata import Metadata
        return Metadata(**kwargs)

    def test_equal(self):
        #: Set up the metadata objects.

        mapping = {'name': 'common', 'version': '1.0'}
        meta_one = self.make_one(mapping=mapping)
        meta_two = self.make_one(mapping=mapping)
        self.assertEqual(meta_one, meta_two)
        #: Change the name to ensure that differnt dist
        #  with the same version aren't equal.
        mapping['name'] = 'notcommon'
        meta_two = self.make_one(mapping=mapping)
        self.assertNotEqual(meta_one, meta_two)

    def test_less_or_lessequal(self):
        #: Set up the metadata objects.
        meta_one = self.make_one(mapping={'name': 'common',
                                          'version': '1.0'})
        meta_two = self.make_one(mapping={'name': 'common',
                                          'version': '2.0'})
        self.assertLess(meta_one, meta_two)
        #: Change the name to ensure that differnt dist
        #  with the same version aren't equal.
        self.assertLessEqual(meta_one, meta_two)

    def test_greater_or_greaterequal(self):
        #: Set up the metadata objects.
        meta_one = self.make_one(mapping={'name': 'common',
                                          'version': '1.0.1'})
        meta_two = self.make_one(mapping={'name': 'common',
                                          'version': '1.0a1'})
        self.assertGreater(meta_one, meta_two)
        #: Change the name to ensure that differnt dist
        #  with the same version aren't equal.
        self.assertGreaterEqual(meta_one, meta_two)

    def test_lessthan_for_incompatible_types_comparison(self):
        random_object = object()
        meta_one = self.make_one(mapping={'name': 'common',
                                          'version': '1.0.1'})
        with self.assertRaises(TypeError):
            comparision = meta_one < random_object

    def test_equal_for_incompatible_types_comparison(self):
        random_object = object()
        meta_one = self.make_one(mapping={'name': 'common',
                                          'version': '1.0.1'})
        with self.assertRaises(TypeError):
            comparision = meta_one == random_object
