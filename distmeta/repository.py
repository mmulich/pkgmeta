# -*- coding: utf-8 -*-
import os
from UserDict import DictMixin
from distmeta.metadata import DistributionMetadata
from distmeta.releases import ReleaseSet

__all__ = ('MetadataRepository',)


class MetadataRepository(object, DictMixin):
    """A repository of Python distribution metadata stored in a directory
    structure on the file system. The structure would organized by
    distribution name then by release (or version)."""

    def __init__(self, data=[]):
        #: Intialize the data in a dictionary of distribution names
        #  (keys) with a list of versions (values).
        self._data = data

    @classmethod
    def from_path(cls, path):
        """Initialize the data in self._repo from a filesystem structure."""
        if not os.path.exists(path):
            raise Exception("Can't find the repository location at %s"
                            % location)
        elif not os.path.isdir(path):
            raise Exception("Expected a distribution metadata structure at "
                            "%s, but found a file instead." % self.location)
        structure = os.walk(path)
        root, dist_dirs = structure.next()[:2]
        data = [ReleaseSet.from_path(os.path.join(root, dist))
                for dist in dist_dirs]
        inst = cls(data)
        inst.path = path
        return inst

    def __repr__(self):
        cls_name = self.__class__.__name__
        if hasattr(self, 'path'):
            abs_location = os.path.abspath(self.path)
            return '%s.from_path("%s")' % (cls_name, abs_location)
        releases_repr = ', '.join([repr(x) for x in self._data])
        return '<%s of %s>' % (cls_name, releases_repr)

    def __setitem__(self, key, value):
        if key in self:
            raise NotImplementedError("Not sure what to do yet.")
        if isinstance(value, ReleaseSet):
            raise NotImplementedError("todo...")
        elif isinstance(value, DistributionMetadata):
            raise NotImplementedError("todo...")
        else:
            raise TypeError("Unknown value type: %s" % type(value))

    def __getitem__(self, key):
        release_set = None
        for rs in self._data:
            if rs.name == key:
                release_set = rs
                break
        if not release_set:
            raise KeyError("Release set for %s could not be found" % key)
        return release_set

    def keys(self):
        return [rs.name for rs in self._data]
