#!/usr/bin/python3
"""This is the console command"""
import sys, cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command or Console"""
    prompt = '(hbnb) '
    classes = {
        'BaseModel' : BaseModel
    }

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

        if class_name not in HBNBCommand.classes:
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
        if class_name not in HBNBCommand.classes:
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

        new_instance = HBNBCommand.classes[class_name](**attributes)

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

        if c_name not in HBNBCommand.classes:
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

        if c_name not in HBNBCommand.classes:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
