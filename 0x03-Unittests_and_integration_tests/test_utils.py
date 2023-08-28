#!/usr/bin/env python3
"""Python testcase module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """The test class for access nested map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, result):
        """Access function"""
        nest = access_nested_map(nested_map, path)
        self.assertEqual(nest, result)

    @parameterized.expand([
        ({}, ("a",), ("a")),
        ({"a": 1}, ("a", "b"), "b"),
        ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        """Exception function"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), f"'{key}'")


class TestGetJson(unittest.TestCase):
    """get_json class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """get_json function test"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """memozation test class"""
    def a_method(self):
        """method that returns 42"""
        return 42

    @memoize
    def a_property(self):
        """A memoized property"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test suite for memoize decorator"""
    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method):
        """Testing thr memoize decorator"""
        instance = TestClass()

        mock_method.return_value = 42

        result1 = instance.a_property
        result2 = instance.a_property

        mock_method.assert_called_once()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
