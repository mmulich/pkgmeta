# -*- coding: utf-8 -*-
import os
from collections import Mapping
from pkgmeta.exceptions import UnknownRepositoryStorageType
from pkgmeta.releases import ReleaseSet
from pkgmeta.metadata import Metadata

def lookup_storage_by_type(type):
    types = dict(STORAGE_TYPES)
    try:
        return types[type]
    except KeyError:
        raise UnknownRepositoryStorageType(type)

def _releaseset_from_fs(path):
    """Initialize a pkgmeta.releases.ReleaseSet from a filesystem path."""
    releases = []
    for release in os.listdir(path):
        metadata_file = os.path.join(path, release, 'METADATA')
        metadata = Metadata(path=metadata_file)
        releases.append(metadata)
    return ReleaseSet(releases)


class FileSystemStorage(Mapping):
    """Storage on the filesystem."""

    def __init__(self, config, location=None):
        self.config = config
        self.location = location

        path = self.location
        # ??? What do we do when the path doesn't exist?
        if not os.path.isdir(path):
            raise RuntimeError("Expected a distribution metadata structure "
                               "at %s, but found a file instead." % \
                               self.location)
        structure = os.walk(path)
        root, dist_dirs = next(structure)[:2]
        self._root = root
        self._data = {dist:_releaseset_from_fs(os.path.join(root, dist))
                      for dist in dist_dirs}

    # ############################### #
    #   Abstract method definitions   #
    # ############################### #

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)


FS_STORAGE_TYPE = 'fs'

STORAGE_TYPES = [
    (FS_STORAGE_TYPE, FileSystemStorage,),
    ]
