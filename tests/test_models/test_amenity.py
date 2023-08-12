#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test(unittest.TestCase):
    """
    test for amenity inherting
    """

    def test_amenity(self):
        """
        amenity inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
