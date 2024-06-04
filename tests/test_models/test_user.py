#!/usr/bin/python3

"""Unittests for User"""

import unittest
from models import User


class TestUser(unittest.TestCase):
    """defines unittests for methods in User"""

    def test_attr(self):
        """test that attributes of User are correct attribute"""
        user_1 = User()
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.last_name, str)

if __name__ == '__main__':
    unittest.main()
