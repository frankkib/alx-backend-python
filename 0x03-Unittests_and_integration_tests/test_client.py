#!/usr/bin/env python3
"""Testing the GithubOrgClient module"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """The test suite for the GithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
        ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test the client method"""
        result = {"name": org_name}
        mock_get_json.return_value = result

        client = GithubOrgClient(org_name)
        response = client.org

        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org_name))
        self.assertEqual(response, result)


if __name__ == "__main__":
    unittest.main()
