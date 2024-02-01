#!/usr/bin/python3
import cmd

"""main module for the console"""


class HBNBCommand(cmd.Cmd):
    """main class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """function to quit when typing quit"""
        exit()

    def do_EOF(self, line):
        """function to exit when EOF (ctrl+D)"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
