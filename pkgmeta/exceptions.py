# -*- coding: utf-8 -*-

__all__ = ('ConfigNotFound', 'RepositoryIsNotMutable',)
 

class ConfigNotFound(Exception):
    """Configuration could not be found"""


class RepositoryIsNotMutable(Exception):
    """Repositories are not mutable once they have been read in."""

