#!/usr/bin/python3
from models.base_model import BaseModel
"""Review class model"""


class Review(BaseModel):
    """
        Review model class inherits from BaseModel
        Attributes:
            place_id : the place_id of the review of the user
            user_id : the user_id of the review of the user
            text : the text of the review of the user
    """
    place_id: str = ''
    user_id: str = ''
    text: str = ''
