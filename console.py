#!/usr/bin/python3
""" module description : console in python
instead of frontend to test system"""


import cmd
import importlib
#from models.engine.file_storage import FileStorage
from models import *

class HBNBCommand(cmd.Cmd):
    """ airbnb console(command processor) """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ quit from airbnb console on quit command """
        return True

    def do_EOF(self, line):
        """ exit on EOF (ctrl+D) """
        return True

    def do_create(self, line):
        """ creates an instance(obj) of input class
        also save it to json file (file.json)
        Return: print the id of created instance 
        example : create BaseModel
        this will create instance of BaseModel class
        """
        # line is arguments or (just all text after main content)
        # print(f"line is: {line}")
        # line is always of type str
        # print(f"line is: {type(line)}")

        # short circuit if line is None
        if line is None or len(line) < 1:
            print("** class name missing **")
            return

        # line is classname
        snake_class_name = self.pascal_to_snake(line)
        try:
            module = importlib.import_module('models.' + snake_class_name)
        except Exception:
            print("** class doesn't exist **")
            return

        # print("class does exist")

        # Now create instance of this class
        myclass = getattr(module, line)  # Again line is class name
        created_inst = myclass() 
        created_inst.save()
        print(created_inst.id)


    def do_show(self, line):  # get by ID
        """ show an instance(obj) of input class by
        Id given by user
        Like get resource by ID in any web API

        format : show BaseModel {id : int}
        example : show BaseModel 1234-1234-1234
        this will show an instance of BaseModel class
        """

        # short circuit if line is None
        if line is None or len(line) < 1:
            print("** class name missing **")
            return

        myargs = line.split(' ')

        # check if this class name exist
        # myargs[0] is classname
        snake_class_name = self.pascal_to_snake(myargs[0])
        try:
            module = importlib.import_module('models.' + snake_class_name)
        except Exception:
            print("** class doesn't exist **")
            return

        # check if ID is not given in the input
        if len(myargs) != 2:  # or use < 2 
            print("** instance id missing **")
            return

        # print("class does exist")

        # If the instance of the class name
        # doesn’t exist for the id
        # print ** no instance found **

        # %%% To be implemented later here %%%
        req_inst = f"{myargs[0]}.{myargs[1]}"
        if req_inst not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()[req_inst])


    def do_destroy(self, line):  # delete by ID
        """ deletes an instance(obj) of
        input class by Id given by user
        Like delete resource by ID in any web API

        format : destroy BaseModel {id : int}
        example : destroy BaseModel 1234-1234-1234
        this will delete an instance of BaseModel class
       """

        # short circuit if line is None
        if line is None or len(line) < 1:
            print("** class name missing **")
            return

        myargs = line.split(' ')

        # check if this class name exist
        # myargs[0] is classname
        snake_class_name = self.pascal_to_snake(myargs[0])
        try:
            module = importlib.import_module('models.' + snake_class_name)
        except Exception:
            print("** class doesn't exist **")
            return

        # check if ID is not given in the input
        if len(myargs) != 2:  # or use < 2 
            print("** instance id missing **")
            return

        # print("class does exist")

        req_inst = f"{myargs[0]}.{myargs[1]}"
        if req_inst not in storage.all():
            print("** no instance found **")
            return
        else:
           # delete the instance by ID
           # via del keyword that deletes objects
           del storage.all()[req_inst]
           # update json file to reflect the deleted instance
           storage.save()


    @staticmethod
    def pascal_to_snake(name):
        """ conver class name (pascal case)
        to file name(snake case)
        """
        snake_name = name[0].lower()  # first cap letter
        for char in name[1:]:
            if char.isupper():
                snake_name += '_' + char.lower()
            else:
                snake_name += char
        return snake_name        
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
