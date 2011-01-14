# -*- coding: utf-8 -*-
import os
from distmeta.metadata import DistributionMetadata

__all__ = ('ReleaseSet',)


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
        self.sort()

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
