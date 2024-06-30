#!/usr/bin/env python3
""" a test suit for utils.access_nested_map
"""
from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized
from typing import Mapping, Tuple


class TestAccessNestedMap(TestCase):
    """ a test suit class to test access_nested_map function """
    @parameterized.expand([
        ('one_key_one_object', {"a": 1}, ("a",), 1),
        ('one_key_two_objects', {"a": {"b": 2}}, ("a",), {"b": 2}),
        ('two_keys_two_objects', {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n: str, np: Mapping, p: Tuple, exp: int):
        self.assertEqual(access_nested_map(np, p), exp)
