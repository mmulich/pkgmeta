# -*- coding: utf-8 -*-
import sys
import io
import argparse
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import ALL_DISTS, SOLARCAL
from pkgmeta.tests.utils import populate_repo


class SearchSubcommandTestCase(BaseTestCase):

    def _make_one(self):
        from pkgmeta.cli import SearchCommand
        parser = argparse.ArgumentParser(SearchCommand.__doc__)
        return parser, SearchCommand(parser)        

    def setUp(self):
        super(SearchSubcommandTestCase, self).setUp()
        self._orig_stdout = sys.stdout
        self.stdout = io.StringIO()
        sys.stdout = self.stdout
        # Repository configuration
        from pkgmeta.config import RepositoryConfig
        name = 'test'
        location = self.repo_directory
        self.repo_config = RepositoryConfig(name, location)
        # Populate repository
        populate_repo(ALL_DISTS, self.repo_directory)

    def tearDown(self):
        sys.stdout = self._orig_stdout
        try:
            del self._output_lines
        except AttributeError:
            pass

    def _get_output_lines(self):
        if not hasattr(self, '_output_lines'):
            self.stdout.seek(0)
            readlines = self.stdout.readlines
            self._output_lines = [line.strip() for line in readlines()]
        return self._output_lines

    def test_simple_term_search(self):
        parser, command = self._make_one()
        args_namespace = parser.parse_args(['cal'])

        command(self.repo_config, args_namespace)

        output = self._get_output_lines()
        # FIXME: Hardcoded result values. Use the mock data to populate these
        #        in off chance that the mock data is changed.
        expected_output = """\
p   solarcal          - Calendar based on solar dates.
p   webcal            - Web calendaring application""".split('\n')
        self.assertEqual(output, expected_output)
