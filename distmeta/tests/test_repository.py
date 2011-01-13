# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest

HERE = os.path.abspath(os.path.dirname(__file__))
REPO = os.path.join(HERE, 'metadata_repo')

class BaseTestCase(unittest.TestCase):
    """Base test case to set up the repository examples."""

    def setUp(self):
        self.repo_location = REPO

    def tearDown(self):
        pass


class TestReleaseSet(BaseTestCase):
    """ """
    


class TestMetadataRepository(BaseTestCase):
    """Metadata directory storage structure test.
    This will be the foundation for example data to be used throughout the
    test environment."""

    def setUp(self):
        super(TestMetadataRepository, self).setUp()
        from distmeta import MetadataRepository
        self.repo = MetadataRepository(self.repo_location)

    def tearDown(self):
        del self.repo
        super(TestMetadataRepository, self).tearDown()

    def test_init(self):
        self.assertIn('solarcal', self.repo)

    def test_get(self):
        releases = self.repo.get('solarcal', None)
        from distmeta import ReleaseSet
        self.assertIsInstance(releases, ReleaseSet)
        import ipdb; ipdb.set_trace()
