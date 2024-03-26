#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""Test case for the amenity class"""


class MyTestCase(unittest.TestCase):

    def test_name(self):
        """Test the name input"""
        user1 = Amenity()
        user1.name = 'life'
        self.assertEqual(user1.name, 'life')


if __name__ == '__main__':
    unittest.main()
