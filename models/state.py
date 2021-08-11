#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'State'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities= relationship('City', backref='State', cascade='all, delete')

    else:
        @property
        def cities(self):
            """return all cities"""
            cts = models.storage.all(City)
            cts_st = []
            for key, value in cts.items():
                if self.id == value.state_id:
                    cts_st.append(value)
            return cts_st
