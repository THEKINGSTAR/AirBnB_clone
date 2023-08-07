#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY TOW FUNDCITONS TO WRITE OBJECT INTO JSON FILE
Class FileStorage that serializes instances to a JSON file
and
deserializes JSON file to instances:
"""

import json


class FileStorage():
    """ filestorage class in engine folder """
    def save_to_json_file(my_obj, filename):
        """
        function that writes an Object to a text file,
        using a JSON representation:
        """

        # if isinstance(my_obj, set):
        #   my_obj = list(my_obj)

        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(my_obj, file, ensure_ascii=False)

    def load_from_json_file(filename):
        """
        Write a function that creates an
        Object from a “JSON file”:
        """
        with open(filename, 'r', encoding="utf-8") as file:
            data = file.read()
            python_obj = json.loads(data)
        return (python_obj)
