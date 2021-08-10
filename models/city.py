#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.sql.expression import column
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = column(String(60), nullable=False)
    state_id = column(String(60), ForeignKey('states_id'), nullable=False)
