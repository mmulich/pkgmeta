# -*- coding: utf-8 -*-
import os
import tempfile
import shutil
from pkgmeta.tests import unittest


class BaseTestCase(unittest.TestCase):
    """Base test case to set up the repository location."""

    def setUp(self):
        self.repo_directory = tempfile.mkdtemp('-repo', 'pkg-metadata-')
        nil, self.repo_pickle = tempfile.mkstemp('.pickle', 'pkg-metadata-')
        del nil

    def tearDown(self):
        shutil.rmtree(self.repo_directory)
        os.remove(self.repo_pickle)
