#!/usr/bin/env python3
""" test client module
"""
from client import GithubOrgClient
from parameterized import parameterized  # type: ignore
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ("google", {'repos_url': "https://api.github.com/orgs/google"}),
        ("abc", {'repos_url': "https://api.github.com/orgs/abc"})
    ])
    def test_public_repos_url(self, org_name, expected) -> None:
        """ test _public_repos_url method """
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = expected
            test_class = GithubOrgClient(org_name)
            payload_url = test_class._public_repos_url
            mock_org.assert_called_once()
            self.assertEqual(payload_url, expected['repos_url'])
