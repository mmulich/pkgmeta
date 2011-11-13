# -*- coding: utf-8 -*-
import os
import sysconfig
import tempfile
from pkgmeta.tests import unittest


# TEST_PKGMETA_CFG = """\
# [global]
# root = {appdata.persistent}
# cache = {appdata.disposable}

# [test1-repo]
# sources =
#     %(source_one)s

# [test2-repo]
# sources =
#     %(source_two)s
#     %(source_one)s
# """

# SOURCES = {'source_one': 'file:///', 'source_two': 'file:///'}


class PkgMetaConfigTestCase(unittest.TestCase):

    def make_repo_config(self, *args, **kwargs):
        """Make a RepositoryConfig object."""
        from pkgmeta.config import RepositoryConfig
        return RepositoryConfig(*args, **kwargs)

    def make_one(self, *args, **kwargs):
        from pkgmeta.config import PkgMetaConfig
        return PkgMetaConfig(*args, **kwargs)

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
