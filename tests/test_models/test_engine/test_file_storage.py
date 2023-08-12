#!/usr/bin/python3
"""
test module
"""
import unittest
from models.engine import file_storage
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    FileStorage = file_storage.FileStorage

    def test_default_values_fs(self):
        """test default value"""
        self.FileStorage.save()

    def test_default_values(self):
        """test default value"""
        self.FileStorage.reload()

        self.assertDictEqual(self.FileStorage.all(), {})
