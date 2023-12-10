#!/usr/bin/python3
""" unittest for base_model """

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """ The class methods and attributes """
    def setUp(self):
        """ This method will be called before every test """
        self.instance_model = BaseModel()

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

    def test_attributes(self):
        """ Test if the attributes are initialized correctly """
        self.assertIsNotNone(self.instance_model.id)
        self.assertIsInstance(self.instance_model.created_at, datetime)
        self.assertIsInstance(self.instance_model.updated_at, datetime)

    def test_two_universal_unique_ids(self):
        """ Test the variability of uuid """
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_created_at_attaribute(self):
        """ Test the difference between two created_at times """
        old_created_at = self.instance_model.created_at
        sleep(0.06)
        new_created_at = BaseModel().created_at
        time_difference = new_created_at - old_created_at
        self.assertGreaterEqual(time_difference.total_seconds(), 0.06)

    def test_save_method(self):
        """ Test the save method """
        old_updated_at = self.instance_model.updated_at
        new_updated_at = self.instance_model.save()
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """ Test the to_dict method """
        obj = self.instance_model.to_dict()
        self.assertIsInstance(obj, dict)
        self.assertIn('id', obj)
        self.assertIn('created_at', obj)
        self.assertIn('updated_at', obj)
        self.assertIn('__class__', obj)

    def test_creat_from_dict_method(self):
        """ Test creating an instance from a dictionary """
        obj = {
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2023-12-01T12:00:00.000000',
            'updated_at': '2023-12-01T13:00:00.000000',
            '__class__': 'BaseModel',
            'custom_attribute': 'some_value'
        }
        new_obj = BaseModel(**obj)
        self.assertEqual(new_obj.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)
        self.assertEqual(new_obj.custom_attribute, 'some_value')

    def test_str_method(self):
        """ Test the __srt__ method """
        obj = self.instance_model
        date = datetime.today()
        date_repr = repr(date)
        obj.id = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        obj.created_at = obj.updated_at = date
        obj_str = obj.__str__()
        self.assertIn("[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579)",
                      obj_str)
        self.assertIn("'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579'", obj_str)
        self.assertIn("'created_at': " + date_repr, obj_str)
        self.assertIn("'updated_at': " + date_repr, obj_str)


if __name__ == '__main__':
    unittest.main()
