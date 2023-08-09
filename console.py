#!/usr/bin/python3
""" module description : console in python
instead of frontend to test system"""


import cmd
import importlib

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
        """ creates instances(objs) of input class
        also save it to json file (file.json)
        Return: print the id of created instance 
        example : create BaseModel
        this will create instance of BaseModel class
        """
        # line is arguments or (just all text after main content)
        # print(f"line is: {line}")

        if len(line) < 1:
            print("** class name missing **")
            return
        # line is classname
        snake_class_name = self.pascal_to_snake(line)
        try:
            module = importlib.import_module('models.' + snake_class_name)
        except Exception:
            print("** class doesn't exist **")
            return
        print("class does exist")


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
