#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            _list = []
            for city in self.cities:
                if city.state_id == self.id:
                    _list.append(city)
            return _list

    if os.getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            _list = []
            for _id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    _list.append(city)
            return _list
