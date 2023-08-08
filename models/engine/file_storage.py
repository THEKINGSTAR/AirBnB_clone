#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY TOW FUNDCITONS TO WRITE OBJECT INTO JSON FILE
Class FileStorage that serializes instances to a JSON file
and
deserializes JSON file to instances:
"""

import json
import os


class FileStorage():
    """
    Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)

    __objects: dictionary - empty but will store all objects by <class name>.id
    (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)

    Public instance methods:

    all(self): returns the dictionary __objects

    new(self, obj): sets in __objects the obj with key <obj class name>.id

    save(self): serializes __objects to the JSON file (path: __file_path)

    reload(self): deserializes the JSON file to __objects

    (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    """ filestorage class in engine folder """
    def  save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        function that writes an Object to a text file,
        using a JSON representation:
        """

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file, ensure_ascii=False)

    def reload(self):
        """
        deserializes the JSON file to __objects
        Write a function that creates an
        Object from a “JSON file”:
        """
        if not os.path.isfile(self.__file_path):
            return

        with open(self.__file_path, 'r', encoding="utf-8") as file:
            data = file.read()
            python_obj = json.loads(data)
        return (python_obj)
