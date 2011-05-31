# -*- coding: utf-8 -*-
import os
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import ALL_DISTS
from pkgmeta.tests.utils import populate_repo


class TestMetadataRepository(BaseTestCase):
    """Metadata directory storage structure test.
    This will be the foundation for example data to be used throughout the
    test environment."""

    def setUp(self):
        super(TestMetadataRepository, self).setUp()
        populate_repo(ALL_DISTS, self.repo_directory)

    def makeOne(self, location=None):
        from pkgmeta.repository import Repository
        if location is None:
            return Repository()
        return Repository.from_directory(location)

    def test_repr(self):
        # Check representation from a blank instance.
        repo = self.makeOne()
        self.assertEqual(repr(repo), '<Repository of >')
        # Check representation from a repository instance created from a
        # directory location.
        repo_from_directory = self.makeOne(self.repo_directory)
        self.assertEqual(repr(repo_from_directory),
                         'Repository.from_directory("{0}")'.format(self.repo_directory))

    def test_init(self):
        repo = self.makeOne(self.repo_directory)
        self.assertIn('solarcal', repo)

    def test_get(self):
        repo = self.makeOne(self.repo_directory)
        releases = repo.get('solarcal', None)
        from pkgmeta.releases import ReleaseSet
        self.assertIsInstance(releases, ReleaseSet)
        self.assertRaises(KeyError, lambda a: repo[a], ('bogus'))
        
    def test_search(self):
        repo = self.makeOne(self.repo_directory)
        self.assertRaises(TypeError, repo.search, ('cal',))
        cal_search = lambda s: s.find('cal') >= 0
        cal_results = [rs.name for rs in repo.search(cal_search)]
        self.assertTrue('solarcal' in cal_results,
                        "Expected to find solarcal in the search results.")

    def test_to_and_from_pickle(self):
        # To and from a specified pickle location.
        repo = self.makeOne(self.repo_directory)
        pickle = repo.to_pickle(self.repo_pickle)
        self.assertEqual(self.repo_pickle, pickle)
        from pkgmeta.repository import Repository
        loaded_repo = Repository.from_pickle(pickle)
        self.assertEqual(repo, loaded_repo)
        # To and from unspecified pickle location... use pkgmeta.cfg settings.
        self.fail("pkgmeta.cfg isn't implemented yet")
