#!/usr/bin/python3

"""This is the console command"""

import sys
import cmd
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command or Console"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """exits the console"""
        return True

    def do_EOF(self, args):
        """'End of File' - exits the console"""
        return True

    def emptyline(self):
        """does nothing"""
        return False

    def do_all(self, args):
        """prints string representation of all instances of class

        if no class name passed, print string representation of all classes
        """

        # first initialize list to store python obj instances
        print_list = []
        # split args (input) and grab first (or only) argument
        # assign to class_name variable
        class_name = args.split()[0] if ' ' in args else args

        # get all class instances stored in __objects and put in obj_dict
        obj_dict = storage.all()

        # if no class name is specified, add all obj instances to list
        # add dictionary of objs to list as string representations
        if class_name == "":
            for key in obj_dict:
                print_list.append(str(obj_dict[key]))
            for item in print_list:
                print(item)
            return

        # if arg is passed, but not a valid class, give below error
        if class_name not in models.class_dict:
            print("** class doesn't exist **")
            return

        # here on assumes valid class name was passed
        # only adds objs from specified class
        for key, value in obj_dict.items():
            if class_name in key:
                print_list.append(str(value))
            for item in print_list:
                print(item)

    def do_create(self, args):
        """creates new instance of class

        additional attributes can be provided as key/value pairs
        """

        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        # assumes first arg is class name
        class_name = args_list[0]

        # checks if arg is valid <class name> (in class_dict)
        if class_name not in models.class_dict:
            print("** class doesn't exist **")
            return

        # since class name is taken care of
        # now evaluate remaining args from input
        args_list = args_list[1:]

        attributes = {}

        # search through the list of arguments
        for arg in args_list:
            # key/value pairs split and saved into arg_toks list
            arg_toks = arg.split("=")

            # Unquote, underscore to space
            if len(args_list) != 2:
                continue
            key, value = arg_toks[0], arg_toks[1]

            # convert values to appropriate data types
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('_', ' ')
            try:
                value = float(value)
            except ValueError:
                pass
            try:
                value = int(value)
            except ValueError:
                pass
            attributes[key] = value

        new_instance = models.class_dict[class_name](**attributes)

        # save call
        storage.new(new_instance)
        storage.save()

        print(new_instance.id)

    def do_show(self, args):
        """displays string representation of specified object

        requires class name and id as input arguments
        """

        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in models.class_dict:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = f"{c_name}.{c_id}"

        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """destroys a specified object

        requires class name and id as input arguments
        """

        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in models.class_dict:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_update(self, args):
        """updates an object with a given attribute

        requires class name and id as input arguments
        only one attribute can be updated at a time
        """

        if not args:
            print("** class name missing **")
            return

        args_list = args.split()

        # make sure args (input) includes all parameters
        if len(args_list) == 0:
            print("** class name missing **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        elif len(args_list) == 2:
            print("** attribute name missing **")
            return
        elif len(args_list) == 3:
            print("** value missing **")
            return

        # ensures list of arguments is 4 (args after 4 discarded)
        while (len(args_list) > 4):
            args_list.pop()

        class_name = args_list[0]

        if class_name not in models.class_dict:
            print("** class doesn't exist **")
            return

        class_id = args_list[1]

        key = f"{class_name}.{class_id}"

        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return

        attr_name = args_list[2]
        attr_val = args_list[3]

        # gets dictionary representation of object
        instance = obj_dict[key]

        # attempts to update below attributes will fail
        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        # cast attr_val to appropriate data type
        try:
            # checks if attr_val is a float (if it has decimal point)
            if "." in attr_val:
                attr_val = float(attr_val)
            else:
                attr_val = int(attr_val)
        except ValueError:
            # attr_val stays a string in this case
            pass

        setattr(instance, attr_name, attr_val)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
