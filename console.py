#!/usr/bin/python3
"""module name: console
This is the entry point of the interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The program prompt.
    ex: (hbnb)
    """
    prompt = "(hbnb) "

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
    HBNBCommand().cmdloop()
