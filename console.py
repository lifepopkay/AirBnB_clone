#!/usr/bin/python3
"""module name: console
This is the entry point of the interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The program prompt.
    ex: (hbnb)
    """
    prompt = "(hbnb) "

    def do_create(self, modelName):
        """Creates a new instance of BaseModel"""
        if modelName == "BaseModel":
            print(f"creating {modelName}")
            newInstance = BaseModel()
            newInstance.save()
            print(newInstance.id)
            
        elif modelName == "":
            print(f"** class name missing **")
        else:
            print(f"** class doesn't exist **")

    def do_split_cmd(self, line):
        return (line.split())

    def do_update(self, line):
        args = self.do_split_cmd(line)
        if line == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) >= 2:
            instance = args[0]+"."+args[1]
            all_instance = storage.all()
            for obj in all_instance.keys():
                if obj == instance:
                    update_instance = (all_instance[obj])
                    break
            else:
                print("** no instance found **")
        if len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        # this is where i stopped all other function working fine ATM
        
            

    def do_show(self, line):
        args = self.do_split_cmd(line)
        if line == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        if len(args) >= 2:
            instance = args[0]+"."+args[1]
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
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        if len(args) >= 2:
            instance = args[0]+"."+args[1]
            all_instance = storage.all()
            for obj in all_instance.keys():
                if obj == instance:
                    all_instance.pop(obj)
                    break
            else:
                print("** no instance found **")

    def do_all(self, line):
        all_obj = []
        if line == '' or line == 'BaseModel':
            all_instance = storage.all()
            for obj in all_instance.keys():
                all_obj.append(str(all_instance[obj]))
            print(all_obj)
        else:
            print("** class doesn't exist **")
    
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

    def postloop(self):
        """Implement the print of a newline during exit"""
        print(end="")

    def emptyline(self):
        """Handle when an empty string is passed"""
        pass

    def default(self, line):
        """Handles unknown commands."""
        print("Unknown command:", line)


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
