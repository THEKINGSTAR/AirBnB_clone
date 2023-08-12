#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.city import City


class Test(unittest.TestCase):
    """
    test for CITY inherting
    """

    def test_amenity(self):
        """
        CITY inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
