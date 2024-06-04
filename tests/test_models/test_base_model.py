import unittest
from models.base_model import BaseModel
from console import *
import sys
import os


class BaseModel(unittest.TestCase):
    b1 = BaseModel()

    def test_save(self):
        self.b1.save()

        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_to_dict(self):
        dict_repr = self.b1.to_dict()

        #Check if created returned dict contains all attributes
        self.assertIsInstance(dict_repr,dict)


if __name__ == '__main__':
    unittest.main()
