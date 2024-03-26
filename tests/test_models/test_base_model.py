#!/usr/bin/python3
import json
import unittest
from datetime import datetime
from time import sleep

"""
    Unit test for BaseModel class
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Create a test model"""
        self.my_base = BaseModel()

        self.her_base = BaseModel()

    def tearDown(self):
        """Delete test data"""
        del self.my_base
        del self.her_base

    def test_base_instance(self):
        """Test BaseModel instance"""
        self.assertIsInstance(self.my_base, BaseModel)
        self.assertIsInstance(self.her_base, BaseModel)

    def test_my_base_instance(self):
        """Test BaseModel attributes"""
        self.my_base.name = "Life"
        self.my_base.my_number = 8133334443
        self.my_base.save()
        my_base_json = self.my_base.to_dict()

        self.assertEqual(self.my_base.name, my_base_json['name'])
        self.assertEqual(self.my_base.my_number, my_base_json['my_number'])
        self.assertEqual('BaseModel', my_base_json['__class__'])
        self.assertEqual(self.my_base.id, my_base_json['id'])

    def test_her_base_instance(self):
        """Test BaseModel attributes"""
        self.her_base.name = "Nife"
        self.her_base.my_number = 8146590434
        self.her_base.save()
        her_base_json = self.her_base.to_dict()

        self.assertEqual(self.her_base.name, her_base_json['name'])
        self.assertEqual(self.her_base.my_number, her_base_json['my_number'])
        self.assertEqual('BaseModel', her_base_json['__class__'])
        self.assertEqual(self.her_base.id, her_base_json['id'])

    def test_kwargs_initialization(self):
        """Test the initialization of a class using kwargs"""
        kwargs = {"__class__": "BaseModel", "created_at":
                  "2021-06-25T19:52:36.252305",
                  "id": "83b3c8a8-b72b-4472-9d80-c52b2e090f04",
                  "updated_at": "2021-06-25T19:52:36.252312"}
        Test_Base = BaseModel(**kwargs)
        self.assertEqual(Test_Base.id, kwargs['id'])
        self.assertEqual(Test_Base.created_at.isoformat(),
                         kwargs['created_at'])
        self.assertEqual(Test_Base.updated_at.isoformat(),
                         kwargs['updated_at'])

    def test_attributes_exist(self):
        """Test that class BaseModel has the required methods and attributes"""
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(self.my_base, 'id'))
        self.assertTrue(hasattr(self.my_base, 'created_at'))
        self.assertTrue(hasattr(self.my_base, 'updated_at'))
        self.assertTrue(hasattr(self.my_base, 'save'))
        self.assertTrue(hasattr(self.my_base, 'to_dict'))
        self.assertTrue(hasattr(BaseModel, '__str__'))

    def test_instance_uuid(self):
        """Test BaseModel uuid is they same"""
        self.assertNotEqual(self.my_base.id, self.her_base.id)

    def test_to_dict(self):
        """Test the return value of the to_dict() method"""
        test_dict = {key: value for key,
                     value in self.my_base.__dict__.items()}
        test_dict['created_at'] = self.my_base.created_at.isoformat()
        test_dict['updated_at'] = self.my_base.updated_at.isoformat()
        test_dict['__class__'] = type(self.my_base).__name__
        self.assertEqual(self.my_base.to_dict(), test_dict)

    def test_str_representation(self):
        """Test the format of the return value of the __str__ method"""
        msg = "[{}] ({}) {}".format(type(self.her_base).__name__,
                                    self.her_base.id,
                                    self.her_base.__dict__)
        self.assertEqual(str(self.her_base), msg)

    def test_updated_at_save(self):
        """Test updated_at attribute is actually updated"""
        time_1 = self.her_base.updated_at
        sleep(.5)
        self.her_base.save()
        self.assertNotEqual(time_1, self.her_base.updated_at)
        self.assertLess(time_1, self.her_base.updated_at)

    def test_object_saved(self):
        """Test whether an object is stored in a file when using save method"""
        self.her_base.save()
        try:
            with open("my_file.json", mode='r', encoding='UTF-8') as f:
                saved_data = json.load(f)

            her_base_id = "BaseModel." + self.her_base.id
            value = saved_data[her_base_id]
            self.assertEqual(value, self.her_base.to_dict())
        except FileNotFoundError:
            pass
