#!/usr/bin/env python3
""" a test suit for utils.access_nested_map
"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized  # type: ignore
from typing import Tuple, Union


class TestAccessNestedMap(TestCase):
    """ a test suit class to test access_nested_map function """
    @parameterized.expand([
        ('', {"a": 1}, ("a",), 1),
        ('', {"a": {"b": 2}}, ("a",), {"b": 2}),
        ('', {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            _,
            nested_map: dict,
            path: Tuple[str],
            expected: Union[int, dict]
            ) -> None:
        """ test method for access_nested_map function
        with 3 different inputs """
        self.assertEqual(access_nested_map(nested_map, path), expected)
