# -*- coding: utf-8 -*-
from packaging.errors import IrrationalVersionError
from packaging.metadata import Metadata as BaseMetadata
from packaging.version import suggest_normalized_version, NormalizedVersion

__all__ = ('Metadata', 'InvalidVersion',)


class InvalidVersion(Exception):
    """An invalid version that can not be normalized by packaging."""


class Metadata(BaseMetadata):
    """Subclass of packaging.metadata.Metadata to add comparison
    operators."""

    def __repr__(self):
        name = self.get('Name')
        version = self.get('Version')
        return "<Metadata \"%s (%s)\">" % (name, version)

    @property
    def normalized_version(self):
        version = suggest_normalized_version(self['Version'])
        if version is None:
            raise InvalidVersion("cannot determine the normalized version "
                                 "for:  %s" % self['Version'])
        return NormalizedVersion(version)

    @property
    def _comparison_parts(self):
        return (self.normalized_version, self['Name'],)

    def _cannot_compare(self, other):
        raise TypeError("cannot compare %s and %s"
                % (type(self).__name__, type(other).__name__))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            self._cannot_compare(other)
        return self._comparison_parts == other._comparison_parts

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            self._cannot_compare(other)
        return self._comparison_parts < other._comparison_parts

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not (self.__lt__(other) or self.__eq__(other))

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    # See http://docs.python.org/reference/datamodel#object.__hash__
    def __hash__(self):
        return hash(self.normalized_version)
