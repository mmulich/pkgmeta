# -*- coding: utf-8 -*-
import os
from collections import Mapping
try:
    import cPickle as pickle
except ImportError:
    import pickle

from pkgmeta.metadata import Metadata
from pkgmeta.releases import ReleaseSet
from pkgmeta.exceptions import RepositoryIsNotMutable

__all__ = ('Repository',)


class Repository(Mapping):
    """A repository of Python distribution metadata. The structure is
    organized by package name then by release (version)."""

    def __init__(self, _data={}, **kwargs):
        #: Initialize the data in a dictionary of package names (keys)
        #  with a list of versions (values).
        if not isinstance(_data, dict):
            raise TypeError("First argument should be a dictionary object")
        self._data = _data
        self._data.update(kwargs)

    @classmethod
    def from_directory(cls, path):
        """Initialize the data from a filesystem directory structure."""
        from_init_name = 'from_directory'
        path = os.path.abspath(path)

        if not os.path.exists(path):
            raise Exception("Can't find the repository location at %s"
                            % location)
        elif not os.path.isdir(path):
            raise Exception("Expected a distribution metadata structure at "
                            "%s, but found a file instead." % self.location)

        structure = os.walk(path)
        root, dist_dirs = next(structure)[:2]
        data = {dist:ReleaseSet.from_directory(os.path.join(root, dist))
                for dist in dist_dirs}
        inst = cls(data)
        inst.path = path
        inst.__from__ = from_init_name
        return inst

    def __repr__(self):
        cls_name = self.__class__.__name__
        if hasattr(self, '__from__'):
            cls_init = '.'.join([cls_name, self.__from__])
        else:
            cls_init = cls_name
        if hasattr(self, 'path'):
            representation = '%s("%s")' % (cls_init, self.path)
        else:
            releases_repr = ', '.join([repr(x) for x in self._data])
            representation = '<%s of %s>' % (cls_name, releases_repr)
        return representation

    # ############################### #
    #   Abstract method definitions   #
    # ############################### #

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return self._data.__iter__()

    def __len__(self):
        return len(self._data)

    # ############## #
    #   Public API   #
    # ############## #

    def search(self, search_callable, property_names=['name']):
        if not hasattr(search_callable, '__call__'):
            # Must be a callable that returns a boolean
            raise TypeError()
        if not hasattr(property_names, '__iter__'):
            # Must be a sequence
            property_names = [property_names]
        search_results = []
        for prop in property_names:
            ##search_results.extend([rs for rs in self._data
            ##                       if search_callable(getattr(rs, prop))])
            for release_set in self._data.values():
                if search_callable(getattr(release_set, prop)):
                    search_results.append(release_set)
        return set(search_results)

