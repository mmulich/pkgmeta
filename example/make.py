# -*- coding: utf-8 -*-
"""Used to make an example filesystem based repository."""
import os
from pkgmeta.config import PkgMetaConfig
from pkgmeta.repository import Repository
from pkgmeta.tests.mock_metadata import ALL_DISTS
from pkgmeta.tests.utils import populate_repo

HERE = os.path.abspath(os.path.dirname(__file__))

def main():
    # Must create the repository location before we read in the configuration.
    repository_location = os.path.expanduser('~/example-main')
    if not os.path.exists(repository_location):
        print("Creating the main repository directory.")
        os.mkdir(repository_location)

        print("Populating repository with example data...")
        populate_repo(ALL_DISTS, repository_location)

    cfg_file = os.path.join(HERE, 'example.cfg')
    print("Using configuration: %s" % cfg_file)

    print("Read configuration...")
    config = PkgMetaConfig.from_file(cfg_file)
    repo_config = config.get_repository_config()

    repo = Repository(repo_config)
    print("Loaded %s distributions into the repository" % len(repo))

if __name__ == '__main__':
    main()
