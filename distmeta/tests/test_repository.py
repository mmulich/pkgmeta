# -*- coding: utf-8 -*-
import os
import tempfile
import shutil
from distmeta.tests import unittest
from distmeta.tests.utils import populate_repo, ALL_DISTS


class BaseTestCase(unittest.TestCase):
    """Base test case to set up the repository examples."""

    def setUp(self):
        self.repo_location = tempfile.mkdtemp('-repo', 'dist-metadata-')

    def tearDown(self):
        shutil.rmtree(self.repo_location)


class TestReleaseSet(BaseTestCase):
    """ """
    


class TestMetadataRepository(BaseTestCase):
    """Metadata directory storage structure test.
    This will be the foundation for example data to be used throughout the
    test environment."""

    def setUp(self):
        super(TestMetadataRepository, self).setUp()
        populate_repo(ALL_DISTS, self.repo_location)
        self.repo = self.makeOne()

    def tearDown(self):
        del self.repo
        super(TestMetadataRepository, self).tearDown()

    def makeOne(self):
        from distmeta import MetadataRepository
        return MetadataRepository(self.repo_location)

    def test_repr(self):
        # FIXME hardcoded class name
        self.assertEqual(repr(self.repo),
                         'MetadataRepository("%s")' % self.repo_location)

    def test_init(self):
        self.assertIn('solarcal', self.repo)

    def test_get(self):
        releases = self.repo.get('solarcal', None)
        from distmeta import ReleaseSet
        self.assertIsInstance(releases, ReleaseSet)
