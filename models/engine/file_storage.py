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
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        json_objs = {}
        for key, val in self.__objects.items():
            json_objs[key] = val.to_dict()
        with open(self.__file_path, "w+") as f:
            dump(json_objs, f)

    def reload(self):
        """
        Deserializes the JSON objects in file.json to a python dictionary
        format then pass it as a kwargs to BaseModel constructor to convert it
        BaseModel class representing format
        """
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                json_objs = json.load(f)
            models = {
                'User': User,
                'BaseModel': BaseModel,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
            }
            for key, val in json_objs.items():
                constractor = val["__class__"]
                for model, cls in models.items():
                    if constractor == model:
                        self.__objects[key] = cls(**val)

        except FileNotFoundError:
            pass
        except Exception as e:
            pass
