#!/usr/bin/python3
"""
test module
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConstructor(unittest.TestCase):
    def test_help_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertIn("Quit command to exit the program.", f.getvalue())

            HBNBCommand().onecmd("help EOF")
            self.assertIn("EOF command to exit the program.", f.getvalue())

            HBNBCommand().onecmd("help create")
            self.assertIn("""Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id""", f.getvalue())

            HBNBCommand().onecmd("help show")
            self.assertIn("""Print the string representation of an instance
        based on the class name and id.""", f.getvalue())

            HBNBCommand().onecmd("help destroy")
            self.assertIn("""Delete an instance based on the class name and id.
        (save the change into the JSON file).""", f.getvalue())

            HBNBCommand().onecmd("help all")
            self.assertIn("""Print all string representation of all instances
        based or not on the class name.""", f.getvalue())

            HBNBCommand().onecmd("help update")
            self.assertIn("""Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).""", f.getvalue())
