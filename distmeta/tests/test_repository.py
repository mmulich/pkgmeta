# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest
from distmeta.tests.base import BaseTestCase
from distmeta.tests.utils import populate_repo, ALL_DISTS


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
        from distmeta.repository import MetadataRepository
        return MetadataRepository(self.repo_location)

    def test_repr(self):
        # FIXME hardcoded class name
        self.assertEqual(repr(self.repo),
                         'MetadataRepository("%s")' % self.repo_location)

    def test_init(self):
        self.assertIn('solarcal', self.repo)

    def test_get(self):
        releases = self.repo.get('solarcal', None)
        from distmeta.releases import ReleaseSet
        self.assertIsInstance(releases, ReleaseSet)
        
