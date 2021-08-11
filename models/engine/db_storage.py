#!/usr/bin/python3
"""Initialize a database"""

from sqlalchemy.orm.session import Session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """assing all instances in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                pool_pre_ping=True)
        )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """show all instances"""
        dictionary = {}
        lista = []
        if cls is None:
            types_obj = [State, City, User, Place, Review]
            for i in types_obj:
                lista += self.__session.query(i).all()

        else:
            lista += self.__session.query(cls).all()

        for obj in lista:
            key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
            dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """add a new object"""
        self.__session.add(obj)

    def save(self):
        """save all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete a object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload objects"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
