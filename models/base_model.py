#!/usr/bin/python3
"""This is the base model class for AirBnB"""

import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

        if not self.id:
            self.id = str(uuid.uuid4())

        d = datetime.now()
        if not self.created_at:
            self.created_at = self.updated_at = d

        if not self.updated_at:
            self.updated_at = d

    def __str__(self):
        """Returns a string"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns a string representation"""
        return self.__str__()

    def save(self):
        """Updates the public instance attribute updated_at to current"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates dictionary of the class and returns"""

        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        if my_dict.get('_sa_instance_state'):
            del my_dict['_sa_instance_state']

        return my_dict

    def delete(self):
        """Deletes the current instance from the storage"""

        models.storage.delete(self)

