#!/usr/bin/python3

"""Unittests for console"""

import unittest
from models import User


class TestUser(unittest.TestCase):
    """defines unittests for methods in User"""

    def test_email(self):
        """test assigning email"""
        user_1 = User()
        # self.assertTrue("email" in u.__dir__())
        # u.email = "airbnb@mail.com"
        # self.assertEqual(u.email, "airbnb@mail.com")
        self.assertIsInstance(user_1.email, str)

# Test User: User.email
# Test User: User.password
# Test User: User.first_name
# Test User: User.last_name

if __name__ == '__main__':
    unittest.main()
