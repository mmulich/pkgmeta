# -*- coding: utf-8 -*-
import os
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import ALL_DISTS, SOLARCAL
from pkgmeta.tests.utils import populate_repo


class RepositoryTestCase(BaseTestCase):
    """Metadata directory storage structure test.
    This will be the foundation for example data to be used throughout the
    test environment."""

    def setUp(self):
        super(RepositoryTestCase, self).setUp()
        from pkgmeta.config import RepositoryConfig
        from pkgmeta.storage import FS_STORAGE_TYPE
        # Populate the repository with a single distribution
        populate_repo(ALL_DISTS, self.repo_directory)
        # Create the repository from a repository config
        self.config = RepositoryConfig('test', type=FS_STORAGE_TYPE,
                                       location=self.repo_directory)

    @property
    def target_cls(self):
        from pkgmeta.repository import Repository
        return Repository

    def make_one(self, location=None):
        if location is None:
            location = self.repo_directory
        from pkgmeta.config import RepositoryConfig
        from pkgmeta.storage import FS_STORAGE_TYPE
        config = RepositoryConfig('', type=FS_STORAGE_TYPE, location=location)
        return self.target_cls(config)

    def test_init_without_config(self):
        with self.assertRaises(TypeError):
            self.target_cls(None)

    def test_init(self):
        # Create the repository from a repository config
        repo = self.target_cls(self.config)
        # Test...
        self.assertEqual(repo.config, self.config)
        self.assertIn('solarcal', repo)

    def test_get(self):
        repo = self.make_one()
        releases = repo.get('solarcal', None)
        from pkgmeta.releases import ReleaseSet
        self.assertIsInstance(releases, ReleaseSet)
        self.assertRaises(KeyError, lambda a: repo[a], ('bogus'))
        
    def test_search(self):
        repo = self.make_one()
        self.assertRaises(TypeError, repo.search, ('cal',))
        cal_search = lambda s: s.find('cal') >= 0
        cal_results = [rs.name for rs in repo.search(cal_search)]
        self.assertTrue('solarcal' in cal_results,
                        "Expected to find solarcal in the search results.")

    def test_search_with_single_property(self):
        repo = self.make_one()
        cal_search = lambda s: s.find('cal') >= 0
        cal_results = [rs.name for rs in repo.search(cal_search, 'name')]
        self.assertTrue('solarcal' in cal_results,
                        "Expected to find solarcal in the search results.")        

    def test_iteration(self):
        repo = self.make_one()
        values = [name for name in repo]
        values.sort()
        expected_values = [dist[0]['name'] for dist in ALL_DISTS]
        expected_values.sort()
        self.assertEqual(values, expected_values)

    def test_len(self):
        repo = self.make_one()
        self.assertEqual(len(repo), len(ALL_DISTS))
