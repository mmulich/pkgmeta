# -*- coding: utf-8 -*-
import os
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import ALL_DISTS, SOLARCAL
from pkgmeta.tests.utils import populate_repo


class BaseRepositoryTestCase(BaseTestCase):
    """Metadata directory storage structure test.
    This will be the foundation for example data to be used throughout the
    test environment."""

    def setUp(self):
        super(BaseRepositoryTestCase, self).setUp()
        from pkgmeta.config import FileSystemRepositoryConfig
        # Populate the repository with a single distribution
        populate_repo([SOLARCAL], self.repo_directory)
        # Create the repository from a repository config
        self.config = FileSystemRepositoryConfig('test', self.repo_directory)

    def test_init(self):
        from pkgmeta.repository import BaseRepository
        # Create the repository from a repository config
        repo = BaseRepository(self.config)
        # Test...
        self.assertEqual(repo.config, self.config)
        self.assertIn('solarcal', repo._data)

    def test_repr(self):
        from pkgmeta.repository import BaseRepository
        # Create the repository from a repository config
        repo = BaseRepository(self.config)
        self.assertEqual(repr(repo), "<BaseRepository of 'solarcal'>")
        # # Check representation from a repository instance created from a
        # # directory location.
        # repo_from_directory = self.makeOne(self.repo_directory)
        # self.assertEqual(repr(repo_from_directory),
        #                  'Repository.from_directory("{0}")'.format(self.repo_directory))


class RepositoryTestCase(BaseTestCase):

    def setUp(self):
        super(RepositoryTestCase, self).setUp()
        populate_repo(ALL_DISTS, self.repo_directory)

    def make_one(self, location=None):
        from pkgmeta.repository import Repository
        if location is None:
            location = self.repo_directory
        return Repository.from_directory(location)

    def test_repr(self):
        # Check representation from a repository instance created from a
        # directory location.
        repo_from_directory = self.make_one(self.repo_directory)
        self.assertEqual(repr(repo_from_directory),
                         'Repository.from_directory("{0}")'.format(self.repo_directory))

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
