#!/usr/bin/python3

"""Unittests for Review"""

import unittest
from models import Review


class TestReview(unittest.TestCase):
    """defines unittests for methods in Review"""

    def test_attr(self):
        """test that attributes of Review are correct attribute"""
        review_1 = Review()
        self.assertIsInstance(review_1.place_id, str)
        self.assertIsInstance(review_1.user_id, str)
        self.assertIsInstance(review_1.text, str)

if __name__ == '__main__':
    unittest.main()
