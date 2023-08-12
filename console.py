#!/usr/bin/python3
"""Console module."""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter class."""

    prompt = '(hbnb) '
    classes_dict = {"BaseModel": BaseModel, "State": State, "State": State,
                    "City": City, "Amenity": Amenity,
                    "Place": Place, "Review": Review, "User": User}

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if line == "":
            print("** class name missing **")
            return
        else:
            try:
                myclass = eval(line + "()")
                myclass.save()
                print(myclass.id)
            except Exception as e:
                print("** class doesn't exist **")
                return

    def do_show(self, line):
        """Print the string representation of an instance
        based on the class name and id."""
        line_vactor = line.split()

        if line_vactor == []:
            print("** class name missing **")
            return
        elif self.classes_dict.get(line_vactor[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(line_vactor) != 2:
            print("** instance id missing **")
            return
        myobjects = storage.all()
        returned_object = myobjects.get(line_vactor[0] + "." + line_vactor[1])
        if returned_object is None:
            print("** no instance found **")
            return
        else:
            myclass = eval(line_vactor[0] + "(**returned_object)")
            print(myclass)

    def do_destroy(self, line):
        """Delete an instance based on the class name and id.
        (save the change into the JSON file).
        """
        line_vactor = line.split()
        if line_vactor == []:
            print("** class name missing **")
            return
        elif self.classes_dict.get(line_vactor[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(line_vactor) != 2:
            print("** instance id missing **")
            return
        myobjects = storage.all()
        try:
            myobjects.pop(line_vactor[0] + "." + line_vactor[1])
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, line):
        """Print all string representation of all instances
        based or not on the class name.
        """
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
                if calss_name == class_to_represent:
                    myclass = eval(calss_name + "(**o_value)")
                else:
                    continue
            else:
                myclass = eval(calss_name + "(**o_value)")
            objects_string_representation.append(myclass.__str__())
        print(objects_string_representation)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        # TODO dont update create id
        line_vector = line.split()
        vector_len = len(line_vector)
        if line_vector == []:
            print("** class name missing **")
            return
        elif line_vector[0] not in self.classes_dict:
            print("** class doesn't exist **")
            return
        elif vector_len < 2:
            print("** instance id missing **")
            return
        else:
            objects_dict = storage.all()
            object_key = line_vector[0] + "." + line_vector[1]
            if object_key not in objects_dict:
                print("** no instance found **")
                return
            elif vector_len < 3:
                print("** attribute name missing **")
                return
            elif vector_len < 4:
                print("** value missing **")
                return
            else:
                object_class = eval(
                    line_vector[0] + "(**objects_dict[object_key])")
                setattr(object_class, line_vector[2],  eval(line_vector[3]))
                objects_dict[object_key] = object_class.to_dict()
                object_class.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
