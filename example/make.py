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
    repository_location = os.path.expanduser('~/example-repo')
    if not os.path.exists(repository_location):
        print("Creating the repository directory:  %s" % repository_location)
        os.mkdir(repository_location)

        print("Populating repository with example data...")
        populate_repo(ALL_DISTS, repository_location)

    cfg_file_in = os.path.join(HERE, 'example.cfg.in')
    cfg_file = os.path.expanduser('~/example.cfg')
    with open(cfg_file, 'w') as out_file:
        with open(cfg_file_in, 'r') as in_file:
            out_file.write(in_file.read() % repository_location)
    print("Writing configuration:  %s" % cfg_file)

    print("Reading configuration...")
    config = PkgMetaConfig.from_file(cfg_file)
    repo_config = config.get_repository_config()

    repo = Repository(repo_config)
    print("Loaded %s distributions into the repository" % len(repo))
    print("-" * 80)
    print("You can now use the example data by supplying the pkgmeta script "
          "with the configuration file flag:  -c ~/example.cfg")

if __name__ == '__main__':
    main()
