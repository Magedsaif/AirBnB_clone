#!/usr/bin/python3
"""Console module"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    command interprater class
    """
    prompt = '(hbnb) '
    classes_dict = {"BaseModel": BaseModel}

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        else:
            try:
                myclass = eval(line + "()")
                myclass.save()
                print(myclass.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, line):
        line_vactor = line.split()

        if line_vactor == []:
            print("** class name missing **")
        elif self.classes_dict.get(line_vactor[0]) is None:
            print("** class doesn't exist **")
        elif len(line_vactor) != 2:
            print("** instance id missing **")
        myobjects = storage.all()
        returned_object = myobjects.get(line_vactor[0] + "." + line_vactor[1])
        if returned_object is None:
            print("** no instance found **")
        else:
            myclass = eval(line_vactor[0] + "(**returned_object)")
            print(myclass)

    def do_destroy(self, line):
        line_vactor = line.split()
        if line_vactor == []:
            print("** class name missing **")
        elif self.classes_dict.get(line_vactor[0]) is None:
            print("** class doesn't exist **")
        elif len(line_vactor) != 2:
            print("** instance id missing **")
        myobjects = storage.all()
        try:
            myobjects.pop(line_vactor[0] + "." + line_vactor[1])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        line_vactor = line.split()

        objects_string_representation = []
        class_to_represent = None
        if line_vactor != []:
            class_to_represent = line_vactor[0]
            if class_to_represent not in self.classes_dict:
                print("** class doesn't exist **")
                return

        myobjects = storage.all()
        for o_key, o_value in myobjects.items():
            calss_name = o_key.split(".")[0]
            if class_to_represent is not None:
                print(f"class name {calss_name}")
                print(f"class_to_represent {class_to_represent}")
                if calss_name == class_to_represent:

                    myclass = eval(calss_name + "(**o_value)")
                else:
                    continue
            else:
                myclass = eval(calss_name + "(**o_value)")
            objects_string_representation.append(myclass.__str__())
        print(objects_string_representation)

    def do_update(self, line):
        #             0         1         2                 3
        # update <class name> <id> <attribute name> "<attribute value>"
        line_vector = line.split()
        v_len = len(line_vector)
        if line_vector == []:
            print("** class name missing **")

        elif line_vector[0] not in self.classes_dict:
            print("** class doesn't exist **")
        elif v_len < 2:
            print("** instance id missing **")
        else:
            myobjects = storage.all()
            my_dict_object = myobjects.get(
                line_vector[0] + "." + line_vector[1])
            if my_dict_object is None:
                print("** no instance found **")
            elif v_len < 3:
                print("** attribute name missing **")
            elif v_len < 4:
                print("** value missing **")
            else:
                myclass = eval(line_vector[0] + "(**my_dict_object)")
                setattr(myclass, line_vector[2], line_vector[3])  
                my_dict_object[line_vector[0] + "." + line_vector[1]] = myclass.to_dict()
                myclass.save()
                print(myobjects)
                print("\n\n\n")
                print(myclass)
                print("\n\n\n")
                print("saved")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
