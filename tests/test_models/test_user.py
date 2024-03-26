#!/usr/bin/python3
import unittest
from datetime import datetime

"""
    Unit test for User class
"""
from models.user import User
from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Create an instances before each test"""
        self.user1 = User()

    def tearDown(self):
        """Close all instances after each test"""
        del self.user1

    def test_User_type(self):
        """Test the type of class"""
        self.assertEqual(type(self.user1), User)
        self.assertTrue(issubclass(User, BaseModel))

    def test_User_attribute_type(self):
        """Test the user attributes"""
        self.assertEqual(type(self.user1.email), str)
        self.assertEqual(type(self.user1.password), str)
        self.assertEqual(type(self.user1.first_name), str)
        self.assertEqual(type(self.user1.last_name), str)
        self.assertEqual(type(self.user1.id), str)
        self.assertEqual(type(self.user1.created_at), datetime)
        self.assertEqual(type(self.user1.updated_at), datetime)

    def test_User_has_attributes(self):
        """Test the User attributes"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertFalse(hasattr(User, 'created_at'))
        self.assertFalse(hasattr(User, 'updated_at'))
        self.assertFalse(hasattr(User, 'id'))

    def test_instance_attributes(self):
        """Test the instance attributes"""
        self.assertTrue(hasattr(self.user1, 'created_at'))
        self.assertTrue(hasattr(self.user1, 'updated_at'))
        self.assertTrue(hasattr(self.user1, 'id'))
