#!/usr/bin/python3

"""Unittests for Amenity"""

import unittest
from models import Amenity


class TestAmenity(unittest.TestCase):
    """defines unittests for methods in Amenity"""

    def test_attr(self):
        """test that attributes of Amenity are correct attribute"""
        amenity_1 = Amenity()
        self.assertIsInstance(amenity_1.name, str)

if __name__ == '__main__':
    unittest.main()
