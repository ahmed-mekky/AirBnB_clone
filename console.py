#!/usr/bin/python3
"""main module for the console"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models import storage


classes = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """main class"""

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, line):
        """function to quit when typing quit"""
        exit()

    def do_EOF(self, line):
        """function to exit when EOF (ctrl+D)"""
        return True

    def do_create(self, line):
        """function that creats an instance of a class"""
        commands = line.strip().split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in classes:
            print("** class doesn't exist **")
        else:
            MyModel = classes[commands[0]]()
            print(MyModel.id)
            storage.save()

    def do_show(self, line):
        """function to list an instance by its id"""
        commands = line.strip().split()
        if len(commands) < 1:
            print("** class name missing **")
        elif len(commands) < 2:
            print("** instance id missing **")
        elif commands[0] not in classes:
            print("** class doesn't exist **")
        else:
            try:
                print(storage.all()[f"{commands[0]}.{commands[1]}"])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """function that deletes instances"""
        commands = line.strip().split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            rmkey = None
            for key in storage.all().keys():
                if re.match(rf"^{commands[0]}.{commands[1]}", key):
                    rmkey = key
            if rmkey:
                storage.all().pop(rmkey)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """function to print instances"""
        commands = line.strip().split()
        models = []
        notExist = True
        for key, model in storage.all().items():
            if len(commands) >= 1:
                if re.match(rf"^{commands[0]}*", key):
                    models.append(str(model))
                    notExist = False
            else:
                models.append(str(model))
                notExist = False
        if notExist:
            print("** class doesn't exist **")
        else:
            print(models)

    def do_update(self, line):
        """function that updates instances"""
        commands = line.strip().split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            model = None
            modelkey = None
            for key in storage.all().keys():
                if re.match(rf"^{commands[0]}.{commands[1]}", key):
                    model = storage.all().get(key)
                    modelkey = key
            if model is None:
                print("** no instance found **")
            else:
                if len(commands) < 3:
                    print("** attribute name missing **")
                elif len(commands) < 4:
                    print("** value missing **")
                else:
                    model.__setattr__(commands[2], commands[3])
                    storage.all()[modelkey] = model
                    storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
