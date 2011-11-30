# -*- coding: utf-8 -*-
from collections import Mapping
from configparser import ConfigParser
from pkgmeta.exceptions import PkgMetaConfigFileError
from pkgmeta.storage import lookup_storage_by_type
__all__ = ('PkgMetaConfig',
           'RepositoryConfig', 'FileSystemRepositoryConfig',
           )


class RepositoryConfig:
    """A repository configuration"""

    def __init__(self, name, type=None, sources=None,
                 **kwargs):
        self.name = name
        self.type = type
        self.sources = sources
        if self.sources is None:
            self.sources = []
        for name, value in kwargs.items():
            setattr(self, name, value)
        storage_factory = lookup_storage_by_type(self.type)
        self.storage = storage_factory(self)


class PkgMetaConfig(Mapping):
    """Main pkgmeta configuration object"""

    def __init__(self, repositories, default=None):
        if not hasattr(repositories, '__iter__'):
            repositories = [repositories]
        self.repositories = repositories
        for repo in self.repositories:
            if not isinstance(repo, RepositoryConfig):
                raise TypeError("%s is not a RepsitoryConfig" % repr(repo))
        self.default = default
        if self.default is None:
            self.default = repositories[0].name

    @classmethod
    def from_file(cls, file):
        cfg = ConfigParser(allow_no_value=True)
        cfg.read(file)
        if cfg.has_section('pkgmeta') and cfg.has_option('pkgmeta', 'default'):
            default = cfg.get('pkgmeta', 'default')
        else:
            default = None
        repositories = []
        for section in cfg.sections():
            if section == 'pkgmeta':
                continue
            # TODO Wrap config init errors with a PkgMetaConfigFileError
            config = RepositoryConfig(section, **dict(cfg.items(section)))
            repositories.append(config)
        if len(repositories) == 0:
            raise PkgMetaConfigFileError("Missing a repository definition")
        # Find the default repositories index
        if default is not None:
            repo_keys = [r.name for r in repositories]
            try:
                repo_keys.index(default)
            except ValueError as err:
                raise PkgMetaConfigFileError("Invalid default repository")
        inst = cls(repositories, default=default)
        setattr(inst, '__from__', 'from_file')
        setattr(inst, '_file', file)
        return inst

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

    # ############################### #
    #   Abstract method definitions   #
    # ############################### #

    def __len__(self):
        return len(self.repositories)

    def __iter__(self):
        return iter(self.repositories)

    def __getitem__(self, key):
        return self.get_repository_config(key)
