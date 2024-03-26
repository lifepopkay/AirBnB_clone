#!/usr/bin/python3
import unittest
from datetime import datetime

from models.base_model import BaseModel
from models.state import State


class MyTestCase(unittest.TestCase):

    def test_State_type(self):
        """Test the type of class"""
        user1 = State()
        self.assertEqual(type(user1), State)
        self.assertTrue(issubclass(State, BaseModel))

    def test_State_attribute_type(self):
        """Test the State name"""
        user1 = State()
        self.assertEqual(type(user1.name), str)
        self.assertEqual(type(user1.id), str)
        self.assertEqual(type(user1.created_at), datetime)
        self.assertEqual(type(user1.updated_at), datetime)

    def test_State_has_attributes(self):
        """Test the State attributes"""
        self.assertTrue(hasattr(State, 'name'))
        self.assertFalse(hasattr(State, 'created_at'))
        self.assertFalse(hasattr(State, 'updated_at'))
        self.assertFalse(hasattr(State, 'id'))

    def test_instance_attributes(self):
        """Test the instance attributes"""
        user1 = State()
        self.assertTrue(hasattr(user1, 'created_at'))
        self.assertTrue(hasattr(user1, 'updated_at'))
        self.assertTrue(hasattr(user1, 'id'))
