# -*- coding: utf-8 -*-
from pkgmeta.storage import lookup_storage_by_type
__all__ = ('PkgMetaConfig',
           'RepositoryConfig', 'FileSystemRepositoryConfig',
           )


class PkgMetaConfig(object):
    """Configuration
    """

    def __init__(self, repositories, default=None):
        if not hasattr(repositories, '__iter__'):
            repositories = [repositories]
        self.repositories = repositories
        for repo in self.repositories:
            if not isinstance(repo, RepositoryConfig):
                raise TypeError("%s is not a RepsitoryConfig" % repr(repo))
        if default is None:
            self.default = repositories[0].name

    def __iter__(self):
        return iter(self.repositories)

    def get_repository_config(self, name=None):
        """Get a RepositoryConfig by name. If name is not given,
        the default repository will be returned."""
        if name is None:
            name = self.default
        try:
            repo_config = [r for r in self.repositories if r.name == name][0]
        except IndexError:
            raise LookupError("Could not find '%s'" % name)
        return repo_config


class RepositoryConfig:
    """A repository configuration"""

    def __init__(self, name, type=None, sources=None,
                 **kwargs):
        self.name = name
        self.type = type
        self.sources = sources
        if self.sources is None:
            self.sources = []
        storage_factory = lookup_storage_by_type(self.type)
        self.storage = storage_factory(self, **kwargs)
