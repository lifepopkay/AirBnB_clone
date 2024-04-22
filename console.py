#!/usr/bin/python3
"""
module name: console
This is the entry point of the interpreter.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """This is the console for Airbnb"""
    """
        The program prompt.
        ex: (hbnb)
    """
    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    def do_create(self, line):
        """Create a new instance od basemodel"""

        if not line:
            print("** class name missing **")
        elif line not in self.l_classes:
            print("** class doesn't exist **")
        else:
            print("createing {}".format(line))
            print()
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """Print string representation of an instance"""

        if line == '':
            print("** class name missing **")
            return

        args = line.split()

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            """call all instances from the storage"""
            my_storage = storage.all()
            for obj in my_storage.keys():
                instance = args[0] + '.' + args[1]
                if obj == instance:
                    print(my_storage[obj])
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance from the storage"""

        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            """call storage file and check present of instance"""
            my_storage = storage.all()
            for obj, val in my_storage.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == args[0] and ob_id == args[1]:
                    del val
                    del storage._FileStorage__objects[obj]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        all_obj = []
        if line == '' or line == 'BaseModel':
            all_instance = storage.all()
            for obj in all_instance.keys():
                all_obj.append(str(all_instance[obj]))
            print(all_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argv in arg.split(','):
            a = a + argv

        args = shlex.split(a)

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """Quit command to exit the program.
        An easy way to exit the program"""
        return True

    def do_EOF(self, line):
        """A method for proper terminal exit"""
        print()
        return True

    def emptyline(self):
        """Handle when an empty string is passed"""
        pass

    def default(self, line):
        """Handles unknown commands."""
        print("Unknown command:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
