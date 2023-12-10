#!/usr/bin/python3
""" unittest for base_model """

import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ Test cases """
    def test_type_id(self):
        """ test if id is a string """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_uniq_id(self):
        """ test if the id is unique """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_to_dict(self):
        """ test to_dict """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict.keys())
        self.assertIn('created_at', obj_dict.keys())
        self.assertIn('updated_at', obj_dict.keys())

    def test_doc_string(self):
        """ test doc string """
        self.assertIsNotNone(BaseModel.__doc__, True)
        self.assertIsNotNone(BaseModel.__init__.__doc__, True)
        self.assertIsNotNone(BaseModel.save.__doc__, True)
        self.assertIsNotNone(BaseModel.to_dict.__doc__, True)
        self.assertIsNotNone(BaseModel.__str__.__doc__, True)


if __name__ == '__main__':
    unittest.main()
