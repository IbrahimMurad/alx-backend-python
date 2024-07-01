#!/usr/bin/env python3
""" test client module
"""
from client import GithubOrgClient
from parameterized import parameterized  # type: ignore
from unittest.mock import patch
from unittest import TestCase


class TestGithubOrgClient(TestCase):
    """ test class for GithubOrgClient.org  """
    @parameterized.expand([
        ("google", {'name': "google"}),
        ("abc", {'name': "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json) -> None:
        """ test org method """
        mock_get_json.return_value = expected
        test_class = GithubOrgClient(org_name)
        response = test_class.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(response, expected)
