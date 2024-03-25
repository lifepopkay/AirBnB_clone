#!/usr/bin/python3
"""Defines a file storage class"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ File Storage class
        Attr:
            __file_path (str) : the file path
            __objects (dict) : stores all objects

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retures all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id
        key_name = obj_class_name + "." + obj_id
        FileStorage.__objects[key_name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode='w') as file:
            obj_dict = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn't exist,
        no exception should be raised"""
        retrieved_objects = {}
        try:
            """Load our data back from file storage"""
            with open(FileStorage.__file_path, mode='r') as file:
                retrieved_objects = json.load(file)

                object_to_store = {}
                for key, value in retrieved_objects.items():
                    """
                        Get the class name from the '__class__'
                        key inside the value
                    """
                    class_name = value['__class__']
                    properties = value
                    object_to_store[key] = eval(class_name)(**properties)
                FileStorage.__objects.update(object_to_store)
        except FileNotFoundError:
            pass
