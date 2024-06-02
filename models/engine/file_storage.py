#!/usr/bin/python3

"""This module defines a class named FileStorage"""

import json
from os.path import exists
import models


class FileStorage():
    """This class serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """saves obj to __objects with object's class and unique id as key

        Args:
            obj: python object to add to dictionary
        """

        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}" : obj})

    def save(self):
        """saves each object in __objects to JSON file"""

        json_dict = {}
        with open(self.__file_path, "w") as f:
            for key, value in self.__objects.items():
                json_dict.update({f"{key}" : value.to_dict()})

            json.dump(json_dict, f)

    def reload(self):
        """reloads __objects dictionary with objects from JSON file"""

        if exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)
