#!/usr/bin/python3

"""Unittests for FileStorage"""

import unittest
from models import BaseModel
from models import storage
from os.path import exists

from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """defines unittests for methods in FileStorage"""

    __file_path = "file.json"
    test_model = BaseModel()

    def test_new(self):
        """test if object is added to objects storage after creation"""
        storage.new(self.test_model)
        test_class_name = self.test_model.__class__.__name__
        test_id = self.test_model.id
        key = f"{test_class_name}.{test_id}"
        self.assertIn(key, storage.all())

    def test_all(self):
        """test that all returns correct data type"""
        self.assertIsInstance(storage.all(), dict)

    def test_save(self):
        """test that file exists after being saved"""
        storage.save()
        self.assertTrue(exists(self.__file_path))

    def test_reload(self):
        """test if object reloaded is same as before"""
        storage.new(self.test_model)
        test_class_name = self.test_model.__class__.__name__
        test_id = self.test_model.id
        key = f"{test_class_name}.{test_id}"

        storage.save()

        storage_reload = FileStorage()

        self.assertIn(key, storage_reload.all())


if __name__ == '__main__':
    unittest.main()
