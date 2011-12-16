# -*- coding: utf-8 -*-
import os
from collections import MutableMapping

from pkgmeta.exceptions import ReleaseNotFound
from pkgmeta.config import RepositoryConfig
from pkgmeta.metadata import Metadata
from pkgmeta.releases import ReleaseSet

__all__ = ('Repository',)


class Repository(MutableMapping):
    """A repository of Python distribution metadata. The structure is
    organized by package name then by release (version)."""

    def __init__(self, config):
        self.config = config
        self.storage = self.config.storage  # For convenience

    # ############################### #
    #   Abstract method definitions   #
    # ############################### #

    def __getitem__(self, key):
        try:
            return self.storage[key]
        except KeyError:
            raise ReleaseNotFound(key)

    def __iter__(self):
        return self.storage.__iter__()

    def __len__(self):
        return len(self.storage)

    def __setitem__(self, key, value):
        if not isinstance(value, ReleaseSet):
            raise TypeError("Expected a pkgmeta.releases.ReleaseSet, "
                            "received '%s'" % type(value))
        self.storage[key] = value

    def __delitem__(self, key):
        del self.storage[key]

    # ############## #
    #   Public API   #
    # ############## #

    def search(self, search_callable, property_names=['name']):
        if not hasattr(search_callable, '__call__'):
            # Must be a callable that returns a boolean
            raise TypeError()
        if not (isinstance(property_names, list) \
                or isinstance(property_names, tuple)):
            # Must be a sequence
            property_names = [property_names]
        search_results = []
        for prop in property_names:
            ##search_results.extend([rs for rs in self._data
            ##                       if search_callable(getattr(rs, prop))])
            for release_set in self.storage.values():
                if search_callable(getattr(release_set, prop)):
                    search_results.append(release_set)
        return set(search_results)
