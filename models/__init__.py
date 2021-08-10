#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.db_storage import DBStorage
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
	Storage = DBStorage()
else:
	Storage = FileStorage()

storage.reload()
