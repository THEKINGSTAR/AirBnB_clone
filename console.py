#!/usr/bin/python3
""" module description : console in python
instead of frontend to test system"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ airbnb console(command processor) """

    prompt = '(hbnb) '

    def do_greet(self, line):
        """ just for testing """
        print("hello")

    def do_quit(self, line):
        """ quit from airbnb console on quit command """
        return True

    def do_EOF(self, line):
        """ exit on EOF (ctrl+D) """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
