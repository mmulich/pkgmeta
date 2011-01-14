# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest
from distmeta.tests.base import BaseTestCase
from distmeta.tests.utils import populate_repo, SOAPBAR


class TestReleaseSet(BaseTestCase):

    def setUp(self):
        super(TestReleaseSet, self).setUp()
        populate_repo([SOAPBAR], self.repo_location)
        self.release_set = self.makeOne()

    def tearDown(self):
        del self.release_set
        super(TestReleaseSet, self).tearDown()

    def makeOne(self):
        from distmeta.releases import ReleaseSet
        dist_name = SOAPBAR[0]['name']
        release_path = os.path.join(self.repo_location, dist_name)
        return ReleaseSet.from_path(release_path)

    def test_from_path(self):
        release_count = len(SOAPBAR[1])
        self.assertEqual(len(self.release_set), release_count)

    def test_order(self):
        #: Ensure they are out of order first by shifting them.
        def shift(l, n):
            if len(l):
                n = n % len(l)
            else:
                n = 0
            return l[n:] + l[:n]
        from distmeta.releases import ReleaseSet
        release_set = ReleaseSet(shift(self.release_set, 7))
        #: Reset the order via the private method called at __init__ time.
        release_set.sort()
        #: Check to see if the order is correct by rolling through the
        #  versions list.
        str_ify = lambda l: '|'.join(l)
        versions = SOAPBAR[1]
        self.assertEqual(str_ify(versions),
                         str_ify([m['Version'] for m in release_set]))
