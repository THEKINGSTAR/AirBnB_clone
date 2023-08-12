#!/usr/bin/python3
"""
MODEL BALSE TEST CASES 
"""


import unittest
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


class Test(unittest.TestCase):
    """
    TEST FOR THE CLASS INHERITS AND ITS ATRRIUTES
    """
    
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

if __name__ == "__main__":
    unittest.main()
