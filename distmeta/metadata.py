# -*- coding: utf-8 -*-
import os
from UserDict import IterableUserDict
from distutils2.version import get_version_predicate
from distutils2.metadata import DistributionMetadata as DM

__all__ = ('MetadataRepository', 'ReleaseSet',)


class DistributionMetadata(DM):
    """Subclass of distutils2.metadata.DistributionMetadata to add comparison
    operators."""

    @property
    def normalized_version(self):
        return self.version

    @property
    def _comparison_parts(self):
        return (self['Name'], self.normalized_version,)

    def _cannot_compare(self, other):
        raise TypeError("cannot compare %s and %s"
                % (type(self).__name__, type(other).__name__))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            self._cannot_compare(other)
        return self._comparison_parts == other._comparison_parts

    def __lt__(self, other):
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    # See http://docs.python.org/reference/datamodel#object.__hash__
    ##def __hash__(self):
    ##    return hash(self.normalized_version)
