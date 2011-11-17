# -*- coding: utf-8 -*-
"""Command line interface (CLI) to the repository through a series of
sub commands.
"""
import os
import sys
import argparse
from collections import MutableMapping

from pkgmeta.config import PkgMetaConfig
from pkgmeta.repository import Repository

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
            command_help = command_class.__doc__
            command_parser = subparsers.add_parser(name,
                                                   help=command_help)
            self.cmds[name] = command_class(command_parser)

commands = CommandRegistry()


# ################ #
#   Sub-commands   #
# ################ #

class BaseCommand:
    """Base sub-command class"""

    name = None

    def __init__(self, parser):
        self.command_parser = parser

    def __call__(self, repo_config, namespace):
        # In the future we may want to do things here.
        self.cmd(repo_config, namespace)

    def cmd(self, repo_config, namespace):
        """Command logic"""
        raise NotImplementedError


class UpdateCommand(BaseCommand):
    """Update the repository from the sources list"""
    name = 'update'

    def cmd(self, repo_config, namespace):
        """Read in the source.list, download the sources and update
        the repository."""
        pass

commands.add(UpdateCommand)


class SearchCommand(BaseCommand):
    """Search the repository for packages"""
    name = 'search'

    def __init__(self, parser):
        super(SearchCommand, self).__init__(parser)
        self.command_parser.add_argument('search_terms', nargs='+',
                                         help="list of of search criteria")

    def cmd(self, repo_config, namespace):
        repo = Repository(repo_config)
        search_terms = namespace.search_terms
        # FIXME: Simple search with a lack of features
        _search = lambda s: True in [s.find(term) >= 0 for term in search_terms]
        releases = repo.search(_search)
        # TODO: It'd be great if we have some kind of formatting adapter here.
        for release in releases:
            state = 'p'  # FIXME: other states besides just package?
            o = "{state:{fill}{align}4}{release.name:{fill}{align}17} - " \
                "{summary:{fill}{align}56}".format(state=state, release=release,
                                            summary=release.get('summary'),
                                            fill=' ', align='<')
            print(o)
            

commands.add(SearchCommand)


class ShowCommand(BaseCommand):
    """Show a package's metadata"""
    name = 'show'

    def __init__(self, parser):
        super(ShowCommand, self).__init__(parser)
        self.command_parser.add_argument('package_name', nargs=1,
                                         help="package to be shown")

    def cmd(self, repo_config, namespace):
        repo = Repository(repo_config)
        package = namespace.package_name[0]
        release_set = repo[package]
        for property_name, value in release_set.items():
            if isinstance(value, list):
                value = ', '.join(value)
            if not value:
                continue
            o = "{0}: {1}".format(property_name, value)
            print(o)

commands.add(ShowCommand)


def main():
    """CLI main function"""
    parser = argparse.ArgumentParser(description="Tool for working with a "
                                                 "Python package repository")
    parser.add_argument('-c', '--configuration', metavar='CONFIG', nargs=1,
                        default=DEFAULT_CONFIG,
                        help="repository configuration file location")
    parser.add_argument('-r', '--repository-name', nargs=1,
                        # Default is handled by the
                        # Config.get_repository_config method.
                        help="a specific non-default repository name, "
                             "defaults to the default repository")
    subparsers = parser.add_subparsers(dest="command",
                                       help="sub-commands, use --help with "
                                            "action for more help")
    commands.init_subcommands(subparsers)

    args = parser.parse_args()

    # Process action
    cmd = commands[args.command]
    # Retrieve the repository configuration
    config = PkgMetaConfig.from_file(args.configuration)
    repo_config = config.get_repository_config(args.repository_name)
    # Run the command
    return cmd(repo_config, args)

run = main

if __name__ == '__main__':
    main()
