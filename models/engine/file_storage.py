#!/usr/bin/python3
"""
THIS MODULE CONTAIN THE ENGINE FUNDCITONS TO WRITE OBJECT INTO JSON FILE
Class FileStorage that serializes instances to a JSON file
and
deserializes JSON file to instances:
"""


import json
import os
from models import *  # Import all classes
import importlib


class FileStorage:
    """
    Class FileStorage that serializes
    instances to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        function that writes an Object to a text file,
        using a JSON representation: """
        # Get the objects from the class.__objects
        seral_objcts = {}
        for key, obj in FileStorage.__objects.items():
            seral_objcts[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(seral_objcts, file, ensure_ascii=False)

    def reload(self):
        """
        deserializes the JSON file to __objects
        Write a function that creates an
        Object from a “JSON file”:
        """
        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
            data = file.read()
            if data:
                python_obj = json.loads(data)
                for key, value in python_obj.items():
                    class_name, obj_id = key.split('.')
                    snake_class_name = self.pascal_to_snake(class_name)
                    # print(f"snake_class_name: {snake_class_name}")
                    module = importlib.import_module('models.' +
                                                     snake_class_name)
                    # __import__('models.' +class_name,fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

    @staticmethod
    def pascal_to_snake(name):
        """
        conver class name (pascal case)
        to file name(snake case)
        """
        snake_name = name[0].lower()  # first cap letter
        for char in name[1:]:
            if char.isupper():
                snake_name += '_' + char.lower()
            else:
                snake_name += char
        return snake_name
