#!/usr/bin/python3

import json


class FileStorage:
    """This stores intances of objects in a file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """retures the dicts objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w') as file:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects 
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised"""
        retrieved_objects = []
        try:
            with open(self.__file_path, mode='r') as file:
                retrieved_objects = json.load(file)
                for key, value in retrieved_objects.items():
                    class_name, obj_id = key.split(".")
                    cls = globals()[class_name]
                    obj = cls(**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

