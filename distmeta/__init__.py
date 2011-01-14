# -*- coding: utf-8 -*-
import os
from UserDict import IterableUserDict
from distutils2.version import get_version_predicate
from distutils2.metadata import DistributionMetadata

__all__ = ('MetadataRepository', 'ReleaseSet',)


class ReleaseSet(list):
    """A set of releases for a distribution ordered by version number.

    Initialized by an optional list of dist-info directories.
    """

    def __init__(self, iterable=[]):
        super(ReleaseSet, self).__init__(iterable)
        self._reorder()

    def _reorder(self):
        """Reorder the releases by version number from lowest (0) to highest.
        """
        pass

    @classmethod
    def from_path(cls, path):
        """Initialize the set from a filesystem path."""
        releases = []
        for release in os.listdir(path):
            metadata_file = os.path.join(path, release, 'METADATA')
            metadata = DistributionMetadata(path=metadata_file)
            releases.append(metadata)
        return cls(releases)

    @property
    def name(self):
        try:
            name = self[0].get('Name')
        except IndexError:
            name = 'UNKNOWN'
        return name


class MetadataRepository(IterableUserDict):
    """A repository of Python distribution metadata stored in a directory
    structure on the file system. The structure would organized by
    distribution name then by release (or version)."""

    def __init__(self, location):
        IterableUserDict.__init__(self)
        self.location = location
        if not os.path.exists(self.location):
            raise Exception("Can't find the repository location at %s"
                            % location)
        #: Intialize the data in a dictionary of distribution names
        #  (keys) with a list of versions (values).
        self._init_repo()

    def _init_repo(self):
        """Initialize the data in self._repo from a filesystem structure."""
        if not os.path.isdir(self.location):
            raise Exception("Expected a distribution metadata structure at "
                            "%s, but found a file instead." % self.location)
        for dist in os.listdir(self.location):
            dist_path = os.path.join(self.location, dist)
            if dist.startswith('.') \
               or os.path.isfile(dist_path) \
               or os.path.islink(dist_path):
                #: Nevermind, it's not a distribution...
                continue
            for version in os.listdir(dist_path):
                if dist not in self.data:
                    self.data[dist] = []
                metadata_file = os.path.join(dist_path, version, 'METADATA')
                if os.path.exists(metadata_file):
                    self.data[dist].append(version)
                else:
                    # XXX Need to warn the user that the metadata is missing!
                    pass

    def __repr__(self):
        cls_name = self.__class__.__name__ 
        abs_location = os.path.abspath(self.location)
        return '%s("%s")' % (cls_name, abs_location)
