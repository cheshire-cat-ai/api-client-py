# coding: utf-8

"""
    😸 Cheshire-Cat API

    Customizable AI architecture  # noqa: E501

    The version of the OpenAPI document: 0.0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import cheshire_cat_api
from cheshire_cat_api.api.embedder_api import EmbedderApi  # noqa: E501
from cheshire_cat_api.rest import ApiException


class TestSettingsEmbedderApi(unittest.TestCase):
    """SettingsEmbedderApi unit test stubs"""

    def setUp(self):
        self.api = cheshire_cat_api.api.embedder_api.EmbedderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_embedder_settings(self):
        """Test case for get_embedder_settings

        Get Embedder Settings  # noqa: E501
        """
        pass

    def test_upsert_embedder_setting(self):
        """Test case for upsert_embedder_setting

        Upsert Embedder Setting  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
