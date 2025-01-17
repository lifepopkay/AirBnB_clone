#!/usr/bin/python3
"""module name: console
This is the entry point of the interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The program prompt.
    ex: (hbnb)
    """
    prompt = "(hbnb) "

    all_classes = ['BaseModel', 'User', 'Amenity',
                   'Place', 'City', 'State', 'Review']
    a_f = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def preloop(self):
        print('Welcome to My Console')
        super(HBNBCommand, self).preloop()

    def precmd(self, line):
        """interchange the funtion and the class position"""
        if '.' in line and '(' in line and ')' in line:
            args_1 = line.split('.')
            d_cls = args_1[0]
            args_2 = args_1[1].split('(')
            func_1 = args_2[0]
            args_3 = args_2[1].split(')')
            func_2 = args_3[0]

            if d_cls in HBNBCommand.all_classes and func_1 in HBNBCommand.a_f:
                line = func_1 + ' ' + d_cls + ' ' + func_2
        return line

    def do_create(self, modelName):
        """Creates a new instance of BaseModel"""
        if modelName in HBNBCommand.all_classes:
            print("creating {}".format(modelName))
            newInstance = eval(modelName)()
            newInstance.save()
            print(newInstance.id)
        elif modelName == "":
            print(f"** class name missing **")
        else:
            print(f"** class doesn't exist **")

    def do_split_cmd(self, line):
        return line.split()

    def do_update(self, line):
        args = self.do_split_cmd(line)
        if line == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance = args[0] + "." + args[1]
            all_instance = storage.all()
            for obj in all_instance.keys():
                if obj == instance:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(all_instance[obj], args[2], args[3])
                        storage.save()
                    return
            else:
                print("** no instance found **")

    def do_show(self, line):
        args = self.do_split_cmd(line)
        if line == "":
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        if len(args) >= 2:
            instance = args[0] + "." + args[1]
            all_instance = storage.all()
            for obj in all_instance.keys():
                if obj == instance:
                    print(all_instance[obj])
                    break
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        args = self.do_split_cmd(line)
        if line == "":
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        if len(args) >= 2:
            all_instance = storage.all()
            for obj, val in all_instance.items():
                ob_name = val.__class__.__name__
                ob_id = val.id
                if ob_name == args[0] and ob_id == args[1]:
                    del val
                    del storage._FileStorage__objects[obj]
                    storage.save()
                    return
            else:
                print("** no instance found **")

    def do_all(self, line):
        all_obj = []
        all_instance = storage.all()
        if line == '':
            for obj in all_instance.keys():
                all_obj.append(str(all_instance[obj]))
            print(all_obj)
        elif line in HBNBCommand.all_classes:
            for obj in all_instance.keys():
                if obj.split('.')[0] == line:
                    all_obj.append(str(all_instance[obj]))
            print(all_obj)
        else:
            print("** class doesn't exist **")

    def do_count(self, line):
        """counts number of instances of a class"""
        count = 0
        all_instances = storage.all()
        for obj in all_instances.keys():
            obj_Class = obj.split('.')
            if obj_Class[0] == line:
                count = count + 1
        print(count)

    def do_EOF(self, line):
        """A method for proper terminal exit"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program.
        An easy way to exit the program"""
        return True

    def help_quit(self):
        """Helps to format the description of quit method"""
        print('\n'.join(['Quit: command to exit the program.',
                         'An easy way to exit the program.']))

    def emptyline(self):
        """Handle when an empty string is passed"""
        pass

    def default(self, line):
        """Handles unknown commands."""
        print("Unknown command:", line)

    def postloop(self):
        print('Goodbye, See you soon!')
        super(HBNBCommand, self).postloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
