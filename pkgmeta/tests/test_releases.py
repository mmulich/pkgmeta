# -*- coding: utf-8 -*-
import os
from pkgmeta.tests import unittest
from pkgmeta.tests.base import BaseTestCase
from pkgmeta.tests.mock_metadata import SOAPBAR
from pkgmeta.tests.utils import populate_repo


class TestReleaseSet(BaseTestCase):

    def setUp(self):
        super(TestReleaseSet, self).setUp()
        populate_repo([SOAPBAR], self.repo_directory)

    def tearDown(self):
        super(TestReleaseSet, self).tearDown()

    def makeOne(self):
        from pkgmeta.releases import ReleaseSet
        dist_name = SOAPBAR[0]['name']
        release_path = os.path.join(self.repo_directory, dist_name)
        return ReleaseSet.from_directory(release_path)

    def test_from_directory(self):
        release_set = self.makeOne()
        release_count = len(SOAPBAR[1])
        self.assertEqual(len(release_set), release_count)

    def test_order(self):
        #: Ensure they are out of order first by shifting them.
        def shift(l, n):
            if len(l):
                n = n % len(l)
            else:
                n = 0
            return l[n:] + l[:n]
        from pkgmeta.releases import ReleaseSet
        orig_release_set = self.makeOne()
        release_set = ReleaseSet(shift(orig_release_set.releases, 7))
        #: Reset the order via the private method called at __init__ time.
        release_set._reorder()
        #: Check to see if the order is correct by rolling through the
        #  versions list.
        str_ify = lambda l: '|'.join(l)
        versions = SOAPBAR[1]
        self.assertEqual(str_ify(versions),
                         str_ify([m['Version'] for m in release_set.releases]))
