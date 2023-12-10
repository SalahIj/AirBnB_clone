#!/usr/bin/env python3
""" Imported modules """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    """The class methods and attributes """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ The all method """
        return (FileStorage.__objects)

    def new(self, obj):
        """ The new method
        Args:
            obj: the input
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obJ

    def save(self):
        """ The save method """
        obj = FileStorage.__objects
        dict = {}
        for key in obj.keys():
            dict[key] = obj[key].to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as File:
            json.dump(dict, File)

    def reload(self):
        """ The reload method """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as File:
                obj = FileStorage.__objects
                dictionnary = json.load(File)
                for key, value in dictionnary.items():
                    obj[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
