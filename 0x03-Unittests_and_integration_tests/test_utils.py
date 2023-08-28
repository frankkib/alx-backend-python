#!/usr/bin/env python3
"""Python testcase module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
