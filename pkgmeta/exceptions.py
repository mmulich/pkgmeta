# -*- coding: utf-8 -*-

__all__ = ('ConfigNotFound', 'RepositoryIsNotMutable',)
 

class ConfigNotFound(Exception):
    """Configuration could not be found"""


class ConfigReadError(Exception):
    """Configuration could not be read in."""

    def __init__(self, message=''):
        self.message = message


class RepositoryIsNotMutable(Exception):
    """Repositories are not mutable once they have been read in."""


class RepositoryNotFound(Exception):
    """The repository could not be found a the specified location."""


class ReleaseNotFound(KeyError):
    """A release set could not be found for the requested package."""
