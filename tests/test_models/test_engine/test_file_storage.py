#!/usr/bin/python3
""" unittest for  file_storage """
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """ set up the test envirenement """
        self.file_path = (
            "/Users/zakariagrari/Documents/"
            "ALX/AirBnB_clone/file.json"
        )
        self.file_storage = FileStorage()
        self.file_storage.__file_path = self.file_path

    def tearDown(self):
        """ Clean up after the test """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        self.file_storage._FileStorage__objects = {}
        del self.file_storage

    def test_all_empty(self):
        """ test all when storage is empty """
        objects = self.file_storage.all()
        self.assertEqual(objects, {})

    def test_new_all(self):
        """ test new and all methodes """
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        objects = self.file_storage.all()
        self.assertEqual(len(objects), 2)
        self.assertIn("BaseModel {}".format(obj1.id), objects)
        self.assertIn("BaseModel {}".format(obj2.id), objects)
        self.assertEqual(objects["BaseModel {}".format(obj1.id)], obj1)
        self.assertEqual(objects["BaseModel {}".format(obj2.id)], obj2)

    def test_save_and_reload(self):
        """ test save and reaload methode """
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.__file_path = self.file_path
        new_file_storage.reload()

        objects = new_file_storage.all()
        self.assertEqual(len(objects), 4)
        self.assertIn("BaseModel {}".format(obj1.id), objects)
        self.assertIn("BaseModel {}".format(obj2.id), objects)

    def test_doc_string(self):
        """ test doc string """
        self.assertIsNotNone(FileStorage.__doc__, True)
        self.assertIsNotNone(FileStorage.__init__.__doc__, True)
        self.assertIsNotNone(FileStorage.all.__doc__, True)
        self.assertIsNotNone(FileStorage.new.__doc__, True)
        self.assertIsNotNone(FileStorage.save.__doc__, True)
        self.assertIsNotNone(FileStorage.reload.__doc__, True)


if __name__ == '__main__':
    unittest.main()
