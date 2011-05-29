# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest
from distmeta.tests.base import BaseTestCase
from distmeta.tests.mock_metadata import ALL_DISTS
from distmeta.tests.utils import populate_repo


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
        return MetadataRepository.from_path(self.repo_location)

    def test_repr(self):
        # FIXME hardcoded class name
        self.assertEqual(repr(self.repo),
                         'MetadataRepository.from_path("%s")' % self.repo_location)

    def test_init(self):
        self.assertIn('solarcal', self.repo)

    def test_get(self):
        releases = self.repo.get('solarcal', None)
        from distmeta.releases import ReleaseSet
        self.assertIsInstance(releases, ReleaseSet)
        #: It'd be easier to do this with the with statement, but it's not
        #  Python <2.6 compatible.
        self.assertRaises(KeyError, lambda a: self.repo[a], ('bogus'))
        
    def test_search(self):
        self.assertRaises(TypeError, self.repo.search, ('cal',))
        cal_search = lambda s: s.find('cal') >= 0
        cal_results = [rs.name for rs in self.repo.search(cal_search)]
        self.assertTrue('solarcal' in cal_results,
                        "Expected to find solarcal in the search results.")
