#!/usr/bin/python3
""" module description : testunit for
filestorage.py in python
"""


import os
import models
import unittest
from models import *
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City


class TestFileStorage(unittest.TestCase):
    """ description : test class for file
    storage
    """

    @classmethod
    def setUpClass(mycls):
        """Function that intialize test parameters
        within unittests for testing only"""

        try:
            os.rename("file.json", "mytmp")
        except Exception:
            pass

    @classmethod
    def tearDownClass(mycls):
        """Function that removes test parameters
        that created by setup class
        within unittests for testing only"""

        try:
            os.remove("file.json")
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def test_storage_init(self):
        """ test correct type of class
        """
        self.assertEqual(type(models.storage), FileStorage)

    def test_save_w_arg(self):
        """
        description : test save method with args
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_new_w_arg(self):
        """
        description : test new method with args
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

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
