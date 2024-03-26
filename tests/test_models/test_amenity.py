#!/usr/bin/python3
import unittest
from datetime import datetime

"""
    Unit test for Amenity class
"""
from models.amenity import Amenity
from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):

    def test_amenity_type(self):
        """Test the type of class"""
        user1 = Amenity()
        self.assertEqual(type(user1), Amenity)
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attribute_type(self):
        """Test the amenity name"""
        user1 = Amenity()
        self.assertEqual(type(user1.name), str)
        self.assertEqual(type(user1.id), str)
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_amenity_has_attributes(self):
        """Test the amenity attributes"""
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertFalse(hasattr(Amenity, 'created_at'))
        self.assertFalse(hasattr(Amenity, 'updated_at'))
        self.assertFalse(hasattr(Amenity, 'id'))

    def test_instance_attributes(self):
        """Test the instance attributes"""
        user1 = Amenity()
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))
        self.assertTrue(hasattr(user1, 'id'))
