#!/usr/bin/python3
""" unittest for amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """ test cases """
    def setUp(self):
        """ this methode will be called for each test """
        self.amenity = Amenity()

    def test_instance_creation(self):
        """Test if an instance of Amenity is created."""
        self.assertIsInstance(self.amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test if the Amenity instance has the required attributes."""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_doc_string(self):
        """ test doc string """
        self.assertIsNotNone(Amenity.__doc__, True)
