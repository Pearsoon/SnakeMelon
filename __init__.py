import information
from plugins import Robot
import os
import importlib

if __name__ == '__main__':
    q = information.run()
    Robot = Robot()
    modules = [f[:-3] for f in os.listdir('plugins') if f.endswith('.py')]
    modules.remove("__init__")
    print(modules)
    for module_name in modules:
        module = importlib.import_module(f'plugins.{module_name}')
        Robot.add_plugin(plugin=module)
    while True:
        try:
            message = q.get()
            print(message)
            Robot.handle_message(message=message)
        except:
            pass
