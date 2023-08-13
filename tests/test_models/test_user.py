#!/usr/bin/python3
"""
TEST INHERTINCE OF THE BASEMODEL CLASE
"""


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    test for USER inherting
    """

    def test_user(self):
        """
        USER inhertin test
        """
        # result = function_to_test(input_data)
        # self.assertEqual(result, expected_output)

        self.assertTrue(issubclass(User, BaseModel))

    def test_city_class_documintation(self):
        """
        check the documintation of the
        User class
        """
        bmclsdc = """ User class that inherits from BaseModel: """
        bmdoc = User.__doc__
        self.assertEqual(bmclsdc, bmdoc)

    def test_city_class_attributes_email(self):
        """
        check the attributes of the
        User class
        """
        User.id = 123

        usr = User()
        usr.id = 123
        usr.email = "base@mode.tes"
        usr.password = "123"
        usr.first_name = "fn_usr"
        usr.last_name = "ln_usr"

        self.assertEqual(usr.id, User.id)
        self.assertTrue(type(usr.id) is int)

        self.assertIsNotNone(User.email)
        self.assertTrue(type(User.email) is str)
        self.assertFalse(type(User.email) is int)

    def test_city_class_attributes_pass(self):
        """
        check the attributes of the
        User class
        """
        usr = User()
        usr.id = 123
        usr.password = "123"

        self.assertIsNotNone(User.password)
        self.assertTrue(type(User.password) is str)
        self.assertFalse(type(User.password) is int)

    def test_city_class_attributes_f_name(self):
        """
        check the attributes of the
        User class
        """
        usr = User()
        usr.id = 123
        usr.first_name = "fn_usr"
        usr.last_name = "ln_usr"

        self.assertIsNotNone(User.first_name)
        self.assertTrue(type(User.first_name) is str)
        self.assertFalse(type(User.first_name) is int)

    def test_city_class_attributes_l_name(self):
        """
        check the attributes of the
        User class
        """
        usr = User()
        usr.id = 123
        usr.last_name = "ln_usr"

        self.assertIsNotNone(User.last_name)
        self.assertTrue(type(User.last_name) is str)
        self.assertFalse(type(User.last_name) is int)


if __name__ == "__main__":
    unittest.main()
