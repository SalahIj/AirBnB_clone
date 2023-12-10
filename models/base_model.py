#!/usr/bin/env python3
""" Imported modules """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ The class methods and attributes """

    def __init__(self, *args, **kwargs):
        """ The constructor:
        Args:
            args: the fisrt input
            kwargs: the second input
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                time_form = "%Y-%m-%dT%H:%M:%S.%f"
                if (key == '__class__'):
                    continue
                elif (key == "created_at" or key == "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, time_form)
                else:
                    setattr(self, key, value)

    def save(self):
        """ save method """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ The to_dict method """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)

    def __str__(self):
        """ The str representation method """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
