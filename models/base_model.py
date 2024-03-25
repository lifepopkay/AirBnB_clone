#!/usr/bin/python3

"""Import the uuid - unique identifier, the datetime module, and storage"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel for creating and managing instances

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): Date and time when instance was last updated.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if kwargs:
            for attr_name, value in kwargs.items():
                if attr_name == 'created_at' or attr_name == 'updated_at':
                    try:
                        fmt = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.fromisoformat(kwargs[attr_name])
                    except AttributeError:
                        value = datetime.strptime(kwargs[attr_name], fmt)
                if attr_name == '__class__':
                    pass
                else:
                    setattr(self, attr_name, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()

        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def save(self):
        """Saves the instance to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) ({})"\
        .format(self.__class__.__name__, self.id, self.__dict__)
