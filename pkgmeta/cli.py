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
    cmds = {}  # Instantiated subcommand
    cmd_clses = {}  # Subcommand classes
    def __getitem__(self, key):
        return self.cmds[key]
    def __setitem__(self, key, value):
        self.cmds[key] = value
    def __delitem__(self, key):
        del self.cmds[key]
    def __iter__(self):
        self.cmds.__iter__()
    def __len__(self):
        return len(self.data)

    def add(self, cls):
        self.cmd_clses[cls.name] = cls

    def init_subcommands(self, subparsers):
        """Command initiallization using an argparse subparsers object."""
        if not isinstance(subparsers, argparse._SubParsersAction):
            raise TypeError("Expected an argparse._SubParsersAction object")
        for name, command_class in self.cmd_clses.items():
            self.cmds[name] = command_class(subparsers)

commands = CommandRegistry()


# ################ #
#   Sub-commands   #
# ################ #

class BaseCommand:
    """Base sub-command class"""

    name = None

    def __init__(self, subparsers):
        command_parser = subparsers.add_parser(self.name, help=self.__doc__)

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

commands.add(UpdateCommand)


class SearchCommand(BaseCommand):
    """Search the repository for packages"""
    name = 'search'

    def cmd(self, namespace):
        
        print(self.name)
        pass

commands.add(SearchCommand)


class ShowCommand(BaseCommand):
    """Show a package's metadata"""
    name = 'show'

    def cmd(self, namespace):
        pass

commands.add(ShowCommand)


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
    commands.init_subcommands(subparsers)
    # parser_search = subparsers.add_parser('search',
    #                                       help="search the repository")
    # parser_update = subparsers.add_parser('update',
    #                                       help="update the repository")
    # parser_search.add_argument('search-terms', nargs='+',
    #                            help="list of of search criteria")
    args = parser.parse_args()

    # Process action
    cmd = commands[args.command]
    return cmd(args)


run = main

if __name__ == '__main__':
    main()
