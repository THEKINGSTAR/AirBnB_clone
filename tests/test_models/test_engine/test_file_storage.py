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

    def test_new_w_none(self):
        """
        description : test new method with none
        as
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_w_arg(self):
        """
        description : test new method with args
        """
        # TypeError: new() takes 2 positional
        # arguments but 3 were given
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel, 2)

    def test_reload_w_none(self):
        """
        description : test reload method with
        None as args
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

    def test_check_file_storage_documintation(self):
        """
        Function to check the documintation of the
        functions in file storage class
        """
        fsclsdc = (
            " Class FileStorage that serializes\n    instances to a JSON file "
        )
        fsdoc = FileStorage.__doc__
        self.assertEqual(fsclsdc, fsdoc)

    def test_check_FileStorage_method_all(self):
        """
        Function to check the documintation of the
        functions in filestorage class
        """
        all_dc = " returns the dictionary __objects "
        self.assertEqual(FileStorage.all.__doc__, all_dc)

    def test_check_FileStorage_method_new(self):
        """
        Function to check the documintation of the
        functions in filestorage class
        """
        all_dc = (
            '\n        sets in __objects the obj with key <obj class name>.id'
        )
        self.assertEqual(FileStorage.new.__doc__, all_dc)

    def test_check_FileStorage_method_save(self):
        """
        Function to check the documintation of the
        functions in filestorage class
        """
        save_dc = """ serializes __objects to the JSON file (path: __file_path)
        function that writes an Object to a text file,
        using a JSON representation: """

        self.assertEqual(FileStorage.save.__doc__, save_dc)

    def test_check_FileStorage_method_reload(self):
        """
        Function to check the documintation of the
        functions in filestorage class
        """
        rld_dc = """
        deserializes the JSON file to __objects
        Write a function that creates an
        Object from a “JSON file”:
        """

        self.assertEqual(FileStorage.reload.__doc__, rld_dc)

    def test_file_storage_atributes(self):
        """
        check the attributes of file storage
        """
        json_storage = FileStorage()
        self.assertEqual(json_storage._FileStorage__file_path, "file.json")
        self.assertTrue(isinstance(json_storage._FileStorage__objects, dict))


if __name__ == "__main__":
    unittest.main()
