#!/usr/bin/python3
"""
test module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestConstructor(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    fs = FileStorage()

    def test_default_values_fs(self):
        """test default value"""
        
        self.fs.save()
        self.fs.reload()
