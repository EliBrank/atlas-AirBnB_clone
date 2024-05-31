#!/usr/bin/python3
"""This is the console command"""
import sys, cmd


class HBNBCommand(cmd.Cmd):
    """Command or Console"""
    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()