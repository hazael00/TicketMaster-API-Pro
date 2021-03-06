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
from picketer.apis.classifications_api import ClassificationsApi


class TestClassificationsApi(unittest.TestCase):
    """ ClassificationsApi unit test stubs """

    def setUp(self):
        self.api = picketer.apis.classifications_api.ClassificationsApi()

    def tearDown(self):
        pass

    def test_classification_details(self):
        """
        Test case for classification_details

        Get classification details by ID
        """
        pass

    def test_genre_details(self):
        """
        Test case for genre_details

        Get genre details by ID
        """
        pass

    def test_search_classifications(self):
        """
        Test case for search_classifications

        Search classifications
        """
        pass

    def test_segment_details(self):
        """
        Test case for segment_details

        Get segment details by ID
        """
        pass

    def test_subgenre_details(self):
        """
        Test case for subgenre_details

        Get subgenre details by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
