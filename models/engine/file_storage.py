#!/usr/bin/python3
"""This is the file_storage."""

from json import dump
from json import load
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File storage Class.

    serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Init constructor."""
        pass

    def all(self):
        """All.

        Returns:
            dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key.

        Args:
            obj (object): object
        """
        myobj_to_dict = obj.to_dict()
        self.__objects[myobj_to_dict["__class__"] +
                       "." + myobj_to_dict["id"]] = myobj_to_dict

    def save(self):
        """Serialize __objects to the JSON file."""
        json_objs = {}
        for key, val in self.__objects.items():
            json_objs[key] = val.to_dict()
        with open(self.__file_path, "w+") as f:
            dump(self.__objects, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = load(f)
        except FileNotFoundError:
            pass
