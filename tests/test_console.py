#!/usr/bin/python3
"""
test module
"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models.user import User
from models import storage


class TestConstructor(unittest.TestCase):
    """test class"""

    def test_help_method(self):
        """test help"""
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

    def test_create(self):
        """test create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Emad")
            self.assertEqual("** class doesn't exist **", f.getvalue()[:-1])

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            classes_dict = storage.all()
            self.assertTrue("User."+f.getvalue()[:-1] in storage.all().keys())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """test create"""
        HBNBCommand().onecmd("create BaseModel")
        output = mock_stdout.getvalue()
        self.assertTrue(len(output) == 37)  # Length of UUID
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

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertIn("** class name missing **", f.getvalue())

            HBNBCommand().onecmd("show Emad")
            self.assertIn("** class doesn't exist **", f.getvalue())

            HBNBCommand().onecmd("show User")
            self.assertIn("** instance id missing **", f.getvalue())

            HBNBCommand().onecmd("show User 3212133")
            self.assertIn("** no instance found **", f.getvalue())

            new_user = User()
            new_user.save()
            HBNBCommand().onecmd(f"show User {new_user.id}")
            self.assertIn(new_user.__str__(), f.getvalue())

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
            new_user = User()

            new_user.save()
            HBNBCommand().onecmd(f"update User {new_user.id}")
            self.assertIn("** attribute name missing **", f.getvalue())

            HBNBCommand().onecmd(f"update User {new_user.id} name")
            self.assertIn("** value missing **", f.getvalue())

            HBNBCommand().onecmd(f"update User {new_user.id} name 'emad'")
            self.assertIn("", f.getvalue())
            # TODO destroy class
