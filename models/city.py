#!/usr/bin/python3
from models.base_model import BaseModel
"""City model class"""


class City(BaseModel):
    """
        City Model class inherited from BaseModel
        Attributes:
            state_id: state identification number
            name: The name of the city
    """
    state_id = ''
    name = ''
