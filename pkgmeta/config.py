# -*- coding: utf-8 -*-
import os
import sysconfig

__all__ = ('PkgMetaConfig', 'RepositoryConfig',)

# FIXME: Should be using packaging.resources.get_file{_path}, but these are
#        currently not working in the tests because of missing logic in
#        packaging.command.test.


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

    def list_repositories(self):
        """List available repositories."""
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

    def __init__(self, name, sources=None):
        self.name = name
        self.sources = sources
        if self.sources is None:
            self.sources = []
