#!/usr/bin/python3
""" module description : testunit for console.py in python
"""


import unittest
import sys
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class Test(unittest.TestCase):
    """ desc---ription """

    def testc1(self):
        """ desc.....ription """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)
        # pass

        # Set the expected output here
        expected_output = "dummy text"

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help show")
            actual_output = file.getvalue()  # Get the captured output

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
