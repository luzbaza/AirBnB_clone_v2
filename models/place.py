#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
import models
import os


class Place(BaseModel, Base):
    """ A place to stay """
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
    amenity_id = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            """ """
            rws_plc = []
            rws = models.storage.all(Review)
            for key, value in rws.items():
                if self.id == value.state_id:
                    rws_plc.append(value)
            return rws_plc
