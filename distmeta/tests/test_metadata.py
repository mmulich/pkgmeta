# -*- coding: utf-8 -*-
from distmeta.tests import unittest


class TestDistributionMetadataComparisons(unittest.TestCase):
    """Test for metadata version comparison functionality."""

    def test_equal(self):
        #: Set up the metadata objects
        from distmeta.metadata import DistributionMetadata
        mapping = {'name': 'common', 'version': '1.0'}
        meta_one = DistributionMetadata(mapping=mapping)
        meta_two = DistributionMetadata(mapping=mapping)
        self.assertEqual(meta_one, meta_two)
