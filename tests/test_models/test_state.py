#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    test for state inherting
    """

    def test_state(self):
        """
        state inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(State, BaseModel))
