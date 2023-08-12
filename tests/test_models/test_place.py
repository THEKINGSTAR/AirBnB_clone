#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class Test(unittest.TestCase):
    """
    test for place inherting
    """

    def test_place(self):
        """
        place inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
