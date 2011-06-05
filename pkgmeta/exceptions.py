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

