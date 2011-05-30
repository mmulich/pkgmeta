# -*- coding: utf-8 -*-
import os
from collections import Mapping
from pkgmeta.metadata import Metadata

__all__ = ('ReleaseSet',)


class ReleaseSet(Mapping):
    """A set of releases for a distribution ordered by version number.

    Initialized by an optional list of dist-info directories.
    """

    def __init__(self, iterable=[]):
        self.releases = list(iterable)
        self._reorder()
        # FIXME: Find a better way to determine the stable release.
        self._stable_release = len(self) - 1

    def _reorder(self):
        """Reorder the releases by version number from lowest (0) to highest.
        """
        self.releases.sort()

    @classmethod
    def from_directory(cls, path):
        """Initialize the set from a filesystem path."""
        releases = []
        for release in os.listdir(path):
            metadata_file = os.path.join(path, release, 'METADATA')
            metadata = Metadata(path=metadata_file)
            releases.append(metadata)
        return cls(releases)

    def __hash__(self):
        release_hash = 0
        for release in self.releases:
            release_hash += hash(release)
        return len(self) + release_hash

    @property
    def name(self):
        try:
            name = self.releases[self._stable_release].get('Name')
        except IndexError:
            name = 'UNKNOWN'
        return name

    def __len__(self):
        return len(self.releases)

    def __iter__(self):
        return self.releases[self._stable_release].__iter__()

    def __getitem__(self, key):
        return self.releases[self._stable_release][key]
