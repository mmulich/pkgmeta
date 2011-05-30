# -*- coding: utf-8 -*-
import os
import tempfile
import shutil
from pkgmeta.tests import unittest


class BaseTestCase(unittest.TestCase):
    """Base test case to set up the repository location."""

    def setUp(self):
        self.repo_location = tempfile.mkdtemp('-repo', 'dist-metadata-')

    def tearDown(self):
        shutil.rmtree(self.repo_location)
