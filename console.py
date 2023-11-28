#!/usr/bin/python3

"""console module for the airbnb"""


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """command interpeter"""

    prompt = '(hbnb) '

    def do_create(self, arg):
        """method that creates an instance of a class name
        if obj:
            if obj == "BaseModel":
                instance = BaseModel()
                print(instance.id)
                instance.save()
            elif obj == "User":
                instance = User()
                print(instance.id)
                instance.save()
        else:
            print("** class is missing **")"""

        """creates a new instance of a class\n"""
        if arg:
            obj = arg.split()
            obj_dict = {"BaseModel": BaseModel,
                        "User": User,
                        "State": State,
                        "Amenity": Amenity,
                        "Place": Place,
                        "Review": Review,
                        "City": City}

            for key, value in obj_dict.items():
                if key == obj[0]:
                    class_obj = value
                    instance = class_obj()
                    if len(obj) > 1:
                        for i in range(1, len(obj)):
                            new_obj = obj[i].split('=')
                            value = new_obj[1]
                            if value[0] == value[-1] == '"':
                                value = value[1: -1]
                                if '_' in value:
                                    value = new_obj[1].replace('_', ' ')
                            else:
                                try:
                                    value = int(value)
                                except:
                                    try:
                                        value = float(value)
                                    except:
                                        continue
                            setattr(instance, new_obj[0], value)
                    
                        instance.save()
                        print(instance.id)
                    instance.save()
                    return

            print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def do_show(self, line):
        """prints the string representation of an instance based on
        the class name and id\n"""

        classes = ["BaseModel", "User", "State", "Amenity", "Place", "Review", "City"]
        instance = storage.all()
        if not line:
            print("** class name missing **")
            return
        argv = line.split()
        if 0 < len(argv) < 2:
            print("** instance id missing **")
            return
        elif argv[0] not in classes:
            print("class doesn't exist")
            return

        obj = argv[0] + '.' + argv[1]
        for key, value in instance.items():
            if obj == key:
                print(value)
                return
        print("** no instance found **")

    def do_all(self, obj):
        """prints all string representation of all instances
        based or not on a class name\n"""

        if not obj:
            instances = storage.all()
            for values in instances.values():
                print(values)
            return
        else:
            classes = ["BaseModel", "User", "State", "Amenity",
                       "Place", "Review", "City"]
            if obj not in classes:
                print("** class doesn't exist **")
                return
            instances = storage.all(obj)
            for values in instances.values():
                print(values)

    def do_destroy(self, line):
        """destroys an instance based on name and id of the class\n"""

        classes = ["BaseModel", "User", "State", "Amenity", "Place", "Review", "City"]
        instance = storage.all()
        if not line:
            print("** class name missing **")
            return
        argv = line.split()
        if 0 < len(argv) < 2:
            print("** instance id missing **")
            return
        elif argv[0] not in classes:
            print("class doesn't exist")
            return
        obj = argv[0] + '.' + argv[1]
        if obj in instance.keys():
            del instance[obj]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, line):
        """updates an instance based on the class name and id\n"""

        classes = ["BaseModel", "User", "State", "Amenity", "Place", "Review", "City"]
        instance = storage.all()
        if not line:
            print("** class name missing **")
            return
        argv = line.split()
        if 0 < len(argv) < 2:
            print("** instance id missing **")
            return
        elif 0 < len(argv) < 3:
            print("**attribute name missing **")
            return
        elif 0 < len(argv) < 4:
            print("** value missing **")
            return
        elif argv[0] not in classes:
            print("class doesn't exist")
        obj = argv[0] + '.' + argv[1]
        if obj not in instance.keys():
            print("** no instance found**")
            return
        setattr(instance[obj], argv[2], argv[3])
        storage.save()

    def do_count(self, class_n):
        """
        Method counts instances of a certain class
        """
        count_instance = 0
        for instance_object in storage.all().values():
            if instance_object.__class__.__name__ == class_n:
                count_instance += 1
        print(count_instance)

    def default(self, line):
        """method that handels calling the command like
           this <class name>.commnad()
        """

        names = ["BaseModel", "User", "State", "Amenity", "Place", "Review", "City"]
        classes = {"all": self.do_all,
                   "count": self.do_count,
                   "show": self.do_show,
                   "destroy": self.do_destroy}

        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args:
            args = args.groups()
        if not args or args[0] not in names:
            super().default(line)
            return

        if args[1] in ["all", "count"]:
            classes[args[1]](args[0])

        elif args[1] in ["show", "destroy"]:
            classes[args[1]](args[0] + ' ' + args[2])

    def emptyline(self):
        """print empty line\n"""
        pass

    def do_EOF(self, line):
        """signal for ending the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True


if __name__ == '__main__':

    HBNBCommand().cmdloop()
