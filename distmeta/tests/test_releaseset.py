# -*- coding: utf-8 -*-
import os
from distmeta.tests import unittest
from distmeta.tests.base import BaseTestCase
from distmeta.tests.utils import populate_repo, SOAPBAR


class TestReleaseSet(BaseTestCase):
    """ """

    def setUp(self):
        super(TestReleaseSet, self).setUp()
        populate_repo(SOAPBAR)
        
