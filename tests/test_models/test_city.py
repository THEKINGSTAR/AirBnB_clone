#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    test for CITY inherting
    """

    def test_city_class(self):
        """
        CITY inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(City, BaseModel))

    def test_city_class_documintation(self):
        """
        Function to check the documintation of the
        functions in basemodel class
        """
        bmclsdc = """ city class code here"""
        bmdoc = City.__doc__
        self.assertEqual(bmclsdc, bmdoc)

    def test_city_class_attributes(self):
        """
        Function to check the documintation of the
        functions in basemodel class
        """
        bmclsdc = """ city class code here"""
        bmdoc = City.__doc__
        self.assertEqual(bmclsdc, bmdoc)


if __name__ == "__main__":
    unittest.main()
