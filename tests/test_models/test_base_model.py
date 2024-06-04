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

if __name__ == '__main__':
    unittest.main()
