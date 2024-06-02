#!/usr/bin/python3
"""This module defines a class named FileStorage"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """This class serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects"""
        return self.__objects