#!/usr/bin/python3
from models.base_model import BaseModel
"""Place class model"""


class Place(BaseModel):
    """
        A place model that inherits from basemodel class
        Attributes:
            city_id (string): ID of the city the place is in
            user_id (string): ID of the person who's put up the place on AirBnb
            name (string): name of the place
            description (string): Description of the place
            number_rooms (int): number of rooms
            number_bathrooms (int): number of bathrooms
            max_guest (int): maximum number of guests the place can host
            price_by_night (int): price to hire the place per night
            latitude (float): latitude coordinate of the place
            longitude (float): longitude coordinate of the place
            amenity_ids (list): a list of amenities (Amenity.i
    """
    city_id: str = ''
    user_id: str = ''
    name: str = ''
    description: str = ''
    numbers_rooms: int = ''
    numbers_bathroom: int = ''
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
