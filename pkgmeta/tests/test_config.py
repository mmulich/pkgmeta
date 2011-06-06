# -*- coding: utf-8 -*-
import os
import sysconfig
import tempfile
from pkgmeta.tests import unittest


TEST_PKGMETA_CFG = """\
[global]
root = {appdata.persistent}
cache = {appdata.disposable}

[test1-repo]
sources =
    %(source_one)s

[test2-repo]
sources =
    %(source_two)s
    %(source_one)s
"""

SOURCES = {'source_one': 'file:///', 'source_two': 'file:///'}


class PkgMetaConfigTestCase(unittest.TestCase):

    def setUp(self):
        # Testing config file
        self.pkgmeta_cfg = tempfile.mkstemp('.cfg', 'pkgmeta-')[1]

    def tearDown(self):
        os.remove(self.pkgmeta_cfg)

    def _init_config(self, sources=SOURCES):
        with open(self.pkgmeta_cfg, 'w') as f:
            f.write(TEST_PKGMETA_CFG % sources)        

    def _make_one(self, cfg=None):
        from pkgmeta.config import PkgMetaConfig
        if cfg is not None:
            return PkgMetaConfig(cfg)
        return PkgMetaConfig()

    def test_global_config_section_missing(self):
        # No global config section found in the config
        from pkgmeta.exceptions import ConfigReadError
        with open(self.pkgmeta_cfg, 'w') as f:
            f.write('[no-global-but-not-empty]')
        with self.assertRaises(ConfigReadError) as err:
            self._make_one(self.pkgmeta_cfg)
        self.assertEqual(err.exception.message, "[global] section missing.")

    def test_partial_necessary_configuration(self):
        # Partial config without the root option
        from pkgmeta.exceptions import ConfigReadError
        with open(self.pkgmeta_cfg, 'w') as f:
            f.write("[global]")
        with self.assertRaises(ConfigReadError) as err:
            self._make_one(self.pkgmeta_cfg)
        self.assertEqual(err.exception.message,
                         "[global] section missing a root value")

    def test_global_config_vars_load(self):
        self._init_config()
        # Testing config
        from pkgmeta import config
        # Two in one test, since we aren't giving the configuratin a pkgmeta.cfg path.
        config.PKGMETA_CFGS = [self.pkgmeta_cfg]
        # Without a cfg path argument, the object will instantiate with the first value in
        # PKGMETA_CFGS.
        config = self._make_one()
        self.assertEqual(config._file, self.pkgmeta_cfg)
        self.assertEqual(config.root, sysconfig.get_paths()['appdata.persistent'])
        self.assertEqual(config.cache, sysconfig.get_paths()['appdata.disposable'])

    def test_list_repositories(self):
        self._init_config()
        # List configuration
        config = self._make_one(self.pkgmeta_cfg)
        self.assertEqual(config.list_repositories(), ['test1-repo', 'test2-repo'])

    def test_get_repository_config_default(self):
        from pkgmeta.config import RepositoryConfig
        # get_repository_config method test
        self._init_config()
        config = self._make_one(self.pkgmeta_cfg)
        # Test without a repository name, should get the first listed repository.
        repo_config = config.get_repository_config()
        self.assertTrue(isinstance(repo_config, RepositoryConfig))
        self.assertEqual(repo_config.name, 'test1-repo')

    def test_get_repository_config_with_name(self):
        source_one = 'file:///home/repouser'
        source_two = 'http://localhost:8020'
        self._init_config(sources=dict(source_one=source_one, source_two=source_two))
        config = self._make_one(self.pkgmeta_cfg)
        # Second test with a specific repository name
        repo_name = 'test2-repo'
        repo_config = config.get_repository_config(repo_name)
        self.assertEqual(repo_config.sources, [source_two, source_one])
        repo_location = os.path.join(sysconfig.get_paths()['appdata.persistent'], repo_name)
        self.assertEqual(repo_config.location, repo_location)