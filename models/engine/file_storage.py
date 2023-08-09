#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY TOW FUNDCITONS TO WRITE OBJECT INTO JSON FILE
Class FileStorage that serializes instances to a JSON file
and
deserializes JSON file to instances:
"""


import json
import os
from models import *  # Import all classes


class FileStorage:
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
        """print("#" * 30)"""
        """print(f"TEST CHECK all  __objects method {FileStorage.__objects}")"""
        """print("#" * 30)"""
        
        return (FileStorage.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, str(obj.id))
        
        """print("#" * 30)"""
        """print(f"TEST CHECK new method key  {key}")"""
        """print("#" * 30)"""
        
        FileStorage.__objects[key] = obj

    """ filestorage class in engine folder """
    def  save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        function that writes an Object to a text file,
        using a JSON representation:
        """
        seral_objcts = {}
        for key, obj in FileStorage.__objects.items():
            seral_objcts[key] = obj.to_dict()
        
        """print(f"TEST CHECK SERIALIZED OBJECTS {seral_objcts}")"""
        
        """
        FIX THE {} IN 'file.json'
        NOW WILL CHEC IF THERE IS DATA IN THE FILE LOAD IT IN DICTIONARY
        AND CONTINUE TO UPDATE seral_obexts with it 
        FINALY ADD THESE DATA TO THE 'file.json'
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as read:
                read_data = json.load(read)
            seral_objcts.update(read_data)
        
        """print(f"TEST CHECK IF UPDATED SERIALIZED OBJECTS {seral_objcts}")"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            
            """print("#" * 30)"""
            """print(f"TEST CHECK save methond  {FileStorage.__objects}")"""
            """print("#" * 30)"""
            
            json.dump(seral_objcts, file, ensure_ascii=False)

    def reload(self):
        """
        deserializes the JSON file to __objects
        Write a function that creates an
        Object from a “JSON file”:
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        import importlib
        with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
            data = file.read()
            if data:
                python_obj = json.loads(data)
                for key, value in python_obj.items():
                    class_name, obj_id = key.split('.')
                    snake_class_name = self.pascal_to_snake(class_name)
                    # print(f"snake_class_name: {snake_class_name}")
                    module = importlib.import_module('models.' + snake_class_name)
                    # module = __import__('models.' + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj

    @staticmethod
    def pascal_to_snake(name):
        snake_name = name[0].lower()  # first cap letter
        for char in name[1:]:
            if char.isupper():
                snake_name += '_' + char.lower()
            else:
                snake_name += char
        return snake_name
