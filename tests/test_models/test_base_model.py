#!/usr/bin/python3
""" my module description: Unittest module
for BaseModel class
"""

from models.base_model import BaseModel
import unittest
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ unit test Class to test BaseModel
    on models/base_model.py
    """

    @classmethod
    def setUpClass(mycls):
        """Function that intialize test parameters
        within unittests for testing only"""

        mycls.mybase = BaseModel()
        mycls.mybase.myname = "Hesham"
        mycls.mybase.id = 55
        try:
            os.rename("file.json", "mytmp")
        except Exception:
            pass

    @classmethod
    def tearDownClass(mycls):
        """Function that removes test parameters
        that created by setup class
        within unittests for testing only"""

        del mycls.mybase
        try:
            os.remove("file.json")
        except Exception:
            pass

        try:
            os.rename("mytmp", "file.json")
        except Exception:
            pass

    def test_base_model(self):
        """
        CHECK THE INHERETANCE AND THE ATRIBUTES
        WHEN CREATING SUB CLASES
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

        base1.name = "ABDEL-MOHSEN"
        base2.name = "KHALED"
        self.assertNotEqual(base1.name, "KHALED")
        self.assertEqual(base1.name, "ABDEL-MOHSEN")
        self.assertEqual(base2.name, "KHALED")
        self.assertTrue(isinstance(base1.id, str))
        self.assertTrue(isinstance(base2.name, str))
        self.assertTrue(isinstance(base2.to_dict(), dict))
        self.assertTrue(isinstance(base1.created_at, datetime))
        self.assertTrue(isinstance(base1.updated_at, datetime))
        self.assertTrue(isinstance(base2.created_at, datetime))
        self.assertTrue(isinstance(base2.updated_at, datetime))

    def test_doc_str(self):
        """ tests basemodel doc string
        exist or not
        """

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.convert_to_datetime.__doc__)

    def test_inst_type(self):
        """ Func.: Tests type of instance"""

        self.assertTrue(isinstance(self.mybase, BaseModel))

    def test_save_func(self):
        """ Func.: tests save() method of BaseModel
        to save json file with updated_at time
        and instance Id existance"""

        self.mybase.save()
        # after save: created_at must be less than updated_at
        self.assertLess(self.mybase.created_at, self.mybase.updated_at)

        with open("file.json", "r") as f:
            # check if instance Id in test json file
            self.assertIn(str(self.mybase.id), f.read())

    def test_to_dict(self):
        """ Func.: tests to_dict() method
        of BaseModel
        """
        my_dict = self.mybase.to_dict()
        self.assertIsInstance(my_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
