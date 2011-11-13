# -*- coding: utf-8 -*-
from pkgmeta.exceptions import UnknownRepositoryStorageType


def lookup_storage_by_type(type):
    types = dict(STORAGE_TYPES)
    try:
        return types[type]
    except KeyError:
        raise UnknownRepositoryStorageType(type)


class FileSystemStorage:
    """Storage on the filesystem."""

    def __init__(self, config, location=None):
        self.config = config
        self.location = location


FS_STORAGE_TYPE = 'fs'

STORAGE_TYPES = [
    (FS_STORAGE_TYPE, FileSystemStorage,),
    ]
