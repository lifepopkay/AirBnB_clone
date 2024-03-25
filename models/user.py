#!/usr/bin/python3
from  models.base_model import BaseModel
"""User class model"""


class User(BaseModel):
    """
            A user file class
        Attributes:
            email (str): The email address of the user
            password (str): The password of the user
            first_name (str): The first name of the user
            last_name (str): The last name of the user
    """
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
