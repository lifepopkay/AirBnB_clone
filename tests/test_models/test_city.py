#!/usr/bin/python3
import unittest
from datetime import datetime
"""
    Unit test for City class
"""
from models.base_model import BaseModel
from models.city import City


class MyTestCase(unittest.TestCase):

    def test_class_type(self):
        """Test the class type of instance"""
        user1 = City()
        self.assertEqual(type(user1), City)
        self.assertTrue(issubclass(City, BaseModel))

    def test_class_attributes(self):
        """Test the class attributes of an instance"""
        user1 = City()
        self.assertTrue(hasattr(user1, 'state_id'))
        self.assertTrue(hasattr(user1, 'name'))
        self.assertFalse(hasattr(City, 'created_at'))
        self.assertFalse(hasattr(City, 'updated_at'))
        self.assertFalse(hasattr(City, 'id'))

    def test_instance_attributes(self):
        """Test the instance attributes of an instance"""
        user1 = City()
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))
        self.assertTrue(hasattr(user1, 'id'))

    def test_instance_Attributes_type(self):
        """Test the type of instance attributes"""
        user1 = City()
        self.assertTrue(isinstance(user1.name, str))
        self.assertTrue(isinstance(user1.state_id, str))
        self.assertTrue(isinstance(user1.created_at, datetime))
        self.assertTrue(isinstance(user1.updated_at, datetime))
        self.assertTrue(isinstance(user1.id, str))
