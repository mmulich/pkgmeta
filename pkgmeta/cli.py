# -*- coding: utf-8 -*-
"""Command line interface (CLI) to the repository through a series of
sub commands.
"""
import os
import sys
import argparse
from collections import MutableMapping

# FIXME: Get the default config from pkgmeta.config when available.
DEFAULT_CONFIG = None


class CommandRegistry(MutableMapping):
    """A registry of commands added by name."""
    data = {}
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        del self.data[key]
    def __iter__(self):
        self.data.__iter__()
    def __len__(self):
        return len(self.data)

    def add(self, c):
        self[c.name] = c

commands = CommandRegistry()


# ################ #
#   Sub-commands   #
# ################ #

class BaseCommand:
    """Base sub-command class"""

    name = None

    def __call__(self, namespace):
        self.cmd(namespace)

    def cmd(self, namespace):
        """Command logic"""
        raise NotImplementedError


class UpdateCommand(BaseCommand):
    """Update the repository from the sources list"""
    name = 'update'

    def cmd(self, namespace):
        """Read in the source.list, download the sources and update
        the repository."""
        pass

commands.add(UpdateCommand())


class SearchCommand(BaseCommand):
    """Search the repository"""
    name = 'search'

    def cmd(self, namespace):
        
        print(self.name)
        pass

commands.add(SearchCommand())


class ShowCommand(BaseCommand):
    """Show a package's metadata"""
    name = 'show'

    def cmd(self, namespace):
        pass

commands.add(ShowCommand())


def main():
    """CLI main function"""
    parser = argparse.ArgumentParser(description="Tool for working with a "
                                     "Python package repository")
    parser.add_argument('-c', '--configuration', metavar='CONFIG', nargs=1,
                        default=DEFAULT_CONFIG,
                        help="repository configuration file location "
                        "(default: \"%s\")." % DEFAULT_CONFIG)
    subparsers = parser.add_subparsers(dest="command",
                                       help="sub-commands, use --help with "
                                       "action for more help")
    parser_search = subparsers.add_parser('search',
                                          help="search the repository")
    parser_update = subparsers.add_parser('update',
                                          help="update the repository")
    parser_search.add_argument('search-terms', nargs='+',
                               help="list of of search criteria")
    args = parser.parse_args()

    # Process action
    cmd = commands[args.command]
    return cmd(args)


run = main

if __name__ == '__main__':
    main()
