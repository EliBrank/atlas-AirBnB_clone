#!/usr/bin/python3

"""This module defines a class named FileStorage"""

import json, models
from os.path import exists
from models.base_model import BaseModel


class FileStorage():
    """This class serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """saves obj to __objects with object's class and unique id as key

        Args:
            obj: python object to add to dictionary
        """

        FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}" : obj})

    def save(self):
        """saves each object in __objects to JSON file

        Args:
            __objects: python objects to be converted and saved
        """

        json_list = []
        with open(FileStorage.__file_path, "w") as f:
            for obj in FileStorage.__objects:
                json_list.append(obj.to_dict())
            json.dump(json_list, f)

    def reload(self):
        """reloads __objects dictionary with objects from JSON file"""

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
