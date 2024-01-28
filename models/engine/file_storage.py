#!/usr/bin/python3
"""storage model of the airbnb"""
import json
from pathlib import Path


class BaseModel:
    """convert the dictionary representation to a JSON string"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        file_path = Path(self.__file_path)
        if file_path.exists():
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
