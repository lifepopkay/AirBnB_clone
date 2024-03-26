#!/usr/bin/python3
import unittest
from datetime import datetime

"""
    Unit test for Place class
"""
from models.place import Place
from models.base_model import BaseModel


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Create an instances before each test"""
        self.Place1 = Place()

    def tearDown(self):
        """Close all instances after each test"""
        del self.Place1

    def test_Place_type(self):
        """Test the type of class"""
        self.assertEqual(type(self.Place1), Place)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Place_attribute_type(self):
        """Test the Place attributes"""
        self.assertEqual(type(self.Place1.city_id), str)
        self.assertEqual(type(self.Place1.user_id), str)
        self.assertEqual(type(self.Place1.name), str)
        self.assertEqual(type(self.Place1.description), str)
        self.assertEqual(type(self.Place1.numbers_rooms), int)
        self.assertEqual(type(self.Place1.numbers_bathroom), int)
        self.assertEqual(type(self.Place1.max_guest), int)
        self.assertEqual(type(self.Place1.price_by_night), int)
        self.assertEqual(type(self.Place1.latitude), float)
        self.assertEqual(type(self.Place1.longitude), float)
        self.assertEqual(type(self.Place1.amenity_ids), list)
        self.assertEqual(type(self.Place1.id), str)
        self.assertEqual(type(self.Place1.created_at), datetime)
        self.assertEqual(type(self.Place1.updated_at), datetime)

    def test_Place_has_attributes(self):
        """Test the Place attributes"""
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'numbers_rooms'))
        self.assertTrue(hasattr(Place, 'numbers_bathroom'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))
        self.assertFalse(hasattr(Place, 'created_at'))
        self.assertFalse(hasattr(Place, 'updated_at'))
        self.assertFalse(hasattr(Place, 'id'))

    def test_instance_attributes(self):
        """Test the instance attributes"""
        self.assertTrue(hasattr(self.Place1, 'created_at'))
        self.assertTrue(hasattr(self.Place1, 'updated_at'))
        self.assertTrue(hasattr(self.Place1, 'id'))
