# -*- coding: utf-8 -*-
import os
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import SOAPBAR, SOLARCAL
from pkgmeta.tests.utils import make_metadata, populate_repo


class RuntimeStorageTestCase(unittest.TestCase):
    """Test the RuntimeStorage class"""

    def test_init_from_releaseset_iterable(self):
        from pkgmeta.metadata import Metadata
        from pkgmeta.releases import ReleaseSet
        #: Create a base set of releases
        releases = [ReleaseSet(make_metadata(*info, cls=Metadata))
                    for info in (SOAPBAR, SOLARCAL,)]

        from pkgmeta.storage import RuntimeStorage
        #: Make the storage object
        storage = RuntimeStorage(None, releases)
        values = list(storage)
        values.sort()
        expected_values = [r.name for r in releases]
        expected_values.sort()
        self.assertEqual(values, expected_values)
