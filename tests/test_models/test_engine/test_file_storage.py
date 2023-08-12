#!/usr/bin/python3
""" module description : testunit for
filestorage.py in python
"""


import os
import models
import unittest
from models import *


class Test(unittest.TestCase):
    """ description : test class for file
    storage
    """
    def test_reload_no_json(self):
        """ test case if no json file exist 
        """
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()
            raise FileNotFoundError

    def test_storage_init(self):
        """ test correct type of class
        """
        self.assertEqual(type(models.storage), FileStorage)

if __name__ == "__main__":
    unittest.main()
