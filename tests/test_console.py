#!/usr/bin/python3
"""
test module
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class TestConstructor(unittest.TestCase):
    """test class"""
    __classes_dict = {"BaseModel": BaseModel, "State": State, "State": State,
                      "City": City, "Amenity": Amenity,
                      "Place": Place, "Review": Review, "User": User}

    def test_help_method(self):
        """test help"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(
                "Quit command to exit the program.", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual("EOF command to exit the program.",
                             f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                """Creates a new instance of BaseModel, saves it""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual("""Print the string representation of an instance
        based on the class name and id.""", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                """Delete an instance based on the class name and id.""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(
                """Print all string representation of all instances""",
                f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(
                """Updates an instance based on the class name and id""",
                f.getvalue()[:-1])

        #         with patch('sys.stdout', new=StringIO()) as f:
        #             HBNBCommand().onecmd("help")
        #             self.assertEqual(
        #                 """
        # Documented commands (type help <topic>):
        # ========================================
        # EOF  all  count  create  destroy  help  quit  show  update
        # """, f.getvalue()[:-1])

    def rest_file_storage(self):
        if os.path.isfile("file.json"):
            os.remove("file.json")
        storage._FileStorage__objects = {}

    def create_new_objects(self):
        u = User()
        a = Amenity()
        s = State()
        c = City()
        p = Place()
        r = Review()
        b = BaseModel()
        storage.save()

    def test_create(self):
        """test create"""
        self.rest_file_storage()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        for k in self.__classes_dict.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(f"create {k}")
                classes_dict = storage.all()
                self.assertTrue(f"{k}."+f.getvalue()
                                [:-1] in storage.all().keys())
        self.assertTrue(os.path.isfile("file.json"))
    
    # def test_show(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("show")
    #         self.assertEqual("** class name missing **", f.getvalue()[:-1])

    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("show Emad")
    #         self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("show User")
    #         self.assertEqual("** instance id missing **", f.getvalue()[:-1])

    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("show User 3212133")
    #         self.assertEqual("** no instance found **", f.getvalue()[:-1])
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         new_user = User()
    #         new_user.save()
    #         HBNBCommand().onecmd(f"show User {new_user.id}")
    #         self.assertEqual(new_user.__str__(), f.getvalue()[:-1])

    # def test_show(self):
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("show")
    #         self.assertIn("** class name missing **", f.getvalue())

    #         HBNBCommand().onecmd("show Emad")
    #         self.assertIn("** class doesn't exist **", f.getvalue())

    #         HBNBCommand().onecmd("show User")
    #         self.assertIn("** instance id missing **", f.getvalue())

    #         HBNBCommand().onecmd("show User 3212133")
    #         self.assertIn("** no instance found **", f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertIn("** class name missing **", f.getvalue())

            HBNBCommand().onecmd("destroy Emad")
            self.assertIn("** class doesn't exist **", f.getvalue())

            HBNBCommand().onecmd("destroy User")
            self.assertIn("** instance id missing **", f.getvalue())

            HBNBCommand().onecmd("destroy User 3212133")
            self.assertIn("** no instance found **", f.getvalue())
            # TODO destroy class

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Emad")
            self.assertIn("** class doesn't exist **", f.getvalue())

            # TODO all class

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertIn("** class name missing **", f.getvalue())

            HBNBCommand().onecmd("update Emad")
            self.assertIn("** class doesn't exist **", f.getvalue())

            HBNBCommand().onecmd("update User")
            self.assertIn("** instance id missing **", f.getvalue())

            HBNBCommand().onecmd("update User 3212133")
            self.assertIn("** no instance found **", f.getvalue())
            # create a new user
            # TODO destroy class
