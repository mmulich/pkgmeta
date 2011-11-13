# -*- coding: utf-8 -*-

__all__ = (
    'InvalidVersion',
    'RepositoryIsNotMutable', 'RepositoryNotFound',
    'ReleaseNotFound',
    )


class InvalidVersion(Exception):
    """An invalid version that can not be normalized by packaging."""


class RepositoryIsNotMutable(Exception):
    """Repositories are not mutable once they have been read in."""


class RepositoryNotFound(Exception):
    """The repository could not be found a the specified location."""


class ReleaseNotFound(KeyError):
    """A release set could not be found for the requested package."""

