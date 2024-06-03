#!/usr/bin/python3
"""This is the console command"""
import sys, cmd, models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command or Console"""
    prompt = '(hbnb) '

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """Quitter"""
        exit()

    def do_EOF(self, arg):
        """Handles EOF to exit prog"""
        print()
        exit()

    def emptyline(self):
        """Does nothing"""
        pass

    def do_all(self, args):
        print_list = []
        class_name = args.split(' ')[0] if ' ' in args else args

        if class_name not in models.class_dict:
            print("** class name doesn't exist **")
            return

        for key, value in storage._FileStorage__objects.items():
            if class_name in key:
               print_list.append(str(value))

            if not print_list:
                print("** class doesn't exist **")
                return

            else:
                for item in print_list:
                    print(item)



    def do_create(self, args):
        """creates new instance of class"""
        if not args:
            print("** class name missing **")
            return

        args_len = args.split()
        class_name = args_len[0]
        #is class in HBNBcommand?
        if class_name not in models.class_dict:
            print("** class doesn't exist **")
            return

        args_len = args_len[:1]

        attributes = {}
        #Searsch through the list of arguements
        for arg in args_len:
            arg_toks = arg.split("=")
            #Unquote, underscore to space
            if len(args_len) != 2:
                continue
            key, value = arg_toks[0], arg_toks[1]
            #convert values to appropriate data types
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

        #save call
        storage.new(new_instance)
        storage.save()

        print(new_instance.id)

    def do_show(self, args):
        """Display"""
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
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destroys a specified object """
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
        """Updates an instance by its ID"""
        args_split = args.split(' ')
        if len(args_split)!= 5:
            print("** Invalid Syntax: Usage: update <class name> <id> <attribute name> <new value> **")
            return

        c_name = args_split[0]
        c_id  = args_split[1]
        attr_name = args_split[2]
        attr_val = args_split[3]

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        if not attr_name:
            print("** attribute name missing **")
            return

        if not attr_name:
            print("** value missing **")

        key = f"{c_name}.{c_id}"

        if key not in storage._FileObject__objects:
            print("** no instance found **")
            return

        instance = storage._FileObjects__objects[key]
        attr_type = type(getattr(instance, attr_name, None))

        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        try:
            if isinstance(attr_type, str):
                value = attr_val.strip('"')
            elif isinstance(attr_type, float):
                value = float(attr_val)
            elif isinstance(attr_type, int):
                value = int(attr_val)
            else:
                raise ValueError
        except ValueError:
            print("** value missing **")
            return

        obj = storage._FileStorage__objects[key]

        storage.update(obj, attr_name, value)








if __name__ == '__main__':
    HBNBCommand().cmdloop()
