#!/usr/bin/python3
""" module description : testunit for
filestorage.py in python
"""


import os
import models
import unittest
from models import *


class TestFileStorage(unittest.TestCase):
    """ description : test class for file
    storage
    """

    def test_storage_init(self):
        """ test correct type of class
        """
        self.assertEqual(type(models.storage), FileStorage)

    def test_reload_w_arg(self):
        """
        description : test reload method with args
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_no_json(self):
        """ test case if no json file exist
        """
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()
            raise FileNotFoundError

    def test_reload(self):
        """ test reload method after
        saving
        """
        rvie = Review()
        models.storage.new(rvie)
        models.storage.save()
        models.storage.reload()
        objcts = FileStorage._FileStorage__objects
        self.assertIn("Review." + rvie.id, objcts)


if __name__ == "__main__":
    unittest.main()
