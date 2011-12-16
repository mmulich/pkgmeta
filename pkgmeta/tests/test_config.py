# -*- coding: utf-8 -*-
import os
import sysconfig
import tempfile
from pkgmeta.tests import unittest

TEST_PKGMETA_CFG = """\
[pkgmeta]
default = repo2

[repo1]

[repo2]

[repo3]
type = filesystem
location = %(location)s
"""


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
        config = self.make_one([repos])

        self.assertEqual(config.repositories[0].name, repo_name)

    def test_iteration(self):
        repo_names = ['test1-repo', 'test2-repo']
        repos = [self.make_repo_config(n) for n in repo_names]
        config = self.make_one(repos)

        self.assertEqual(list(config), repo_names)

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
        # __getitem__ uses get_repository_config
        repo_config = config[repo_name]
        self.assertEqual(repo_config.name, repo_name)


class TestRepositoryConfig(unittest.TestCase):

    def make_one(self, *args, **kwargs):
        from pkgmeta.config import RepositoryConfig
        return RepositoryConfig(*args, **kwargs)

    def test_unknown_storage_type(self):
        from pkgmeta.exceptions import UnknownRepositoryStorageType
        with self.assertRaises(UnknownRepositoryStorageType):
            config = self.make_one('name', type='DB2')

    def test_storage_init(self):
        config = self.make_one('repo')
        from pkgmeta.storage import RuntimeStorage
        #: Should default to a RuntimeStorage
        self.assertTrue(isinstance(config.storage, RuntimeStorage))

    def test_arbitrary_attributes(self):
        config = self.make_one('repo', foo='foo', bar='foobar')
        self.assertEqual(config.foo, 'foo')
        self.assertEqual(config.bar, 'foobar')


class ConfigurationFromAFileTest(unittest.TestCase):
    """Read in the configuration from a pkgmeta.cfg file."""

    def write_config(self, content):
        dummy, file = tempfile.mkstemp()
        with open(file, 'w') as f:
            f.write(content)
        return file

    def make_one(self, file):
        from pkgmeta.config import PkgMetaConfig
        return PkgMetaConfig.from_file(file)

    def test_blank_file(self):
        from pkgmeta.exceptions import PkgMetaConfigFileError
        file = self.write_config('\n')
        with self.assertRaises(PkgMetaConfigFileError) as error:
            self.make_one(file)
        self.assertEqual(str(error.exception),
                         "Missing a repository definition")

    def test_invalid_default_value(self):
        from pkgmeta.exceptions import PkgMetaConfigFileError
        content = """\
[pkgmeta]
default = nothere

[repo]
"""
        file = self.write_config(content)
        with self.assertRaises(PkgMetaConfigFileError) as error:
            self.make_one(file)
        self.assertEqual(str(error.exception),
                         "Invalid default repository")

    def test_correct_init_values(self):
        location = tempfile.mkdtemp()
        file = self.write_config(TEST_PKGMETA_CFG % dict(location=location))
        config = self.make_one(file)
        default_repo = config.get_repository_config()
        self.assertEqual(default_repo.name, 'repo2')
        # Check to see if the configuration variables made it through
        from pkgmeta.storage import FileSystemStorage
        repo3 = config.get_repository_config('repo3')
        self.assertTrue(isinstance(repo3.storage, FileSystemStorage))
