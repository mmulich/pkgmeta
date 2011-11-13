# -*- coding: utf-8 -*-
import os
import sysconfig
import tempfile
from pkgmeta.tests import unittest


class PkgMetaConfigTestCase(unittest.TestCase):

    def make_repo_config(self, *args, **kwargs):
        """Make a RepositoryConfig object."""
        from pkgmeta.config import RepositoryConfig
        return RepositoryConfig(*args, **kwargs)

    def make_one(self, *args, **kwargs):
        from pkgmeta.config import PkgMetaConfig
        return PkgMetaConfig(*args, **kwargs)

    def test_init_without_iterable_repository_value(self):
        repo_name = 'test1-repo'
        repos = self.make_repo_config(repo_name)
        config = self.make_one(repos)

        self.assertEqual(config.repositories[0].name, repo_name)

    def test_init_with_non_RepositoryConfig_value(self):
        with self.assertRaises(TypeError):
            self.make_one([self.make_repo_config('bingo'), 'just-a-name'])

    def test_iteration(self):
        repo_names = ['test1-repo', 'test2-repo']
        repos = [self.make_repo_config(n) for n in repo_names]
        config = self.make_one(repos)

        self.assertEqual(list(config), repos)

    def test_get_repository_config_default(self):
        repo_names = ['test1-repo', 'test2-repo']
        repos = [self.make_repo_config(n) for n in repo_names]
        config = self.make_one(repos)

        # Test without a repository name,
        # should return the default first listed repository.
        repo_config = config.get_repository_config()
        from pkgmeta.config import RepositoryConfig
        self.assertTrue(isinstance(repo_config, RepositoryConfig))
        self.assertEqual(repo_config.name, repo_names[0])

    def test_invalid_name_with_get_repository_config(self):
        repo_names = ['test1-repo', 'test2-repo']
        repos = [self.make_repo_config(n) for n in repo_names]
        config = self.make_one(repos)

        # Test with a non-existent repository name.
        with self.assertRaises(LookupError):
            repo_config = config.get_repository_config('bogus')

    def test_get_repository_config_with_name(self):
        repo_names = ['test1-repo', 'test2-repo', 'test3-repo', 'test4-repo']
        repos = [self.make_repo_config(n) for n in repo_names]
        # Create the config and specifically assign the default to
        # a repo we aren't calling by name.
        config = self.make_one(repos, default=repo_names[1])

        # Test with a specific repository name
        repo_name = repo_names[-1]
        repo_config = config.get_repository_config(repo_name)
        self.assertEqual(repo_config.name, repo_name)


class TestRepositoryConfig(unittest.TestCase):

    def test_storage_init(self):
        self.fail()

    def test_unknown_storage_type(self):
        from pkgmeta.exceptions import UnknownRepositoryStorageType
        from pkgmeta.config import RepositoryConfig
        with self.assertRaises(UnknownRepositoryStorageType):
            config = RepositoryConfig('name', type='DB2')
