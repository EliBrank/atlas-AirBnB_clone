#!/usr/bin/python3

"""Unittests for console"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """defines unittests for methods in Console"""

    def test_EOF(self):
        """test if EOF correctly exits prompt"""
        obj_4 = Base()
        self.assertEqual(obj_4.id, 3)

# (hbnb) help
#
# Documented commands (type help <topic>):
# ========================================
# EOF  help  quit
#
# (hbnb) 
# (hbnb) help quit
# Quit command to exit the program
#
# (hbnb) 
# (hbnb) 
# (hbnb) quit 

if __name__ == '__main__':
    unittest.main()
