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

    def test_help_eof(self):
        """ tests help EOF outputi n console"""
        # Set the expected output here
        expected_output = " exit on EOF (ctrl+D) \n"

        with patch('sys.stdout', new=StringIO()) as file:
            HBNBCommand().onecmd("help EOF")
            actual_output = file.getvalue()  # Get the captured output

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
