# coding: utf-8

"""
    Ticketmaster Discovery API

    Swagger spec based on Ticketmaster Discovery API

    OpenAPI spec version: 1.0.0
    Contact: git@edward.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import picketer
from picketer.rest import ApiException
from picketer.models.event_images import EventImages


class TestEventImages(unittest.TestCase):
    """ EventImages unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventImages(self):
        """
        Test EventImages
        """
        model = picketer.models.event_images.EventImages()


if __name__ == '__main__':
    unittest.main()