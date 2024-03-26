#!/usr/bin/python3
import unittest
from datetime import datetime
""""
    Unit tests for Review class
"""
from models.base_model import BaseModel
from models.review import Review


class MyTestCase(unittest.TestCase):

    def test_Review_type(self):
        """Test the type of class"""
        user1 = Review()
        self.assertEqual(type(user1), Review)
        self.assertTrue(issubclass(Review, BaseModel))

    def test_Review_attribute_type(self):
        """Test the Review name"""
        user1 = Review()
        self.assertEqual(type(user1.place_id), str)
        self.assertEqual(type(user1.user_id), str)
        self.assertEqual(type(user1.text), str)
        self.assertEqual(type(user1.id), str)
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_Review_has_attributes(self):
        """Test the Review attributes"""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))
        self.assertFalse(hasattr(Review, 'created_at'))
        self.assertFalse(hasattr(Review, 'updated_at'))
        self.assertFalse(hasattr(Review, 'id'))

    def test_instance_attributes(self):
        """Test the instance attributes"""
        user1 = Review()
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))
        self.assertTrue(hasattr(user1, 'id'))
