# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest

HERE = os.path.abspath(os.path.dirname(__file__))


class TestMetadataRepository(unittest.TestCase):
    """First test to flesh out the metadata directory storage structure.
    This will be the foundation for example data to be used throughout the
    test environment."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load(self):
        temp_repo = os.path.join(HERE, 'metadata_repo')
        from distmeta import MetadataRepository
        repo = MetadataRepository(temp_repo)
        self.assertIn('solarcal', repo)
