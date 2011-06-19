# -*- coding: utf-8 -*-
"""
Create a Python metadata repository from a Python Package Index.
"""
import os
import logging
import argparse
from packaging.errors import IrrationalVersionError
from packaging.pypi.simple import Crawler, DEFAULT_SIMPLE_INDEX_URL

from pkgmeta.index2repo.config import LOGGER_NAME


def main():
    parser = argparse.ArgumentParser("Index to Repository")
    parser.add_argument('-d', '--debug', action='store_true', default=False)

    args = parser.parse_args()
    logger = logging.getLogger(LOGGER_NAME)

    if args.debug:
        logger.setLevel(logging.DEBUG)

    package_downloads = os.path.join(os.curdir, 'downloads')
    package_downloads = os.path.abspath(package_downloads)
    if not os.path.exists(package_downloads):
        os.mkdir(package_downloads)

    
    crawler = Crawler(follow_externals=False)
    projects = crawler.search_projects('')

    # XXX Randomly selection a sample from ~16000 packages with 20% error
    #     acceptance, so about 40 packages in the sample size
    _sample_size = 40
    count = 0
    new_projects_list = []
    from random import choice
    logger.info("Randomly sampling:")
    # XXX special cases that should be tests =/
    # Insert special case: Yarrow 1.2 Download IO error
    # Insert special case: sake 0.0 Download URL error
    special_cases = ('sake', 'Yarrow')
    for p in projects:
        if p.name in special_cases:
            logger.info("Selecting special case: {0}".format(p.name))
            count += 1
            new_projects_list.append(p)
    # end special cases
    while count != _sample_size:
        p = choice(projects)
        if p not in new_projects_list:
            logger.info("  Selecting: {0}".format(p.name))
            new_projects_list.append(p)
            count += 1
    projects = new_projects_list
    # XXX end sample size block

    for project in projects:
        package_name = project.name
        package_dir = os.path.join(package_downloads, package_name)
        if not os.path.exists(package_dir):
            os.mkdir(package_dir)
        logger.debug("Downloading {0} to {1}".format(package_name,
                                                     package_dir))
        releases = crawler.get_releases(package_name, force_update=True)
        for release_info in releases:
            version = str(release_info.version)
            download_dir = os.path.join(package_dir, version)
            if not os.path.exists(download_dir):
                os.mkdir(download_dir)
            # FIXME It'd be nice if I could say where it was being
            #       downloaded from...
            logger.info("  Downloading {0} ({1})...".format(package_name,
                                                       version))
            try:
                release_info.download(download_dir)
            except IrrationalVersionError as err:
                logger.error("    Unable to download {0} ({1}) because it "
                             "contains an irrational "
                             "version.".format(package_name, version))
            # XXX Temp: see http://bugs.python.org/issue12366
            #     - ValueError from sake 0.0.0
            #     - IOError from Yarrow 1.2
            except (ValueError, IOError) as err:
                logger.error("    Problem downloading {0} ({1}): \n{2}"\
                             .format(package_name, version, err))

    return 0


run = main

if __name__ == '__main__':
    main()
