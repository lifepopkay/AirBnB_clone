#!/usr/bin/python3
"""Defines a file storage class"""

import json
from models.base_model import BaseModel


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
        obj_class_name = obj.__class__.name
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
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised"""
        retrieved_objects = {}
        try:
            """Load our data back from file storage"""
            with open(FileStorage.__file_path, mode='r') as file:
                retrieved_objects = json.load(file)
                for key, value in retrieved_objects.items():
                    """
                        Get the class name from the '__class__'
                        key inside the value
                    """
                    class_name = value['__class__']
                    properties = value
                    object_to_store = eval(class_name)(**properties)
                FileStorage.__objects[key] = object_to_store
        except FileNotFoundError:
            pass
