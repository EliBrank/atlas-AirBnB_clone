#!/usr/bin/python3

"""Unittests for City"""

import unittest
from models import City


class TestCity(unittest.TestCase):
    """defines unittests for methods in City"""

    def test_attr(self):
        """test that attributes of City are correct attribute"""
        city_1 = City()
        self.assertIsInstance(city_1.state_id, str)
        self.assertIsInstance(city_1.name, str)

if __name__ == '__main__':
    unittest.main()
