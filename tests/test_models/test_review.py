#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test for review inherting
    """

    def test_review(self):
        """
        review inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
