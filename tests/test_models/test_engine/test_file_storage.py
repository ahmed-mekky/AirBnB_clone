#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Sets up test methods."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tears down test methods."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Tests instantiation of FileStorage class"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_path(self):
        """Tests file_path attribute"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects(self):
        """Tests objects attribute"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        """Tests all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Tests new method"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Tests save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn(obj.id, f.read())

    def test_reload(self):
        """Storage file is successfully loaded to __objects"""
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()["id"], loaded.to_dict()["id"])

    def test_reload_empty(self):
        """Load from an empty file"""
        with open("file.json", "w") as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(storage.reload(), None)
