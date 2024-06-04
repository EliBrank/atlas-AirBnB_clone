#!/usr/bin/python3

"""Unittests for State"""

import unittest
from models import State


class TestState(unittest.TestCase):
    """defines unittests for methods in State"""

    def test_attr(self):
        """test that attributes of State are correct attribute"""
        state_1 = State()
        self.assertIsInstance(state_1.name, str)

if __name__ == '__main__':
    unittest.main()
