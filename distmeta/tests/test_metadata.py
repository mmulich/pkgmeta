# -*- coding: utf-8 -*-
from distmeta.tests import unittest


class TestDistributionMetadataComparisons(unittest.TestCase):
    """Test for metadata version comparison functionality."""

    def makeOne(self, **kwargs):
        from distmeta.metadata import DistributionMetadata
        return DistributionMetadata(**kwargs)

    def test_equal(self):
        #: Set up the metadata objects.

        mapping = {'name': 'common', 'version': '1.0'}
        meta_one = self.makeOne(mapping=mapping)
        meta_two = self.makeOne(mapping=mapping)
        self.assertEqual(meta_one, meta_two)
        #: Change the name to ensure that differnt dist
        #  with the same version aren't equal.
        mapping['name'] = 'notcommon'
        meta_two = self.makeOne(mapping=mapping)
        self.assertNotEqual(meta_one, meta_two)

    def test_less_or_lessequal(self):
        #: Set up the metadata objects.
        meta_one = self.makeOne(mapping={'name': 'meta_one',
                                         'version': '1.0'})
        meta_two = self.makeOne(mapping={'name': 'meta_two',
                                         'version': '2.0'})
        self.assertLess(meta_one, meta_two)
        #: Change the name to ensure that differnt dist
        #  with the same version aren't equal.
        self.assertLessEqual(meta_one, meta_two)
