#!/usr/bin/env python3
""" Import modules """

import cmd
import json
import shlex
import re
import ast
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ The class definition """
    prompt = "(hbnb) "

    __classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
            }

    def do_create(self, line):
        """ create method
        Args:
            line: the input
        """
        arg = line.split()
        if (len(line) == 0):
            print("** class name missing **")
            return
        elif (arg[0] in self.__classes.keys()):
            new_obj = self.__classes[arg[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """ quit method
        Args:
            line: the input
        """
        return (True)

    def do_EOF(self, line):
        """ EOF method
        Args:
            line: the input
        """
        print("")
        return (True)

    def emptyline(self):
        """ emptyline method """
        pass

    def do_show(self, line):
        """ show method
        Args:
            line: the input
        """
        arg = line.split()
        if (len(line) == 0):
            print("** class name missing **")
            return
        elif (arg[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(arg) > 1):
            Str = f"{arg[0]}.{arg[1]}"
            if (Str in storage.all().keys()):
                print(storage.all()[Str])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, line):
        """ destroy method
        Args:
            line: the input
        """
        arg = line.split()
        if (len(line) == 0):
            print("** class name missing **")
            return
        elif (arg[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(arg) > 1):
            Str = f"{arg[0]}.{arg[1]}"
            if (Str in storage.all()):
                storage.all().pop(Str)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, line):
        """ all method
        Args:
            line: the input
        """
        arg = shlex.split(line)
        obj_list = []
        if (len(arg) == 0):
            for val in storage.all().values():
                obj_list.append(str(val))
            print(obj_list)
        else:
            if (arg[0] not in self.__classes.keys()):
                print("** class doesn't exist **")
                return
            else:
                for obj in storage.all().values():
                    if (type(obj).__name__ == arg[0]):
                        obj_list.append(str(obj))
                print(obj_list)

    def do_count(self, line):
        """ count method
        Args:
            line: the input
        """
        args = line.split()
        if (len(args) == 0):
            print("** class name missing **")
            return
        name_of_class = args[0]
        if (name_of_class not in self.__classes.keys()):
            print("** class doesn't exist **")
            return
        counter = 0
        for inst in storage.all().values():
            if (inst.__class__.__name__ == name_of_class):
                counter += 1
        print(counter)

    def do_update(self, line):
        """ update method
        Args:
            line: the input
        """
        arg = line.split()
        if (len(arg) == 0):
            print("** class name missing **")
            return
        elif (len(arg) == 1):
            print("** instance id missing **")
            return
        elif (arg[0] not in self.__classes.keys()):
            print("** class doesn't exist **")
            return
        else:
            Str = arg[0] + "." + arg[1]
            if (len(arg) < 3):
                print("** attribute name missing **")
                return
            elif (len(arg) < 4):
                print("** value missing **")
                return
            elif (Str not in storage.all().keys()):
                print("** no instance found **")
            else:
                setattr(storage.all()[Str], arg[2], arg[3])
                storage.save()

    def default(self, line):
        """ default method
        Args:
            line: the input
        """
        Comd_dict = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'count': self.do_count
                }
        if (line is None):
            return
        args = line.split(".")
        if (len(args) != 2):
            super().default(line)
            return

        Comd_Pattern = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        Para_Pattern_part1 = r'^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\})))?'
        Para_Pattern_part2 = r'(?:,\s*(?:("?[^"]+"?)))?'
        Para_Pattern = Para_Pattern_part1 + Para_Pattern_part2
        matching = re.match(Comd_Pattern, line)
        if (not matching):
            super().default(line)
            return
        Name_of_class, Method, Param = matching.groups()
        matching = re.match(Para_Pattern, Param)
        if (matching):
            Param = []
            for item in matching.groups():
                if (item):
                    Param.append(item)
        else:
            Param = []

        command = " ".join([Name_of_class] + Param)
        if (Method == 'update'):
            dict_match = re.search(r'\{([^}]+)\}', str(Param[1]))
            if dict_match:
                param_dict_str = dict_match.group(1)
                param_dict_str = param_dict_str.replace("\\'", "'")
                param_dict = eval('{' + param_dict_str + '}')
                if isinstance(param_dict, dict):
                    for key, value in param_dict.items():
                        cmd = '{} {} {} {}'.format(Name_of_class, Param[0],
                                                   key, value)
                        self.do_update(cmd)
            else:
                return (self.do_update(command))
        else:
            for key in Comd_dict.keys():
                if (Method == key):
                    return (Comd_dict[key](command))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
