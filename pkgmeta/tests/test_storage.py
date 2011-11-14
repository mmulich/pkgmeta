# -*- coding: utf-8 -*-
import os
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import SOAPBAR, SOLARCAL
from pkgmeta.tests.utils import make_metadata, populate_repo


class BaseStorageTestCase(unittest.TestCase):
    """Test the Abstract Base Class (ABC) implemenation is correct.
    It doesn't matter what is put in the storage as long as it acts
    like a mapping."""

    @property
    def target_cls(self):
        from pkgmeta.storage import BaseStorage
        return BaseStorage

    def test_set_get_and_del(self):
        storage = self.target_cls(None)
        storage['key'] = 'value'
        self.assertEqual(storage['key'], 'value')
        del storage['key']
        with self.assertRaises(KeyError):
            value = storage['key']

    def test_len(self):
        storage = self.target_cls(None)
        storage['one'] = 1
        storage['two'] = 2
        self.assertEqual(len(storage), 2)

    def test_iteration(self):
        storage = self.target_cls(None)
        keys = ['one', 'two', 'three']
        for value, key in enumerate(keys):
            storage[key] = value
        keys.sort()
        iter_keys = [x for x in storage]
        iter_keys.sort()
        self.assertEqual(iter_keys, keys)


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


class FileSystemStorageTestCase(unittest.TestCase):
    """Test the FileSystem class"""

    def test_nonexistent_path_error(self):
        from pkgmeta.storage import FileSystemStorage
        path = "some/directory/you/should/not/have"
        location = os.path.join(os.curdir, path)
        with self.assertRaises(RuntimeError):
            storage = FileSystemStorage(None, location)
