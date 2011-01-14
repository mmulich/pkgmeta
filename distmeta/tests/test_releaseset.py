# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest
from distmeta.tests.base import BaseTestCase
from distmeta.tests.utils import populate_repo, SOAPBAR


class TestReleaseSet(BaseTestCase):
    """ """

    def setUp(self):
        super(TestReleaseSet, self).setUp()
        populate_repo([SOAPBAR], self.repo_location)
        self.release_set = self.makeOne()

    def tearDown(self):
        del self.release_set
        super(TestReleaseSet, self).tearDown()

    def makeOne(self):
        from distmeta import ReleaseSet
        dist_name = SOAPBAR[0]['name']
        release_path = os.path.join(self.repo_location, dist_name)
        return ReleaseSet.from_path(release_path)

    def test_from_path(self):
        self.fail()


    def test_order(self):
        self.fail()
