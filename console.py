#!/usr/bin/python3
""" module description : console in python
instead of frontend to test system"""


import cmd
import importlib
# from models.engine.file_storage import FileStorage
from models import *
import re


class HBNBCommand(cmd.Cmd):
    """ airbnb console(command processor) """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """ quit from airbnb console on quit command """
        return True

    def do_EOF(self, line):
        """ exit on EOF (ctrl+D) """
        return True

    def emptyline(self):
        """ Handle empty line : Do nothing if it's
        an empty line.
        """
        pass

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
        module = self.cls_name_checker(line)

        if module is None:
            return  # return to console (without doing anything)

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

        # myargs[0] is classname
        module = self.cls_name_checker(myargs[0])

        if module is None:
            return

        # check if ID is not given in the input
        if len(myargs) != 2:  # or use < 2
            print("** instance id missing **")
            return

        # print("class does exist")

        # If the instance of the class name
        # doesn’t exist for the id
        # print ** no instance found **

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

        module = self.cls_name_checker(myargs[0])

        if module is None:
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
            # storage.rolad()
            # update json file to reflect the deleted instance
            storage.save()

    def do_all(self, line):  # get all objs of aclass
        """ show all instances(objs) of input class
        or show all instances if no class specified
        Like get all resource in any web API

        format : all {ClassName} or all
        example : all BaseModel or all
        this will show all instances of BaseModel class
        """

        # check if class name passed as argument to command all
        if line is not None and len(line) > 1:
            # myargs = line.split(' ')

            # check if this class name exist
            snake_class_name = self.pascal_to_snake(line)
            try:
                module = importlib.import_module('models.' + snake_class_name)
                # print(f"storage.all: {storage.all()}")
                str_list = []
                for key, objval in storage.all().items():
                    if line in key:  # if classname in key
                        # add string version of the object
                        str_list.append(str(objval))
                print(str_list)
                return

            except Exception as e:
                # print(f"error: {type(e).__name__}: {e}")
                print("** class doesn't exist **")
                return

        else:  # command is just all, without class name as argument
            str_list = [str(objval) for key, objval in storage.all().items()]
            print(str_list)

    def do_update(self, line):  # get by ID
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

        module = self.cls_name_checker(myargs[0])

        if module is None:
            return

        # check if ID is not given in the input
        if len(myargs) < 2:
            print("** instance id missing **")
            return

        req_inst = f"{myargs[0]}.{myargs[1]}"
        if req_inst not in storage.all():
            print("** no instance found **")
            return

        # print(storage.all()[req_inst])
        # print("instance exist complete your code here")

        # check if attrubiute name is not given in input
        if len(myargs) < 3:  # update BaseModel existing-id
            print("** attribute name missing **")
            return

        # check if attrubiute value is not given in input
        if len(myargs) < 4:  # update BaseModel Id first_name
            print("** value missing **")
            return

        attr_name = myargs[2]

        # myargs was created by spliting string with space delimeter
        # myargs items and line always of tyoe string that how cmd cast them
        # print(f"type of myargs[3]: {type(myargs[3])}")

        # order matters : this line handle case one word inside double quotes
        attr_val = myargs[3]  # other cases handled below
        # if other conditions was false this will be applied

        if myargs[3][0] == '"':  # if first char is double quote
            # join all myargs from index 3 till end in one string
            src_str = ' '.join(myargs[3:])
            # string in double quotes with optional leading/trailing spaces
            regex = r'^\s*"(.*?)"\s*$'
            match = re.search(regex, src_str)
            if match:  # or if match is not None:
                # found a match: get value between first double quotes
                # only first match, get str within double quotes
                # print(f"match group[0] :{match.group(0)}")
                # print(f"match group[1] :{match.group(1)}")

                attr_val = match.group(0)[1:-1]  # or attr_val = match.group(1)

            else:  # no match found only leading " exist
                print("## you forget to close double quotes on attr value##")

        else:  # no leading " in myargs[3]
            # then it could be one owrd string or int or float type
            attr_val = myargs[3]
            cast = None
            if '.' in attr_val:
                # handle casting if input was intended to be int or float
                cast = float
            elif re.search(r'[a-zA-Z]', attr_val):
                # attr_val conatain at least one letter so it is a string
                cast = None
            else:  # it is an integer it doesn't have any letters or . or "
                cast = int

        try:
            attr_val = cast(attr_val)
        except Exception:  # casting Failed
            pass

        # update or create attribute
        setattr(storage.all()[req_inst], attr_name, attr_val)
        # storage.reload()
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

    def cls_name_checker(self, line):
        """ check if this class name exist
        """
        snake_class_name = self.pascal_to_snake(line)
        try:
            return (importlib.import_module('models.' + snake_class_name))
        except Exception:
            print("** class doesn't exist **")
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
