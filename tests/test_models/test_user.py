#!/usr/bin/python3

"""Unittests for console"""

import unittest
from models import User


class TestUser(unittest.TestCase):
    """defines unittests for methods in User"""

    def test_attr(self):
        """test that all attributes of User are correct attribute"""
        user_1 = User()
        self.assertIsInstance(user_1.email, str)
        self.assertIsInstance(user_1.password, str)
        self.assertIsInstance(user_1.first_name, str)
        self.assertIsInstance(user_1.last_name, str)

# Test User: User.email
# Test User: User.password
# Test User: User.first_name
# Test User: User.last_name

if __name__ == '__main__':
    unittest.main()
