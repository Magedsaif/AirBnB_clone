#!/usr/bin/python3
"""
test module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestFileStorageMethods(unittest.TestCase):

    def setUp(self):
        self.fs = FileStorage()

    def test_all_method(self):
        # Initially, the all() method should return an empty dictionary
        all_objects = self.fs.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        new_base_model = BaseModel()
        self.fs.new(new_base_model)
        
        all_objects = self.fs.all()
        self.assertIn(f"BaseModel.{new_base_model.id}", all_objects)
        self.assertIs(all_objects[f"BaseModel.{new_base_model.id}"], new_base_model)

    def test_save_method(self):
        new_base_model = BaseModel()
        self.fs.new(new_base_model)
        self.fs.save()

        with open(self.fs._FileStorage__file_path, 'r') as file:
            file_contents = file.read()
            self.assertIn(new_base_model.id, file_contents)

    def test_reload_method(self):
        new_base_model = BaseModel()
        self.fs.new(new_base_model)
        self.fs.save()

        self.fs.reload()

        all_objects = self.fs.all()
        self.assertIn(f"BaseModel.{new_base_model.id}", all_objects)
        self.assertIsInstance(all_objects[f"BaseModel.{new_base_model.id}"], BaseModel)
        self.assertEqual(all_objects[f"BaseModel.{new_base_model.id}"].id, new_base_model.id)
        self.assertEqual(all_objects[f"BaseModel.{new_base_model.id}"].created_at, new_base_model.created_at)
        self.assertEqual(all_objects[f"BaseModel.{new_base_model.id}"].updated_at, new_base_model.updated_at)
