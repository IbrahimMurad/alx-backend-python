#!/usr/bin/env python3
""" a test suit for utils.access_nested_map
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import (
    Sequence,
    Union,
    Dict,
    Type,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """ a test suit class to test access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Sequence[str],
            expected: Union[Dict, int]
            ) -> None:
        """ test method for access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Sequence[str],
            expected: Union[Type[BaseException]]
            ) -> None:
        """ test method for access_nested_map function """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ test class for testing get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
        mock_get
    ) -> None:
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        json = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(json, test_payload)


class TestMemoize(unittest.TestCase):
    """ test class for testing 'memoize' decorator """
    def test_memoize(self):
        """ a method to test 'memoize' decorator """

        class TestClass:
            """ a test class for memoize decorator """
            def a_method(self):
                """ a test method that returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ a test property that calls a_method """
                return self.a_method()

        with patch.object(
                TestClass,
                'a_method',
                return_value=42
                ) as mock_method:
            test_instance = TestClass()
            first_call = test_instance.a_property
            second_call = test_instance.a_property

            mock_method.assert_called_once()
            self.assertEqual(first_call, 42)
            self.assertEqual(first_call, second_call)


if __name__ == "__main__":
    unittest.main()
