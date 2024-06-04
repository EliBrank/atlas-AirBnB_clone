#!/usr/bin/python3

"""Unittests for Place"""

import unittest
from models import Place


class TestPlace(unittest.TestCase):
    """defines unittests for methods in Place"""

    def test_attr(self):
        """test that attributes of Place are correct attribute"""
        place_1 = Place()
        self.assertIsInstance(place_1.city_id, str)
        self.assertIsInstance(place_1.user_id, str)
        self.assertIsInstance(place_1.name, str)
        self.assertIsInstance(place_1.description, str)
        self.assertIsInstance(place_1.number_rooms, int)
        self.assertIsInstance(place_1.number_bathrooms, int)
        self.assertIsInstance(place_1.max_guest, int)
        self.assertIsInstance(place_1.price_by_night, int)
        self.assertIsInstance(place_1.latitude, float)
        self.assertIsInstance(place_1.longitude, float)
        self.assertIsInstance(place_1.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
