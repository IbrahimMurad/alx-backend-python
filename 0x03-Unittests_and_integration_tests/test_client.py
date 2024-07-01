#!/usr/bin/env python3
""" test client module
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
from unittest import TestCase, main


class TestGithubOrgClient(TestCase):
    """ test class for GithubOrgClient.org  """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('requests.get')
    def test_org(self, org_name, mock_get_json):
        """ test org method """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once()
    