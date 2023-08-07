#!/usr/bin/python3
""" module description """


import uuid
from datetime import datetime
from datetime import datetime, timezone

from models import storage

class BaseModel():
    """ class BaseModel """

    def __init__(self, *args, **kwargs):
        """ instance intialization function """
        # id: string - via uuid when an instance is created
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(tz=timezone.utc)
        self.updated_at = datetime.now(tz=timezone.utc)

    def save(self):
        """ save function to set current time
        for instance attribute updated at
        """
        self.updated_at = datetime.now(tz=timezone.utc)
        storage.save()

    def to_dict(self):
        """
        returns a dictionary
        containing all keys/values
        of dict of the instance:
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)

    def __str__(self):
        """ return : string as required by task """
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))
