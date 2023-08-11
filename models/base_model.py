#!/usr/bin/python3
""" module description """


import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ class BaseModel """

    def __init__(self, *args, **kwargs):
        """ instance intialization function """
        if kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == 'created_at':
                    dtime_obj_val = self.convert_to_datetime(val)
                    setattr(self, key, dtime_obj_val)
                elif key == 'updated_at':
                    dtime_obj_val = self.convert_to_datetime(val)
                    setattr(self, key, dtime_obj_val)
                elif key != '__class__':
                    setattr(self, key, val)

        else:
            # id: string - via uuid when an instance is created
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ save function to set current time
        for instance attribute updated at
        """
        self.updated_at = datetime.now()
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

        """
        print("#" * 30)
        print(f"CHECK THE RETURND DICTIONARY {my_dict}")
        print("#" * 30)
        """

        return (my_dict)

    def __str__(self):
        """ return : string as required by task """
        return ("[{}] ({}) {}".format(type(self).__name__,
                self.id, self.__dict__))

    @staticmethod
    def convert_to_datetime(datetime_string):
        """ Return: datetime object
        convert string to datatime object
        via datetime.strptime
        """
        dtime_string = str(datetime_string)
        dtime_format = "%Y-%m-%dT%H:%M:%S.%f"
        dtime_obj = datetime.strptime(dtime_string, dtime_format)
        return (dtime_obj)
