import information
from plugins import Robot
from sys import argv
from os import path, listdir
from importlib import import_module

BASE_DIR = path.dirname(path.realpath(argv[0]))

if __name__ == '__main__':
    q = information.run()
    Robot = Robot()
    modules = [f[:-3] for f in listdir(path.join(BASE_DIR, "plugins")) if f.endswith('.py')]
    modules.remove("__init__")
    for module_name in modules:
        module = import_module(f'plugins.{module_name}')
        Robot.add_plugin(plugin=module)
    while True:
        message = q.get()
        print(message)
        Robot.handle_message(message=message)
