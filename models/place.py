#!/usr/bin/python3
"""This is the place class"""

from os import environ as env
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models

place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey("places.id")),
    Column('amenity_id', String(60), ForeignKey("amenities.id"))
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: price for a staying in int
        latitude: latitude in float
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        backref="place",
        viewonly=False
    )

    @property
    def reviews(self):
        """Get all reviews with the current place id"""
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        return [v for k, v in models.storage.all(models.Review).items() if v.place_id == self.id]

    @property
    def amenities(self):
        """Get all amenities with the current place id"""
        if env.get('HBNB_TYPE_STORAGE') == 'db':
            return self.__amenities
        return [v for k, v in models.storage.all(models.Amenity).items() if v.id in self.amenity_ids]

