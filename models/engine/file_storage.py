#!usr/bin/python3

""" File storage model """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():

    """
    FileStorage class
    Usage : implement the functionality of storing objects and retrieving them
    Cicle : <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
    <class 'str'> ->FILE -> <class 'str'> -> JSON load -> <class 'dict'>
    -> <class 'BaseModel'
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """do nothing"""
        pass

    def all(self):
        """
        Returns all objects in BaseModel class representing format
        """
        return self.__objects

    def new(self, obj):
        """
        Add new created objects to __objects var to serialize them
        into json objects using save() later
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """"
        Serialize BaseModel objects in __objects to json objects and
        save them in file.json file format
        """
        json_objs = {}
        for key, val in self.__objects.items():
            json_objs[key] = val.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(json_objs, f, indent=4)

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
