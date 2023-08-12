#!/usr/bin/python3
"""This is the file_storage."""

from json import dump
from json import load


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
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = load(f)
        except FileNotFoundError:
            pass
