#!/usr/bin/python3
"""This is the console command"""
import sys, cmd


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

    def do_create(self, args):
        """ A Doozy"""
        # If the class name is missing, print ** class name missing ** (ex: $ create)
        if not args:
            print("** class name missing **")
            return

        args_len =  args_len.split()

        class_name = args_len[0]

        # If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        if class_name not in HBNBCommand():
            print("** class doesnt exist**")
            return

        args_len =  args_len[1:]

    def do_show(self, args):
        """Shows"""
        pass

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
